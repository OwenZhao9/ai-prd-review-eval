// 审查网页的 Cloudflare Pages 版本：静态页面由 env.ASSETS 提供，这里只处理 /api/*。
// 浏览器把 PRD 拆成审查项后逐项调用 /api/item（免费版每次请求最多 50 个子请求，所以不在服务端一次审完）。
// API Key、复核口令只从 Cloudflare 密钥读取，不会发到浏览器。服务器不保存 PRD 原文。
import { PROMPTS, RULE_NAMES, VERSIONS } from './prompts.js';

const PER_IP_DEFAULT = 500;  // 每个访客每天的额度（F11）：最长的样本 PRD 有 479 项；部署变量 PER_IP_DAILY 可以改
const LINKS_PER_DAY = 30;    // 每个访客每天最多导入的链接数（F3）
const MAX_TEXT = 6000;       // 单个审查项最多字符数；整段检查按 1500 字分组，这里只防滥用
const FETCH_MAX = 5 * 1024 * 1024, FETCH_MS = 10000;
const SHARE_DAYS = 7;              // 分享链接保存天数
const SHARE_MAX = 900 * 1024;      // 单个分享最多字符数
const SHARES_PER_DAY = 50;         // 每个访客每天最多创建的分享数
const rid = n => { const a = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'; const b = crypto.getRandomValues(new Uint8Array(n)); return [...b].map(x => a[x % a.length]).join(''); };
const RULE_ID = { sentence: /^R[1-6]$/, doc: /^D[1-3]$/, account: /^A[1-4]$/ };
const LABEL = { sentence: '需求', doc: '功能段落', account: '功能段落' };

const json = (obj, status = 200, extra = {}) => new Response(JSON.stringify(obj), {
  status, headers: { 'Content-Type': 'application/json; charset=utf-8', ...extra },
});
const fail = (error, status = 400, code = '') => json({ error, code }, status);
const today = () => new Date().toISOString().slice(0, 10);
const globalDaily = env => +(env.GLOBAL_DAILY || 20000);
const perIpDaily = env => +(env.PER_IP_DAILY || PER_IP_DEFAULT);

const bump = (env, key, by = 1) => env.DB.prepare(
  'INSERT INTO usage (day, key, n) VALUES (?1, ?2, ?3) ON CONFLICT(day, key) DO UPDATE SET n = n + ?3 RETURNING n'
).bind(today(), key, by).first('n');
const usageOf = (env, key) => env.DB.prepare('SELECT n FROM usage WHERE day = ?1 AND key = ?2').bind(today(), key).first('n');

// 先占额度再调用；超出任何一个上限就不调用模型
async function takeQuota(env, ip) {
  const [all, mine] = await Promise.all([bump(env, 'all'), bump(env, 'ip:' + ip)]);
  if (all <= globalDaily(env) && mine <= perIpDaily(env)) return true;
  await env.DB.prepare('INSERT OR IGNORE INTO usage (day, key, n) VALUES (?1, ?2, 1)').bind(today(), 'qo:' + ip).run();
  return false;
}

function parseJson(raw) {
  const i = raw.indexOf('{');
  if (i < 0) return null;
  // 只取第一个完整的 JSON 对象，后面多出的文字忽略
  let depth = 0, inStr = false, esc = false;
  for (let j = i; j < raw.length; j++) {
    const c = raw[j];
    if (inStr) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') inStr = false; continue; }
    if (c === '"') inStr = true;
    else if (c === '{') depth++;
    else if (c === '}' && --depth === 0) {
      try { return JSON.parse(raw.slice(i, j + 1)); } catch { return null; }
    }
  }
  return null;
}

async function chat(env, system, user, temperature = 0) {
  const r = await fetch(env.LLM_BASE_URL.replace(/\/$/, '') + '/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + env.LLM_API_KEY },
    body: JSON.stringify({
      model: env.LLM_MODEL, temperature, response_format: { type: 'json_object' },
      messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }),
  });
  if (!r.ok) throw new Error('模型接口返回 ' + r.status);
  return (await r.json()).choices[0].message.content;
}

async function reviewItem(env, kind, text) {
  for (let attempt = 0; attempt < 2; attempt++) {
    const data = parseJson(await chat(env, PROMPTS[kind], `${LABEL[kind]}：\n${text}`));
    if (data && typeof data === 'object') {
      return (data.violations || []).map(v => ({
        rule: String(v.rule || '').trim().toUpperCase().slice(0, 2),
        evidence: v.evidence || '', reason: v.reason || '',
      })).filter(v => RULE_ID[kind].test(v.rule)).map(v => ({ ...v, name: RULE_NAMES[v.rule] }));
    }
  }
  throw new Error('模型返回的结果无法解析');
}

// 修改建议（F18）：针对已报出的问题改写一句需求，不增加原文没有的事实；提示词在 prompts/suggest_v2.md，评测见 suggest_eval.py
async function suggest(env, text, findings) {
  const user = `需求：${text}\n问题：\n${findings.map(f => `- ${f.rule} ${f.name}：${f.reason}`).join('\n')}`;
  for (let attempt = 0; attempt < 2; attempt++) {
    const d = parseJson(await chat(env, PROMPTS.suggest, user));
    // 拆成几条时，第一条之后的各占一行
    if (d && typeof d.rewrite === 'string' && d.rewrite.trim()) return [d.rewrite, ...(Array.isArray(d.others) ? d.others : [])].map(x => String(x).trim()).filter(Boolean).join('\n');
  }
  throw new Error('模型返回的结果无法解析');
}

/* ---------- 导入链接（F3） ---------- */
const LOGIN_HOST = /(^|\.)(feishu\.cn|feishu\.net|larksuite\.com|docs\.qq\.com|yuque\.com|notion\.so|notion\.site)$|^docs\.google\.com$/;
function blockedHost(host) {
  host = host.toLowerCase().replace(/^\[|\]$/g, '');
  if (host === 'localhost' || host.endsWith('.localhost') || host.endsWith('.local') || host.endsWith('.internal') || host === 'metadata.google.internal') return true;
  const m = host.match(/^(\d+)\.(\d+)\.(\d+)\.(\d+)$/);
  if (m) {
    const [a, b] = [+m[1], +m[2]];
    return a === 0 || a === 10 || a === 127 || (a === 169 && b === 254) || (a === 172 && b >= 16 && b <= 31) || (a === 192 && b === 168) || (a === 100 && b >= 64 && b <= 127) || a >= 224;
  }
  if (host.includes(':')) return host === '::1' || host === '::' || /^f[cd]/.test(host) || /^fe[89ab]/.test(host) || host.startsWith('::ffff:');
  if (/^\d+$/.test(host) || /^0x/i.test(host)) return true; // 十进制、十六进制写法的地址
  return false;
}
function rawUrl(u) {
  // GitHub 文件链接取原始 Markdown；GitLab 同理
  let m = u.match(/^https:\/\/github\.com\/([^/]+)\/([^/]+)\/blob\/(.+)$/);
  if (m) return [`https://raw.githubusercontent.com/${m[1]}/${m[2]}/${m[3]}`, 'github', 'GitHub 文件'];
  m = u.match(/^https:\/\/gitlab\.com\/(.+?)\/-\/blob\/(.+)$/);
  if (m) return [`https://gitlab.com/${m[1]}/-/raw/${m[2]}`, 'gitlab', 'GitLab 文件'];
  return [u, '', ''];
}
const FILE_EXT = /\.(md|markdown|txt|docx|pptx|pdf)$/i;
const decodeEntities = s => s.replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
  .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d)).replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16))).replace(/&amp;/g, '&');
// 网页正文转成带标题层级的文字
function htmlToMd(html) {
  let s = html.replace(/<!--[\s\S]*?-->/g, '').replace(/<(script|style|noscript|svg|nav|header|footer|aside|form)[\s\S]*?<\/\1>/gi, '');
  const main = s.match(/<(article|main)[^>]*>([\s\S]*?)<\/\1>/i);
  if (main) s = main[2];
  s = s.replace(/<h([1-4])[^>]*>([\s\S]*?)<\/h\1>/gi, (_, n, t) => `\n\n${'#'.repeat(+n)} ${t.replace(/<[^>]+>/g, '').trim()}\n\n`)
    .replace(/<li[^>]*>/gi, '\n- ').replace(/<tr[^>]*>/gi, '\n|').replace(/<\/t[dh]>/gi, ' |').replace(/<(br|\/p|\/div|\/li|\/tr|\/table)[^>]*>/gi, '\n')
    .replace(/<[^>]+>/g, '');
  s = decodeEntities(s).split('\n').map(l => l.replace(/[ \t]+/g, ' ').trim()).join('\n');
  // 表格行补上分隔行，让拆分按表头转写
  s = s.replace(/^(\|[^\n]*\|)\n(?=\|)/m, (m0, first) => `${first}\n|${first.split('|').slice(1, -1).map(() => ' --- ').join('|')}|\n`);
  return s.replace(/\n{3,}/g, '\n\n').trim();
}
async function fetchDoc(url) {
  let cur = url;
  for (let hop = 0; hop < 5; hop++) {
    const u = new URL(cur);
    if (!['http:', 'https:'].includes(u.protocol) || blockedHost(u.hostname)) throw Object.assign(new Error('不支持这个地址'), { code: 'blocked' });
    if (LOGIN_HOST.test(u.hostname)) throw Object.assign(new Error('没有读到正文，这个页面可能需要登录，请下载文件后上传'), { code: 'login' });
    const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), FETCH_MS);
    let r;
    try { r = await fetch(cur, { redirect: 'manual', signal: ctl.signal, headers: { 'User-Agent': 'ai-prd-review (+https://ai-prd-review.pages.dev)' } }); }
    catch (e) { clearTimeout(t); throw Object.assign(new Error(`这个链接打不开（${e.name === 'AbortError' ? '10 秒内没有响应' : '连接失败'}），请下载文件后上传`), { code: 'open' }); }
    if (r.status >= 300 && r.status < 400 && r.headers.get('location')) { clearTimeout(t); cur = new URL(r.headers.get('location'), cur).href; continue; }
    if (!r.ok) { clearTimeout(t); throw Object.assign(new Error(`这个链接打不开（返回 ${r.status}），请检查链接是否正确、文档是否公开，或下载文件后上传`), { code: 'open' }); }
    const reader = r.body.getReader(); const chunks = []; let size = 0;
    try {
      for (;;) {
        const { done, value } = await reader.read();
        if (done) break;
        size += value.length;
        if (size > FETCH_MAX) { ctl.abort(); throw Object.assign(new Error('文档超过 5 MB，请下载文件后上传'), { code: 'size' }); }
        chunks.push(value);
      }
    } catch (e) {
      if (e.code) throw e;
      throw Object.assign(new Error('这个链接打不开（10 秒内没有收完），请下载文件后上传'), { code: 'open' });
    } finally { clearTimeout(t); }
    const buf = new Uint8Array(size); let o = 0; for (const c of chunks) { buf.set(c, o); o += c.length; }
    return { buf, type: (r.headers.get('content-type') || '').toLowerCase(), finalUrl: cur };
  }
  throw Object.assign(new Error('这个链接打不开（跳转次数过多），请下载文件后上传'), { code: 'open' });
}
async function importLink(url) {
  let u;
  try { u = new URL(url); } catch { throw Object.assign(new Error('这个链接打不开（链接格式不对），请下载文件后上传'), { code: 'open' }); }
  if (!['http:', 'https:'].includes(u.protocol) || blockedHost(u.hostname)) throw Object.assign(new Error('不支持这个地址'), { code: 'blocked' });
  if (LOGIN_HOST.test(u.hostname)) throw Object.assign(new Error('这个链接需要登录才能看，请在原平台导出为 Word（.docx）或 PDF 后上传'), { code: 'login' });
  const [target, type, label] = rawUrl(u.href);
  const { buf, type: ct, finalUrl } = await fetchDoc(target);
  const ext = (new URL(finalUrl).pathname.match(FILE_EXT) || [])[1]?.toLowerCase();
  const b64 = () => { let s = ''; for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode(...buf.subarray(i, i + 0x8000)); return btoa(s); };
  if (['docx', 'pptx', 'pdf'].includes(ext) || /officedocument|application\/pdf/.test(ct)) {
    const e = ext || (ct.includes('pdf') ? 'pdf' : ct.includes('presentation') ? 'pptx' : 'docx');
    return { base64: b64(), ext: e, type: 'file', label: { docx: 'Word 文件', pptx: 'PPT 文件', pdf: 'PDF 文件' }[e] };
  }
  const text = new TextDecoder('utf-8').decode(buf);
  if (type || ['md', 'markdown', 'txt'].includes(ext) || /text\/(markdown|plain|x-markdown)/.test(ct)) {
    return { text, type: type || 'file', label: label || (ext === 'txt' ? '纯文本文件' : 'Markdown 文件') };
  }
  if (!/text\/html|application\/xhtml/.test(ct)) throw Object.assign(new Error('这个链接的内容不是文档'), { code: 'type' });
  const md = htmlToMd(text);
  if (md.replace(/\s/g, '').length < 200) throw Object.assign(new Error('没有读到正文，这个页面可能需要登录，请下载文件后上传'), { code: 'login' });
  return { text: md, type: 'web', label: '公开网页' };
}

/* ---------- 反馈（F19–F21） ---------- */
const FB_FILTER = { status: 'status', type: 'type', rule: 'rule', level: 'level' };
async function listFeedback(env, q) {
  const where = [], args = [];
  for (const [k, col] of Object.entries(FB_FILTER)) if (q.get(k)) { args.push(q.get(k)); where.push(`${col} = ?${args.length}`); }
  if (q.get('version')) { args.push(q.get('version')); where.push(`(json_extract(versions, '$.sentence') = ?${args.length} OR json_extract(versions, '$.document') = ?${args.length} OR json_extract(versions, '$.account') = ?${args.length})`); }
  const { results } = await env.DB.prepare(`SELECT * FROM feedback ${where.length ? 'WHERE ' + where.join(' AND ') : ''} ORDER BY created DESC LIMIT 500`).bind(...args).all();
  const cases = await env.DB.prepare("SELECT COUNT(*) AS n FROM feedback WHERE status = 'accepted'").first('n');
  const { results: vs } = await env.DB.prepare('SELECT DISTINCT versions FROM feedback WHERE versions IS NOT NULL').all();
  const versions = [...new Set(vs.flatMap(r => { try { const v = JSON.parse(r.versions); return [v.sentence, v.document, v.account].filter(Boolean); } catch { return []; } }))].sort();
  return {
    feedback: results.map(r => ({ ...r, predicted: JSON.parse(r.predicted || '[]'), versions: r.versions ? JSON.parse(r.versions) : null })),
    cases, versions,
  };
}
// 与本机版 app.py 写出的格式一致：误判 = 原本报的规则去掉被反馈的那条；漏判 = 加上被反馈的那条
function toCase(r) {
  const pred = new Set(JSON.parse(r.predicted || '[]'));
  const labels = r.type === 'false_positive' ? [...pred].filter(x => x !== r.rule).sort() : [...new Set([...pred, r.rule])].sort();
  return { id: 'F' + r.id, kind: 'feedback', level: r.level, text: r.text, labels, source_feedback: r.id };
}

/* ---------- 指标（第 7 节）：只记次数和类别 ---------- */
const EVENTS = new Set(['import_start', 'import_ok', 'import_fail', 'preview', 'review_start', 'review_complete', 'review_incomplete', 'items', 'item_fail', 'export', 'feedback', 'quota_out', 'adopt_all', 'share']);
async function metrics(env) {
  const since = new Date(Date.now() - 30 * 864e5).toISOString().slice(0, 10);
  const { results } = await env.DB.prepare('SELECT key, SUM(n) AS n FROM metrics WHERE day >= ?1 GROUP BY key').bind(since).all();
  const m = {}; for (const r of results) m[r.key] = r.n;
  const sum = p => Object.entries(m).filter(([k]) => k === p || k.startsWith(p + ':')).reduce((a, [, n]) => a + n, 0);
  const parts = p => Object.entries(m).filter(([k]) => k.startsWith(p + ':') && k.length > p.length + 1).map(([k, n]) => `${k.slice(p.length + 1)} ${n}`).join('，');
  const ratio = (a, b) => b ? a / b : null;
  const items = Object.entries(m).filter(([k]) => k.startsWith('items:')).flatMap(([k, n]) => Array(Math.min(n, 1000)).fill(+k.slice(6))).sort((a, b) => a - b);
  const median = items.length ? items[Math.floor(items.length / 2)] : null;
  const done = sum('review_complete'), started = sum('review_start'), finished = done + sum('review_incomplete');
  const { results: fbr } = await env.DB.prepare("SELECT rule, SUM(status = 'accepted') AS a, SUM(status != 'pending') AS d FROM feedback WHERE created >= ?1 GROUP BY rule").bind(Date.now() - 30 * 864e5).all();
  const { results: qo } = await env.DB.prepare("SELECT day, COUNT(*) AS n FROM usage WHERE key LIKE 'qo:%' AND day >= ?1 GROUP BY day").bind(since).all();
  const calls = await env.DB.prepare("SELECT SUM(n) AS n FROM usage WHERE key = 'all' AND day >= ?1").bind(since).first('n');
  return {
    rows: [
      { name: '导入成功率', value: ratio(sum('import_ok'), sum('import_start')), pct: true, detail: parts('import_ok') },
      { name: '导入失败（按原因）', value: sum('import_fail'), detail: parts('import_fail') },
      { name: '预览到审查的转化率', value: ratio(started, sum('preview')), pct: true },
      { name: '审查完成率', value: ratio(done, started), pct: true, detail: parts('review_incomplete') },
      { name: '每次审查的项数（中位数 / 最大）', value: median == null ? null : `${median} / ${items[items.length - 1]}` },
      { name: '失败项占比', value: ratio(sum('item_fail'), calls || 0), pct: true, detail: parts('item_fail') },
      { name: '导出率', value: ratio(sum('export'), finished), pct: true, detail: parts('export') },
      { name: '反馈率', value: ratio(sum('feedback'), finished), pct: true, detail: parts('feedback') },
      { name: '批量采用修改建议的次数', value: sum('adopt_all') },
      { name: '创建分享链接的次数', value: sum('share') },
      { name: '采纳率（按规则）', value: fbr.length ? fbr.map(r => `${r.rule} ${r.d ? Math.round(r.a / r.d * 100) + '%' : '—'}`).join('，') : null },
      { name: '额度用完的访客数（近 30 天合计）', value: qo.reduce((a, r) => a + r.n, 0) },
    ],
  };
}

/* ---------- 飞书授权导入（F4）：需要在部署配置里填飞书应用 ---------- */
async function feishu(env, path, d, origin) {
  if (!env.FEISHU_APP_ID || !env.FEISHU_APP_SECRET) throw new Error('在线版还没有配置飞书应用');
  const api = 'https://open.feishu.cn/open-apis';
  const call = async (url, token, body) => {
    const r = await fetch(api + url, { method: body ? 'POST' : 'GET', headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
    const j = await r.json(); if (j.code) throw new Error(j.msg || ('错误码 ' + j.code)); return j.data;
  };
  const tok = String(d.url || '').match(/\/(docx|docs|wiki)\/([A-Za-z0-9]+)/);
  if (path === 'start') {
    if (!d.code) return { authUrl: `https://open.feishu.cn/open-apis/authen/v1/authorize?app_id=${env.FEISHU_APP_ID}&redirect_uri=${encodeURIComponent(origin + '/?feishu=1')}&state=${encodeURIComponent(d.url || '')}` };
    const app = await (await fetch(api + '/auth/v3/app_access_token/internal', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ app_id: env.FEISHU_APP_ID, app_secret: env.FEISHU_APP_SECRET }) })).json();
    const u = await call('/authen/v1/oidc/access_token', app.app_access_token, { grant_type: 'authorization_code', code: d.code });
    return { token: u.access_token };
  }
  if (!tok) throw new Error('不是飞书文档链接');
  if (path === 'export') return { ticket: (await call('/drive/v1/export_tasks', d.token, { file_extension: 'docx', token: tok[2], type: tok[1] === 'docs' ? 'doc' : 'docx' })).ticket };
  if (path === 'result') {
    const r = (await call(`/drive/v1/export_tasks/${d.ticket}?token=${tok[2]}`, d.token)).result;
    if (r.job_status === 1 || r.job_status === 2) return { done: false };
    if (r.job_status !== 0) throw new Error(r.job_error_msg || '导出失败');
    const f = await fetch(`${api}/drive/v1/export_tasks/file/${r.file_token}/download`, { headers: { Authorization: 'Bearer ' + d.token } });
    if (!f.ok) throw new Error('下载导出文件失败（' + f.status + '）');
    const buf = new Uint8Array(await f.arrayBuffer()); let s = ''; for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode(...buf.subarray(i, i + 0x8000));
    return { done: true, base64: btoa(s) };
  }
  throw new Error('not found');
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    if (!path.startsWith('/api/')) return env.ASSETS.fetch(request);
    const ip = request.headers.get('CF-Connecting-IP') || 'local';
    const versions = { ...VERSIONS, model: env.LLM_MODEL };
    try {
      if (path === '/api/meta' && request.method === 'GET') {
        const used = (await usageOf(env, 'ip:' + ip)) || 0;
        return json({ versions, rules: RULE_NAMES, quota: { perIp: perIpDaily(env), remaining: Math.max(0, perIpDaily(env) - used) } });
      }
      if (path === '/api/item' && request.method === 'POST') {
        const { kind, text } = await request.json();
        if (!RULE_ID[kind] || !text) return fail('参数不对');
        if (!(await takeQuota(env, ip))) return fail('今天的额度已用完，明天再点「审查未完成的条目」；示例 PRD 不受限制', 429, 'quota');
        return json({ findings: await reviewItem(env, kind, String(text).slice(0, MAX_TEXT)) });
      }
      if (path === '/api/suggest' && request.method === 'POST') {
        const { text, findings } = await request.json();
        if (!text || !Array.isArray(findings) || !findings.length) return fail('参数不对');
        if (!(await takeQuota(env, ip))) return fail('今天的额度已用完', 429, 'quota');
        return json({ rewrite: await suggest(env, String(text).slice(0, 600), findings.slice(0, 6)) });
      }
      if (path === '/api/fetch' && request.method === 'POST') {
        const { url: link } = await request.json();
        if ((await bump(env, 'link:' + ip)) > LINKS_PER_DAY) return fail('今天导入链接的次数已用完（每天 30 个），请下载文件后上传', 429, 'limit');
        try { return json(await importLink(String(link || ''))); }
        catch (e) { return fail(e.message, e.code === 'blocked' ? 400 : 422, e.code || 'open'); }
      }
      if (path.startsWith('/api/feishu/') && request.method === 'POST') {
        return json(await feishu(env, path.slice(12), await request.json(), url.origin));
      }
      if (path === '/api/feedback' && request.method === 'GET') {
        return json(await listFeedback(env, url.searchParams));
      }
      if (path === '/api/feedback' && request.method === 'POST') {
        const d = await request.json();
        if (!['false_positive', 'missed'].includes(d.type)) return fail('type 只能是 false_positive 或 missed');
        const level = ['doc', 'account'].includes(d.level) ? d.level : 'sentence';
        const id = crypto.randomUUID().slice(0, 8);
        const time = new Date(Date.now() + 8 * 3600e3).toISOString().slice(0, 16).replace('T', ' ');
        await env.DB.prepare(
          'INSERT INTO feedback (id, time, created, status, type, level, text, rule, note, predicted, versions) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11)'
        ).bind(id, time, Date.now(), 'pending', d.type, level,
          String(d.text || '').slice(0, MAX_TEXT), String(d.rule || '').slice(0, 2), String(d.note || '').slice(0, 300),
          JSON.stringify((d.predicted || []).slice(0, 9)), JSON.stringify(versions)).run();
        return json({ ok: true, id });
      }
      if (path === '/api/feedback/resolve' && request.method === 'POST') {
        const d = await request.json();
        // 只有复核人能采纳或驳回：口令存在 Cloudflare 密钥 REVIEW_KEY 里，没设置时一律拒绝
        if (!env.REVIEW_KEY || d.key !== env.REVIEW_KEY) return fail('复核口令不对', 403);
        const status = d.decision === 'accept' ? 'accepted' : 'rejected';
        const r = await env.DB.prepare("UPDATE feedback SET status = ?1, reason = ?2 WHERE id = ?3 AND status = 'pending'")
          .bind(status, String(d.reason || '').slice(0, 300), d.id).run();
        if (!r.meta.changes) return fail('找不到这条待复核的反馈', 404);
        return json({ ok: true, status });
      }
      if (path === '/api/feedback/export' && request.method === 'POST') {
        const d = await request.json();
        if (!env.REVIEW_KEY || d.key !== env.REVIEW_KEY) return fail('复核口令不对', 403);
        const { results } = await env.DB.prepare("SELECT * FROM feedback WHERE status = 'accepted' ORDER BY created").all();
        return new Response(results.map(r => JSON.stringify(toCase(r)) + '\n').join(''), {
          headers: { 'Content-Type': 'application/x-ndjson; charset=utf-8', 'Content-Disposition': 'attachment; filename="feedback_cases.jsonl"' },
        });
      }
      if (path === '/api/event' && request.method === 'POST') {
        const d = await request.json().catch(() => ({}));
        if (!EVENTS.has(d.name)) return fail('未知事件');
        const dim = String(d.dim || '').replace(/[^a-z0-9_.-]/gi, '').slice(0, 24);
        const key = d.name === 'items' ? 'items:' + (+dim || 0) : d.name + (dim ? ':' + dim : '');
        await env.DB.prepare('INSERT INTO metrics (day, key, n) VALUES (?1, ?2, 1) ON CONFLICT(day, key) DO UPDATE SET n = n + 1').bind(today(), key).run();
        return json({ ok: true });
      }
      if (path === '/api/metrics' && request.method === 'GET') return json(await metrics(env));
      // 只读分享：只在用户点「分享」并确认后保存，7 天后删除；创建人凭撤销口令可以提前删除
      if (path === '/api/share' && request.method === 'POST') {
        const raw = await request.text();
        if (raw.length > SHARE_MAX) return fail('这份结果太大，不能分享；可以导出评审意见后发送', 413);
        let d; try { d = JSON.parse(raw); } catch { return fail('参数不对'); }
        if (!d || !d.result || !Array.isArray(d.result.sections)) return fail('参数不对');
        if ((await bump(env, 'share:' + ip)) > SHARES_PER_DAY) return fail('今天创建分享的次数已用完', 429);
        const now = Date.now(), id = rid(10), token = rid(20), expires = now + SHARE_DAYS * 864e5;
        await env.DB.prepare('DELETE FROM shares WHERE expires < ?1').bind(now).run();
        await env.DB.prepare('INSERT INTO shares (id, token, created, expires, data) VALUES (?1, ?2, ?3, ?4, ?5)').bind(id, token, now, expires, JSON.stringify(d.result)).run();
        return json({ id, token, expires });
      }
      if (path.startsWith('/api/share/') && request.method === 'GET') {
        const r = await env.DB.prepare('SELECT data, expires FROM shares WHERE id = ?1').bind(path.slice(11)).first();
        if (!r || r.expires < Date.now()) return fail('这个分享链接不存在或已过期', 404);
        return json({ result: JSON.parse(r.data), expires: r.expires });
      }
      if (path.startsWith('/api/share/') && request.method === 'DELETE') {
        const { token } = await request.json().catch(() => ({}));
        const r = await env.DB.prepare('DELETE FROM shares WHERE id = ?1 AND token = ?2').bind(path.slice(11), String(token || '')).run();
        if (!r.meta.changes) return fail('撤销口令不对，或分享已过期', 403);
        return json({ ok: true });
      }
      return fail('not found', 404);
    } catch (e) {
      return fail(e.message, 500);
    }
  },
};

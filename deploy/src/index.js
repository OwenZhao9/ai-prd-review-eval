// 审查网页的 Cloudflare Worker 版本：静态页面由 assets 提供，这里只处理 /api/*。
// 浏览器把 PRD 拆成条目后逐条调用 /api/item（免费版每次请求最多 50 个子请求，所以不在服务端一次审完）。
// API Key 只从 Cloudflare 密钥 LLM_API_KEY 读取，不会发到浏览器。
import { PROMPTS, RULE_NAMES, VERSIONS } from './prompts.js';

const PER_IP_DAILY = 150;   // 每个访客每天最多调用模型的次数
const GLOBAL_DAILY = 1000;  // 全站每天最多调用模型的次数
const MAX_TEXT = 4000;      // 单个条目最多字符数
const RULE_ID = /^(R[1-6]|D[1-3])$/;

const json = (obj, status = 200) => new Response(JSON.stringify(obj), {
  status, headers: { 'Content-Type': 'application/json; charset=utf-8' },
});
const today = () => new Date().toISOString().slice(0, 10);

// 先占额度再调用；超出任何一个上限就不调用模型
async function takeQuota(env, ip) {
  const day = today();
  const bump = (key) => env.DB.prepare(
    'INSERT INTO usage (day, key, n) VALUES (?1, ?2, 1) ON CONFLICT(day, key) DO UPDATE SET n = n + 1 RETURNING n'
  ).bind(day, key).first('n');
  const [all, mine] = await Promise.all([bump('all'), bump('ip:' + ip)]);
  return all <= GLOBAL_DAILY && mine <= PER_IP_DAILY;
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

async function chat(env, system, user) {
  const r = await fetch(env.LLM_BASE_URL.replace(/\/$/, '') + '/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + env.LLM_API_KEY },
    body: JSON.stringify({
      model: env.LLM_MODEL, temperature: 0, response_format: { type: 'json_object' },
      messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }),
  });
  if (!r.ok) throw new Error('模型接口返回 ' + r.status);
  return (await r.json()).choices[0].message.content;
}

async function reviewItem(env, kind, text) {
  const label = kind === 'doc' ? '功能段落' : '需求';
  for (let attempt = 0; attempt < 2; attempt++) {
    const data = parseJson(await chat(env, PROMPTS[kind], `${label}：\n${text}`));
    if (data && typeof data === 'object') {
      return (data.violations || []).map(v => ({
        rule: String(v.rule || '').trim().toUpperCase().slice(0, 2),
        evidence: v.evidence || '', reason: v.reason || '',
      })).filter(v => RULE_ID.test(v.rule)).map(v => ({ ...v, name: RULE_NAMES[v.rule] }));
    }
  }
  throw new Error('模型返回的结果无法解析');
}

async function listFeedback(env) {
  const { results } = await env.DB.prepare('SELECT * FROM feedback ORDER BY created DESC LIMIT 200').all();
  const cases = await env.DB.prepare("SELECT COUNT(*) AS n FROM feedback WHERE status = 'accepted'").first('n');
  return {
    feedback: results.map(r => ({ ...r, predicted: JSON.parse(r.predicted || '[]') })),
    cases,
  };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    if (!path.startsWith('/api/')) return env.ASSETS.fetch(request);
    const ip = request.headers.get('CF-Connecting-IP') || 'local';
    try {
      if (path === '/api/meta' && request.method === 'GET') {
        return json({ versions: { ...VERSIONS, model: env.LLM_MODEL }, perIpDaily: PER_IP_DAILY });
      }
      if (path === '/api/item' && request.method === 'POST') {
        const { kind, text } = await request.json();
        if (!['doc', 'sentence'].includes(kind) || !text) return json({ error: '参数不对' }, 400);
        if (!(await takeQuota(env, ip))) return json({ error: '今天的审查次数已用完，明天再试；示例 PRD 不受限制' }, 429);
        return json({ findings: await reviewItem(env, kind, String(text).slice(0, MAX_TEXT)) });
      }
      if (path === '/api/feedback' && request.method === 'GET') {
        return json(await listFeedback(env));
      }
      if (path === '/api/feedback' && request.method === 'POST') {
        const d = await request.json();
        if (!['false_positive', 'missed'].includes(d.type)) return json({ error: 'type 只能是 false_positive 或 missed' }, 400);
        const id = crypto.randomUUID().slice(0, 8);
        const time = new Date(Date.now() + 8 * 3600e3).toISOString().slice(0, 16).replace('T', ' ');
        await env.DB.prepare(
          'INSERT INTO feedback (id, time, created, status, type, level, text, rule, note, predicted) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10)'
        ).bind(id, time, Date.now(), 'pending', d.type, d.level === 'doc' ? 'doc' : 'sentence',
          String(d.text || '').slice(0, MAX_TEXT), String(d.rule || '').slice(0, 2), String(d.note || '').slice(0, 300),
          JSON.stringify((d.predicted || []).slice(0, 9))).run();
        return json({ ok: true, id });
      }
      if (path === '/api/feedback/resolve' && request.method === 'POST') {
        const d = await request.json();
        // 只有复核人能采纳或驳回：口令存在 Cloudflare 密钥 REVIEW_KEY 里，没设置时一律拒绝
        if (!env.REVIEW_KEY || d.key !== env.REVIEW_KEY) return json({ error: '复核口令不对' }, 403);
        const status = d.decision === 'accept' ? 'accepted' : 'rejected';
        const r = await env.DB.prepare("UPDATE feedback SET status = ?1 WHERE id = ?2 AND status = 'pending'").bind(status, d.id).run();
        if (!r.meta.changes) return json({ error: '找不到这条待复核的反馈' }, 404);
        return json({ ok: true, status });
      }
      return json({ error: 'not found' }, 404);
    } catch (e) {
      return json({ error: e.message }, 500);
    }
  },
};

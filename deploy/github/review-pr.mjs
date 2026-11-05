// GitHub 合并请求自动审查（F29）：只审这次改动涉及的需求和它们所在的段落，结果作为一条评论发在合并请求下。
// 同一个合并请求再次推送时更新这条评论，不新增评论。审查失败只在评论里写明，不阻止合并。
// 拆分逻辑（split.js）和提示词（prompts.json）与审查网页用同一份，由 deploy/build.py 生成。
// 环境变量：PRD_PATHS（逗号分隔）、LLM_BASE_URL、LLM_MODEL、LLM_API_KEY、GITHUB_TOKEN、BASE_SHA、HEAD_SHA、PR_NUMBER、REPO
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { splitPrd, jobsFor } = require('./split.js');
const P = JSON.parse(readFileSync(new URL('./prompts.json', import.meta.url)));
const env = process.env;
const MARK = '<!-- ai-prd-review -->';
const LABEL = { sentence: '需求', doc: '功能段落', account: '功能段落' };
const RULE_ID = { sentence: /^R[1-6]$/, doc: /^D[1-3]$/, account: /^A[1-4]$/ };

const show = (sha, path) => { try { return execFileSync('git', ['show', `${sha}:${path}`], { encoding: 'utf8', maxBuffer: 64 << 20 }); } catch { return ''; } };

function parseJson(raw) {
  const i = raw.indexOf('{'); if (i < 0) return null;
  for (let j = raw.length; j > i; j--) { try { return JSON.parse(raw.slice(i, j)); } catch { /* 继续缩短 */ } }
  return null;
}
async function review(kind, text) {
  for (let attempt = 0; attempt < 2; attempt++) {
    const r = await fetch(env.LLM_BASE_URL.replace(/\/$/, '') + '/chat/completions', {
      method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + env.LLM_API_KEY },
      body: JSON.stringify({ model: env.LLM_MODEL, temperature: 0, response_format: { type: 'json_object' },
        messages: [{ role: 'system', content: P.prompts[kind] }, { role: 'user', content: `${LABEL[kind]}：\n${text}` }] }),
    });
    if (!r.ok) throw new Error('模型接口返回 ' + r.status);
    const d = parseJson((await r.json()).choices[0].message.content);
    if (d && typeof d === 'object') return (d.violations || []).map(v => ({ rule: String(v.rule || '').trim().toUpperCase().slice(0, 2), reason: v.reason || '' })).filter(v => RULE_ID[kind].test(v.rule));
  }
  throw new Error('模型返回的结果无法解析');
}

// 改动涉及的审查项：新版里旧版没有的需求，以及这些需求所在段落的整段检查和账号与权限检查
function changedJobs(oldText, newText) {
  const oldSecs = splitPrd(oldText); const newSecs = splitPrd(newText);
  const oldReqs = new Set(oldSecs.flatMap(s => s.reqs));
  const oldTexts = new Set(oldSecs.map(s => s.text));
  const jobs = [];
  newSecs.forEach((s, si) => {
    const changed = s.reqs.filter(r => !oldReqs.has(r));
    if (!changed.length && oldTexts.has(s.text)) return;
    if (!changed.length) return;
    for (const j of jobsFor(s, si)) if (j.kind !== 'sentence' || changed.includes(j.text)) jobs.push({ ...j, title: s.title });
  });
  return { jobs, changed: jobs.filter(j => j.kind === 'sentence').length };
}

const cell = t => String(t || '').replace(/\|/g, '\\|').replace(/\n+/g, ' ');
async function main() {
  const paths = (env.PRD_PATHS || 'docs/PRD.md').split(',').map(s => s.trim()).filter(Boolean);
  const rows = [], failed = []; let changed = 0, problems = 0;
  for (const path of paths) {
    const { jobs, changed: n } = changedJobs(show(env.BASE_SHA, path), show(env.HEAD_SHA, path));
    changed += n;
    let i = 0;
    await Promise.all(Array.from({ length: 4 }, async () => {
      while (i < jobs.length) {
        const j = jobs[i++];
        const where = j.kind === 'sentence' ? j.text : `（${j.kind === 'doc' ? '整段检查' : '账号与权限检查'}）`;
        try {
          const fs = await review(j.kind, j.text);
          problems += fs.length;
          for (const f of fs) rows.push([path, j.title, where, `${f.rule} ${P.rules[f.rule] || ''}`, f.reason]);
        } catch (e) { failed.push([path, j.title, where, e.message]); }
      }
    }));
  }
  const body = [MARK, `### AI 审 PRD：本次改动 ${changed} 条需求，发现 ${problems} 个问题`, '',
    `规则版本：单句 ${P.versions.sentence}，文档级 ${P.versions.document}，账号与权限 ${P.versions.account} · 模型 ${env.LLM_MODEL} · 提交 ${String(env.HEAD_SHA).slice(0, 7)}`, ''];
  if (failed.length) body.push(`> ⚠️ 有 ${failed.length} 项调用失败，可重新运行这个检查：`, ...failed.map(f => `> - ${f[1]} · ${f[2]}：${f[3]}`), '');
  if (rows.length) body.push('| 文件 | 段落 | 需求 | 问题 | 理由 |', '| --- | --- | --- | --- | --- |', ...rows.map(r => '| ' + r.map(cell).join(' | ') + ' |'));
  else if (!failed.length) body.push('改动涉及的需求没有发现问题。');
  const text = body.join('\n');
  if (!env.GITHUB_TOKEN || !env.PR_NUMBER) { console.log(text); return; }
  const gh = (url, init = {}) => fetch('https://api.github.com' + url, { ...init, headers: { Authorization: 'Bearer ' + env.GITHUB_TOKEN, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' } });
  const list = await (await gh(`/repos/${env.REPO}/issues/${env.PR_NUMBER}/comments?per_page=100`)).json();
  const mine = Array.isArray(list) && list.find(c => (c.body || '').startsWith(MARK));
  const r = mine ? await gh(`/repos/${env.REPO}/issues/comments/${mine.id}`, { method: 'PATCH', body: JSON.stringify({ body: text }) })
    : await gh(`/repos/${env.REPO}/issues/${env.PR_NUMBER}/comments`, { method: 'POST', body: JSON.stringify({ body: text }) });
  if (!r.ok) throw new Error('写评论失败：' + r.status + ' ' + await r.text());
  console.log(mine ? '已更新评论' : '已发表评论');
}
main().catch(e => { console.error(e.message); process.exit(0); });

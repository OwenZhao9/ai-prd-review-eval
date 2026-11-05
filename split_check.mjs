// F6–F8 验收：用网页同一份拆分逻辑（web/split.js）重新拆 158 份样本 PRD，统计
// - 表格行原样当成需求（带竖线开头结尾）的条数（F6，目标 0）
// - 来自代码块的需求条数（F7，目标 0）
// - 超过 1500 字的整段检查项数（F8，目标 0）
// 用法：node split_check.mjs，结果写进 results/split_check.json
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
const { splitPrd, jobsFor } = createRequire(import.meta.url)('./web/split.js');

const codeLinesOf = text => {
  const set = new Set(); let open = null;
  for (const l of text.split('\n')) {
    const m = l.match(/^\s*(`{3,}|~{3,})/);
    if (!open) { if (m) open = m[1]; continue; }
    if (m && m[1][0] === open[0] && m[1].length >= open.length && /^\s*(`{3,}|~{3,})\s*$/.test(l)) { open = null; continue; }
    if (l.trim()) set.add(l.trim().replace(/^[-*+]\s+/, ''));
  }
  return set;
};
const out = { prds: 0, reqs: 0, table_row_reqs: 0, table_reqs_rewritten: 0, code_block_reqs: 0, doc_checks: 0, doc_checks_over_1500: 0, longest_doc_check: 0 };
for (const dir of ['data/raw', 'data/raw_zh']) for (const f of readdirSync(dir).filter(f => f.endsWith('.md'))) {
  const text = readFileSync(`${dir}/${f}`, 'utf8'); const code = codeLinesOf(text); out.prds++;
  splitPrd(text).forEach((s, i) => {
    if (s.skip) return;
    for (const r of s.reqs) {
      out.reqs++;
      if (/^\s*\|.*\|\s*$/.test(r)) out.table_row_reqs++;
      if (/^[^：]{1,40}：[^；]*；/.test(r)) out.table_reqs_rewritten++;
      if (code.has(r)) out.code_block_reqs++;
    }
    for (const j of jobsFor(s, i)) if (j.kind === 'doc') { out.doc_checks++; out.longest_doc_check = Math.max(out.longest_doc_check, j.text.length); if (j.text.length > 1500) out.doc_checks_over_1500++; }
  });
}
writeFileSync('results/split_check.json', JSON.stringify(out, null, 1));
console.log(out);

// 格式一致性评测（F23）第 2 步：用网页同一份解析代码（web/convert.js）读转出的 Word、PPT、PDF，
// 再用同一份拆分逻辑（web/split.js）拆分，和直接拆 Markdown 的结果逐条比较。不调用模型。
// 用法：cd data/format && npm i && node eval.mjs
// 输出：results/format/metrics.json、results/format/diff.md
import { readFileSync, readdirSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, '..', '..');
globalThis.DOMParser = require('@xmldom/xmldom').DOMParser;
globalThis.JSZip = require('jszip');
globalThis.pdfjsLib = require('pdfjs-dist/legacy/build/pdf.js');
const { splitPrd } = require(join(ROOT, 'web', 'split.js'));
const { fileToMd } = require(join(ROOT, 'web', 'convert.js'));

const shape = md => {
  const secs = splitPrd(md);
  return { titles: secs.map(s => s.title), reqs: secs.filter(s => !s.skip).flatMap(s => s.reqs) };
};

const names = [...readdirSync(join(ROOT, 'data', 'raw')).map(f => ['raw', f]), ...readdirSync(join(ROOT, 'data', 'raw_zh')).map(f => ['raw_zh', f])]
  .filter(([, f]) => f.endsWith('.md'));
const metrics = {}, diff = ['# 格式一致性评测：不一致的条目', '', '由 `data/format/eval.mjs` 生成。每份 PRD 只列前 10 处差异。', ''];
for (const ext of ['docx', 'pptx', 'pdf']) {
  let titleSame = 0, reqSame = 0, total = 0, common = 0, mdReqs = 0, failed = 0;
  diff.push(`## ${ext}`, '');
  for (const [dir, f] of names) {
    const n = f.replace(/\.md$/, '');
    const path = join(HERE, ext, `${n}.${ext}`);
    if (!existsSync(path)) continue;
    total++;
    const a = shape(readFileSync(join(ROOT, 'data', dir, f), 'utf8'));
    let b;
    try { const buf = readFileSync(path); b = shape((await fileToMd(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.length), ext)).md); }
    catch (e) { failed++; diff.push(`### ${n}`, '', `解析失败：${e.message}`, ''); mdReqs += a.reqs.length; continue; }
    const tSame = JSON.stringify(a.titles) === JSON.stringify(b.titles);
    const rSame = JSON.stringify(a.reqs) === JSON.stringify(b.reqs);
    titleSame += tSame; reqSame += rSame;
    const pool = new Map(); b.reqs.forEach(r => pool.set(r, (pool.get(r) || 0) + 1));
    let c = 0; for (const r of a.reqs) if (pool.get(r)) { c++; pool.set(r, pool.get(r) - 1); }
    common += c; mdReqs += a.reqs.length;
    if (!tSame || !rSame) {
      const onlyA = a.reqs.filter(r => !b.reqs.includes(r)).slice(0, 10), onlyB = b.reqs.filter(r => !a.reqs.includes(r)).slice(0, 10);
      const tA = a.titles.filter(t => !b.titles.includes(t)).slice(0, 5), tB = b.titles.filter(t => !a.titles.includes(t)).slice(0, 5);
      diff.push(`### ${n}`, '', `段落标题${tSame ? '一致' : '不一致'}，需求条目 ${c} / ${a.reqs.length} 一致（${ext} 拆出 ${b.reqs.length} 条）`, '');
      tA.forEach(t => diff.push(`- 标题只在 Markdown：${t}`)); tB.forEach(t => diff.push(`- 标题只在 ${ext}：${t}`));
      onlyA.forEach(r => diff.push(`- 需求只在 Markdown：${r}`)); onlyB.forEach(r => diff.push(`- 需求只在 ${ext}：${r}`));
      diff.push('');
    }
  }
  metrics[ext] = { prds: total, parse_failed: failed, titles_identical: titleSame, reqs_identical: reqSame, md_reqs: mdReqs, common_reqs: common,
    req_match_rate: mdReqs ? +(common / mdReqs).toFixed(4) : null };
  console.log(ext, metrics[ext]);
}
mkdirSync(join(ROOT, 'results', 'format'), { recursive: true });
writeFileSync(join(ROOT, 'results', 'format', 'metrics.json'), JSON.stringify({ generated_by: 'data/format/eval.mjs', ...metrics }, null, 1));
writeFileSync(join(ROOT, 'results', 'format', 'diff.md'), diff.join('\n'));

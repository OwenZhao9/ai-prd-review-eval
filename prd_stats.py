"""统计评测集来源的 158 份开源 PRD 的结构，按审查网页现在的拆分方式算出每份会产生多少审查项。

用法：python3 prd_stats.py      结果写进 results/prd_stats.json，docs/PRD.md 里的统计数字都来自这个文件。
拆分用 app.py 的 split_prd，与审查网页（本机版和 Cloudflare 版）一致：
- 审查项 = 每个功能段落的整段检查（至少 2 条需求时才做）+ 每条单句需求；
- 网页一次最多审 60 项、只审前 30000 字；在线版每个访客每天最多调用模型 150 次。
"""
import glob, json, os, re, statistics

from app import MAX_ITEMS, split_prd

ROOT = os.path.dirname(os.path.abspath(__file__))
PER_IP_DAILY = 150      # deploy/src/index.js
MAX_CHARS = 30000       # app.py / deploy/build.py
MAX_TEXT = 4000         # deploy/src/index.js：单个审查项最多发给模型的字数


def jobs(sections):
    return sum((1 if not s['skip'] and len(s['reqs']) >= 2 else 0) + len(s['reqs']) for s in sections)


def code_lines(text):
    out, inside = set(), False
    for line in text.splitlines():
        if line.strip().startswith('```'):
            inside = not inside
            continue
        if inside and line.strip():
            out.add(line.strip())
    return out


def strip_code(text):
    out, inside = [], False
    for line in text.splitlines():
        if line.strip().startswith('```'):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return '\n'.join(out)


rows = []
for path in sorted(glob.glob(os.path.join(ROOT, 'data', 'raw', '*.md'))) + sorted(glob.glob(os.path.join(ROOT, 'data', 'raw_zh', '*.md'))):
    text = open(path, encoding='utf-8').read()
    sections = split_prd(text)
    reqs = [r for s in sections for r in s['reqs']]
    code = code_lines(text)
    rows.append({
        'file': os.path.relpath(path, ROOT),
        'chars': len(text),
        'sections': len(sections),
        'skipped_sections': sum(s['skip'] for s in sections),
        'items': jobs(sections),
        'items_in_first_30000_chars': jobs(split_prd(text[:MAX_CHARS])),
        'reqs': len(reqs),
        'doc_sections': sum(1 for s in sections if not s['skip'] and len(s['reqs']) >= 2),
        'doc_sections_over_4000_chars': sum(1 for s in sections if not s['skip'] and len(s['reqs']) >= 2 and len(s['text']) > MAX_TEXT),
        'doc_sections_over_1500_chars': sum(1 for s in sections if not s['skip'] and len(s['reqs']) >= 2 and len(s['text']) > 1500),
        'has_heading': bool(re.search(r'^#{1,6} ', text, re.M)),
        'has_table': any(l.strip().startswith('|') for l in text.splitlines()),
        'table_row_reqs': sum(1 for r in reqs if r.startswith('|') or r.count('|') >= 2),
        'code_block_reqs': sum(1 for r in reqs if any(r in c for c in code)),
        # 只数正文里的图片：代码块和行内代码里写的图片语法不算
        'images': len(re.findall(r'!\[[^\]]*\]\([^)]*\)|<img ', re.sub(r'`[^`\n]*`', '', strip_code(text)))),
    })

items = sorted(r['items'] for r in rows)
q = statistics.quantiles(items, n=10)
summary = {
    'prds': len(rows),
    'en': sum(r['file'].startswith('data/raw/') for r in rows),
    'zh': sum(r['file'].startswith('data/raw_zh/') for r in rows),
    'items_median': statistics.median(items),
    'items_p10': q[0],
    'items_p90': q[-1],
    'items_max': items[-1],
    'items_total': sum(items),
    f'over_{MAX_ITEMS}_items': sum(r['items'] > MAX_ITEMS for r in rows),
    f'over_{MAX_ITEMS}_items_in_first_30000_chars': sum(r['items_in_first_30000_chars'] > MAX_ITEMS for r in rows),
    f'over_{PER_IP_DAILY}_items': sum(r['items'] > PER_IP_DAILY for r in rows),
    'over_300_items': sum(r['items'] > 300 for r in rows),
    f'over_{MAX_CHARS}_chars': sum(r['chars'] > MAX_CHARS for r in rows),
    'without_heading': sum(not r['has_heading'] for r in rows),
    'with_table': sum(r['has_table'] for r in rows),
    'with_table_row_reqs': sum(r['table_row_reqs'] > 0 for r in rows),
    'table_row_reqs': sum(r['table_row_reqs'] for r in rows),
    'with_code_block_reqs': sum(r['code_block_reqs'] > 0 for r in rows),
    'code_block_reqs': sum(r['code_block_reqs'] for r in rows),
    'reqs_total': sum(r['reqs'] for r in rows),
    'doc_sections': sum(r['doc_sections'] for r in rows),
    f'doc_sections_over_{MAX_TEXT}_chars': sum(r['doc_sections_over_4000_chars'] for r in rows),
    f'prds_with_doc_sections_over_{MAX_TEXT}_chars': sum(r['doc_sections_over_4000_chars'] > 0 for r in rows),
    'doc_sections_over_1500_chars': sum(r['doc_sections_over_1500_chars'] for r in rows),
    'with_images': sum(r['images'] > 0 for r in rows),
    # 整段检查的评测集里最长的段落（字数），用来对照上面的段落长度
    'evalset_paragraph_max_chars': {name: max(len(json.loads(l)['text']) for l in open(os.path.join(ROOT, 'data', name + '.jsonl')))
                                    for name in ('doc_evalset', 'doc_holdout', 'module_account_evalset', 'module_account_holdout')},
}
out = os.path.join(ROOT, 'results', 'prd_stats.json')
json.dump({'summary': summary, 'prds': rows}, open(out, 'w'), ensure_ascii=False, indent=1)
for k, v in summary.items():
    print(f'{k}: {v}')

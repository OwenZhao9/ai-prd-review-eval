"""从中文 PRD 里抽出候选需求条目，每份 PRD 最多取 6 条，写到 data/zh_pool.json。"""
import json, random, re

src = json.load(open('data/zh_sources.json'))
REQ = re.compile(r'(必须|应当|应该|需要|须|支持|允许|可以|能够|不得|禁止)')
cands = []
for s in src:
    seen = set()
    for line in open(s['file']).read().splitlines():
        l = re.sub(r'^\s*([-*+]|\d+(\.\d+)*[.)、]?|#+|>|\[[ xX]\])\s*', '', line).strip()
        l = re.sub(r'\*\*|`|~~', '', l).strip().strip('|').strip()
        zh = len(re.findall(r'[一-鿿]', l))
        if not (14 <= zh and len(l) <= 140): continue
        if not REQ.search(l): continue
        if re.search(r'http|\|.*\||```|[？?]$', l): continue
        if l in seen: continue
        seen.add(l)
        cands.append({'repo': s['repo'], 'license': s['license'], 'text': l})
random.seed(11); random.shuffle(cands)
cnt, pool = {}, []
for c in cands:
    if cnt.get(c['repo'], 0) >= 6: continue
    cnt[c['repo']] = cnt.get(c['repo'], 0) + 1
    pool.append(c)
for i, c in enumerate(pool): c['cid'] = f'Z{i + 1:03d}'
json.dump(pool, open('data/zh_pool.json', 'w'), ensure_ascii=False, indent=0)
print(len(src), 'PRDs →', len(cands), 'candidates →', len(pool), 'in pool')

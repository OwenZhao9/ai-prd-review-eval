"""算出设计图里用到的拆分数字，结果写进 results/design_counts.json。

用法：python3 design/counts.py
- 拆分用 app.py 的 split_prd（审查网页现在的规则），再按 docs/PRD.md 的新规则处理：
  F7 代码块里的行不算需求、也不算标题；F8 超过 1500 字的整段检查按列表项、自然段、表格行分组；
  F10 段落含账号与权限关键词时加一次账号与权限检查。
- 三份 PRD：示例 caesarloo/obsidian-svn（网页示例用的节选，deploy/public/sample.json）、
  yaomindong1996/forge-admin（长文档）、calderbuild/MD_Audit（额度不够）。
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from app import split_prd  # noqa: E402

LIMIT = 1500
KW = re.compile('登录|注册|密码|验证码|免登录|会话|权限|角色|管理员')


def strip_code(text):
    out, inside = [], False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            inside = not inside
            out.append('')
            continue
        out.append('' if inside else line)
    return '\n'.join(out)


def blocks(text):
    lines, out, cur = text.split('\n')[1:], [], []
    for l in lines:
        if not l.strip():
            if cur:
                out.append(cur)
                cur = []
            continue
        if (l.startswith('- ') or l.startswith('**')) and cur and not cur[0].startswith('|'):
            out.append(cur)
            cur = []
        cur.append(l)
    if cur:
        out.append(cur)
    for b in out:
        s = '\n'.join(b)
        if len(s) > LIMIT and b[0].startswith('|'):  # 表格按行拆，每组带表头
            head, cur = b[:2], list(b[:2])
            for r in b[2:]:
                if len('\n'.join(cur + [r])) > LIMIT:
                    yield '\n'.join(cur)
                    cur = list(head)
                cur.append(r)
            yield '\n'.join(cur)
        else:
            yield s


def groups(text):
    gs, cur = [], ''
    for b in blocks(text):
        if cur and len(cur) + len(b) + 1 > LIMIT:
            gs.append(cur)
            cur = b
        else:
            cur = cur + '\n' + b if cur else b
    if cur:
        gs.append(cur)
    return len(gs)


def count(text, account=True):
    secs = split_prd(strip_code(text))
    rows, total = [], {'sections': len(secs), 'skipped': 0, 'reqs': 0, 'doc_checks': 0, 'account_checks': 0}
    for s in secs:
        if s['skip']:
            total['skipped'] += 1
            continue
        doc = 0
        if len(s['reqs']) >= 2:
            doc = groups(s['text']) if len(s['text']) > LIMIT else 1
        acc = 1 if account and s['reqs'] and KW.search(s['title'] + s['text']) else 0
        total['reqs'] += len(s['reqs'])
        total['doc_checks'] += doc
        total['account_checks'] += acc
        if s['reqs']:
            rows.append({'title': s['title'], 'chars': len(s['text']), 'reqs': len(s['reqs']), 'doc_checks': doc,
                         'account_keywords': sorted(set(KW.findall(s['title'] + s['text']))) if acc else []})
    total['calls'] = total['reqs'] + total['doc_checks'] + total['account_checks']
    return {'total': total, 'sections_with_reqs': rows}


sample = json.load(open(os.path.join(ROOT, 'deploy', 'public', 'sample.json')))['text']
out = {
    'sample_obsidian_svn': count(sample, account=False),
    'forge_admin': count(open(os.path.join(ROOT, 'data', 'raw_zh', 'yaomindong1996__forge-admin.md'), encoding='utf-8').read()),
    'md_audit': count(open(os.path.join(ROOT, 'data', 'raw_zh', 'calderbuild__MD_Audit.md'), encoding='utf-8').read(), account=False),
}
json.dump(out, open(os.path.join(ROOT, 'results', 'design_counts.json'), 'w'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, v['total'])

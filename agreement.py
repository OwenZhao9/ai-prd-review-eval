"""算多人标注一致率：两份标注对同一批段落逐条规则比对，输出每条规则的一致率、Cohen's kappa 和分歧清单。

用法：python3 agreement.py 标注A.jsonl 标注B.jsonl [--rules module_account_v1]
两份文件每行一个 {"id": ..., "labels": [...]}，只比较两份都有的 id。
kappa 扣除了两人碰巧一致的部分：1 表示完全一致，0 表示和随机标注没有区别。
"""
import argparse, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    pa, pb = sum(a for a, _ in pairs) / n, sum(b for _, b in pairs) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return po, (po - pe) / (1 - pe) if pe < 1 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('--rules', default='module_account_v1')
    x = ap.parse_args()
    load = lambda p: {d['id']: set(d['labels']) for d in map(json.loads, open(p))}
    A, B = load(x.a), load(x.b)
    ids = sorted(A.keys() & B.keys())
    rules = [r['id'] for r in json.load(open(os.path.join(ROOT, 'rules', f'{x.rules}.json')))['rules']]
    print(f'共同段落 {len(ids)} 段')
    for r in rules:
        po, k = kappa([(r in A[i], r in B[i]) for i in ids])
        print(f'{r}  一致率 {po:.0%}  kappa {"—" if k is None else f"{k:.2f}"}')
    diff = [i for i in ids if A[i] != B[i]]
    print(f'\n分歧 {len(diff)} 段：')
    for i in diff:
        print(f'- {i}  A：{sorted(A[i]) or "无问题"}  B：{sorted(B[i]) or "无问题"}')


if __name__ == '__main__':
    main()

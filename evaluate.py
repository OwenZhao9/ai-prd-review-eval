"""跑评测：用某个版本的提示词审查评测集里的每一条需求，和标准答案对比算指标。

用法：python3 evaluate.py v1 [--runs 3]
结果写到 results/<版本>/：predictions.jsonl（每条预测）、metrics.json（指标）、errors.md（漏判与误判清单）
"""
import argparse, json, os, sys
from concurrent.futures import ThreadPoolExecutor
import review

ROOT = os.path.dirname(os.path.abspath(__file__))
RULES = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6']


def rule_ids(version):
    return [r['id'] for r in json.load(open(os.path.join(ROOT, 'rules', f'{version}.json')))['rules']]


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return round(p, 3), round(r, 3), round(f, 3)


def score(items, preds, rules=None):
    rules = rules or RULES
    per = {k: {'tp': 0, 'fp': 0, 'fn': 0} for k in rules}
    clean_total = clean_flagged = 0
    for it in items:
        gold, got = set(it['labels']), {v['rule'] for v in preds[it['id']]}
        for k in rules:
            if k in gold and k in got: per[k]['tp'] += 1
            elif k in got: per[k]['fp'] += 1
            elif k in gold: per[k]['fn'] += 1
        if not gold:
            clean_total += 1
            clean_flagged += bool(got)
    out = {'per_rule': {}}
    T = {'tp': 0, 'fp': 0, 'fn': 0}
    for k, c in per.items():
        p, r, f = prf(c['tp'], c['fp'], c['fn'])
        out['per_rule'][k] = dict(c, precision=p, recall=r, f1=f)
        for x in T: T[x] += c[x]
    p, r, f = prf(T['tp'], T['fp'], T['fn'])
    out['micro'] = dict(T, precision=p, recall=r, f1=f)
    out['clean_false_alarm_rate'] = round(clean_flagged / clean_total, 3) if clean_total else None
    out['clean_total'] = clean_total
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('version'); ap.add_argument('--runs', type=int, default=1); ap.add_argument('--workers', type=int, default=6); ap.add_argument('--set', default='evalset')
    a = ap.parse_args()
    review.load_env()
    items = [json.loads(l) for l in open(os.path.join(ROOT, 'data', f'{a.set}.jsonl'))]
    system = review.load_prompt(a.version)
    ids = rule_ids(a.version); label = '需求' if ids[0].startswith('R') else '功能段落'
    outdir = os.path.join(ROOT, 'results', a.set, a.version); os.makedirs(outdir, exist_ok=True)
    runs = []
    for run in range(a.runs):
        with ThreadPoolExecutor(a.workers) as ex:
            res = list(ex.map(lambda it: review.review(system, it['text'], 0.0 if run == 0 else 0.7, label), items))
        preds = {it['id']: r for it, r in zip(items, res)}
        runs.append(preds)
        with open(os.path.join(outdir, f'predictions_run{run + 1}.jsonl'), 'w') as f:
            for it in items:
                f.write(json.dumps({'id': it['id'], 'labels': it['labels'], 'pred': preds[it['id']]}, ensure_ascii=False) + '\n')
        print(f'run {run + 1} done', file=sys.stderr)
    metrics = {'version': a.version, 'set': a.set, 'model': os.environ.get('LLM_MODEL'), 'items': len(items), 'runs': [score(items, p, ids) for p in runs]}
    if len(runs) > 1:
        same = sum(len({frozenset(v['rule'] for v in p[it['id']]) for p in runs}) == 1 for it in items)
        metrics['consistency'] = round(same / len(items), 3)
    json.dump(metrics, open(os.path.join(outdir, 'metrics.json'), 'w'), ensure_ascii=False, indent=1)
    # 漏判与误判清单（取第一次，温度 0）
    p0 = runs[0]; lines = [f'# {a.version} 漏判与误判\n']
    for it in items:
        gold, got = set(it['labels']), {v['rule'] for v in p0[it['id']]}
        miss, extra = gold - got, got - gold
        if miss or extra:
            lines.append(f"## {it['id']}  标准：{sorted(gold) or '无问题'}  预测：{sorted(got) or '无问题'}")
            lines.append(f"> {it['text']}")
            if miss: lines.append(f"- 漏判：{sorted(miss)}")
            for v in p0[it['id']]:
                if v['rule'] in extra: lines.append(f"- 误判 {v['rule']}：「{v['evidence']}」{v['reason']}")
            lines.append('')
    open(os.path.join(outdir, 'errors.md'), 'w').write('\n'.join(lines))
    m = metrics['runs'][0]
    print(json.dumps({'micro': m['micro'], 'clean_false_alarm_rate': m['clean_false_alarm_rate'], 'consistency': metrics.get('consistency')}, ensure_ascii=False))


if __name__ == '__main__':
    main()

"""修改建议的上线前评测（F18）。

用法：python3 suggest_eval.py [提示词版本] [集合,集合]，例如 python3 suggest_eval.py suggest_v2 evalset,evalset_zh
1. 取开发集和留出测试集里单句 v4 第 1 次运行报出问题的条目，用 prompts/suggest_v1.md 生成改写。
2. 用 v4 把改写再审一遍（温度 0）。
3. 统计「原来的规则不再报出，也没有报出其他规则」的比例。
改写的提示词只按开发集的结果调整；留出集只用来打分。
拆成几条时每条都再审，全部没有问题才算解决。
输出：results/suggest/<提示词版本>/<集合>.jsonl（每条的原文、原问题、改写、再审结果）和 metrics.json。
"""
import json, os
from concurrent.futures import ThreadPoolExecutor
import review

ROOT = os.path.dirname(os.path.abspath(__file__))
import sys
PROMPT = sys.argv[1] if len(sys.argv) > 1 else 'suggest_v2'
SETS_ARG = sys.argv[2].split(',') if len(sys.argv) > 2 else None
SETS = {'evalset': 'dev', 'evalset_zh': 'dev', 'holdout': 'holdout', 'holdout_zh': 'holdout'}


def rewrite(system, text, found):
    user = f'需求：{text}\n问题：\n' + '\n'.join(f"- {f['rule']} {names[f['rule']]}：{f['reason']}" for f in found)
    for _ in range(3):
        d = review.parse_json(review.chat(system, user, 0.0))
        if isinstance(d, dict) and str(d.get('rewrite', '')).strip():
            # 拆成几条时，第一条之后的各占一行
            return '\n'.join([d['rewrite'].strip()] + [str(o).strip() for o in (d.get('others') or []) if str(o).strip()])
    raise ValueError('改写结果无法解析')


if __name__ == '__main__':
    review.load_env()
    names = {r['id']: r['name'] for r in json.load(open(os.path.join(ROOT, 'rules', 'v4.json')))['rules']}
    sug_sys = open(os.path.join(ROOT, 'prompts', f'{PROMPT}.md')).read().strip()
    rev_sys = review.load_prompt('v4')
    os.makedirs(os.path.join(ROOT, 'results', 'suggest', PROMPT), exist_ok=True)
    metrics = {'prompt': PROMPT, 'model': os.environ.get('LLM_MODEL'), 'rules': 'v4', 'sets': {}}
    for s, role in SETS.items():
        if SETS_ARG and s not in SETS_ARG:
            continue
        items = {d['id']: d for d in map(json.loads, open(os.path.join(ROOT, 'data', f'{s}.jsonl')))}
        preds = [d for d in map(json.loads, open(os.path.join(ROOT, 'results', s, 'v4', 'predictions_run1.jsonl'))) if d['pred']]

        def run(p):
            text = items[p['id']]['text']
            try:
                new = rewrite(sug_sys, text, p['pred'])
                again = [f['rule'] for line in new.split('\n') for f in review.review(rev_sys, line, 0.0, '需求')]
                return {'id': p['id'], 'text': text, 'found': [f['rule'] for f in p['pred']], 'rewrite': new, 'again': again, 'ok': not again}
            except Exception as e:
                return {'id': p['id'], 'text': text, 'found': [f['rule'] for f in p['pred']], 'error': str(e), 'ok': False}

        with ThreadPoolExecutor(8) as ex:
            rows = list(ex.map(run, preds))
        with open(os.path.join(ROOT, 'results', 'suggest', PROMPT, f'{s}.jsonl'), 'w') as f:
            f.write(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
        ok = sum(r['ok'] for r in rows)
        metrics['sets'][s] = {'role': role, 'flagged': len(rows), 'resolved': ok, 'rate': round(ok / len(rows), 3) if rows else None,
                              'errors': sum('error' in r for r in rows)}
        print(s, metrics['sets'][s])
    json.dump(metrics, open(os.path.join(ROOT, 'results', 'suggest', PROMPT, 'metrics.json'), 'w'), ensure_ascii=False, indent=1)

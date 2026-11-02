"""把复核采纳的反馈用例并进开发集：单条需求进 data/evalset_zh.jsonl，整段进 data/doc_evalset.jsonl。

只进开发集，不进留出测试集——反馈来自使用中暴露的误判，拿它改规则，留出集才能继续当公平的考卷。
已经并入过的用例不会重复写入。用法：python3 merge_feedback.py
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(ROOT, 'data', 'feedback_cases.jsonl')
TARGET = {'sentence': 'evalset_zh.jsonl', 'doc': 'doc_evalset.jsonl'}

if not os.path.exists(CASES):
    print('还没有采纳的反馈用例'); raise SystemExit
added = {}
for c in (json.loads(l) for l in open(CASES)):
    path = os.path.join(ROOT, 'data', TARGET[c['level']])
    have = {json.loads(l)['id'] for l in open(path)}
    if c['id'] in have:
        continue
    with open(path, 'a') as f:
        f.write(json.dumps({'id': c['id'], 'kind': 'feedback', 'lang': 'zh', 'text': c['text'], 'labels': c['labels'],
                            'source_feedback': c['source_feedback']}, ensure_ascii=False) + '\n')
    added[TARGET[c['level']]] = added.get(TARGET[c['level']], 0) + 1
print('并入：', added or '没有新的用例')

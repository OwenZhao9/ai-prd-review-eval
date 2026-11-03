"""生成健康看板：读 results/ 下的指标，写出 dashboard.html。每个指标都写明「变差说明什么、该怎么处理」。"""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
RULES_ALL = {r['id']: r['name'] for f in ('v1.json', 'doc_v1.json', 'module_account_v1.json') for r in json.load(open(os.path.join(ROOT, 'rules', f)))['rules']}
SETS = [('holdout_zh', '中文留出测试集（改规则前标好，只用来对比）'), ('holdout', '英文留出测试集（改规则前标好，只用来对比）'), ('evalset_zh', '中文开发集（用来分析误判、改规则）'), ('evalset', '英文开发集（用来分析误判、改规则）'), ('doc_holdout', '文档级留出测试集：整段功能描述（改规则前标好）'), ('doc_evalset', '文档级开发集：整段功能描述'), ('module_account_holdout', '账号与权限模块留出测试集（改规则前标好，只用来对比）'), ('module_account_evalset', '账号与权限模块开发集')]
VERS = ['v1', 'v2', 'v3', 'v4', 'v5']
# 各组规则的版本与定版版本
FAMILIES = {'doc': (['doc_v1', 'doc_v2', 'doc_v3'], 'doc_v1'), 'module_account': (['module_account_v1', 'module_account_v2', 'module_account_v3'], 'module_account_v3')}

ACTIONS = {
    'recall': ('召回率低：真问题被漏掉', '打开 errors.md 看「漏判」条目，把漏掉的句型补进这条规则的「判定」里'),
    'precision': ('准确率低：报了不存在的问题', '看「误判」条目的触发词，把这类情况写进这条规则的「不算违反」'),
    'clean': ('干净需求被错报：审查员在制造噪音', '按规则拆开看是哪条在错报，优先收紧那条规则的「不算违反」'),
    'consistency': ('结果不稳定：同一条需求每次答案不同', '把这些条目挑出来看是哪条规则在摇摆，给它补边界例子；必要时降低采样温度'),
}


def load(s, v):
    p = os.path.join(ROOT, 'results', s, v, 'metrics.json')
    return json.load(open(p)) if os.path.exists(p) else None


def cls(x, good, warn):
    return 'good' if x >= good else ('warn' if x >= warn else 'bad')


def card(label, a, b, fmt, lower_better=False, good=0.85, warn=0.7):
    if b is None:
        return ''
    val = (1 - b) if lower_better else b
    delta = '' if a is None else (b - a)
    dtxt = '' if a is None else f"{'+' if delta >= 0 else ''}{fmt(delta)} 对比 {FIRST} {fmt(a)}"
    return f'<div class="card {cls(val, good, warn)}"><div class="lbl">{label}</div><div class="num">{fmt(b)}</div><div class="delta">{dtxt}</div></div>'


FIRST = 'v1'
pct = lambda x: f'{x * 100:.0f}%'
num = lambda x: f'{x:.3f}'
parts = []
for s, title in SETS:
    fam = next((f for f in FAMILIES if s.startswith(f)), None)
    vers, final = FAMILIES[fam] if fam else (VERS, 'v4')
    have = [v for v in vers if load(s, v)]
    if not have:
        continue
    last = final or have[-1]  # 定版版本
    first = have[0]
    m1, m2 = (load(s, first) if first != last else None), load(s, last)
    FIRST = first
    r1, r2 = (m1['runs'][0] if m1 else None), m2['runs'][0]
    cards = ''.join([
        card('总体 F1', r1 and r1['micro']['f1'], r2['micro']['f1'], num),
        card('准确率（报出的问题里真问题占比）', r1 and r1['micro']['precision'], r2['micro']['precision'], pct),
        card('召回率（真问题被找出的比例）', r1 and r1['micro']['recall'], r2['micro']['recall'], pct),
        card('干净需求被错报', r1 and r1['clean_false_alarm_rate'], r2['clean_false_alarm_rate'], pct, lower_better=True, good=0.9, warn=0.8),
        card('三次运行结果一致', m1 and m1.get('consistency'), m2.get('consistency'), pct),
    ])
    rows = ''
    for k in r2['per_rule']:
        name = RULES_ALL[k]
        a = r1['per_rule'][k] if r1 else None
        b = r2['per_rule'][k]
        issue = '—'
        if b['tp'] + b['fn'] and b['recall'] < 0.8:
            issue = ACTIONS['recall'][0] + '<br><span class="act">→ ' + ACTIONS['recall'][1] + '</span>'
        elif b['tp'] + b['fp'] and b['precision'] < 0.8:
            issue = ACTIONS['precision'][0] + '<br><span class="act">→ ' + ACTIONS['precision'][1] + '</span>'
        hist = ''.join(f'<td>{num(load(s, v)["runs"][0]["per_rule"][k]["f1"])}</td>' for v in have if v != last)
        rows += (f'<tr><td><b>{k}</b> {html.escape(name)}</td><td>{b["tp"] + b["fn"]}</td>{hist}'
                 f'<td class="{cls(b["f1"], 0.85, 0.7)}">{num(b["f1"])}</td><td>{pct(b["precision"])}</td><td>{pct(b["recall"])}</td>'
                 f'<td>{b["fp"]} / {b["fn"]}</td><td class="issue">{issue}</td></tr>')
    parts.append(f'''<section><h2>{html.escape(title)} <span class="meta">{m2["items"]} 条 · 定版 {last} · 模型 {html.escape(str(m2["model"]))}</span></h2>
<div class="cards">{cards}</div>
<table><thead><tr><th>规则</th><th>标准答案中的问题数</th>{''.join(f'<th>{v} F1</th>' for v in have if v != last)}<th>{last} F1（定版）</th><th>准确率</th><th>召回率</th><th>误判 / 漏判</th><th>对应问题与处理动作</th></tr></thead><tbody>{rows}</tbody></table></section>''')

guide = ''.join(f'<li><b>{html.escape(t)}</b>：{html.escape(a)}</li>' for t, a in ACTIONS.values())
page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 审 PRD 健康看板</title>
<style>
:root{{--bg:#f6f5f2;--card:#fff;--ink:#1d1d1f;--sub:#6b6b70;--line:#e4e2dc;--good:#1f8a5b;--warn:#c27a14;--bad:#c9372c}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151517;--card:#1e1e21;--ink:#ececee;--sub:#9a9aa2;--line:#2c2c30}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.6 -apple-system,"PingFang SC",sans-serif;padding:32px 16px}}
main{{max-width:1120px;margin:0 auto}}h1{{font-size:26px;margin:0 0 4px}}.lead{{color:var(--sub);margin:0 0 24px}}
h2{{font-size:17px;margin:28px 0 12px}}.meta{{font-weight:400;color:var(--sub);font-size:13px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:14px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;border-top:4px solid var(--sub)}}
.card.good{{border-top-color:var(--good)}}.card.warn{{border-top-color:var(--warn)}}.card.bad{{border-top-color:var(--bad)}}
.lbl{{color:var(--sub);font-size:12px}}.num{{font-size:26px;font-weight:700;font-variant-numeric:tabular-nums}}.delta{{color:var(--sub);font-size:12px}}
.table-wrap{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
th,td{{padding:9px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-variant-numeric:tabular-nums}}th{{font-size:12px;color:var(--sub);font-weight:600}}
td.good{{color:var(--good);font-weight:700}}td.warn{{color:var(--warn);font-weight:700}}td.bad{{color:var(--bad);font-weight:700}}
.issue{{font-size:12.5px;min-width:240px}}.act{{color:var(--sub)}}ul{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 14px 14px 32px}}
</style></head><body><main>
<h1>AI 审 PRD 健康看板</h1>
<p class="lead">按 NASA 需求编写检查清单的 6 条规则逐条审查 PRD 需求。v1 初版；v2 按英文误判修改；v3 补中文写法后误报大涨；v4 收紧「不算违反」条款，定版；v5 补 R3 的写法，R3 变好但误报增加，未采用。每一版只改规则文字。文档级审查整段功能描述（3 条规则）；账号与权限模块包按 NIST 数字身份标准审查登录、密码、登录状态和权限管理段落（4 条规则）。</p>
{''.join(f'<div class="table-wrap">{p}</div>' for p in parts)}
<h2>指标变差时怎么处理</h2><ul>{guide}</ul>
</main></body></html>'''
open(os.path.join(ROOT, 'dashboard.html'), 'w').write(page)
print('wrote dashboard.html')

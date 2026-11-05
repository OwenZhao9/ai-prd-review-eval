"""生成 Cloudflare Pages 版审查网页需要的文件。

用法：python3 deploy/build.py [--refresh-sample]
- src/prompts.js：三组定版规则（单句 v4、文档级 doc_v1、账号与权限 module_account_v3）的提示词和规则名，从 rules/、prompts/ 读取。
- public/index.html、public/split.js：页面和拆分逻辑，从 web/ 复制，规则名写进页面。
- public/github/：合并请求自动审查用的脚本和提示词（F29），与网页用同一份拆分逻辑和定版规则。
- public/dashboard.json：健康看板的离线指标，全部从 results/*/metrics.json 和 predictions_run*.jsonl 算出。
- public/sample.json：示例 PRD 的审查结果提前算好，点「填入示例 PRD」后不调用模型、不扣额度。
  已有结果只补算缺的审查项（例如新接入的账号与权限检查）；--refresh-sample 时全部重算。补算需要 .env。
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PUBLIC = os.path.join(HERE, 'public')
sys.path.insert(0, ROOT)
import review  # noqa: E402

SENT, DOC, ACC = 'v4', 'doc_v1', 'module_account_v3'
KIND_VER = {'sentence': SENT, 'doc': DOC, 'account': ACC}
LABEL = {'sentence': '需求', 'doc': '功能段落', 'account': '功能段落'}


def rule_names():
    return {r['id']: r['name'] for v in (SENT, DOC, ACC) for r in json.load(open(os.path.join(ROOT, 'rules', f'{v}.json')))['rules']}


def prompts():
    return {k: review.load_prompt(v) for k, v in KIND_VER.items()}


SUGGEST = 'suggest_v2'  # 修改建议的提示词（F18），评测见 suggest_eval.py


def write_prompts():
    allp = {**prompts(), 'suggest': open(os.path.join(ROOT, 'prompts', f'{SUGGEST}.md')).read().strip()}
    js = ('// 由 deploy/build.py 生成，不要手改\n'
          f'export const VERSIONS = {json.dumps({"sentence": SENT, "document": DOC, "account": ACC})};\n'
          f'export const RULE_NAMES = {json.dumps(rule_names(), ensure_ascii=False)};\n'
          f'export const PROMPTS = {json.dumps(allp, ensure_ascii=False, indent=1)};\n')
    open(os.path.join(HERE, 'src', 'prompts.js'), 'w').write(js)


def write_page():
    s = open(os.path.join(ROOT, 'web', 'index.html')).read()
    start = s.index('/*RULES*/') + len('/*RULES*/')
    end = s.index(';', start)
    s = s[:start] + json.dumps(rule_names(), ensure_ascii=False) + s[end:]
    # 规则说明（判定、不算、出处）写进页面，问题卡片上点「规则说明」时显示
    info = {}
    for v in (SENT, DOC, ACC):
        d = json.load(open(os.path.join(ROOT, 'rules', f'{v}.json')))
        src = str(d.get('source', '')).split('（')[0].split(' (')[0]
        for r in d['rules']:
            ref = r.get('nasa') or r.get('nist') or ''
            info[r['id']] = {'judge': r['判定'], 'not': r['不算'], 'ref': ref, 'source': src}
    start = s.index('/*RULE_INFO*/') + len('/*RULE_INFO*/')
    end = s.index(';', start)
    s = s[:start] + json.dumps(info, ensure_ascii=False) + s[end:]
    os.makedirs(os.path.join(PUBLIC, 'github'), exist_ok=True)
    open(os.path.join(PUBLIC, 'index.html'), 'w').write(s)
    # Pages 用 public/_worker.js 处理接口，部署时 wrangler 会把 src/index.js 一起打包
    open(os.path.join(PUBLIC, '_worker.js'), 'w').write("// 由 deploy/build.py 生成：Pages 的接口入口，代码在 src/index.js\nexport { default } from '../src/index.js';\n")
    for f in ('split.js', 'convert.js'):
        shutil.copy(os.path.join(ROOT, 'web', f), os.path.join(PUBLIC, f))
    shutil.copy(os.path.join(HERE, 'github', 'review-pr.mjs'), os.path.join(PUBLIC, 'github', 'review-pr.mjs'))
    json.dump({'versions': {'sentence': SENT, 'document': DOC, 'account': ACC}, 'rules': rule_names(), 'prompts': prompts()},
              open(os.path.join(PUBLIC, 'github', 'prompts.json'), 'w'), ensure_ascii=False)


# ---------- 健康看板 ----------
def metrics(set_, ver):
    p = os.path.join(ROOT, 'results', set_, ver, 'metrics.json')
    return json.load(open(p)) if os.path.exists(p) else None


def f1(tp, fp, fn):
    return round(2 * tp / (2 * tp + fp + fn), 3) if tp else 0.0


def combine(sets, ver):
    """多个留出集合并算第 1 次运行的合计 F1（与 CHANGELOG 的口径一致）。"""
    ms = [m for m in (metrics(s, ver) for s in sets) if m]
    if not ms:
        return None
    tp = sum(m['runs'][0]['micro']['tp'] for m in ms); fp = sum(m['runs'][0]['micro']['fp'] for m in ms); fn = sum(m['runs'][0]['micro']['fn'] for m in ms)
    clean_total = sum(m['runs'][0]['clean_total'] for m in ms)
    clean_fp = sum(round(m['runs'][0]['clean_false_alarm_rate'] * m['runs'][0]['clean_total']) for m in ms)
    items = sum(m['items'] for m in ms)
    cons = sum((m.get('consistency') or 0) * m['items'] for m in ms) / items if all(m.get('consistency') is not None for m in ms) else None
    per = {}
    for m in ms:
        for r, v in m['runs'][0]['per_rule'].items():
            a = per.setdefault(r, [0, 0, 0]); a[0] += v['tp']; a[1] += v['fp']; a[2] += v['fn']
    return {'version': ver, 'f1': f1(tp, fp, fn), 'items': items, 'clean_fp': clean_fp, 'clean_total': clean_total,
            'consistency': round(cons, 3) if cons is not None else None, 'per_rule': {r: f1(*v) for r, v in per.items()}}


def read_preds(set_, ver, run):
    p = os.path.join(ROOT, 'results', set_, ver, f'predictions_run{run}.jsonl')
    return {d['id']: d for d in map(json.loads, open(p))} if os.path.exists(p) else None


def majority(set_, ver):
    """多数表决（F26）：3 次运行里至少 2 次报出的规则才算报出，直接从已有的 3 次预测算，不调用模型。"""
    runs = [read_preds(set_, ver, i) for i in (1, 2, 3)]
    if not all(runs):
        return None
    score = lambda pred: [0, 0, 0]
    tp = fp = fn = 0; tp1 = fp1 = fn1 = 0; same = 0
    for iid, d in runs[0].items():
        gold = set(d['labels'])
        sets = [{v['rule'] for v in r[iid]['pred']} for r in runs]
        maj = {x for x in set().union(*sets) if sum(x in s for s in sets) >= 2}
        tp += len(maj & gold); fp += len(maj - gold); fn += len(gold - maj)
        tp1 += len(sets[0] & gold); fp1 += len(sets[0] - gold); fn1 += len(gold - sets[0])
        same += sets[0] == sets[1] == sets[2]
    n = len(runs[0])
    return {'set': set_, 'version': ver, 'items': n, 'single_f1': f1(tp1, fp1, fn1), 'majority_f1': f1(tp, fp, fn),
            'single_consistency': round(same / n, 3), 'majority_consistency': None}


def write_dashboard():
    sent_sets = ['holdout', 'holdout_zh']
    groups = [('单句 R1–R6', sent_sets, ['v1', 'v2', 'v3', 'v4', 'v5'], SENT),
              ('文档级 D1–D3', ['doc_holdout'], ['doc_v1', 'doc_v2', 'doc_v3'], DOC),
              ('账号与权限 A1–A4', ['module_account_holdout'], ['module_account_v1', 'module_account_v2', 'module_account_v3'], ACC)]
    versions = []
    cur = {}
    for name, sets, vers, adopted in groups:
        for v in vers:
            c = combine(sets, v)
            if c:
                versions.append({'group': name, **{k: c[k] for k in ('version', 'f1', 'clean_fp', 'clean_total', 'consistency')}, 'adopted': v == adopted})
                if v == adopted:
                    cur[name] = c
    s, d, a = cur[groups[0][0]], cur[groups[1][0]], cur[groups[2][0]]
    rules = [{'id': r, 'f1': c['per_rule'].get(r)} for c, ids in ((s, 'R1 R2 R3 R4 R5 R6'), (d, 'D1 D2 D3'), (a, 'A1 A2 A3 A4')) for r in ids.split()]
    maj = [m for m in (majority('holdout', SENT), majority('holdout_zh', SENT), majority('doc_holdout', DOC), majority('module_account_holdout', ACC)) if m]
    os.makedirs(os.path.join(ROOT, 'results', 'majority_vote'), exist_ok=True)
    json.dump(maj, open(os.path.join(ROOT, 'results', 'majority_vote', 'metrics.json'), 'w'), ensure_ascii=False, indent=1)
    agreement = []
    ag_dir = os.path.join(ROOT, 'results', 'agreement')
    if os.path.isdir(ag_dir):
        for f in sorted(os.listdir(ag_dir)):
            if f.endswith('.json'):
                g = json.load(open(os.path.join(ag_dir, f)))
                for r, v in (g.get('per_rule') or {}).items():
                    agreement.append({'group': f[:-5], 'rule': r, 'agreement': v.get('agreement'), 'kappa': v.get('kappa')})
    dash = {'cards': {'sentence': {k: s[k] for k in ('version', 'f1', 'items')}, 'doc': {k: d[k] for k in ('version', 'f1', 'items')},
                      'account': {k: a[k] for k in ('version', 'f1', 'items')},
                      'clean': {'fp': s['clean_fp'], 'total': s['clean_total'], 'rate': round(s['clean_fp'] / s['clean_total'], 3)}},
            'rules': rules, 'versions': versions, 'majority': maj, 'agreement': agreement}
    json.dump(dash, open(os.path.join(PUBLIC, 'dashboard.json'), 'w'), ensure_ascii=False, indent=1)


# ---------- 示例 PRD ----------
def write_sample(refresh):
    path = os.path.join(PUBLIC, 'sample.json')
    text = open(os.path.join(ROOT, 'web', 'sample.md')).read().strip()
    old = json.load(open(path)) if os.path.exists(path) else {}
    cache = {} if refresh else {(k, t): f for k, t, f in old.get('cache', [])}
    # 旧格式（整份结果）里已有的单句和整段结果直接沿用
    if not refresh and 'result' in old:
        for s in old['result']['sections']:
            if s.get('doc') and not s['doc'].get('error'):
                cache[('doc', s['text'])] = s['doc']['findings']
            for r in s['reqs']:
                if r.get('findings') is not None and not r.get('error'):
                    cache[('sentence', r['text'])] = r['findings']
    out = subprocess.run(['node', '-e', 'const S=require(process.argv[1]);const t=require("fs").readFileSync(0,"utf8");'
                          'console.log(JSON.stringify(S.splitPrd(t).flatMap((s,i)=>S.jobsFor(s,i)).map(j=>[j.kind,j.text])))',
                          os.path.join(ROOT, 'web', 'split.js')], input=text, capture_output=True, text=True, check=True).stdout
    jobs = [tuple(j) for j in json.loads(out)]
    missing = [j for j in jobs if j not in cache]
    if missing:
        review.load_env()
        names = rule_names(); sys_prompts = prompts()
        for kind, t in missing:
            found = review.review(sys_prompts[kind], t, 0.0, LABEL[kind])
            for f in found:
                f['name'] = names.get(f['rule'], f['rule'])
            cache[(kind, t)] = found
    json.dump({'text': text, 'cache': [[k, t, cache[(k, t)]] for k, t in jobs]}, open(path, 'w'), ensure_ascii=False)
    print(f'sample.json：{len(jobs)} 个审查项，新算 {len(missing)} 个')


if __name__ == '__main__':
    write_prompts()
    write_page()
    write_dashboard()
    write_sample('--refresh-sample' in sys.argv)
    print('done')

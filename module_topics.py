"""第二个业务模块包选题（F30）第 1–2 步：统计功能段落标题的主题。

用法：python3 module_topics.py
- 拆分用网页同一份 web/split.js；只统计不跳过、至少拆出 1 条需求的功能段落。
- 主题按标题里的关键词归类（词表见 TOPICS），算出每个主题出现在多少份 PRD 里、多少个段落。
- 加上「漏了问题」反馈（data/feedback.jsonl 里 type=missed 的整段反馈）的段落标题主题。
- 第 3 步「只选能找到官方标准作为规则依据的主题」需要逐个核对标准原文，不在脚本里做。
输出：results/module_topics.json
"""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
TOPICS = {
    '账号与权限': r'登录|注册|密码|验证码|会话|权限|角色|账号|账户|用户管理|login|sign[ -]?in|sign[ -]?up|register|password|auth|session|permission|\broles?\b|account|rbac',
    '支付与订单': r'支付|付款|订单|退款|结算|计费|账单|订阅|payment|checkout|\borders?\b|refund|billing|invoice|subscription|pricing',
    '通知与消息': r'通知|消息|推送|提醒|邮件|短信|notification|notify|message|push|reminder|email|sms|alert',
    '搜索与筛选': r'搜索|检索|筛选|过滤|查询|search|filter|query|lookup',
    '文件与导入导出': r'文件|上传|下载|导入|导出|附件|file|upload|download|import|export|attachment',
    '数据与隐私': r'隐私|个人信息|数据删除|数据保留|同意|privacy|personal data|gdpr|consent|retention|pii',
    '日志与审计': r'日志|审计|操作记录|\blog(s|ging)?\b|audit|history',
    '无障碍': r'无障碍|可访问|读屏|accessibility|a11y|screen reader|wcag',
    '多语言与本地化': r'多语言|国际化|本地化|语言切换|i18n|l10n|locali[sz]ation|internationali[sz]ation|\blanguages?\b',
    '性能与容量': r'性能|并发|响应时间|吞吐|容量|performance|latency|throughput|scalab|\bload\b',
    '安全': r'安全|加密|防护|攻击|security|encrypt|xss|csrf|injection|vulnerab',
    '设置与配置': r'设置|配置|偏好|setting|config|preference',
    '仪表盘与报表': r'仪表盘|看板|报表|统计|图表|dashboard|report|analytics|chart|metric',
    'AI 与模型': r'\bai\b|模型|大模型|\bllm|\bagents?\b|智能|\bprompt|生成',
}


def split_all(paths):
    code = ('const S=require(process.argv[1]);const fs=require("fs");const out={};'
            'for(const p of JSON.parse(fs.readFileSync(0,"utf8"))){out[p]=S.splitPrd(fs.readFileSync(p,"utf8")).filter(s=>!s.skip&&s.reqs.length).map(s=>s.title)}'
            'console.log(JSON.stringify(out))')
    r = subprocess.run(['node', '-e', code, os.path.join(ROOT, 'web', 'split.js')], input=json.dumps(paths), capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def topics_of(title):
    t = title.lower()
    return [k for k, pat in TOPICS.items() if re.search(pat, t)]


if __name__ == '__main__':
    paths = [os.path.join(ROOT, 'data', d, f) for d in ('raw', 'raw_zh') for f in sorted(os.listdir(os.path.join(ROOT, 'data', d))) if f.endswith('.md')]
    titles = split_all(paths)
    stat = {k: {'prds': 0, 'sections': 0, 'examples': []} for k in TOPICS}
    for p, ts in titles.items():
        seen = set()
        for t in ts:
            for k in topics_of(t):
                stat[k]['sections'] += 1
                seen.add(k)
                if len(stat[k]['examples']) < 5:
                    stat[k]['examples'].append(f'{os.path.basename(p)[:-3]}：{t}')
        for k in seen:
            stat[k]['prds'] += 1
    missed = {}
    fb = os.path.join(ROOT, 'data', 'feedback.jsonl')
    for d in (map(json.loads, open(fb)) if os.path.exists(fb) else []):
        if d.get('type') == 'missed' and d.get('level') == 'doc':
            head = d['text'].strip().splitlines()[0].lstrip('#').strip()
            for k in topics_of(head):
                missed[k] = missed.get(k, 0) + 1
    rows = sorted(({'topic': k, **v, 'missed_feedback': missed.get(k, 0)} for k, v in stat.items()), key=lambda r: -r['prds'])
    out = {'generated_by': 'module_topics.py', 'prds': len(paths), 'functional_sections': sum(len(v) for v in titles.values()), 'topics': rows}
    json.dump(out, open(os.path.join(ROOT, 'results', 'module_topics.json'), 'w'), ensure_ascii=False, indent=1)
    for r in rows:
        print(f"{r['topic']:<10} {r['prds']:>4} 份  {r['sections']:>5} 段  漏报反馈 {r['missed_feedback']}")

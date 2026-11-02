"""AI 审查：按规则库逐条审查需求，输出违反了哪些规则。

模型走 OpenAI 兼容接口，DeepSeek / Gemini 都可以，配置读环境变量：
  LLM_BASE_URL  例：https://api.deepseek.com
  LLM_API_KEY
  LLM_MODEL     例：deepseek-chat
"""
import json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))


def load_env():
    p = os.path.join(ROOT, '.env')
    if os.path.exists(p):
        for line in open(p):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))


def load_prompt(version):
    rules = json.load(open(os.path.join(ROOT, 'rules', f'{version}.json')))['rules']
    tpl = open(os.path.join(ROOT, 'prompts', f'{version}.md')).read()
    rule_text = '\n'.join(f"- {r['id']} {r['name']}：{r['判定']} 不算违反：{r['不算']}" for r in rules)
    return tpl.replace('{RULES}', rule_text)


def chat(system, user, temperature=0.0, retries=3):
    body = json.dumps({
        'model': os.environ['LLM_MODEL'],
        'temperature': temperature,
        'response_format': {'type': 'json_object'},
        'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
    }).encode()
    url = os.environ['LLM_BASE_URL'].rstrip('/') + '/chat/completions'
    for i in range(retries):
        try:
            req = urllib.request.Request(url, body, {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + os.environ['LLM_API_KEY']})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read())['choices'][0]['message']['content']
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))


def review(system, text, temperature=0.0, label='需求'):
    raw = chat(system, f'{label}：\n{text}', temperature)
    m = re.search(r'\{.*\}', raw, re.S)
    data = json.loads(m.group(0)) if m else {}
    out = []
    for v in data.get('violations', []):
        rid = str(v.get('rule', '')).strip().upper()[:2]
        if re.fullmatch(r'R[1-6]|D[1-3]', rid):
            out.append({'rule': rid, 'evidence': v.get('evidence', ''), 'reason': v.get('reason', '')})
    return out

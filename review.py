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


def parse_json(raw):
    """取模型输出里的第一个 JSON 对象，后面多出的文字忽略；取不出时返回 None。"""
    i = raw.find('{')
    if i < 0:
        return None
    try:
        return json.JSONDecoder().raw_decode(raw[i:])[0]
    except json.JSONDecodeError:
        return None


def review(system, text, temperature=0.0, label='需求', attempts=3):
    # 输出不是合法 JSON 时重新调用，不把解析失败当成「没有问题」
    for _ in range(attempts):
        data = parse_json(chat(system, f'{label}：\n{text}', temperature))
        if isinstance(data, dict):
            break
    else:
        raise ValueError('模型连续返回无法解析的结果')
    out = []
    for v in data.get('violations', []):
        rid = str(v.get('rule', '')).strip().upper()[:2]
        if re.fullmatch(r'R[1-6]|D[1-3]|A[1-4]', rid):
            out.append({'rule': rid, 'evidence': v.get('evidence', ''), 'reason': v.get('reason', '')})
    return out

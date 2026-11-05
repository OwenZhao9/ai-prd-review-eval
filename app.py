"""审查网页的本机版：python3 app.py，然后打开 http://localhost:8787

页面、拆分逻辑、文件解析和在线版是同一份（deploy/public/，由 python3 deploy/build.py 生成）；
这里用 Python 实现和在线版（deploy/src/index.js）相同的接口，模型调用走 review.py，读 .env。
- POST /api/item              一个审查项：单句（v4）、整段（doc_v1）或账号与权限（module_account_v3）
- POST /api/suggest           修改建议（prompts/suggest_v2.md）
- POST /api/fetch             导入链接：只接受 http/https，不访问本机和内网地址，5 MB、10 秒
- GET/POST /api/feedback      反馈列表（可按状态、类型、规则、单条或整段、规则版本筛选）和提交
- POST /api/feedback/resolve  复核：采纳的反馈写成评测用例（data/feedback_cases.jsonl）
- POST /api/feedback/export   导出已采纳用例
- POST/GET/DELETE /api/share   只读分享：保存 7 天，凭撤销口令可以提前删除
本机版不限额度、不记使用计数；.env 里设了 REVIEW_KEY 时，采纳、驳回和导出要输入这个口令。
API Key 只在服务端读取，不发到浏览器；服务只监听本机 127.0.0.1。
"""
import ipaddress, json, os, re, socket, time, urllib.parse, urllib.request, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import review

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(ROOT, 'deploy', 'public')
FEEDBACK = os.path.join(ROOT, 'data', 'feedback.jsonl')
CASES = os.path.join(ROOT, 'data', 'feedback_cases.jsonl')
VERSIONS = {'sentence': 'v4', 'document': 'doc_v1', 'account': 'module_account_v3'}   # 当前定版，与 deploy/build.py 一致
KIND_VER = {'sentence': 'v4', 'doc': 'doc_v1', 'account': 'module_account_v3'}
LABEL = {'sentence': '需求', 'doc': '功能段落', 'account': '功能段落'}
RULE_ID = {'sentence': r'R[1-6]', 'doc': r'D[1-3]', 'account': r'A[1-4]'}
MAX_TEXT, FETCH_MAX, FETCH_SECONDS = 6000, 5 * 1024 * 1024, 10
SHARES = os.path.join(ROOT, 'data', 'shares')   # 本机版的分享存在这里，不进仓库
SHARE_DAYS, SHARE_MAX = 7, 900 * 1024

review.load_env()
PROMPTS = {k: review.load_prompt(v) for k, v in KIND_VER.items()}
SUGGEST = open(os.path.join(ROOT, 'prompts', 'suggest_v2.md')).read().strip()
RULE_NAMES = {r['id']: r['name'] for v in KIND_VER.values() for r in json.load(open(os.path.join(ROOT, 'rules', f'{v}.json')))['rules']}
TYPES = {'.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8'}


class UserError(Exception):
    def __init__(self, msg, code='open', status=422):
        super().__init__(msg); self.code = code; self.status = status


def versions():
    return {**VERSIONS, 'model': os.environ.get('LLM_MODEL')}


def suggest(text, findings):
    user = f'需求：{text}\n问题：\n' + '\n'.join(f"- {f['rule']} {f.get('name', '')}：{f.get('reason', '')}" for f in findings)
    for _ in range(2):
        d = review.parse_json(review.chat(SUGGEST, user, 0.0))
        if isinstance(d, dict) and str(d.get('rewrite', '')).strip():
            return '\n'.join(x for x in [str(d['rewrite']).strip(), *[str(o).strip() for o in (d.get('others') or [])]] if x)
    raise ValueError('模型返回的结果无法解析')


# ---------- 导入链接（F3），规则与在线版相同 ----------
LOGIN_HOST = re.compile(r'(^|\.)(feishu\.cn|feishu\.net|larksuite\.com|docs\.qq\.com|yuque\.com|notion\.so|notion\.site)$|^docs\.google\.com$')


def blocked(host):
    host = host.lower().strip('[]')
    if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
        return True
    try:
        addrs = {ipaddress.ip_address(host)}
    except ValueError:
        try:
            addrs = {ipaddress.ip_address(a[4][0]) for a in socket.getaddrinfo(host, None)}
        except socket.gaierror:
            return False
    return any(a.is_private or a.is_loopback or a.is_link_local or a.is_reserved or a.is_multicast or a.is_unspecified for a in addrs)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a):
        return None


def fetch_doc(url):
    for _ in range(5):
        u = urllib.parse.urlparse(url)
        if u.scheme not in ('http', 'https') or blocked(u.hostname or ''):
            raise UserError('不支持这个地址', 'blocked', 400)
        if LOGIN_HOST.search(u.hostname or ''):
            raise UserError('没有读到正文，这个页面可能需要登录，请下载文件后上传', 'login')
        req = urllib.request.Request(url, headers={'User-Agent': 'ai-prd-review (+https://ai-prd-review.pages.dev)'})
        try:
            r = urllib.request.build_opener(NoRedirect).open(req, timeout=FETCH_SECONDS)
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308) and e.headers.get('Location'):
                url = urllib.parse.urljoin(url, e.headers['Location']); continue
            raise UserError(f'这个链接打不开（返回 {e.code}），请检查链接是否正确、文档是否公开，或下载文件后上传')
        except Exception:
            raise UserError('这个链接打不开（10 秒内没有响应或连接失败），请下载文件后上传')
        t0, data = time.time(), b''
        while chunk := r.read(65536):
            data += chunk
            if len(data) > FETCH_MAX:
                raise UserError('文档超过 5 MB，请下载文件后上传', 'size')
            if time.time() - t0 > FETCH_SECONDS:
                raise UserError('这个链接打不开（10 秒内没有收完），请下载文件后上传')
        return data, (r.headers.get('Content-Type') or '').lower(), url
    raise UserError('这个链接打不开（跳转次数过多），请下载文件后上传')


def html_to_md(html):
    s = re.sub(r'<!--.*?-->|<(script|style|noscript|svg|nav|header|footer|aside|form)\b.*?</\1>', '', html, flags=re.S | re.I)
    m = re.search(r'<(article|main)\b[^>]*>(.*?)</\1>', s, re.S | re.I)
    if m:
        s = m.group(2)
    s = re.sub(r'<h([1-4])[^>]*>(.*?)</h\1>', lambda m: f"\n\n{'#' * int(m.group(1))} {re.sub(r'<[^>]+>', '', m.group(2)).strip()}\n\n", s, flags=re.S | re.I)
    s = re.sub(r'<li[^>]*>', '\n- ', s, flags=re.I)
    s = re.sub(r'<tr[^>]*>', '\n|', s, flags=re.I)
    s = re.sub(r'</t[dh]>', ' |', s, flags=re.I)
    s = re.sub(r'<(br|/p|/div|/li|/tr|/table)[^>]*>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    import html as h
    s = '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in h.unescape(s).split('\n'))
    return re.sub(r'\n{3,}', '\n\n', s).strip()


def import_link(url):
    u = urllib.parse.urlparse(url)
    if u.scheme not in ('http', 'https') or not u.hostname:
        raise UserError('这个链接打不开（链接格式不对），请下载文件后上传')
    if LOGIN_HOST.search(u.hostname):
        raise UserError('这个链接需要登录才能看，请在原平台导出为 Word（.docx）或 PDF 后上传', 'login')
    target, typ, label = url, '', ''
    if m := re.match(r'^https://github\.com/([^/]+)/([^/]+)/blob/(.+)$', url):
        target, typ, label = f'https://raw.githubusercontent.com/{m[1]}/{m[2]}/{m[3]}', 'github', 'GitHub 文件'
    elif m := re.match(r'^https://gitlab\.com/(.+?)/-/blob/(.+)$', url):
        target, typ, label = f'https://gitlab.com/{m[1]}/-/raw/{m[2]}', 'gitlab', 'GitLab 文件'
    data, ct, final = fetch_doc(target)
    ext = (re.search(r'\.(md|markdown|txt|docx|pptx|pdf)$', urllib.parse.urlparse(final).path, re.I) or [None, ''])[1].lower()
    if ext in ('docx', 'pptx', 'pdf') or re.search(r'officedocument|application/pdf', ct):
        import base64
        e = ext or ('pdf' if 'pdf' in ct else 'pptx' if 'presentation' in ct else 'docx')
        return {'base64': base64.b64encode(data).decode(), 'ext': e, 'type': 'file', 'label': {'docx': 'Word 文件', 'pptx': 'PPT 文件', 'pdf': 'PDF 文件'}[e]}
    text = data.decode('utf-8', 'replace')
    if typ or ext in ('md', 'markdown', 'txt') or re.search(r'text/(markdown|plain|x-markdown)', ct):
        return {'text': text, 'type': typ or 'file', 'label': label or ('纯文本文件' if ext == 'txt' else 'Markdown 文件')}
    if not re.search(r'text/html|application/xhtml', ct):
        raise UserError('这个链接的内容不是文档', 'type')
    md = html_to_md(text)
    if len(re.sub(r'\s', '', md)) < 200:
        raise UserError('没有读到正文，这个页面可能需要登录，请下载文件后上传', 'login')
    return {'text': md, 'type': 'web', 'label': '公开网页'}


# ---------- 反馈（F19–F21） ----------
def read_jsonl(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def write_jsonl(p, rows):
    with open(p, 'w') as f:
        f.write(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def to_case(row):
    # 误判：原本报的规则去掉被反馈的那条；漏判：加上被反馈的那条（与在线版、merge_feedback.py 一致）
    pred = set(row.get('predicted') or [])
    labels = sorted(pred - {row['rule']}) if row['type'] == 'false_positive' else sorted(pred | {row['rule']})
    return {'id': 'F' + row['id'], 'kind': 'feedback', 'level': row['level'], 'text': row['text'], 'labels': labels, 'source_feedback': row['id']}


def list_feedback(q):
    rows = read_jsonl(FEEDBACK)[::-1]
    for k in ('status', 'type', 'rule', 'level'):
        if q.get(k):
            rows = [r for r in rows if r.get(k) == q[k]]
    if q.get('version'):
        rows = [r for r in rows if q['version'] in (r.get('versions') or {}).values()]
    allv = sorted({v for r in read_jsonl(FEEDBACK) for k, v in (r.get('versions') or {}).items() if k != 'model' and v})
    return {'feedback': rows, 'cases': sum(r['status'] == 'accepted' for r in read_jsonl(FEEDBACK)), 'versions': allv}


def key_ok(d):
    return not os.environ.get('REVIEW_KEY') or d.get('key') == os.environ['REVIEW_KEY']


class H(BaseHTTPRequestHandler):
    def _send(self, body, code=200, ctype='application/json; charset=utf-8', extra=None):
        self.send_response(code); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers(); self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(json.dumps(obj, ensure_ascii=False).encode(), code)

    def _body(self):
        n = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(n) or b'{}')

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        if u.path == '/api/meta':
            return self._json({'versions': versions(), 'rules': RULE_NAMES, 'quota': {'perIp': 0, 'remaining': 10 ** 6}})
        if u.path == '/api/feedback':
            return self._json(list_feedback(q))
        if u.path.startswith('/api/share/'):
            f = os.path.join(SHARES, re.sub(r'[^A-Za-z0-9]', '', u.path[11:]) + '.json')
            d = json.load(open(f)) if os.path.exists(f) else None
            if not d or d['expires'] < time.time() * 1000:
                return self._json({'error': '这个分享链接不存在或已过期'}, 404)
            return self._json({'result': d['result'], 'expires': d['expires']})
        if u.path == '/api/metrics':
            return self._json({'rows': [{'name': '本机版不记使用计数', 'value': None}]})
        path = os.path.normpath(os.path.join(PUBLIC, u.path.lstrip('/') or 'index.html'))
        if not path.startswith(PUBLIC) or not os.path.isfile(path) or os.path.basename(path).startswith('_'):
            path = os.path.join(PUBLIC, 'index.html')
        if not os.path.exists(path):
            return self._send('先运行 python3 deploy/build.py 生成页面'.encode(), 500, 'text/plain; charset=utf-8')
        self._send(open(path, 'rb').read(), 200, TYPES.get(os.path.splitext(path)[1], 'application/octet-stream'))

    def do_POST(self):
        try:
            d = self._body()
            if self.path == '/api/item':
                kind, text = d.get('kind'), str(d.get('text') or '')
                if kind not in PROMPTS or not text:
                    return self._json({'error': '参数不对'}, 400)
                found = [f for f in review.review(PROMPTS[kind], text[:MAX_TEXT], 0.0, LABEL[kind]) if re.fullmatch(RULE_ID[kind], f['rule'])]
                return self._json({'findings': [{**f, 'name': RULE_NAMES.get(f['rule'], f['rule'])} for f in found]})
            if self.path == '/api/suggest':
                if not d.get('text') or not d.get('findings'):
                    return self._json({'error': '参数不对'}, 400)
                return self._json({'rewrite': suggest(str(d['text'])[:600], d['findings'][:6])})
            if self.path == '/api/fetch':
                try:
                    return self._json(import_link(str(d.get('url') or '')))
                except UserError as e:
                    return self._json({'error': str(e), 'code': e.code}, e.status)
            if self.path.startswith('/api/feishu/'):
                return self._json({'error': '本机版不支持飞书授权导入'}, 500)
            if self.path == '/api/share':
                if len(json.dumps(d)) > SHARE_MAX:
                    return self._json({'error': '这份结果太大，不能分享；可以导出评审意见后发送'}, 413)
                if not isinstance(d.get('result'), dict):
                    return self._json({'error': '参数不对'}, 400)
                os.makedirs(SHARES, exist_ok=True)
                now = time.time() * 1000
                for f in os.listdir(SHARES):
                    if json.load(open(os.path.join(SHARES, f)))['expires'] < now:
                        os.remove(os.path.join(SHARES, f))
                sid, token = uuid.uuid4().hex[:10], uuid.uuid4().hex
                row = {'id': sid, 'token': token, 'expires': now + SHARE_DAYS * 864e5, 'result': d['result']}
                json.dump(row, open(os.path.join(SHARES, sid + '.json'), 'w'), ensure_ascii=False)
                return self._json({'id': sid, 'token': token, 'expires': row['expires']})
            if self.path == '/api/event':
                return self._json({'ok': True})
            if self.path == '/api/feedback':
                if d.get('type') not in ('false_positive', 'missed'):
                    return self._json({'error': 'type 只能是 false_positive 或 missed'}, 400)
                row = {'id': uuid.uuid4().hex[:8], 'time': time.strftime('%Y-%m-%d %H:%M'), 'status': 'pending', 'type': d['type'],
                       'level': d.get('level') if d.get('level') in ('doc', 'account') else 'sentence', 'text': str(d.get('text', ''))[:MAX_TEXT],
                       'rule': str(d.get('rule', ''))[:2], 'note': str(d.get('note', ''))[:300], 'predicted': (d.get('predicted') or [])[:9], 'versions': versions()}
                with open(FEEDBACK, 'a') as f:
                    f.write(json.dumps(row, ensure_ascii=False) + '\n')
                return self._json({'ok': True, 'id': row['id']})
            if self.path == '/api/feedback/resolve':
                if not key_ok(d):
                    return self._json({'error': '复核口令不对'}, 403)
                rows = read_jsonl(FEEDBACK)
                row = next((r for r in rows if r['id'] == d.get('id') and r['status'] == 'pending'), None)
                if not row:
                    return self._json({'error': '找不到这条待复核的反馈'}, 404)
                row['status'] = 'accepted' if d.get('decision') == 'accept' else 'rejected'
                row['reason'] = str(d.get('reason') or '')[:300]
                row['resolved_at'] = time.strftime('%Y-%m-%d %H:%M')
                write_jsonl(FEEDBACK, rows)
                if row['status'] == 'accepted':
                    with open(CASES, 'a') as f:
                        f.write(json.dumps(to_case(row), ensure_ascii=False) + '\n')
                return self._json({'ok': True, 'status': row['status']})
            if self.path == '/api/feedback/export':
                if not key_ok(d):
                    return self._json({'error': '复核口令不对'}, 403)
                body = ''.join(json.dumps(to_case(r), ensure_ascii=False) + '\n' for r in read_jsonl(FEEDBACK) if r['status'] == 'accepted').encode()
                return self._send(body, 200, 'application/x-ndjson; charset=utf-8', {'Content-Disposition': 'attachment; filename="feedback_cases.jsonl"'})
            self._json({'error': 'not found'}, 404)
        except Exception as e:
            self._json({'error': str(e)}, 500)

    def do_DELETE(self):
        if not self.path.startswith('/api/share/'):
            return self._json({'error': 'not found'}, 404)
        f = os.path.join(SHARES, re.sub(r'[^A-Za-z0-9]', '', self.path[11:]) + '.json')
        d = self._body()
        if not os.path.exists(f) or json.load(open(f))['token'] != d.get('token'):
            return self._json({'error': '撤销口令不对，或分享已过期'}, 403)
        os.remove(f)
        return self._json({'ok': True})

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8787))
    v = versions()
    print(f"审查网页：http://localhost:{port}  （单句规则 {v['sentence']} · 文档级规则 {v['document']} · 账号与权限 {v['account']} · 模型 {v['model']}）")
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()

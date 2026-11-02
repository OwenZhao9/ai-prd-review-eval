"""审查网页的本地服务：python3 app.py，然后打开 http://localhost:8787

- POST /api/review           粘贴的 PRD → 按标题拆成功能段落做文档级审查，再拆出单条需求做单句审查
- POST /api/feedback         使用者对某条结果点「这是误判」或「漏了问题」
- GET  /api/feedback         反馈列表
- POST /api/feedback/resolve 复核：采纳的反馈变成一条待入库的评测用例（data/feedback_cases.jsonl）
API Key 只在服务端读取（.env），不会发到浏览器。
"""
import json, os, re, time, uuid
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import review

ROOT = os.path.dirname(os.path.abspath(__file__))
SENT_VERSION, DOC_VERSION = 'v4', 'doc_v1'   # 当前定版
FEEDBACK = os.path.join(ROOT, 'data', 'feedback.jsonl')
CASES = os.path.join(ROOT, 'data', 'feedback_cases.jsonl')
MAX_ITEMS = 60

review.load_env()
SENT_SYS, DOC_SYS = review.load_prompt(SENT_VERSION), review.load_prompt(DOC_VERSION)
RULE_NAMES = {r['id']: r['name'] for v in (SENT_VERSION, DOC_VERSION)
              for r in json.load(open(os.path.join(ROOT, 'rules', f'{v}.json')))['rules']}
REQ = re.compile(r'(必须|应当|应该|需要|须|支持|允许|可以|能够|不得|禁止|\b(must|shall|should|will|can|supports?|allows?)\b)', re.I)


SKIP_TITLE = re.compile(r'(背景|目标|范围|不包含|用户与场景|用户画像|场景|概述|简介|术语|附录|里程碑|计划|排期|待确认|未决|参考|版本记录|Background|Goal|Scope|Out of scope|Persona|Overview|Glossary|Appendix|Timeline|Open question)', re.I)
BULLET = re.compile(r'^\s*([-*+]|\d+(\.\d+)*[.)、]|\[[ xX]\])\s+')


def split_prd(text):
    """按 Markdown 标题切成段落。背景、范围、场景这类非功能段落跳过；功能段落里的每个列表项算一条需求。"""
    parts = re.split(r'\n(?=#{1,4} )', '\n' + text.strip())
    sections = []
    for p in parts:
        p = p.strip()
        if not p or p.startswith('>'):
            continue
        lines = p.splitlines()
        has_title = lines[0].startswith('#')
        title = lines[0].lstrip('#').strip() if has_title else '（无标题）'
        body = lines[1:] if has_title else lines
        skip = bool(SKIP_TITLE.search(title))
        reqs = []
        if not skip:
            for line in body:
                if not BULLET.match(line) and not REQ.search(line):
                    continue
                l = re.sub(r'\*\*|`', '', BULLET.sub('', line)).strip()
                zh = len(re.findall(r'[\u4e00-\u9fff]', l))
                if (zh >= 6 or len(l) >= 30) and len(l) <= 300 and not l.endswith(('：', ':')):
                    reqs.append(l)
        sections.append({'title': title, 'text': p, 'reqs': reqs, 'skip': skip})
    return sections


def do_review(text):
    sections = split_prd(text)
    jobs = []
    for si, s in enumerate(sections):
        if not s['skip'] and len(s['reqs']) >= 2:
            jobs.append(('doc', si, None, s['text']))
        for ri, r in enumerate(s['reqs']):
            jobs.append(('sent', si, ri, r))
    jobs = jobs[:MAX_ITEMS]

    def run(j):
        kind, si, ri, t = j
        try:
            if kind == 'doc':
                return j, review.review(DOC_SYS, t, 0.0, '功能段落'), None
            return j, review.review(SENT_SYS, t, 0.0, '需求'), None
        except Exception as e:
            return j, [], str(e)

    t0 = time.time()
    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(run, jobs))
    out = [{'title': s['title'], 'text': s['text'], 'skipped': s['skip'], 'doc': None, 'reqs': [{'text': r, 'findings': None} for r in s['reqs']]} for s in sections]
    errors = 0
    for (kind, si, ri, t), found, err in results:
        errors += bool(err)
        for f in found:
            f['name'] = RULE_NAMES.get(f['rule'], f['rule'])
        if kind == 'doc':
            out[si]['doc'] = {'findings': found, 'error': err}
        else:
            out[si]['reqs'][ri]['findings'] = found
            out[si]['reqs'][ri]['error'] = err
    n_items = sum(1 for j in jobs if j[0] == 'sent')
    n_flag = sum(1 for (k, *_), f, _ in results if k == 'sent' and f)
    return {'sections': out, 'stats': {'sections': len(sections), 'reqs': n_items, 'flagged': n_flag,
                                        'truncated': len(jobs) >= MAX_ITEMS, 'errors': errors, 'seconds': round(time.time() - t0, 1)},
            'versions': {'sentence': SENT_VERSION, 'document': DOC_VERSION, 'model': os.environ.get('LLM_MODEL')}}


def read_jsonl(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def write_jsonl(p, rows):
    with open(p, 'w') as f:
        f.write(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


class H(BaseHTTPRequestHandler):
    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code); self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(n) or b'{}')

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            body = open(os.path.join(ROOT, 'web', 'index.html'), 'rb').read()
            self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)
        elif self.path == '/api/feedback':
            self._json({'feedback': read_jsonl(FEEDBACK)[::-1], 'cases': len(read_jsonl(CASES))})
        elif self.path == '/api/sample':
            self._json({'text': open(os.path.join(ROOT, 'web', 'sample.md')).read()})
        else:
            self._json({'error': 'not found'}, 404)

    def do_POST(self):
        try:
            d = self._body()
            if self.path == '/api/review':
                text = (d.get('text') or '').strip()
                if not text:
                    return self._json({'error': '请先粘贴 PRD 内容'}, 400)
                return self._json(do_review(text[:30000]))
            if self.path == '/api/feedback':
                if d.get('type') not in ('false_positive', 'missed'):
                    return self._json({'error': 'type 只能是 false_positive 或 missed'}, 400)
                row = {'id': uuid.uuid4().hex[:8], 'time': time.strftime('%Y-%m-%d %H:%M'), 'status': 'pending',
                       'type': d['type'], 'level': d.get('level', 'sentence'), 'text': d.get('text', ''),
                       'rule': d.get('rule', ''), 'note': d.get('note', ''), 'predicted': d.get('predicted', []),
                       'versions': {'sentence': SENT_VERSION, 'document': DOC_VERSION}}
                with open(FEEDBACK, 'a') as f:
                    f.write(json.dumps(row, ensure_ascii=False) + '\n')
                return self._json({'ok': True, 'id': row['id']})
            if self.path == '/api/feedback/resolve':
                rows = read_jsonl(FEEDBACK)
                row = next((r for r in rows if r['id'] == d.get('id')), None)
                if not row:
                    return self._json({'error': '找不到这条反馈'}, 404)
                row['status'] = 'accepted' if d.get('decision') == 'accept' else 'rejected'
                row['resolved_at'] = time.strftime('%Y-%m-%d %H:%M')
                write_jsonl(FEEDBACK, rows)
                if row['status'] == 'accepted':
                    # 采纳：按复核结论写成标准答案，作为新的评测用例
                    pred = set(row.get('predicted') or [])
                    labels = sorted(pred - {row['rule']}) if row['type'] == 'false_positive' else sorted(pred | {row['rule']})
                    with open(CASES, 'a') as f:
                        f.write(json.dumps({'id': 'F' + row['id'], 'kind': 'feedback', 'level': row['level'], 'text': row['text'],
                                            'labels': labels, 'source_feedback': row['id']}, ensure_ascii=False) + '\n')
                return self._json({'ok': True, 'status': row['status']})
            self._json({'error': 'not found'}, 404)
        except Exception as e:
            self._json({'error': str(e)}, 500)

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8787))
    print(f'审查网页：http://localhost:{port}  （单句规则 {SENT_VERSION} · 文档级规则 {DOC_VERSION} · 模型 {os.environ.get("LLM_MODEL")}）')
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()

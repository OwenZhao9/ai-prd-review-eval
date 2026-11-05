"""F3 验收：从 data/sources.json、data/zh_sources.json 抽 20 个 GitHub 文件链接，经在线版的链接导入接口导入，
和该文件在 GitHub 同一提交上的原始内容逐字比较。

用法：python3 link_check.py [接口地址，默认 http://localhost:8799]
- 每个文件先用 GitHub API 取最新一次提交的 SHA，链接写成 github.com/<仓库>/blob/<SHA>/<路径>，保证两边是同一提交。
- 抽样固定用随机种子 0，结果写进 results/link_check.json。
"""
import json, random, sys, urllib.request, urllib.parse, subprocess

BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8799'
srcs = json.load(open('data/sources.json')) + json.load(open('data/zh_sources.json'))
random.seed(0)
sample = random.sample(srcs, 20)
rows = []
for s in sample:
    repo, path = s['repo'], s['path']
    try:
        sha = json.loads(subprocess.run(['gh', 'api', f'repos/{repo}/commits?path={urllib.parse.quote(path)}&per_page=1'], capture_output=True, text=True, check=True).stdout)[0]['sha']
        raw = urllib.request.urlopen(f'https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(path)}', timeout=30).read().decode('utf-8')
        req = urllib.request.Request(BASE + '/api/fetch', json.dumps({'url': f'https://github.com/{repo}/blob/{sha}/{path}'}).encode(), {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (link-check)'})
        got = json.loads(urllib.request.urlopen(req, timeout=60).read())
        rows.append({'repo': repo, 'path': path, 'sha': sha, 'identical': got.get('text') == raw, 'chars': len(raw)})
    except Exception as e:
        rows.append({'repo': repo, 'path': path, 'error': str(e)[:200], 'identical': False})
    print(rows[-1]['repo'], rows[-1].get('identical'), rows[-1].get('error', ''))
out = {'checked': len(rows), 'identical': sum(r['identical'] for r in rows), 'rows': rows}
json.dump(out, open('results/link_check.json', 'w'), ensure_ascii=False, indent=1)
print(out['identical'], '/', out['checked'])

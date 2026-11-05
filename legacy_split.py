"""改版前的拆分规则（2026-11-04 的审查网页），只用来复算 docs/PRD.md 里「现在的结果」那几列统计。
网页和 GitHub 合并请求审查现在用 web/split.js。
"""
import re

MAX_ITEMS = 60   # 改版前网页一次最多审的项数
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

"""生成 Cloudflare 版审查网页需要的文件：src/prompts.js、public/index.html、public/sample.json。

用法：python3 deploy/build.py [--refresh-sample]
- 提示词和规则名从 rules/、prompts/ 读取，与本机版 app.py 用同一个定版（单句 v4、文档级 doc_v1）。
- 页面由 web/index.html 改出：拆分 PRD 改在浏览器里做，逐条调用 /api/item。
- 示例 PRD 的审查结果提前算好存进 sample.json，点「填入示例 PRD」后不调用模型；--refresh-sample 时重新计算（需要 .env）。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import review  # noqa: E402

SENT, DOC = 'v4', 'doc_v1'


def rule_names():
    return {r['id']: r['name'] for v in (SENT, DOC) for r in json.load(open(os.path.join(ROOT, 'rules', f'{v}.json')))['rules']}


def write_prompts():
    js = ('// 由 deploy/build.py 生成，不要手改\n'
          f'export const VERSIONS = {json.dumps({"sentence": SENT, "document": DOC})};\n'
          f'export const RULE_NAMES = {json.dumps(rule_names(), ensure_ascii=False)};\n'
          f'export const PROMPTS = {json.dumps({"sentence": review.load_prompt(SENT), "doc": review.load_prompt(DOC)}, ensure_ascii=False, indent=1)};\n')
    open(os.path.join(HERE, 'src', 'prompts.js'), 'w').write(js)


SPLIT_JS = r"""
const SKIP_TITLE=/(背景|目标|范围|不包含|用户与场景|用户画像|场景|概述|简介|术语|附录|里程碑|计划|排期|待确认|未决|参考|版本记录|Background|Goal|Scope|Out of scope|Persona|Overview|Glossary|Appendix|Timeline|Open question)/i;
const BULLET=/^\s*([-*+]|\d+(\.\d+)*[.)、]|\[[ xX]\])\s+/;
const REQ=/(必须|应当|应该|需要|须|支持|允许|可以|能够|不得|禁止|\b(must|shall|should|will|can|supports?|allows?)\b)/i;
const MAX_ITEMS=60;
// 按 Markdown 标题切成段落；背景、范围、场景这类非功能段落跳过；功能段落里的每个列表项算一条需求
function splitPrd(text){const parts=('\n'+text.trim()).split(/\n(?=#{1,4} )/);const out=[];
  for(let p of parts){p=p.trim();if(!p||p.startsWith('>'))continue;const lines=p.split('\n');const hasTitle=lines[0].startsWith('#');
    const title=hasTitle?lines[0].replace(/^#+/,'').trim():'（无标题）';const body=hasTitle?lines.slice(1):lines;const skip=SKIP_TITLE.test(title);const reqs=[];
    if(!skip)for(const line of body){if(!BULLET.test(line)&&!REQ.test(line))continue;const l=line.replace(BULLET,'').replace(/\*\*|`/g,'').trim();
      const zh=(l.match(/[一-鿿]/g)||[]).length;if((zh>=6||l.length>=30)&&l.length<=300&&!/[：:]$/.test(l))reqs.push(l)}
    out.push({title,text:p,reqs,skip})}
  return out}
async function pool(jobs,n,fn){const res=new Array(jobs.length);let i=0;await Promise.all(Array.from({length:Math.min(n,jobs.length)},async()=>{while(i<jobs.length){const k=i++;res[k]=await fn(jobs[k])}}));return res}
async function reviewAll(text){const t0=Date.now();const sections=splitPrd(text.slice(0,30000));let jobs=[];
  sections.forEach((s,si)=>{if(!s.skip&&s.reqs.length>=2)jobs.push(['doc',si,null,s.text]);s.reqs.forEach((r,ri)=>jobs.push(['sentence',si,ri,r]))});
  const truncated=jobs.length>MAX_ITEMS;jobs=jobs.slice(0,MAX_ITEMS);let done=0;
  const results=await pool(jobs,6,async j=>{let out;try{out=[j,(await post('/api/item',{kind:j[0],text:j[3]})).findings,null]}catch(e){out=[j,[],e.message]}
    done++;const p=document.querySelector('#progress');if(p)p.textContent=`${done} / ${jobs.length}`;return out});
  const out=sections.map(s=>({title:s.title,text:s.text,skipped:s.skip,doc:null,reqs:s.reqs.map(r=>({text:r,findings:null}))}));let errors=0;const msgs=new Set();
  for(const [[kind,si,ri],found,err] of results){if(err){errors++;msgs.add(err)}if(kind==='doc')out[si].doc={findings:found,error:err};else{out[si].reqs[ri].findings=found;out[si].reqs[ri].error=err}}
  const nItems=jobs.filter(j=>j[0]==='sentence').length;const flagged=results.filter(([j,f])=>j[0]==='sentence'&&f.length).length;
  return {sections:out,stats:{sections:sections.length,reqs:nItems,flagged,truncated,errors,errorText:[...msgs].join('；'),seconds:Math.round((Date.now()-t0)/100)/10},versions:META.versions}}
let META={versions:{sentence:'v4',document:'doc_v1',model:''}},SAMPLE=null;
fetch('/api/meta').then(r=>r.json()).then(m=>{META=m;$('#ver').textContent=`单句规则 ${m.versions.sentence} · 文档级规则 ${m.versions.document} · 模型 ${m.versions.model}`}).catch(()=>{});
"""


def write_page():
    s = open(os.path.join(ROOT, 'web', 'index.html')).read()
    R = [
        ("$('#sample').onclick=async()=>{$('#prd').value=(await (await fetch('/api/sample')).json()).text};",
         "$('#sample').onclick=async()=>{SAMPLE=SAMPLE||await (await fetch('/sample.json')).json();$('#prd').value=SAMPLE.text};"),
        ("$('#out').innerHTML='<p class=\"hint\"><span class=\"spin\"></span> 审查中，按条目数大约需要 10–40 秒…</p>';",
         "$('#out').innerHTML='<p class=\"hint\"><span class=\"spin\"></span> 审查中，已完成 <span id=\"progress\">0</span> 项，按条目数大约需要 10–40 秒…</p>';"),
        ("try{const r=await post('/api/review',{text});render(r)}",
         "try{if(SAMPLE&&text===SAMPLE.text.trim()){render(SAMPLE.result)}else{render(await reviewAll(text))}}"),
        ("function render(r){", SPLIT_JS + "function render(r){"),
        ("(s.errors?`<p class=\"hint\">有 ${s.errors} 项调用模型失败，结果里标为「审查失败」。</p>`:'')",
         "(s.errors?`<p class=\"hint\">有 ${s.errors} 项调用模型失败，结果里标为「审查失败」${s.errorText?'：'+esc(s.errorText):''}。</p>`:'')"),
        ('<span class="hint">每个功能段落查：',
         '<span class="hint">粘贴的内容会发送给 DeepSeek 模型审查，请不要粘贴涉密内容；点「填入示例 PRD」再点「开始审查」可直接看到结果。<br>每个功能段落查：'),
        ('复核后「采纳」的条目按复核结论写成标准答案，进入 <code>data/feedback_cases.jsonl</code>，下一轮评测时补进评测集。',
         '复核后「采纳」的条目按复核结论写成标准答案，下一轮评测时补进开发集。'),
    ]
    for old, new in R:
        assert s.count(old) == 1, old[:50]
        s = s.replace(old, new)
    os.makedirs(os.path.join(HERE, 'public'), exist_ok=True)
    open(os.path.join(HERE, 'public', 'index.html'), 'w').write(s)


def write_sample(refresh):
    path = os.path.join(HERE, 'public', 'sample.json')
    if os.path.exists(path) and not refresh:
        return
    import app  # 本机版，读取 .env 调用模型
    text = open(os.path.join(ROOT, 'web', 'sample.md')).read().strip()
    json.dump({'text': text, 'result': app.do_review(text)}, open(path, 'w'), ensure_ascii=False)


if __name__ == '__main__':
    write_prompts()
    write_page()
    write_sample('--refresh-sample' in sys.argv)
    print('done')

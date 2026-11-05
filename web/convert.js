// 各种文件格式转成统一的 Markdown 结构（F2、F5）。网页和格式一致性评测（data/format/）共用这一份。
// 浏览器里用页面加载的 JSZip、pdf.js；Node 里由调用方把 DOMParser、JSZip、pdfjsLib 放到全局。
(function(root){
class UserError extends Error{}

// 按文件实际内容判断格式：扩展名和内容不符时以内容为准
async function sniff(buf,ext){const b=new Uint8Array(buf.slice(0,8));
  if(b[0]===0x50&&b[1]===0x4b){const z=await JSZip.loadAsync(buf);if(z.file('word/document.xml'))return['docx',z];if(z.file('ppt/presentation.xml'))return['pptx',z];return['unknown']}
  if(b[0]===0x25&&b[1]===0x50&&b[2]===0x44&&b[3]===0x46)return['pdf'];
  if(b[0]===0xd0&&b[1]===0xcf&&b[2]===0x11&&b[3]===0xe0)return[(ext==='docx'||ext==='pptx'||ext==='xlsx')?'encrypted':'old'];
  if(['md','txt','markdown'].includes(ext))return['text'];
  const s=new TextDecoder('utf-8',{fatal:false}).decode(buf.slice(0,4000));return[/\u0000/.test(s)?'unknown':'text']}

async function fileToMd(buf,ext,onProgress){
  const [kind,zip]=await sniff(buf,ext);
  if(kind==='encrypted')throw new UserError('文件已加密，请解除密码后上传');
  if(kind==='old'||kind==='unknown')throw new UserError('不支持这个格式，请另存为 .docx、.pptx 或 .pdf 后上传');
  if(kind==='text')return{md:new TextDecoder().decode(buf),notices:[]};
  if(kind==='docx')return await docxToMd(zip,onProgress);
  if(kind==='pptx')return await pptxToMd(zip,onProgress);
  if(kind==='pdf')return await pdfToMd(buf,onProgress)}

/* Word：标题样式 → 1–4 级标题；没用标题样式时按编号规则认标题；有修订时按接受全部修订后的内容（F5） */
const HEAD_RULE=/^(\d+(\.\d+)*[.、]?\s*\S|[一二三四五六七八九十]+、|（[一二三四五六七八九十]+）|第\s*[一二三四五六七八九十\d]+\s*章)/;
const guessLevel=t=>{const m=t.match(/^(\d+(\.\d+)*)/);if(m)return Math.min(4,m[1].split('.').length);if(/^第/.test(t))return 1;if(/^[一二三四五六七八九十]+、/.test(t))return 1;return 2};
const qn=(el,name)=>Array.from(el.getElementsByTagName(name));
function wText(el){let s='';const walk=n=>{for(const c of Array.from(n.childNodes)){if(c.nodeName==='w:del'||c.nodeName==='w:delText')continue;if(c.nodeName==='w:t')s+=c.textContent;else if(c.nodeName==='w:tab')s+=' ';else if(c.nodeName==='w:br')s+=' ';else if(c.childNodes&&c.childNodes.length)walk(c)}};walk(el);return s.trim()}
async function docxToMd(zip,onProgress){const xml=new DOMParser().parseFromString(await zip.file('word/document.xml').async('string'),'application/xml');onProgress&&onProgress(40);
  const styles={};if(zip.file('word/styles.xml')){const sx=new DOMParser().parseFromString(await zip.file('word/styles.xml').async('string'),'application/xml');
    qn(sx,'w:style').forEach(s=>{const n=qn(s,'w:name')[0];styles[s.getAttribute('w:styleId')]=(n&&n.getAttribute('w:val'))||''})}
  const headLevel=p=>{const ps=qn(p,'w:pStyle')[0];if(!ps)return 0;const id=ps.getAttribute('w:val')||'';const name=(styles[id]||id).toLowerCase();const m=name.match(/^(heading|标题)\s*([1-6])$/);return m?+m[2]:0};
  const isQuote=p=>{const ps=qn(p,'w:pStyle')[0];if(!ps)return false;const id=ps.getAttribute('w:val')||'';return /quote|block ?text|引用/i.test(styles[id]||id)};
  const isCode=p=>{const ps=qn(p,'w:pStyle')[0];if(!ps)return false;const id=ps.getAttribute('w:val')||'';return /code|代码|preformatted/i.test(styles[id]||id)};
  const body=qn(xml,'w:body')[0];const paras=qn(body,'w:p');const useStyles=paras.some(p=>headLevel(p));
  const revised=qn(xml,'w:ins').length+qn(xml,'w:del').length>0;const images=qn(xml,'w:drawing').length+qn(xml,'w:pict').length;
  const out=[];let inCode=false;
  // 代码样式的段落还原成代码块，和 Markdown 一样不算需求
  const endCode=()=>{if(inCode){out.push('```');inCode=false}};
  for(const el of Array.from(body.childNodes)){
    if(el.nodeName==='w:p'&&isCode(el)){if(!inCode){out.push('```');inCode=true}out.push(wText(el));continue}
    endCode();
    if(el.nodeName==='w:p'){const t=wText(el);if(!t)continue;let lv=headLevel(el);
      if(!useStyles&&!lv&&t.length<=30&&HEAD_RULE.test(t)&&!/[。；;]$/.test(t))lv=guessLevel(t);
      if(lv){out.push('','#'.repeat(lv)+' '+t,'');continue}
      if(qn(el,'w:numPr').length)out.push('- '+t);else if(isQuote(el))out.push('','> '+t,'');else out.push('',t,'')}
    else if(el.nodeName==='w:tbl'){const rows=qn(el,'w:tr').map(tr=>qn(tr,'w:tc').map(tc=>wText(tc).replace(/\|/g,'／')));if(!rows.length)continue;
      out.push('','| '+rows[0].join(' | ')+' |','|'+rows[0].map(()=>' --- ').join('|')+'|',...rows.slice(1).map(r=>'| '+r.join(' | ')+' |'),'')}}
  endCode();
  onProgress&&onProgress(90);const notices=[];if(revised)notices.push('这份 Word 有未接受的修订，已按接受全部修订后的内容审查');if(images)notices.push(`有 ${images} 张图片未审查`);
  return{md:out.join('\n').replace(/\n{3,}/g,'\n\n').trim(),notices,kind:'docx'}}

/* PPT：每页一个段落，页标题作段落标题，没有标题的页记作「第 N 页」；演讲者备注不审 */
async function pptxToMd(zip,onProgress){const files=Object.keys(zip.files).filter(f=>/^ppt\/slides\/slide\d+\.xml$/.test(f)).sort((a,b)=>+a.match(/\d+/)[0]-+b.match(/\d+/)[0]);
  const out=[];let images=0;
  for(let i=0;i<files.length;i++){const x=new DOMParser().parseFromString(await zip.file(files[i]).async('string'),'application/xml');onProgress&&onProgress(Math.round(10+80*i/files.length));
    let title='';const lines=[];images+=qn(x,'p:pic').length;
    for(const sp of qn(x,'p:sp')){const ph=qn(sp,'p:ph')[0];const type=ph&&ph.getAttribute('type');const paras=qn(sp,'a:p').map(p=>qn(p,'a:t').map(t=>t.textContent).join('').trim()).filter(Boolean);
      if(!paras.length)continue;if(!title&&(type==='title'||type==='ctrTitle')){title=paras.join(' ');continue}paras.forEach(p=>lines.push('- '+p))}
    for(const tbl of qn(x,'a:tbl')){const rows=qn(tbl,'a:tr').map(tr=>qn(tr,'a:tc').map(tc=>qn(tc,'a:t').map(t=>t.textContent).join('').replace(/\|/g,'／').trim()));
      if(rows.length)lines.push('','| '+rows[0].join(' | ')+' |','|'+rows[0].map(()=>' --- ').join('|')+'|',...rows.slice(1).map(r=>'| '+r.join(' | ')+' |'),'')}
    out.push('','## '+(title||`第 ${i+1} 页`),'',...lines)}
  const notices=images?[`有 ${images} 张图片未审查`]:[];return{md:out.join('\n').trim(),notices,kind:'pptx'}}

/* PDF：按阅读顺序取文字，去掉每页都重复出现的页眉、页脚和页码 */
async function pdfToMd(buf,onProgress){if(typeof window!=='undefined')pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  let pdf;try{pdf=await pdfjsLib.getDocument({data:new Uint8Array(buf)}).promise}catch(e){if(e&&e.name==='PasswordException')throw new UserError('文件已加密，请解除密码后上传');throw e}
  // 每页按坐标拼成行，记下字号、行高和是否等宽字体
  const pages=[];
  for(let i=1;i<=pdf.numPages;i++){const c=await (await pdf.getPage(i)).getTextContent();onProgress&&onProgress(Math.round(10+80*i/pdf.numPages));
    const rows=new Map();for(const it of c.items){if(!it.str.trim())continue;const y=Math.round(it.transform[5]/2)*2;if(!rows.has(y))rows.set(y,[]);rows.get(y).push(it)}
    pages.push([...rows.entries()].sort((a,b)=>b[0]-a[0]).map(([y,its])=>{its.sort((a,b)=>a.transform[4]-b.transform[4]);
      const size=Math.max(...its.map(t=>Math.abs(t.transform[3])||t.height||0));const mono=its.every(t=>/mono|courier/i.test(((c.styles||{})[t.fontName]||{}).fontFamily||''));
      let text='';its.forEach((t,k)=>{if(k&&/[\w)]$/.test(text)&&/^[\w(]/.test(t.str)&&t.transform[4]-(its[k-1].transform[4]+its[k-1].width)>size*.15)text+=' ';text+=t.str});
      return{y,x:its[0].transform[4],size,mono,text:text.replace(/\s+/g,' ').trim()}}).filter(l=>l.text))}
  // 去掉每页都重复出现的页眉、页脚和页码
  const norm=l=>l.text.replace(/\d+/g,'#');const freq=new Map();pages.forEach(p=>new Set(p.map(norm)).forEach(k=>freq.set(k,(freq.get(k)||0)+1)));
  const repeated=k=>pages.length>=2&&freq.get(k)>=Math.max(2,Math.ceil(pages.length*.8));
  pages.forEach((p,i)=>pages[i]=p.filter(l=>!repeated(norm(l))&&!/^[-—\s]*\d+[-—\s]*$/.test(l.text)&&!/^第\s*\d+\s*页/.test(l.text)));
  const all=pages.flat();if(!all.map(l=>l.text).join('').trim())throw new UserError('这份 PDF 里没有可提取的文字，请上传原始的 Word 文件');
  // 正文字号取出现最多的字号；比正文大的短行算标题，字号从大到小对应 1–4 级
  const w=new Map();all.forEach(l=>{const k=Math.round(l.size*2)/2;w.set(k,(w.get(k)||0)+l.text.length)});const body=[...w.entries()].sort((a,b)=>b[1]-a[1])[0][0];
  const heads=[...new Set(all.filter(l=>l.size>body*1.12&&l.text.length<=120&&!l.mono).map(l=>Math.round(l.size*2)/2))].sort((a,b)=>b-a).slice(0,4);
  const level=l=>{const i=heads.indexOf(Math.round(l.size*2)/2);return i<0||l.mono?0:i+1};
  const cjk=/[　-鿿＀-￯]/;const join=(a,b)=>a+((cjk.test(a.slice(-1))||cjk.test(b[0]))?'':' ')+b;
  const BUL=/^([•●▪◦‣·\-–\ue000-\uf8ff]|\d+[.)])\s*/;
  const out=[];let cur=null,inCode=false,prev=null;
  const flush=()=>{if(cur!==null){out.push(cur,'');cur=null}};
  for(const p of pages){prev=null;for(const l of p){
    if(l.mono){flush();if(!inCode){out.push('```');inCode=true}out.push(l.text);prev=l;continue}
    if(inCode){out.push('```','');inCode=false}
    const lv=level(l);
    if(lv){flush();const t=l.text;if(out.length&&out[out.length-2]&&out[out.length-2].startsWith('#'.repeat(lv)+' ')&&prev&&level(prev)===lv&&l.y<prev.y&&prev.y-l.y<l.size*1.6){out[out.length-2]=join(out[out.length-2],t)}else out.push('#'.repeat(lv)+' '+t,'');prev=l;continue}
    const gap=prev?prev.y-l.y:0;const bullet=BUL.test(l.text)&&!(cur!==null&&/^\d+[.)]\s/.test(l.text)&&prev&&l.x>prev.x+2);
    if(cur===null||bullet||gap>l.size*1.75||gap<0){flush();cur=bullet?'- '+l.text.replace(BUL,''):l.text}
    else cur=join(cur,l.text);prev=l}}
  flush();if(inCode)out.push('```');
  return{md:out.join('\n').replace(/\n{3,}/g,'\n\n').trim(),notices:[],kind:'pdf'}}
const BULLET_RE=/^\s*([-*+]|\d+(\.\d+)*[.)、]|\[[ xX]\])\s+/;
const api={UserError,sniff,fileToMd,docxToMd,pptxToMd,pdfToMd,wText,qn,HEAD_RULE};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else Object.assign(root,api);
})(typeof globalThis!=='undefined'?globalThis:this);

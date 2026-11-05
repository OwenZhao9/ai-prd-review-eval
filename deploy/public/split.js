// PRD 拆分：网页和 GitHub 合并请求审查共用这一份（F5–F9）。
// 输入是统一的 Markdown 结构（标题、段落、列表、表格），各种文件格式先在浏览器里转成这种结构。
(function (root) {
  const SKIP_TITLE = /(背景|目标|范围|不包含|用户与场景|用户画像|场景|概述|简介|术语|附录|里程碑|计划|排期|待确认|未决|参考|版本记录|修订记录|目录|Background|Goal|Scope|Out of scope|Persona|Overview|Glossary|Appendix|Timeline|Open question|Table of contents|Revision history)/i;
  const BULLET = /^\s*([-*+]|\d+(\.\d+)*[.)、]|\[[ xX]\])\s+/;
  const REQ = /(必须|应当|应该|需要|须|支持|允许|可以|能够|不得|禁止|\b(must|shall|should|will|can|supports?|allows?)\b)/i;
  const ACCOUNT = /(登录|注册|密码|验证码|免登录|会话|权限|角色|管理员)/;
  const GROUP_MAX = 1500;  // 整段检查每组最多字数（F8）

  const FENCE = /^\s*(```|~~~)/;
  // 代码块状态：只有和开头同一种符号、长度不短于开头的那一行才算结束（```` 包住的 ``` 不算）
  // 返回 'edge'（开始或结束那一行）、'in'（代码块里）或 false
  function fenceTracker() {
    let open = null;
    return line => {
      const m = line.match(/^\s*(`{3,}|~{3,})/);
      if (!open) { if (m) { open = m[1]; return 'edge'; } return false; }
      if (m && m[1][0] === open[0] && m[1].length >= open.length && /^\s*(`{3,}|~{3,})\s*$/.test(line)) { open = null; return 'edge'; }
      return 'in';
    };
  }
  const isTableRow = l => /^\s*\|.*\|\s*$/.test(l);
  const isTableSep = l => /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(l);
  const cells = l => l.trim().replace(/^\||\|$/g, '').split(/(?<!\\)\|/).map(c => plain(c));

  // 去掉行内 Markdown 格式（链接、图片、代码、粗体、斜体、转义），只留文字；Word、PPT、PDF 里本来就没有这些符号
  function plain(t) {
    // 行内代码里的字符原样保留，先换成占位符，最后放回
    const codes = [];
    t = t.replace(/`([^`]+)`/g, (_, c) => { codes.push(c); return '\u0000' + (codes.length - 1) + '\u0000'; });
    return t.replace(/^\[[ xX]\]\s+/, '').replace(/!?\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/\[([^\]]+)\]\[[^\]]*\]/g, '$1').replace(/\*\*([^*]+?)\*\*|__([^_]+?)__/g, (_, a, b) => a || b)
      .replace(/(^|[^\w*\\])\*(?!\s)([^*]+?)\*(?![\w*])/g, '$1$2').replace(/(^|[^\w\\])_(?!\s)([^_]+?)_(?!\w)/g, '$1$2').replace(/~~([^~]+)~~/g, '$1')
      .replace(/<br\s*\/?>/gi, ' ').replace(/\\([!-\/:-@\[-`{-~])/g, '$1').replace(/<\/?[A-Za-z][\w-]*(\s[^<>]*)?\/?>/g, '').replace(/\*\*|`/g, '')
      .replace(/[“”„]/g, '"').replace(/[‘’]/g, "'").replace(/…/g, '...')
      .replace(/\u0000(\d+)\u0000/g, (_, i) => codes[+i]).trim();
  }

  // 折行的列表项和自然段接成一行（Markdown 的软换行），和转成 Word 后的段落一致
  function joinSoftWraps(lines) {
    const out = []; const fence = fenceTracker();
    for (const line of lines) {
      const f = fence(line);
      if (f === 'edge') { out.push(line); continue; }
      const inCode = f === 'in';
      const prev = out[out.length - 1];
      // 有序列表只有从 1 开始才能打断上一段文字（CommonMark 规则），其余编号算上一段的接续
      const om = line.match(/^\s*(\d+)[.)]\s/);
      const interrupts = BULLET.test(line) && !(om && +om[1] !== 1 && prev !== undefined && prev.trim() && !BULLET.test(prev));
      const cont = !inCode && line.trim() && !interrupts && !isTableRow(line) && !/^#{1,6} /.test(line) && !/^\s*>/.test(line) && !/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(line)
        && prev !== undefined && prev.trim() && !FENCE.test(prev) && !isTableRow(prev) && !/^#{1,6} /.test(prev) && !/ {2}$|\\$|<br\s*\/?>$/i.test(prev);
      // 引用块里折行的几行也接成一行
      const qBody = l => l.replace(/^\s*>\s?/, '');
      const quoteCont = !inCode && /^\s*>\s?\S/.test(line) && !BULLET.test(qBody(line)) && !isTableRow(qBody(line)) && !/^(#|\[!)/.test(qBody(line)) && prev !== undefined && /^\s*>\s?\S/.test(prev) && !/^#|^\[!/.test(qBody(prev)) && !/ {2}$|\\$|<br\s*\/?>$/i.test(prev);
      if (cont) out[out.length - 1] = prev.replace(/\s+$/, '') + ' ' + line.trim();
      else if (quoteCont) out[out.length - 1] = prev.replace(/\s+$/, '') + ' ' + line.replace(/^\s*>\s?/, '').trim();
      else out.push(line);
    }
    return out;
  }

  function keepReq(l) {
    const zh = (l.match(/[一-鿿]/g) || []).length;
    return (zh >= 6 || l.length >= 30) && l.length <= 300 && !/[：:]$/.test(l);
  }

  // 把整段切成块：列表项、自然段、表格（表格按行可再拆），用来给超长段落分组
  function blocks(lines) {
    const out = []; let cur = null;
    const flush = () => { if (cur) out.push(cur); cur = null; };
    const fence = fenceTracker();
    for (const line of lines) {
      const f = fence(line);
      if (f === 'edge') { if (!cur || cur.type !== 'code') { flush(); cur = { type: 'code', lines: [line] }; } else { cur.lines.push(line); flush(); } continue; }
      if (f === 'in') { cur.lines.push(line); continue; }
      if (isTableRow(line)) { if (!cur || cur.type !== 'table') { flush(); cur = { type: 'table', lines: [] }; } cur.lines.push(line); continue; }
      if (!line.trim()) { flush(); continue; }
      if (BULLET.test(line)) { flush(); cur = { type: 'item', lines: [line] }; continue; }
      flush(); cur = { type: 'para', lines: [line] };
    }
    flush();
    return out;
  }

  // 超长段落分组（F8）：按完整的列表项、自然段或表格分组，每组不超过 1500 字；单个表格超长时按行拆，每组带表头
  // 整段检查发给模型的文字：去掉空行和行内格式、列表符号统一成「- 」，这样同一份 PRD 不论原来是什么格式，整段检查看到的文字都一样
  function normBody(lines) {
    const out = []; const fence = fenceTracker();
    for (const line of lines) {
      const f = fence(line);
      if (f === 'edge') { out.push('```'); continue; }
      if (f === 'in') { out.push(line); continue; }
      if (!line.trim()) continue;
      if (isTableRow(line)) { out.push(isTableSep(line) ? line.trim() : '| ' + cells(line).join(' | ') + ' |'); continue; }
      const q = line.replace(/^\s*>\s?/, '');
      out.push(BULLET.test(q) ? '- ' + plain(q.replace(BULLET, '')) : plain(q));
    }
    return out;
  }

  function groupSection(head, bodyLines) {
    bodyLines = normBody(bodyLines);
    const full = [head, ...bodyLines].join('\n');
    if (full.length <= GROUP_MAX) return [full];
    const room = GROUP_MAX - head.length - 1;
    // 单块仍超长（例如没放进代码块的字符画、特别长的一段）：按句子切，切不开就按字数切
    const chop = t => {
      if (t.length <= room) return [t];
      const out = []; let acc = '';
      for (const part of t.split(/(?<=[。！？；.!?;\n])/)) {
        for (let i = 0; i < part.length; i += room) {
          const p = part.slice(i, i + room);
          if (acc && (acc + p).length > room) { out.push(acc); acc = ''; }
          acc += p;
        }
      }
      if (acc) out.push(acc);
      return out;
    };
    const pieces = [];
    for (const b of blocks(bodyLines)) {
      const t = b.lines.join('\n');
      if (b.type !== 'table') { pieces.push(...chop(t)); continue; }
      if (t.length <= room) { pieces.push(t); continue; }
      const hdr = b.lines.slice(0, 2).join('\n');
      let acc = [];
      for (const row0 of b.lines.slice(2)) {
        for (const row of chop(row0).map(r => r.slice(0, Math.max(1, room - hdr.length - 1)))) {
          if ((hdr + '\n' + acc.concat(row).join('\n')).length > room && acc.length) { pieces.push(hdr + '\n' + acc.join('\n')); acc = []; }
          acc.push(row);
        }
      }
      if (acc.length) pieces.push(hdr + '\n' + acc.join('\n'));
    }
    const groups = []; let acc = '';
    for (const p of pieces) {
      if (acc && (head + '\n' + acc + '\n' + p).length > GROUP_MAX) { groups.push(head + '\n' + acc); acc = ''; }
      acc = acc ? acc + '\n' + p : p;
    }
    if (acc) groups.push(head + '\n' + acc);
    return groups;
  }

  // 按 #–#### 标题切段落；代码块里的行不算标题也不算需求（F7）；表格行转写成「表头：值」（F6）
  function splitPrd(text) {
    const lines = joinSoftWraps(String(text || '').replace(/\r\n?/g, '\n').trim().split('\n'));
    const raw = []; let cur = { head: null, body: [] }; const fence = fenceTracker();
    for (const line of lines) {
      const f = fence(line);
      if (!f && /^#{1,4} /.test(line)) { raw.push(cur); cur = { head: line, body: [] }; continue; }
      cur.body.push(line);
    }
    raw.push(cur);
    const sections = [];
    for (const r of raw) {
      const bodyText = r.body.join('\n').trim();
      if (!r.head && (!bodyText || bodyText.startsWith('>'))) continue;
      const title = r.head ? plain(r.head.replace(/^#+/, '').replace(/\s#+\s*$/, '')) : '（无标题）';
      const level = r.head ? r.head.match(/^#+/)[0].length : 1;
      const m = title.match(SKIP_TITLE);
      const reqs = []; let tableHdr = null; const fence = fenceTracker(); let codeLines = 0, images = 0;
      for (const line of r.body) {
        if (fence(line)) { codeLines++; continue; }
        images += (line.match(/!\[[^\]]*\]\([^)]*\)/g) || []).length;
        if (isTableRow(line)) {
          if (isTableSep(line)) continue;
          if (!tableHdr) { tableHdr = cells(line); continue; }
          const c = cells(line);
          const row = c.map((v, i) => `${tableHdr[i] || '列' + (i + 1)}：${v}`).filter((_, i) => c[i]).join('；');
          if (REQ.test(c.join(' ')) && row.length <= 300) reqs.push(row);
          continue;
        }
        tableHdr = null;
        if (!BULLET.test(line.replace(/^\s*>\s?/, '')) && !REQ.test(line)) continue;
        let l0 = line.replace(/^\s*>\s?/, '').replace(BULLET, '');
        if (/^\[[ xX]\]\s+/.test(l0)) l0 = l0.replace(/^\[[ xX]\]\s+/, '').replace(BULLET, '');  // 任务列表「- [x] 1. 某项」
        const l = plain(l0);
        if (keepReq(l)) reqs.push(l);
      }
      const head = r.head || '';
      const full = [head, ...r.body].join('\n').trim();
      const nonCode = r.body.filter(l => l.trim()).length - codeLines;
      sections.push({
        title, level, text: full, reqs, skip: !!m, skipReason: m ? m[0] : '',
        account: ACCOUNT.test(title) || ACCOUNT.test(bodyText),
        groups: groupSection(r.head ? '#'.repeat(level) + ' ' + title : '', r.body),
        chars: full.length, images,
        codeOnly: codeLines > 0 && nonCode <= 0,
      });
    }
    return sections;
  }

  // 一个段落要做的审查项：整段检查（≥2 条需求的功能段落）、账号与权限检查、每条需求的单句检查
  function jobsFor(sec, si) {
    const jobs = [];
    if (sec.skip || sec.off) return jobs;
    if (sec.reqs.length >= 2) sec.groups.forEach((g, gi) => jobs.push({ kind: 'doc', si, gi, text: g }));
    if (sec.account) sec.groups.forEach((g, gi) => jobs.push({ kind: 'account', si, gi, text: g }));
    sec.reqs.forEach((r, ri) => jobs.push({ kind: 'sentence', si, ri, text: r }));
    return jobs;
  }

  const api = { splitPrd, jobsFor, GROUP_MAX, REQ, ACCOUNT };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.PRDSplit = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);

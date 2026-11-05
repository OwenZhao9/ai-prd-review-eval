#!/bin/sh
# 格式一致性评测（F23）第 1 步：把 158 份 Markdown PRD 转成 Word、PPT、PDF。
# Word、PPT 用 pandoc 转；PDF 由转出的 Word 再用 LibreOffice 转，和用户「Word 另存为 PDF」的做法一致。
# PDF 共约 110 MB，不放进仓库，运行本脚本重新生成。
# 用法：sh data/format/convert.sh（需要 pandoc 和 LibreOffice）
set -e
cd "$(dirname "$0")"
mkdir -p docx pptx pdf
for f in ../raw/*.md ../raw_zh/*.md; do
  n=$(basename "$f" .md)
  [ -f "docx/$n.docx" ] || pandoc "$f" -f gfm -o "docx/$n.docx"
  [ -f "pptx/$n.pptx" ] || pandoc "$f" -f gfm --slide-level=2 -o "pptx/$n.pptx"
done
soffice --headless --convert-to pdf --outdir pdf docx/*.docx > /dev/null 2>&1
ls docx | wc -l; ls pptx | wc -l; ls pdf | wc -l

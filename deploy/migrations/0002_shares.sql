-- 只读分享链接：用户主动分享时保存审查结果（含 PRD 原文）7 天，过期删除
CREATE TABLE IF NOT EXISTS shares (
  id TEXT PRIMARY KEY,
  token TEXT NOT NULL,
  created INTEGER NOT NULL,
  expires INTEGER NOT NULL,
  data TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS shares_expires ON shares (expires);

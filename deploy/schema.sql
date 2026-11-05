-- 每天的模型调用次数：key 为 'all'（全站）或 'ip:<地址>'（单个访客）
CREATE TABLE IF NOT EXISTS usage (
  day TEXT NOT NULL,
  key TEXT NOT NULL,
  n INTEGER NOT NULL,
  PRIMARY KEY (day, key)
);

-- 审查结果下的「这是误判 / 漏了问题」反馈与复核结论
CREATE TABLE IF NOT EXISTS feedback (
  id TEXT PRIMARY KEY,
  time TEXT NOT NULL,
  created INTEGER NOT NULL,
  status TEXT NOT NULL,
  type TEXT NOT NULL,
  level TEXT NOT NULL,
  text TEXT NOT NULL,
  rule TEXT NOT NULL,
  note TEXT,
  predicted TEXT,
  versions TEXT,
  reason TEXT
);
CREATE INDEX IF NOT EXISTS feedback_created ON feedback (created);

-- 使用计数（第 7 节）：只记次数和类别，不记 PRD 内容、文件名、链接和访客地址
CREATE TABLE IF NOT EXISTS metrics (
  day TEXT NOT NULL,
  key TEXT NOT NULL,
  n INTEGER NOT NULL,
  PRIMARY KEY (day, key)
);
CREATE TABLE IF NOT EXISTS shares (
  id TEXT PRIMARY KEY,
  token TEXT NOT NULL,
  created INTEGER NOT NULL,
  expires INTEGER NOT NULL,
  data TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS shares_expires ON shares (expires);

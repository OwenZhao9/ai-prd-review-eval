-- 在线库从旧结构升级：反馈记录加规则版本和驳回原因（F19），新增使用计数表（第 7 节）
ALTER TABLE feedback ADD COLUMN versions TEXT;
ALTER TABLE feedback ADD COLUMN reason TEXT;
CREATE TABLE IF NOT EXISTS metrics (
  day TEXT NOT NULL,
  key TEXT NOT NULL,
  n INTEGER NOT NULL,
  PRIMARY KEY (day, key)
);

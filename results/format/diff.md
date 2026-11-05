# 格式一致性评测：不一致的条目

由 `data/format/eval.mjs` 生成。每份 PRD 只列前 10 处差异。

## docx

### ScionResearch__multi-material-printer

段落标题一致，需求条目 97 / 102 一致（docx 拆出 97 条）

- 需求只在 Markdown：Pause printer (retry x3 w/ exponential backoff 0.5/1/2 s).
- 需求只在 Markdown：Wait (config: plate_clear_delay_s).
- 需求只在 Markdown：Drain pump run until computed duration = drain_volume_ml / drain_rate_ml_per_s (±5% tolerance).
- 需求只在 Markdown：Fill pump run similarly (selected material).
- 需求只在 Markdown：Settling delay (settle_delay_s).

### Ariestar__obsidian-dragger

段落标题不一致，需求条目 150 / 150 一致（docx 拆出 241 条）

- 标题只在 docx：13.5 PipelineOutput
- 标题只在 docx：13.6 Lifecycle Rules
- 标题只在 docx：13.7 Internal reducer
- 标题只在 docx：13.8 Target drag file architecture
- 标题只在 docx：13.9 Drag layer rules
- 需求只在 docx：hold_start 的 target 必须已经是平台无关的 HoldTarget。
- 需求只在 docx：selection_start/change 只接收 domain boundary，不接收 DOM 坐标。
- 需求只在 docx：drag_start 只表示真正进入 drag，不表示 pointerdown。
- 需求只在 docx：drop 只接收 platform 已解析好的 DropResolution。
- 需求只在 docx：mobile text long press、desktop handle press、mobile virtual resize handle 都只是不同的输入翻译，不是不同 pipeline。
- 需求只在 docx：CSS class / selector / DOM node
- 需求只在 docx：platform 可以把 drag_over 翻译成 preview DOM 更新，可以把 selection_changed 翻译成 passive selection visual 更新，可以把 drag_source_changed 翻译成当前 drag source visual 更新，可以把 terminal 翻译成 pointer capture / scroll lock / input guard 清理。
- 需求只在 docx：完整生命周期必须由 DragPipeline 维护。
- 需求只在 docx：已选 range 启动 drag 时，不走独立 pipeline，也不使用独立 drag origin。
- 需求只在 docx：holding/ready_to_drag 如果来自 passive selection，必须由 pipeline state 保留 retainedSelection；press cancel 回到 selecting(passive)，不能让 platform 重新拼一份 selection。

### FLYFISH567__ItemMemo

段落标题一致，需求条目 108 / 116 一致（docx 拆出 116 条）

- 需求只在 Markdown：理性消费用户
- 需求只在 Markdown：精致生活 / 收纳管理用户
- 需求只在 Markdown：数码 / 家居 / 装备爱好者
- 需求只在 Markdown：年轻上班族 / 学生
- 需求只在 Markdown：需要一个轻量工具帮助自己管理生活和消费。
- 需求只在 docx：理性消费用户 希望知道买的东西到底值不值，愿意做消费复盘。
- 需求只在 docx：精致生活 / 收纳管理用户 有整理习惯，愿意把生活物品数字化管理。
- 需求只在 docx：数码 / 家居 / 装备爱好者 购买金额高、物品使用周期长，更关心长期价值。
- 需求只在 docx：年轻上班族 / 学生 需要一个轻量工具帮助自己管理生活和消费。
- 需求只在 docx：固定周期提醒 用于有明确更换周期的物品，如牙刷、刀头、护肤品等。
- 需求只在 docx：持有时间提醒 当持有时间达到阈值时提示关注。
- 需求只在 docx：高日均成本提醒 价格较高但持有时间较短，提示关注物品使用效率。
- 需求只在 docx：补购提醒 针对消耗型物品，提醒及时补购。

### FlashingChen__dsh-desktop-hub

段落标题一致，需求条目 53 / 54 一致（docx 拆出 53 条）

- 需求只在 Markdown：决策点：插件操作通道；选择（已落地）：主进程 spawn dsh plugin --profile web add；理由：remove；列4：update（进程树托管、输出流回 UI、支持取消）；列5：与 anywhere-labs desktopPnpm.runPlugin() 同构；dsh 是 bundle reconcile 的权威

### Frank-ay__mimo-mcp

段落标题一致，需求条目 61 / 62 一致（docx 拆出 62 条）

- 需求只在 Markdown：新增 tts_stream(text, voice, *, model, audio_format, opts) -> AsyncIterator[bytes](若 R1 显示不支持流式,则保留 stub 抛 NotSupportedError,此时前端 fallback 一次性)
- 需求只在 docx：新增 tts_stream(text, voice, *, model, audio_format, opts) -> AsyncIteratorbytes

### G1-kiyo__agent

段落标题一致，需求条目 106 / 107 一致（docx 拆出 107 条）

- 需求只在 Markdown：用户输入问题后，AI Agent自主决策是否需要搜索、搜索什么、何时结束并生成答案。
- 需求只在 docx：需求描述： 用户输入问题后，AI Agent自主决策是否需要搜索、搜索什么、何时结束并生成答案。

### JetQiao__football-prediction-skill

段落标题一致，需求条目 127 / 133 一致（docx 拆出 133 条）

- 需求只在 Markdown：将来若想做实时常驻 App，JSON 已现成可用，零锁定——但当前需求并不需要它。
- 需求只在 Markdown：~~产品形态~~ → Skill 优先的混合架构（核心 Skill + 可选薄前端，见 §2）。
- 需求只在 Markdown：~~联赛覆盖范围~~ → 竞彩当日全部场次全覆盖（情报分层为强制，见 §4.3）。
- 需求只在 Markdown：~~历史回测数据~~ → football-data.co.uk（免费 CSV，含 Pinnacle 收盘赔率，25+ 联赛）。
- 需求只在 Markdown：~~竞彩抓取 + 价值计算~~ → SportteryAPI（MIT，可直接复用）+ 官方接口。
- 需求只在 Markdown：~~评分/xG/伤病源~~ → clubelo + understat/soccerdata + API-Football，均免费。
- 需求只在 docx：📌 这是一份"每日快照报告"模式：每天跑一次 Skill → 一个可离线、可转发、可存档的 HTML。 将来若想做实时常驻 App，JSON 已现成可用，零锁定——但当前需求并不需要它。
- 需求只在 docx：产品形态 → Skill 优先的混合架构（核心 Skill + 可选薄前端，见 §2）。
- 需求只在 docx：联赛覆盖范围 → 竞彩当日全部场次全覆盖（情报分层为强制，见 §4.3）。
- 需求只在 docx：历史回测数据 → football-data.co.uk（免费 CSV，含 Pinnacle 收盘赔率，25+ 联赛）。
- 需求只在 docx：竞彩抓取 + 价值计算 → SportteryAPI（MIT，可直接复用）+ 官方接口。
- 需求只在 docx：评分/xG/伤病源 → clubelo + understat/soccerdata + API-Football，均免费。

### Jonnyan404__clip9

段落标题一致，需求条目 0 / 8 一致（docx 拆出 0 条）

- 需求只在 Markdown：#[test] fn csv_converts_to_a_markdown_table() { let csv = b"name,qty\napple,3\npear,5\n"; let out = to_markdown(csv, Some("fruit.csv")).expect("CSV 应当能转"); assert!(out.contains("apple"), "结果里应当有数据：{out}"); assert!(out.contains('|'), "CSV 应当转成表格：{out}"); }
- 需求只在 Markdown：// 正文一个字都不能丢（也不许变成乱码）。 for expected in [ "产品需求文档", "这是一份中文需求文档，用来验证标题层级能不能被识别。", "背景", "用户反馈白板功能缺失，需要补齐。", "验收标准", "标题要变成树形节点，正文要成为卡片。", ] { assert!( out.contains(expected), "转出来的 Markdown 里没有「{expected}」：\n{out}" ); }
- 需求只在 Markdown：/// CSV 没有签名 —— 不给出名字就认不出来。这条差异要可见，不能靠猜。 #[test] fn csv_without_a_filename_is_unsupported() { let csv = b"name,qty\napple,3\n"; let error = to_markdown(csv, None).expect_err("无名 CSV 应当认不出来"); assert!( matches!(error, ActionError::InvalidInput(ref message) if message.contains("格式")), "{error}" ); }
- 需求只在 Markdown：#[test] fn empty_input_is_rejected_before_parsing() { let error = to_markdown(b"", Some("empty.docx")).expect_err("空文件应当报错"); assert!( matches!(error, ActionError::InvalidInput(ref message) if message.contains("空的")), "{error}" ); }
- 需求只在 Markdown：assert!( !converted.markdown.contains("!["), "上游开始输出 Markdown 图片了？那 extract_images 这趟解析可以撤掉：\n{}", converted.markdown ); assert!( converted.markdown.contains("图之后还有一段文字"), "正文不能少" );
- 需求只在 Markdown：let images = converted .images .expect("docx 应当读得出文档模型（PDF 才是 None）"); assert_eq!(images.total, 1, "应当找到 1 张图"); assert_eq!(images.items.len(), 1, "预算足够，不该截断"); assert!(!images.truncated);
- 需求只在 Markdown：fn a_document_without_images_reports_an_empty_set_not_none() { let converted = convert(&chinese_docx(), Some("需求.docx")).expect("应当能转"); let images = converted.images.expect("docx 读得出文档模型"); assert_eq!(images.total, 0); assert!(images.items.is_empty()); assert!(!images.truncated); }
- 需求只在 Markdown：// 预算刚好够：一张都不截 let (items, truncated) = cap_images(&refs[..1], 10); assert!(!truncated); assert_eq!(items.len(), 1, "预算正好等于大小应当装得下（边界不是越界）");

### Jwz-git__Daygo

段落标题一致，需求条目 19 / 20 一致（docx 拆出 20 条）

- 需求只在 Markdown：跟随光标需要显示器枚举、滞后判定和跨调用状态，而截图原语被有意设计成无状态的单次调用
- 需求只在 docx：F-C1 曾写成"跟随光标的活跃显示器"。原生契约冻结时把它改成了系统主显示器： 跟随光标需要显示器枚举、滞后判定和跨调用状态，而截图原语被有意设计成无状态的单次调用 （决策）。对单显示器用户没有区别； 多显示器用户在 v1 只会记录到主显示器。是否恢复跟随行为是一个待决产品问题（§1.7）， 不是实现遗漏。

### L20081125__dsh-lite-theme

段落标题一致，需求条目 50 / 52 一致（docx 拆出 52 条）

- 需求只在 Markdown：v1.1 变更：移除 TUI 支持（用户要求仅 Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 Markdown：~~TUI 端~~：v0.2 起已移除（用户决策：仅支持 Web）。
- 需求只在 docx：版本：v1.1（2026-08-16）｜状态：已评审（4 轮需求反问）+ 实现同步（v0.2） v1.1 变更：移除 TUI 支持（用户要求仅 Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 docx：TUI 端：v0.2 起已移除（用户决策：仅支持 Web）。

### NewLifeX__AntJob

段落标题一致，需求条目 68 / 69 一致（docx 拆出 69 条）

- 需求只在 Markdown：WEB-2a 蚂蚁区域注册：Cube 区域"蚂蚁调度"，AntEntityController\<T> 基类支持 appId 导航栏。
- 需求只在 docx：WEB-2a 蚂蚁区域注册：Cube 区域"蚂蚁调度"，AntEntityController<T> 基类支持 appId 导航栏。

### NewLifeX__NewLife.BACnet

段落标题一致，需求条目 100 / 100 一致（docx 拆出 101 条）

- 需求只在 docx：以下串口传输实现代码存在但已从编译中排除，需跨平台串口兼容性支持后重新启用： TRN-5 MS/TP (RS485) 串口传输、TRN-6 PTP (RS232) 串口传输、TRN-7 通用串口传输基类、 TRN-8 Ethernet 802.3 直连传输、TRN-9 Windows 管道传输

### NewLifeX__X

段落标题一致，需求条目 135 / 136 一致（docx 拆出 136 条）

- 需求只在 Markdown：M5-10 系统配置：SysConfig 基于 Config<T> 的系统名称、版本、显示名称等基本设置管理。
- 需求只在 docx：M5-10 系统配置：SysConfig 基于 Config 的系统名称、版本、显示名称等基本设置管理。

### StoneLL1__llm-wiki-desktop

段落标题一致，需求条目 200 / 202 一致（docx 拆出 200 条）

- 需求只在 Markdown：导入、来源库、本地与远程媒体、OCR、ASR、平台登录态和 AI 整理的已确认产品决策，以 ../docs/superpowers/specs/2026-07-24-import-source-media-flow-design.md 为唯一可信源。本文中的概览不得被解释为"确认导入后自动编译"。
- 需求只在 Markdown：无项目工作台、新建知识库、打开原生或兼容知识库、目录评估、信任 / 受限 / 只读、兼容启用、修复与进入 Import 的已确认产品决策，以 ../docs/superpowers/specs/2026-07-30-first-run-project-open-workbench-design.md 为唯一可信源。本文中的摘要不得被解释为允许把普通资料文件夹原地初始化成项目。

### calderbuild__MD_Audit

段落标题一致，需求条目 99 / 100 一致（docx 拆出 100 条）

- 需求只在 Markdown：过滤掉 "http://", "www.", "class=", "<div>" 等技术术语
- 需求只在 docx：过滤掉 "http://", "www.", "class=", "" 等技术术语

### entropy-cloud__nop-entropy

段落标题一致，需求条目 22 / 24 一致（docx 拆出 23 条）

- 需求只在 Markdown：需求编号：按章节+序号分级（如FR2.1=功能需求3.2节第1条）。
- 需求只在 Markdown：来源：标注原始文档章节及问题编号（如3.1-Q4）。
- 需求只在 docx：结构化字段： > - 需求编号：按章节+序号分级（如FR2.1=功能需求3.2节第1条）。 > - 来源：标注原始文档章节及问题编号（如3.1-Q4）。

### gitxuzhefeng__timelines

段落标题不一致，需求条目 124 / 127 一致（docx 拆出 137 条）

- 标题只在 docx：今天记录： 09:00 VSCode - main.ts 09:30 Chrome - GitHub Pull Request 10:00 Zoom - Team Standup 10:30 Slack - #general ...
- 标题只在 docx：3.1.4 核心接口 接口 说明 参数 返回 start_tracking() 开始追踪
- 标题只在 docx：Result<()> stop_tracking() 停止追踪
- 标题只在 docx：Result<()> get_current_window() 获取当前窗口
- 标题只在 docx：六、开发任务分发 6.1 角色与职责 角色 人数 职责 前端开发 1人 M04, M10 前端部分 后端开发 1人 M06, M07, M08, M09 客户端开发 1人 M01, M02, M03, M05 全栈开发 1人 协调 + 部署 + 测试 6.2 任务分配表 开发人员 A: 客户端开发 (Client) 任务 ID 任务名称 模块 描述 预计工时 T-001 环境搭建
- 需求只在 Markdown：开发环境准备 工具 用途 要求 Node.js 18+ 前端开发、API 服务 必须 Rust 1.70+ Tauri 客户端核心 必须 pnpm / npm 包管理 推荐 pnpm Git 版本控制 必须 VS Code 开发 IDE 推荐 Docker 本地数据库/服务 可选 检查命令： node --version    # 需要 >= 18 rustc --version   # 需要 >= 1.70 pnpm --version
- 需求只在 Markdown：GET /api/v1/data/daily // Query Parameters interface DailyQueryParams { date: string;  // YYYY-MM-DD userId?: string;  // 自己的不需要传 }
- 需求只在 Markdown：推送配置 3.10.2 设置项定义 interface AppSettings { // 追踪设置 tracking: { enabled: boolean; pauseOnLock: boolean;      // 锁屏时暂停 pauseOnIdle: boolean;      // 空闲时暂停 idleThreshold: number;     // 空闲阈值（分钟） };
- 需求只在 docx：Windows: GetForegroundWindow + GetWindowText 数据结构： struct WindowEvent { timestamp: i64, // Unix ms app_name: String, // "VSCode" app_bundle: Option, // "com.microsoft.VSCode" window_title: String, // "main.ts - myproject" duration_ms: i64, // 持续时间 is_active: bool, // 是否正在使用 }
- 需求只在 docx：部署架构 ┌─────────────────────────────────────────────────────────┐ │ 开发阶段 │ ├─────────────────────────────────────────────────────────┤ │ 客户端 → Vercel Serverless → PostgreSQL (Supabase) │ │ ↓ │ │ 飞书测试号 │ └─────────────────────────────────────────────────────────┘
- 需求只在 docx：开发环境准备 工具 用途 要求 Node.js 18+ 前端开发、API 服务 必须 Rust 1.70+ Tauri 客户端核心 必须 pnpm / npm 包管理 推荐 pnpm Git 版本控制 必须 VS Code 开发 IDE 推荐 Docker 本地数据库/服务 可选 检查命令： node --version # 需要 >= 18 rustc --version # 需要 >= 1.70 pnpm --version
- 需求只在 docx：// 序列化 + 压缩 let json = serde_json::to_string(&events)?; let compressed = gzip_compress(json.as_bytes())?;
- 需求只在 docx：// 加密 let encrypted = aes_encrypt(compressed, get_encryption_key())?;
- 需求只在 docx：Ok(CompressedPackage { date: date.to_string(), data: encrypted, checksum: md5(&compressed), events_count: events.len(), }) }
- 需求只在 docx：Token 管理 3.6.2 API 接口 接口 方法 说明 鉴权 /api/v1/user/login POST 飞书 OAuth 登录
- 需求只在 docx：GET /api/v1/data/daily // Query Parameters interface DailyQueryParams { date: string; // YYYY-MM-DD userId?: string; // 自己的不需要传 }
- 需求只在 docx：推送配置 3.10.2 设置项定义 interface AppSettings { // 追踪设置 tracking: { enabled: boolean; pauseOnLock: boolean; // 锁屏时暂停 pauseOnIdle: boolean; // 空闲时暂停 idleThreshold: number; // 空闲阈值（分钟） };
- 需求只在 docx：// 截屏设置 screenshot: { enabled: boolean; onWindowSwitch: boolean; // 切换窗口时截屏 interval: number; // 定时截屏间隔（分钟） quality: number; // 质量 0-100 blurSensitive: boolean; // 模糊敏感内容 };

### hackmagic__opennavicat

段落标题一致，需求条目 117 / 122 一致（docx 拆出 122 条）

- 需求只在 Markdown：~~统一错误模型~~ ✅ open_navicat/errors.py
- 需求只在 Markdown：~~分层核心骨架~~ ✅ open_navicat/drivers/（BaseConnector + registry.py，连接池引擎分支已删）
- 需求只在 Markdown：~~查询取消 / 超时~~ ✅ CancelToken + timeout=（取消为 asyncio.wait 显竞速，勿用嵌套 ensure_future）
- 需求只在 Markdown：~~数据库驱动扩展骨架~~ ✅ 注册表查表 + 连接串解析（drivers/dsn.py）
- 需求只在 Markdown：~~DuckDB / SQL Server / ClickHouse / Oracle 支持~~ ✅（ClickHouse、Oracle 于 2026-09-30 完成；GUI 连接对话框引擎下拉框已接注册表）
- 需求只在 docx：统一错误模型 ✅ open_navicat/errors.py
- 需求只在 docx：分层核心骨架 ✅ open_navicat/drivers/（BaseConnector + registry.py，连接池引擎分支已删）
- 需求只在 docx：查询取消 / 超时 ✅ CancelToken + timeout=（取消为 asyncio.wait 显竞速，勿用嵌套 ensure_future）
- 需求只在 docx：数据库驱动扩展骨架 ✅ 注册表查表 + 连接串解析（drivers/dsn.py）
- 需求只在 docx：DuckDB / SQL Server / ClickHouse / Oracle 支持 ✅（ClickHouse、Oracle 于 2026-09-30 完成；GUI 连接对话框引擎下拉框已接注册表）

### junerver__ComposeHooks

段落标题一致，需求条目 43 / 45 一致（docx 拆出 43 条）

- 需求只在 Markdown：适配 §3.2 的 hooks（useRequest/useForm/useRedux 的反射问题）。
- 需求只在 Markdown：为 §3.3 的 hooks 提供 wasmJs actual 实现（usePersistent 的 localStorage 适配）。

### qtgf520__kai-qt

段落标题一致，需求条目 98 / 114 一致（docx 拆出 114 条）

- 需求只在 Markdown：1. 更改提供商名称 ✅ 已有：renameServiceInstance + displayName 持久化，设置页可编辑，全局生效（v3.2.2 已实现）
- 需求只在 Markdown：2. 思考强度按钮 ✅ 已实现：设置页「思考强度」选择器（默认/低/中低/中/高/最高），写入 reasoning_effort 请求体（v3.2.3+）
- 需求只在 Markdown：3. 流式输出开关 ✅ 已实现：设置页「流式输出」开关，关闭时 stream=false 整体渲染（v3.2.3+）
- 需求只在 Markdown：4. 提示词字数上限 ✅ 已满足：输入框无字符硬截断，文件上限 200KB（20 万字符级），超长内容完整发送
- 需求只在 Markdown：5.1 重新生成 ✅ 已有：BotMessage onRegenerate 按钮，保留上下文重新请求
- 需求只在 Markdown：5.2 修改消息 ✅ 已实现：用户消息下方「编辑」按钮，就地变输入框，保存后截断旧回复并自动重新生成（v3.2.3-3）
- 需求只在 Markdown：5.3 复制消息 ✅ 已有：BotMessage 复制按钮（含代码块复制）
- 需求只在 Markdown：5.4 删除消息 ✅ 已实现：每条消息操作栏「删除」按钮（AI 消息 × 图标 / 用户消息文字），删除单条及其配套工具行，自动保存（v3.2.3-2）
- 需求只在 Markdown：6. 上下文压缩 ✅ 已有：compactHistoryIfNeeded（70% 阈值自动摘要 + 保留最近 4 轮）
- 需求只在 Markdown：7. Skill 功能 ✅ 已有：完整 skills 包（SkillManager/Registry/Marketplaces/前端 SkillsSection）
- 需求只在 docx：更改提供商名称 ✅ 已有：renameServiceInstance + displayName 持久化，设置页可编辑，全局生效（v3.2.2 已实现）
- 需求只在 docx：思考强度按钮 ✅ 已实现：设置页「思考强度」选择器（默认/低/中低/中/高/最高），写入 reasoning_effort 请求体（v3.2.3+）
- 需求只在 docx：流式输出开关 ✅ 已实现：设置页「流式输出」开关，关闭时 stream=false 整体渲染（v3.2.3+）
- 需求只在 docx：提示词字数上限 ✅ 已满足：输入框无字符硬截断，文件上限 200KB（20 万字符级），超长内容完整发送
- 需求只在 docx：☒ 5.1 重新生成 ✅ 已有：BotMessage onRegenerate 按钮，保留上下文重新请求
- 需求只在 docx：☒ 5.2 修改消息 ✅ 已实现：用户消息下方「编辑」按钮，就地变输入框，保存后截断旧回复并自动重新生成（v3.2.3-3）
- 需求只在 docx：☒ 5.3 复制消息 ✅ 已有：BotMessage 复制按钮（含代码块复制）
- 需求只在 docx：☒ 5.4 删除消息 ✅ 已实现：每条消息操作栏「删除」按钮（AI 消息 × 图标 / 用户消息文字），删除单条及其配套工具行，自动保存（v3.2.3-2）
- 需求只在 docx：上下文压缩 ✅ 已有：compactHistoryIfNeeded（70% 阈值自动摘要 + 保留最近 4 轮）
- 需求只在 docx：Skill 功能 ✅ 已有：完整 skills 包（SkillManager/Registry/Marketplaces/前端 SkillsSection）

### raceychan__lihil

段落标题一致，需求条目 75 / 76 一致（docx 拆出 76 条）

- 需求只在 Markdown：字段：ref；类型：string | null；必填：否；说明：若是请求响应，必须回填客户端 ref
- 需求只在 docx：字段：ref；类型：string ／ null；必填：否；说明：若是请求响应，必须回填客户端 ref

### shangbian__Enterprise-Brain-Platform

段落标题不一致，需求条目 23 / 23 一致（docx 拆出 23 条）

- 标题只在 docx：四、整体业务流程图
- 标题只在 docx：五、需求详细说明

### terryso__tv-recommender-mcp-server

段落标题不一致，需求条目 88 / 88 一致（docx 拆出 88 条）

- 标题只在 Markdown：Potential Tool Response Structure (Conceptual)

### tyrchen__index-tts-rs

段落标题一致，需求条目 35 / 40 一致（docx 拆出 40 条）

- 需求只在 Markdown：指标项：Daemon 热态请求响应开销；原版 Python index-tts-2.5-mlx：不支持（每次重跑进程）；index-tts-rs 目标值：$\le$ 5 ms；核心实现手段：Unix Domain Socket + 内存常驻 DashMap 音色池
- 需求只在 Markdown：DSP 特征（mel_spectrogram、campplus_fbank、w2v_features）：余弦相似度 $\ge 0.9999$，最大绝对误差 $< 10^{-4}$。
- 需求只在 Markdown：SpeakerContext 各张量：余弦相似度 $\ge 0.9995$。
- 需求只在 Markdown：Greedy GPT 生成的 Semantic Codes：100% 序列一致（或在浮点边界步重合率 $\ge 99\%$）。
- 需求只在 Markdown：CFM Mel 频谱（给定相同初始噪声 z）与 BigVGAN 输出波形：余弦相似度 $\ge 0.999$，听感完全无退化、无拼接爆音。
- 需求只在 docx：指标项：Daemon 热态请求响应开销；原版 Python index-tts-2.5-mlx：不支持（每次重跑进程）；index-tts-rs 目标值：5 ms；核心实现手段：Unix Domain Socket + 内存常驻 DashMap 音色池
- 需求只在 docx：DSP 特征（mel_spectrogram、campplus_fbank、w2v_features）：余弦相似度 ，最大绝对误差 。
- 需求只在 docx：SpeakerContext 各张量：余弦相似度 。
- 需求只在 docx：Greedy GPT 生成的 Semantic Codes：100% 序列一致（或在浮点边界步重合率 ）。
- 需求只在 docx：CFM Mel 频谱（给定相同初始噪声 z）与 BigVGAN 输出波形：余弦相似度 ，听感完全无退化、无拼接爆音。

### weiwei929__wireguard_plus

段落标题一致，需求条目 98 / 102 一致（docx 拆出 101 条）

- 需求只在 Markdown：作为一个 需要绕过网络限制的用户
- 需求只在 Markdown：我希望 能够简单地部署一个伪装的WireGuard服务
- 需求只在 Markdown：我希望 能够批量管理多个用户的VPN配置
- 需求只在 Markdown：我希望 能够扩展新的伪装模块
- 需求只在 docx：作为一个 需要绕过网络限制的用户 我希望 能够简单地部署一个伪装的WireGuard服务 以便于 在受限网络环境下正常使用VPN服务
- 需求只在 docx：作为一个 系统管理员 我希望 能够批量管理多个用户的VPN配置 以便于 为组织提供统一的VPN服务
- 需求只在 docx：作为一个 网络工具开发者 我希望 能够扩展新的伪装模块 以便于 适应不断变化的网络环境

### wukun2005-gif__patentExaminator

段落标题一致，需求条目 127 / 128 一致（docx 拆出 128 条）

- 需求只在 Markdown：~~反馈系统~~：已删除（用户要求），满意度评估改为 Metrics 体系自动指标（Groundedness、Faithfulness 等）
- 需求只在 docx：反馈系统：已删除（用户要求），满意度评估改为 Metrics 体系自动指标（Groundedness、Faithfulness 等）

### yuqie6__WorkMirror

段落标题一致，需求条目 121 / 132 一致（docx 拆出 121 条）

- 需求只在 Markdown：Local-first & Privacy by default：数据本地；敏感项默认最小化/可脱敏
- 需求只在 Markdown：证据链优先于结论：任何结论必须可点开看到来源覆盖率
- 需求只在 Markdown：失败可见且可操作：空态/异常/降级必须解释原因并给出下一步
- 需求只在 Markdown：Session 为权威路径：所有上层输出统一口径，避免多套"都能跑但不一致"
- 需求只在 Markdown：离线可用：无 AI Key 时仍能产出"规则回顾"，且 UI 明确标注能力差异
- 需求只在 Markdown：托盘 → 打开面板
- 需求只在 Markdown：选择/确认要监控的 Git 项目目录（Diff watch paths）
- 需求只在 Markdown：选择是否启用浏览器采集（并展示自动探测结果）
- 需求只在 Markdown：选择隐私模式：默认开启脱敏（提供推荐规则模板）
- 需求只在 Markdown：选择 AI 模式：离线（默认）或配置 API Key（可跳过）

### ywq2019__ai_test_agent

段落标题一致，需求条目 110 / 111 一致（docx 拆出 111 条）

- 需求只在 Markdown：Docker \& Docker Compose：支持容器化快速部署
- 需求只在 docx：Docker & Docker Compose：支持容器化快速部署

## pptx

### Bytepute__endpointForge

段落标题不一致，需求条目 170 / 170 一致（pptx 拆出 178 条）

- 标题只在 Markdown：Project
- 标题只在 Markdown：Controller / Route Group
- 标题只在 Markdown：Endpoint
- 标题只在 Markdown：First-Time User Flow
- 标题只在 Markdown：Returning User Flow
- 标题只在 pptx：第 2 页
- 需求只在 pptx："Ship frontend flows before the backend exists."
- 需求只在 pptx：A project is the top-level workspace for a mock API surface. It groups routes for a product, feature, demo, or test scenario.
- 需求只在 pptx：A controller is a route group under a project. It represents a base path such as /users, /products, or /orders.
- 需求只在 pptx：Current implementation note: the frontend model includes endpoints, but controller service currently maps this to an empty array because the backend response does not include endpoint counts yet.
- 需求只在 pptx：An endpoint belongs to a controller/route group and defines the mock behavior for a route.
- 需求只在 pptx：If either condition fails, the app redirects to the root domain.
- 需求只在 pptx：{protocol}://{username}.{app-domain}{optional-port}/projects
- 需求只在 pptx：The frontend expects a backend API at VITE_API_URL.

### GoForthTechnology__RoomBooker

段落标题不一致，需求条目 30 / 30 一致（pptx 拆出 34 条）

- 标题只在 Markdown：Epic: User Authentication & Guest Access
- 标题只在 Markdown：Epic: Room Reservation Management
- 标题只在 Markdown：Functional Requirements
- 标题只在 Markdown：Non-Functional Requirements
- 标题只在 Markdown：Infrastructure as Code (IaC)
- 需求只在 pptx：The primary users of this application are members of an organization (e.g., employees, students, or community members) who need to reserve shared spaces for meetings, study sessions, or other events.
- 需求只在 pptx：Epic: User Authentication & Guest Access
- 需求只在 pptx：Epic: Room Reservation Management
- 需求只在 pptx：Continuous Integration & Deployment (CI/CD)

### JulioBorges__gantry

段落标题不一致，需求条目 25 / 25 一致（pptx 拆出 35 条）

- 标题只在 Markdown：6.1 Preflight and models (orchestrator, inline)
- 标题只在 Markdown：6.2 Readiness of the spec (scripts, then a critic)
- 标题只在 Markdown：6.3 Planning (/gantry-plan)
- 标题只在 Markdown：6.4 Rounds (round workflow)
- 标题只在 Markdown：6.5 After the last round
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 14 页
- 标题只在 pptx：第 18 页
- 需求只在 pptx：What it is: a harness-neutral skill pack that runs an agentic software development life cycle inside the operator's coding harness. Deterministic scripts decide which work is ready and whether a delivery is done; agents plan, build, review and refute; the operator decides, in the conversation.
- 需求只在 pptx：Status: requirements agreed on 2026-09-12 (see ADR-0004). The pack evolved from the asdlc skill in this repository (§14). A harness tier is announced only after the fixture exercises it (§13). Vocabulary is defined in CONTEXT.md and is used here without redefinition.
- 需求只在 pptx：Scripts are Python 3.10+ standard library only and need nothing from the harness beyond python3 and git (gh for the run pull request). Cleanup and the Learner are steps of gantry, not skills.
- 需求只在 pptx：This repository is the pack: the four directories above are real directories under .agents/skills/, with .claude/, .cursor/, .opencode/ and .gemini/ skill directories symlinked to it. It also holds fixture/ (§13), docs/adr/, CONTEXT.md, AGENTS.md and this document.
- 需求只在 pptx：6.1 Preflight and models (orchestrator, inline)
- 需求只在 pptx：6.2 Readiness of the spec (scripts, then a critic)
- 需求只在 pptx：If every issue in a round completes, the next round starts without asking. Otherwise the run stops after the round and reports; later rounds may depend on what failed.
- 需求只在 pptx：6.6 Results and protocol failures
- 需求只在 pptx：The setup skill enables recording hooks by default and asks before enabling denying ones. A hook that fires in a harness where the payload lacks a field it needs degrades to recording and says so in the run log.
- 需求只在 pptx：The effective template is the source of structural validation: changing the template is changing the check.

### MrThief123__care-compass

段落标题不一致，需求条目 62 / 62 一致（pptx 拆出 68 条）

- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 22 页
- 需求只在 pptx：No other staff types need access (CIS5 Q&A).
- 需求只在 pptx：Each requirement links to sources and to the features that implement it. Requirements marked "Not scheduled" are confirmed needs without design or priority; they appear in the Parking lot (§17).
- 需求只在 pptx：Common states (States sheet): empty ("All caught up", "No patients assigned yet"), search no-results, list and card skeletons, error with Retry, destructive confirmation modal.
- 需求只在 pptx：Enforcement: database RLS (ADR-01–03); UI controls absent for disallowed actions.
- 需求只在 pptx：Note: OOS-5 (rostering out of scope) is superseded by later client meetings and designs — see OQ-21.
- 需求只在 pptx：Chain: Source → REQ-xx → Phase → Feature (F0/FAM/CAR/ADM/INT) → User story (US-xx) → Acceptance criterion (AC-xx) → Test (T-xx) → Implementation. REQ ↔ feature mapping is in §5; feature ↔ story ↔ AC ↔ test mapping is inside each feature folder.

### ScionResearch__multi-material-printer

段落标题不一致，需求条目 97 / 102 一致（pptx 拆出 145 条）

- 标题只在 Markdown：Executive Summary (Added)
- 标题只在 Markdown：Revision History (Added)
- 标题只在 Markdown：1. Introduction
- 标题只在 Markdown：2. Product Goals & Objectives
- 标题只在 Markdown：3. User Personas
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 需求只在 Markdown：Pause printer (retry x3 w/ exponential backoff 0.5/1/2 s).
- 需求只在 Markdown：Wait (config: plate_clear_delay_s).
- 需求只在 Markdown：Drain pump run until computed duration = drain_volume_ml / drain_rate_ml_per_s (±5% tolerance).
- 需求只在 Markdown：Fill pump run similarly (selected material).
- 需求只在 Markdown：Settling delay (settle_delay_s).
- 需求只在 pptx：Version: 1.0 Date: September 26, 2025 Author: AI Architect Status: DraftDocument Owner: AI Architect / Engineering Lead
- 需求只在 pptx：This document outlines the requirements for Version 1.0, which focuses on delivering a stable, reliable, and user-friendly experience primarily through a modern web-based interface.
- 需求只在 pptx：The primary goal of this project is to create a reliable and accessible tool for researchers and technicians to conduct multi-material 3D printing experiments.
- 需求只在 pptx：Objective 1: Automate the Multi-Material Workflow: Provide a "set it and forget it" system that reliably executes a pre-defined sequence of material changes over the course of a long print job.
- 需求只在 pptx：Objective 2: Ensure System Stability: The software must be robust enough to run for 24+ hours without crashing and gracefully handle common errors like temporary network disconnects.
- 需求只在 pptx：Objective 3: Provide a User-Friendly Interface: The primary interface (web application) must be intuitive for non-developers, allowing for easy recipe creation, print monitoring, and manual control.
- 需求只在 pptx：Objective 4: Deliver Clear, Real-Time Feedback: The user must always have a clear understanding of the system's current state, the action it is performing, and a log of past events.
- 需求只在 pptx：Objective 5 (Added): Provide auditable logs enabling post-run reconstruction of every material change event.
- 需求只在 pptx：1. Dr. Elena Vance (Research Scientist)
- 需求只在 pptx：Role: Primary user who designs the multi-material experiments.

### closedloop-technologies__climbhill

段落标题不一致，需求条目 125 / 125 一致（pptx 拆出 192 条）

- 标题只在 Markdown：5.1 In Scope
- 标题只在 Markdown：5.2 Out Of Scope For Initial Release
- 标题只在 Markdown：6.1 Recursive Optimization
- 标题只在 Markdown：6.2 UX And Supporting Records
- 标题只在 Markdown：6.3 Research
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 12 页
- 需求只在 pptx：Status: Draft target implementation Last updated: 2026-08-19 Primary interface: climbhill CLI Distribution: npm, npx skills, and climbhill.ai
- 需求只在 pptx：ClimbHill is a local-first controlled optimizer for Git repositories. A user states an outcome; ClimbHill gathers evidence, generates alternative Attempts, evaluates them, and determines what to improve next while changing only surfaces for which it has authority.
- 需求只在 pptx：Run -> Attempt -> Evaluation -> Decision
- 需求只在 pptx：A Run freezes the Target and Control commits, declares one writable Focus, pins an external Evaluation Strategy, and identifies a Promotion Target. Task, learning, and alignment work use the same engine with different Focuses. Recursion emerges when an authorized Decision creates a child Run.
- 需求只在 pptx：Jobs are optional UX projections that group Runs and supply defaults. They are not required engine state. Git owns content versioning; ClimbHill does not create a second revision system.
- 需求只在 pptx：The canonical recursive contract is docs/recursive-loops.md. Canonical terminology is mapped in CONTEXT-MAP.md. The rationale for the Run-centered model is recorded in ADR 0001.
- 需求只在 pptx：These are the recursive engine's only first-class concepts.
- 需求只在 pptx：These are typed files or value objects. They do not own independent lifecycles in the MVP.
- 需求只在 pptx：Research retains its own concepts: Resource, Observation, canonical graph Entity, Claim, Relationship, Topic, and OKF Bundle. A recursive Run pins research by Control commit and path rather than owning or duplicating it.
- 需求只在 pptx：Loop = immutable baseline + mutable focus + evaluation strategy + promotion target

### cloud-ai-summit-cz__ai

段落标题不一致，需求条目 46 / 46 一致（pptx 拆出 50 条）

- 标题只在 Markdown：Assumptions
- 标题只在 Markdown：Constraints
- 标题只在 Markdown：Functional
- 标题只在 Markdown：Non-Functional
- 标题只在 Markdown：Research Flow (Non-Deterministic)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 14 页
- 标题只在 pptx：第 17 页
- 需求只在 pptx：Cofilot - Coffee Company in Karlin, Prague
- 需求只在 pptx：Research Flow (Non-Deterministic)
- 需求只在 pptx：flowchart TB User["USER 'Should Cofilot expand to Vienna?'"] User -->|Query + Answers| Scratchpad Scratchpad -->|Questions| User
- 需求只在 pptx：Research Checklist (Termination Criteria)

### e6a5__zenta

段落标题不一致，需求条目 65 / 65 一致（pptx 拆出 104 条）

- 标题只在 Markdown：Unix Philosophy Guidelines:
- 标题只在 Markdown：Development Rules:
- 需求只在 pptx：Core Principle: "Do one thing, and do it well"
- 需求只在 pptx：If any answer is "no," reconsider the change.
- 需求只在 pptx：Developers, sysadmins, or knowledge workers who spend most of their day in the terminal.
- 需求只在 pptx：Users interested in mindfulness, Zen, Stoicism, or productivity.
- 需求只在 pptx：People who struggle with digital distractions and want more clarity and self-awareness.
- 需求只在 pptx：✅ zenta now Display a short mindfulness message or quote.
- 需求只在 pptx：Designed to be triggered manually (e.g., when taking a breath or resetting focus).
- 需求只在 pptx：Pull quotes randomly from a built-in list or custom user-defined list.
- 需求只在 pptx：✅ zenta log "" Log a moment of distraction or reflection.
- 需求只在 pptx：Automatically timestamps each entry with session correlation.

### hasanraiyan__resume

段落标题不一致，需求条目 15 / 15 一致（pptx 拆出 36 条）

- 标题只在 Markdown：（无标题）
- 标题只在 Markdown：Step 1
- 标题只在 Markdown：Step 2
- 标题只在 Markdown：Possible lecture statuses
- 标题只在 Markdown：Step 3
- 标题只在 pptx：第 1 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 15 页
- 需求只在 pptx：I think the biggest mistake would be building this like a spreadsheet. Students won't keep using an app that takes 5 minutes every day. The UX has to let them finish in 10–20 seconds.
- 需求只在 pptx：Tagline: Track your college life, not just your attendance.
- 需求只在 pptx：Build the easiest attendance tracking app for college students.
- 需求只在 pptx：The goal is to reduce daily attendance logging to less than 20 seconds while still providing accurate statistics and predictions.
- 需求只在 pptx：Everything works without internet.
- 需求只在 pptx：Colleges don't follow perfect schedules.
- 需求只在 pptx：without breaking attendance calculations.
- 需求只在 pptx：A user may have multiple semesters.
- 需求只在 pptx：Each semester contains subjects.
- 需求只在 pptx：Users create weekly schedules.

### intervalrain__OpenClaw.Net

段落标题不一致，需求条目 46 / 46 一致（pptx 拆出 64 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：2.1 產品一句話描述
- 标题只在 Markdown：2.2 目標使用者
- 标题只在 Markdown：2.3 非目標
- 标题只在 Markdown：4.1 高階架構
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 pptx：2.1 產品一句話描述
- 需求只在 pptx：一個以 C#/.NET 打造的「可插拔、事件驅動、強型別」AI Agent Runtime，可透過多種 Channel 操作並安全執行真實世界任務。
- 需求只在 pptx：[ Channel Adapter ] ↓ [ Agent Gateway ] ↓ [ Agent Pipeline (Middleware) ] ↓ [ LLM Invoker ] ↓ [ Skill / Plugin Executor ] ↓ [ State / Memory / Storage ]
- 需求只在 pptx：5.3 Agent Pipeline（Middleware）
- 需求只在 pptx：IAgentPipeline  .Use<Auth>()  .Use<RateLimit>()  .Use<PromptGuard>()  .Use<LLMInvoker>()  .Use<SkillExecutor>();
- 需求只在 pptx：public interface IAgentSkill{    string Name { get; }    string Description { get; }    Task<SkillResult> ExecuteAsync(SkillContext ctx);}
- 需求只在 pptx：非目標（第一版）
- 需求只在 pptx：作為 使用者，我希望 透過 Telegram 或 Line 與 OpenClaw 進行對話，以便 不需開啟電腦也能操作 Agent。
- 需求只在 pptx：US-02：遠端桌面/瀏覽器操作可視化
- 需求只在 pptx：作為 Host 管理員，我希望 當程式運行在 Server 容器內時，可透過 SSH 看到 Server 的桌面動作或瀏覽器操作，以便 監控 Agent 的實際執行狀況。

### jpbullalayao__pokemon-vgc-calc-mcp

段落标题不一致，需求条目 14 / 14 一致（pptx 拆出 34 条）

- 标题只在 Markdown：1. Overview & Introduction
- 标题只在 Markdown：2. Problem Statement
- 标题只在 Markdown：3. Goals & Objectives
- 标题只在 Markdown：4. Target Audience / User Personas
- 标题只在 Markdown：5. Functional Requirements
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 4 页
- 需求只在 pptx：Version: 1.0 Date: October 26, 2023 Author: AI Assistant Status: Proposed
- 需求只在 pptx：This document outlines the requirements for the "PokéCalc MCP Server," a serverless API built using the Model-Context Protocol (MCP). The primary function of this server is to provide a standardized, programmatic interface for performing Pokémon damage calculations.
- 需求只在 pptx：This MCP server solves the problem by wrapping the de facto standard Smogon damage calculation engine in a simple, discoverable, and machine-readable API, following the Model-Context Protocol.
- 需求只在 pptx：Primary Goal: To provide a stable, accurate, and easy-to-integrate API endpoint for Pokémon damage calculations.
- 需求只在 pptx：KR1: Successfully implement a single MCP tool, calculateDamage, that accepts attacker, defender, and field data.
- 需求只在 pptx：KR2: The calculateDamage tool correctly computes and returns damage results consistent with the Smogon Damage Calculator for a variety of scenarios, including those with items, abilities, status conditions, and field effects.
- 需求只在 pptx：KR3: The MCP server is successfully deployed to a public Vercel URL and is fully functional.
- 需求只在 pptx：KR4: The server's MCP manifest (/mcp/manifest.json) is valid and correctly describes the calculateDamage tool and its schemas.
- 需求只在 pptx：4. Target Audience / User Personas
- 需求只在 pptx：Alex, the Bot Developer: Alex is building a Pokémon-themed Discord bot. They want to add a /calc command where users can input two Pokémon and see the damage output. Alex needs a simple API endpoint to call, rather than hosting and maintaining the calculation logic themselves.

### profullstack__coinpayportal

段落标题不一致，需求条目 201 / 201 一致（pptx 拆出 214 条）

- 标题只在 Markdown：Business Goals
- 标题只在 Markdown：Product Goals
- 标题只在 Markdown：Non-Goals for MVP
- 标题只在 Markdown：3.1 WooCommerce
- 标题只在 Markdown：3.2 WHMCS
- 需求只在 pptx：CoinPay currently requires merchants to integrate at the API level or through custom implementation. That limits adoption among merchants who prefer off-the-shelf extensions. WooCommerce and WHMCS merchants expect ready-made payment plugins that behave like native gateways.
- 需求只在 pptx：5.3 CoinPay Operations / Support
- 需求只在 pptx：7.1.1 Merchant Authentication and Setup
- 需求只在 pptx：7.1.3 Hosted Checkout Redirect
- 需求只在 pptx：7.1.4 Payment Status Synchronization
- 需求只在 pptx：7.2.4 Currency and Totals Handling
- 需求只在 pptx：7.3.1 Gateway Module Registration
- 需求只在 pptx：7.3.3 Callback / Notification Handling
- 需求只在 pptx：7.3.4 Partial Payments and Credits
- 需求只在 pptx：7.3.5 Subscription and Recurring Billing

### rahilp__gatewright

段落标题不一致，需求条目 29 / 29 一致（pptx 拆出 37 条）

- 标题只在 Markdown：P0 — v0.1 does not ship without these
- 标题只在 Markdown：P1 — v0.2 and v0.3
- 标题只在 Markdown：P2 — v0.4
- 标题只在 Markdown：P2 — v0.5 · memory backend (optional)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 15 页
- 需求只在 pptx：Status: Draft v0.2 · Owner: Rahil · Date: 2026-09-14 (decisions D1–D6 closed) · Revised: 2026-09-20 (T-0139 — the name, D3, R1, R5, R25 and the success metrics corrected against the shipped v0.13.2)
- 需求只在 pptx：The cost of not solving this: repeated context spend at the top of every session, work that gets lost between sessions, and no way to hand a queue of work to agents without a human sitting on top of each one.
- 需求只在 pptx：Solo developer with agents. Runs two or three agent sessions a day on one repo. Wants to stop re-explaining state and wants a record of what agents did. Primary user for v0.1–v0.2.
- 需求只在 pptx：Small team with shared repo. Files work as GitHub issues. Wants agents to pick from that backlog and wants progress visible in the issue without opening a board. Primary user for v0.3.
- 需求只在 pptx：Automation-first operator. Wants a queue of work to run while they're away, with a kill switch and gates they control. Primary user for v0.4.
- 需求只在 pptx：P0 — v0.1 does not ship without these
- 需求只在 pptx：P2 — v0.5 · memory backend (optional)
- 需求只在 pptx：The targets below are as written. Actuals are recorded beside them where they are knowable, measured 2026-09-20 against v0.13.2; an unmeasured target is marked as such rather than left to read as met.

### sudo-Harshk__Skillify

段落标题不一致，需求条目 56 / 56 一致（pptx 拆出 81 条）

- 标题只在 Markdown：3.1 CRITICAL — Gemini API Key Exposed in Git
- 标题只在 Markdown：3.2 HIGH — CORS Defaults to Allow-All in Production
- 标题只在 Markdown：3.3 HIGH — No Rate Limiting on Question Generation
- 标题只在 Markdown：3.4 HIGH — No Input Sanitization (Prompt Injection Risk)
- 标题只在 Markdown：3.5 MEDIUM — Frontend Has No Error Boundary
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 pptx：Author: Product HeadDate: 2026-05-17Status: ActiveAudience: Engineering Team
- 需求只在 pptx：This document defines the problems clearly, sets out the expected outcomes for the engineering team, and draws a boundary around what is in scope for the next engineering sprint.
- 需求只在 pptx：3.1 CRITICAL — Gemini API Key Exposed in Git
- 需求只在 pptx：3.2 HIGH — CORS Defaults to Allow-All in Production
- 需求只在 pptx：Issue: If ALLOWED_ORIGINS is not set as an environment variable, the backend falls back to allowing every origin. This means a deployed production instance with a missing env var accepts cross-origin requests from any website.
- 需求只在 pptx：3.3 HIGH — No Rate Limiting on Question Generation
- 需求只在 pptx：3.4 HIGH — No Input Sanitization (Prompt Injection Risk)
- 需求只在 pptx：Issue: The chapter and subject fields from the request body are interpolated directly into the LLM prompt string without sanitization. A crafted chapter name (e.g., "Ignore all previous instructions and...") is passed verbatim to Gemini.
- 需求只在 pptx：3.5 MEDIUM — Frontend Has No Error Boundary
- 需求只在 pptx：Issue: The entire app is rendered inside a single React component tree with no ErrorBoundary. An unhandled JavaScript error anywhere in the component hierarchy crashes the entire page, showing a blank screen with no recovery option.

### wjsutton__tableau-public-mcp

段落标题不一致，需求条目 84 / 84 一致（pptx 拆出 114 条）

- 标题只在 Markdown：Purpose
- 标题只在 Markdown：Scope
- 标题只在 Markdown：Core Components
- 标题只在 Markdown：Technology Stack
- 标题只在 Markdown：1. Initialize Project
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 21 页
- 需求只在 pptx：📦 Implementation Status: ✅ COMPLETE - All 22 tools implemented, tested, and production-ready
- 需求只在 pptx：Last Updated: 2025-12-31 | Build Status: ✅ Passing | Test Coverage: Comprehensive
- 需求只在 pptx：Step-by-Step: Adding a New Tool
- 需求只在 pptx：src/tools/getWorkbooksList/├── getWorkbooksList.ts└── getWorkbooksList.test.ts
- 需求只在 pptx：File: src/tools/getWorkbooksList/getWorkbooksList.ts
- 需求只在 pptx：Step 4: Update Tool Name Types
- 需求只在 pptx：export const TOOL_NAMES = [  "get_workbooks_list",  "get_user_profile",  // ... add new tool names] as const;export type ToolName = typeof TOOL_NAMES[number];export function isToolName(value: string): value is ToolName {  return TOOL_NAMES.includes(value as ToolName);}
- 需求只在 pptx：File: src/tools/getWorkbooksList/getWorkbooksList.test.ts
- 需求只在 pptx：interface ToolParams<Args extends ZodRawShape | undefined> {  server: Server;  name: string;  description: string;  paramsSchema: Args;  annotations?: Record<string, unknown>;  callback: (args: Args extends ZodRawShape ? z.infer<z.ZodObject<Args>> : never)    => Promise<Ok<CallToolResult>>;}
- 需求只在 pptx：File: src/utils/errorHandling.ts

### 01MVP__blog-starter

段落标题不一致，需求条目 7 / 7 一致（pptx 拆出 91 条）

- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 一句话定位
- 标题只在 Markdown：1.3 项目本质
- 标题只在 Markdown：首页 /
- 标题只在 Markdown：博客列表 /blog
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 46 页
- 标题只在 pptx：第 48 页
- 需求只在 pptx：产品 A：博客 CMS 代码模板产品 B：给 AI 使用的初始化 Skill
- 需求只在 pptx：1. 一个可复用的 Cloudflare-native 博客 CMS 模板2. 一个 AI 可以使用的 Skill，用来自动创建新的博客站点3. 一个统一部署在 blog.01mvp.com 的模板演示站
- 需求只在 pptx：mugnavo/tanstarter-plus 是一个基于 TanStack Start 的现代 monorepo starter，包含 Vite Plus、pnpm workspace、React 19、React Compiler、TanStack Start / Router / Query / Form、Drizzle、Better Auth、Tailwind CSS、shadcn/ui、Base UI 等现代技术栈。它更适合作为一个长期演进的全栈 CMS 模板底座。(GitHub)
- 需求只在 pptx：pnpm create mugnavo -t monorepo
- 需求只在 pptx：这也符合我们希望它作为"现代 AI 友好模板"的定位。(GitHub)
- 需求只在 pptx：TanStack Start + Cloudflare Workers + D1 + R2
- 需求只在 pptx：作为长期技术方向是合理的。
- 需求只在 pptx：运行：Cloudflare Workers数据库：Cloudflare D1对象存储：Cloudflare R2缓存：Cloudflare Cache API / KV防垃圾：Cloudflare Turnstile队列：Cloudflare Queues，可选邮件：Cloudflare Email Service，可选增强部署：Wrangler / Cloudflare API / Cloudflare Skill
- 需求只在 pptx：Cloudflare 官方仍将 Wrangler 定义为 Cloudflare Developer Platform 的命令行工具，用于 Workers 项目的开发、部署和配置。(Cloudflare Docs)
- 需求只在 pptx：内容主格式是 Markdown，但主存储是 D1。

### 259876lr__yolo-sop

段落标题不一致，需求条目 42 / 48 一致（pptx 拆出 79 条）

- 标题只在 Markdown：1.1 产品背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 YOLO26 + MediaPipe技术优势
- 标题只在 Markdown：YOLO26核心优势
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：所有P0优先级功能正常工作
- 需求只在 Markdown：所有P1优先级功能正常工作
- 需求只在 Markdown：Web界面响应正常，无严重UI问题
- 需求只在 Markdown：连续运行24小时无崩溃
- 需求只在 Markdown：异常情况能够自动恢复
- 需求只在 Markdown：内存使用稳定，无泄漏
- 需求只在 pptx：MediaPipe Hands手势识别优势
- 需求只在 pptx：联合检测架构优势
- 需求只在 pptx：2.2 功能模块详细说明
- 需求只在 pptx：2.2.1 视频采集模块
- 需求只在 pptx：2.2.2 实时检测模块
- 需求只在 pptx：2.2.4 异常告警模块
- 需求只在 pptx：2.2.5 数据统计模块
- 需求只在 pptx：2.2.6 报告生成模块
- 需求只在 pptx：2.2.8 模型训练平台
- 需求只在 pptx：3.4 可扩展性需求

### 5kyfkr__siyuan-plugin-task-horizon

段落标题不一致，需求条目 139 / 148 一致（pptx 拆出 142 条）

- 标题只在 Markdown：4.1 本期必须覆盖
- 标题只在 Markdown：4.2 非目标
- 标题只在 Markdown：5.1 任务
- 标题只在 Markdown：5.2 文档分组
- 标题只在 Markdown：5.3 视图
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：插件主壳：顶部工具栏、文档分组、文档页签、规则、搜索、刷新、设置、视图切换。
- 需求只在 Markdown：主页总览：任务完成统计、趋势、热力图、文档分布、最近完成、逾期风险。
- 需求只在 Markdown：任务视图：清单、表格、时间轴、看板、日历、白板。
- 需求只在 Markdown：任务详情：标题、位置、完成状态、重要性、状态、开始/截止日期、时长、耗时、提醒、循环、子任务、备注、附件、自定义字段、更多操作。
- 需求只在 Markdown：批量操作：清单/表格/时间轴中开启多选后批量修改日期、重要性、状态、自定义字段。
- 需求只在 Markdown：设置中心：文档分组、常规、外观、日历、AI、规则、四象限、优先级算法、关于。
- 需求只在 Markdown：quickbar：文档内任务块悬浮编辑条，以及任务行末尾常驻字段。
- 需求只在 Markdown：导入导出：滴答清单 CSV 导入、当前分组任务导出、汇总 Markdown/Excel 类能力。
- 需求只在 Markdown：响应式：桌面页签、Dock、移动端、横屏/窄屏的布局适配。
- 需求只在 pptx：版本基线：plugin.json 2.3.7文档目的：基于当前代码实现，整理给前端重建界面时使用的产品需求、功能范围和验收标准。
- 需求只在 pptx：主界面由顶部工具栏、文档页签/分组区、内容视图、侧栏/详情区、底部浮动条组成。
- 需求只在 pptx：顶栏入口设置还应提供移动端任务侧栏开关。开关关闭时不注册或隐藏移动侧栏 Dock，开启后复用移动端清单布局，默认视图跟随"移动端默认"。

### AlanDXiang__Google_ADK_Chat

段落标题不一致，需求条目 55 / 55 一致（pptx 拆出 95 条）

- 标题只在 Markdown：1. 引言
- 标题只在 Markdown：1.1 项目背景与意义
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 项目范围
- 标题只在 Markdown：1.4 预期读者
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 需求只在 pptx：版本: 1.0 日期: 2025年5月30日
- 需求只在 pptx：1.1 项目背景与意义
- 需求只在 pptx：随着大型语言模型（LLM）技术的飞速发展，其在各个领域的应用潜力日益凸显。为了更便捷地利用和扩展这些模型的能力，我们需要一个灵活、易用且功能强大的开发与交互平台。本项目旨在基于 Google 的 Agent Development Kit (ADK)，构建一个本地化的Web应用，使用户能够方便地与大模型进行对话，并能灵活配置和扩展模型及相关工具。这不仅能加速AI应用的开发迭代，更能激发创新思维，探索大模型应用的更多可能性。🚀
- 需求只在 pptx：本地化Web界面：提供一个在本地运行的Web用户界面，用于与大模型进行实时对话。
- 需求只在 pptx：灵活的模型配置：通过 .env 文件及环境变量，轻松配置大模型的连接参数（如 base_url, model, api_key 等）。
- 需求只在 pptx：可定制的MCP工具：支持用户自定义添加和修改 ADK 中的模型中心处理（MCP）工具，增强应用的扩展性。
- 需求只在 pptx：Python为核心：项目主要采用Python语言进行开发，充分利用其在AI领域的生态优势。
- 需求只在 pptx：本地Web服务器的搭建与UI界面的基础实现。
- 需求只在 pptx：通过UI界面发送用户输入到大模型，并展示模型返回结果。
- 需求只在 pptx：实现从 .env 文件和环境变量读取模型配置信息的功能，并确保环境变量的优先性。

### Ariestar__obsidian-dragger

段落标题不一致，需求条目 135 / 150 一致（pptx 拆出 308 条）

- 标题只在 Markdown：3.1 桌面端
- 标题只在 Markdown：3.2 移动端：未开启长按文本拖拽
- 标题只在 Markdown：3.3 移动端：开启长按文本拖拽
- 标题只在 Markdown：5.1 Interaction Event
- 标题只在 Markdown：5.2 Drag Interaction State
- 标题只在 pptx：第 2 页
- 标题只在 pptx：14. Target CodeMirror Platform File Architecture
- 标题只在 pptx：15. 一次性重构验收范围
- 标题只在 pptx：16. 开放问题
- 需求只在 Markdown：通过手柄拖拽单个块。
- 需求只在 Markdown：通过长按/范围交互进入多选。
- 需求只在 Markdown：对已选中的块再次拖拽时，移动整个选区。
- 需求只在 Markdown：桌面端不需要 mobile drag mode。
- 需求只在 Markdown：通过手柄拖拽单块。
- 需求只在 Markdown：通过手柄相关交互进入多选和调整多选范围。
- 需求只在 Markdown：不需要右上角 mobile drag mode。
- 需求只在 Markdown：不应因为没有开启 mobile drag mode 而禁止手柄拖拽。
- 需求只在 Markdown：如果当前设置不是"始终显示手柄"，移动端应由 platform 实现自己的手柄触达策略，而不是让 drag 层知道移动端差异。
- 需求只在 Markdown：移动端手柄触达策略可以和桌面 hover 不同，但最终仍翻译成 source = handle 的同一种 interaction event。
- 需求只在 pptx：Status: DraftDate: 2026-06-08Scope: 拖拽交互 / 移动端多选 / drag-platform 边界 / CodeMirror 输入适配
- 需求只在 pptx：InteractionEvent 表示平台已经把真实输入翻译成了什么交互事件。事件名贴近用户行为，不包含 mobile/desktop。
- 需求只在 pptx：本系统只有一条 Interaction Pipeline。拖拽和多选都在这条 pipeline 里；多选不是独立 pipeline，移动端多选也不是独立 pipeline。
- 需求只在 pptx：idle | | hold_start(selection) v holding | | hold_ready v ready_to_drag | | drag_start(drop) v dragging | | drag_over(drop)* v dragging | | drop(resolution) / cancel v idle
- 需求只在 pptx：idle | | hold_start(selection) v holding | | selection_start(seed) v selecting | | selection_change(boundary)* v selecting | | selection_finish v selecting(passive)
- 需求只在 pptx：selecting | | hold_start(selection) v holding | | hold_ready v ready_to_drag | | drag_start(drop) v dragging(selection) | | drag_over(drop)* v dragging(selection) | | drop / cancel v idle
- 需求只在 pptx：idle | | hold_start(selection) v holding | +-- selection_start(seed) |     v |   selecting(adjusting)
- 需求只在 pptx：pointerdown(handle) -> platform hit-test: HoldTarget(selection = one block, source = handle) -> hold_start -> platform delay policy (0ms) -> hold_ready / drag_start -> dragging(BlockSelection)
- 需求只在 pptx：touch pointerdown(handle) -> platform hit-test: HoldTarget(selection = one block, source = handle) -> hold_start -> platform delay policy -> hold_ready / drag_start -> dragging(BlockSelection)
- 需求只在 pptx：touch pointerdown(text) -> platform hit-test: HoldTarget(selection = one block, source = text) -> hold_start -> platform long-long-press timer -> selection_start(seed) -> selecting(passive)

### ChrisChen667788__wind-comic

段落标题不一致，需求条目 180 / 183 一致（pptx 拆出 238 条）

- 标题只在 Markdown：1.1 当前 ai-comic-studio 前端基线
- 标题只在 Markdown：1.2 OiiOii 已具备而我方缺失的能力
- 标题只在 Markdown：1.3 我方独有 OiiOii 没有的护城河（不能丢）
- 标题只在 Markdown：2.1 必做（v2.0-α，第 1 周 Sprint 0）
- 标题只在 Markdown：2.2 应做（v2.0-β，第 2-3 周 Sprint 1）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：竞品分析文档：回答"为什么要做、做什么"
- 需求只在 Markdown：本 PRD：回答"具体怎么做、谁来做、什么时候做"
- 需求只在 Markdown：#：6；决策：Seedance 2.0 走即梦官方 API（非 fal.ai）；时间：2026-04-08；理由：中文支持/合规友好；火山引擎稳定；fal.ai 仅作兜底
- 需求只在 pptx：文档版本：PRD v1.1 | 编写日期：2026-04-08 关联文档：competitive-analysis-and-upgrade-plan.md v2.1 触发事件：2026.04.07 OiiOii 全球首发，与本项目架构高度同构（7 Agent vs 我方 8 Agent）
- 需求只在 pptx：1.1 当前 ai-comic-studio 前端基线
- 需求只在 pptx：1.2 OiiOii 已具备而我方缺失的能力
- 需求只在 pptx：1.3 我方独有 OiiOii 没有的护城河（不能丢）
- 需求只在 pptx：核心策略：把 OiiOii 已验证的"基础设施"快速追平，但用我方独有的"专业可控"能力包装升级，避免变成低配版 OiiOii。
- 需求只在 pptx：评分维度：用户价值（1-10）× 实现成本（1-10，越低越易做）× OiiOii 反制权重（×1.0–×1.3）
- 需求只在 pptx：2.2 应做（v2.0-β，第 2-3 周 Sprint 1）
- 需求只在 pptx：2.4 不做（明确放弃）
- 需求只在 pptx：3.1 信息架构变更
- 需求只在 pptx：旧 IA: /                       (登陆页) /create                 (单一表单 → 全屏 Agent) /dashboard/*            (项目管理) /projects/[id]          (工作台)

### Cicada0719__moeplay-tauri

段落标题不一致，需求条目 72 / 87 一致（pptx 拆出 120 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标
- 标题只在 Markdown：1.3 成功指标
- 标题只在 Markdown：3.1 规则引擎重建与源切换修复
- 标题只在 Markdown：3.2 播放器体验修复
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：指标：历史记录同步端到端成功率（双设备验证）；基线（现状）：不支持；目标值：≥ 95%（冲突可解决）
- 需求只在 Markdown：指标：漫画双页模式渲染帧率（1080p，中等配置）；基线（现状）：不支持；目标值：≥ 50 FPS，翻页延迟 < 100ms
- 需求只在 Markdown：内置番剧源 ≥ 6 个，且每日 CI 健康检查（真实搜索关键词"进击的巨人"或等价关键词）通过率 ≥ 80%。
- 需求只在 Markdown：内置漫画源 ≥ 4 个、小说源 ≥ 3 个，健康检查通过标准同上。
- 需求只在 Markdown：每条内置规则包含字段：name, version, contentType, baseUrl, search, detail, chapter, parse（或等价结构），缺字段的规则在加载时被拒绝。
- 需求只在 Markdown：全部内置规则存放在独立目录（如 resources/rules/ 或远端拉取），与代码解耦，可在不发版的情况下通过规则热更新修复。
- 需求只在 Markdown：用户可通过"设置 → 规则管理 → 导入"选择本地 .json/.yaml 规则文件，合法规则出现在源列表，非法规则给出具体校验错误。
- 需求只在 Markdown：导入的自定义规则与内置规则在 UI 上可区分，且可单独删除。
- 需求只在 Markdown：模拟播放地址返回 403，界面在 2 秒内显示错误类型与"切换源"按钮，点击后进入源切换流程且保留进度（联动 FR-02）。
- 需求只在 Markdown：连续重试 2 次失败后，自动弹出源推荐列表（按健康度排序）。
- 需求只在 pptx：3.1 规则引擎重建与源切换修复
- 需求只在 pptx：FR-01 统一规则引擎（P0）
- 需求只在 pptx：FR-02 源切换状态保持（P0）
- 需求只在 pptx：参考 animeko（https://github.com/Animeko-org/Animeko）与 kazumi（https://github.com/Predidit/Kazumi）的源配置方式，重建内置源库：番剧源 ≥ 6 个、漫画源 ≥ 4 个、小说源 ≥ 3 个。规则格式采用与 kazumi 兼容或可直接移植的结构（JSON/YAML 描述 + 解析脚本），并为每条规则附带元数据（名称、语言、内容类型、版本、NSFW 标记）。
- 需求只在 pptx：☐ 内置番剧源 ≥ 6 个，且每日 CI 健康检查（真实搜索关键词"进击的巨人"或等价关键词）通过率 ≥ 80%。
- 需求只在 pptx：☐ 内置漫画源 ≥ 4 个、小说源 ≥ 3 个，健康检查通过标准同上。
- 需求只在 pptx：☐ 每条内置规则包含字段：name, version, contentType, baseUrl, search, detail, chapter, parse（或等价结构），缺字段的规则在加载时被拒绝。
- 需求只在 pptx：☐ 全部内置规则存放在独立目录（如 resources/rules/ 或远端拉取），与代码解耦，可在不发版的情况下通过规则热更新修复。
- 需求只在 pptx：FR-04 规则热更新与源健康状态展示（P1）
- 需求只在 pptx：应用启动时（及每 24 小时）从规则仓库拉取最新规则包（带版本号与签名校验），失败时回退使用本地缓存版本。源列表界面展示每个源的最近健康状态（可用/异常/未知）。

### DTrader-store__formula-ts

段落标题不一致，需求条目 97 / 146 一致（pptx 拆出 168 条）

- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 核心价值主张
- 标题只在 Markdown：2.1 主要用户画像
- 标题只在 Markdown：用户画像 1: Web 金融应用开发者
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：成为金融技术领域最易用、高性能的技术指标公式解析引擎，让开发者能够轻松地在自己的应用中集成强大的技术分析功能。
- 需求只在 Markdown：兼容性: 完全兼容通达信公式语法，降低用户学习成本
- 需求只在 Markdown：高性能: 支持大规模数据计算（10000+ 数据点），增量计算延迟 < 100ms
- 需求只在 Markdown：同构设计: 同时支持浏览器和 Node.js 环境
- 需求只在 Markdown：易于集成: 简洁的 API 设计，开箱即用
- 需求只在 Markdown：可扩展性: 灵活的函数注册机制，易于添加自定义函数
- 需求只在 Markdown：教育工作者: 教授技术分析课程，需要演示工具
- 需求只在 Markdown：个人投资者: 具备编程能力，希望自建分析工具
- 需求只在 Markdown：能正确解析 MA、MACD、KDJ 等经典指标公式
- 需求只在 Markdown：对于语法错误，能准确定位并给出清晰的错误信息（行号、列号）
- 需求只在 pptx：版本: 1.0 日期: 2025-11-13 负责人: 产品团队 状态: 规划中
- 需求只在 pptx：☐ 能正确解析 MA、MACD、KDJ 等经典指标公式
- 需求只在 pptx：☐ 对于语法错误，能准确定位并给出清晰的错误信息（行号、列号）
- 需求只在 pptx：☐ 单元测试覆盖率 > 80%
- 需求只在 pptx：☐ 计算结果与通达信官方结果一致（误差 < 0.01%）
- 需求只在 pptx：☐ 支持至少 1000 个数据点的计算
- 需求只在 pptx：☐ 每个函数都有完整的单元测试
- 需求只在 pptx：F3: 基础错误处理
- 需求只在 pptx：☐ 所有可预见的错误都有明确的错误类型
- 需求只在 pptx：☐ 错误信息对用户友好，易于理解

### FLYFISH567__ItemMemo

段落标题不一致，需求条目 91 / 116 一致（pptx 拆出 126 条）

- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品简介
- 标题只在 Markdown：1.3 产品目标
- 标题只在 Markdown：1.4 产品定位
- 标题只在 Markdown：2.1 背景
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：更理性地理解消费
- 需求只在 Markdown：更系统地管理生活物品
- 需求只在 Markdown：更及时地处理更换和补购
- 需求只在 Markdown：更直观地发现高价值物品和低效购买
- 需求只在 Markdown：理性消费用户
- 需求只在 Markdown：精致生活 / 收纳管理用户
- 需求只在 Markdown：数码 / 家居 / 装备爱好者
- 需求只在 Markdown：年轻上班族 / 学生
- 需求只在 Markdown：需要一个轻量工具帮助自己管理生活和消费。
- 需求只在 Markdown：买了很多东西，后面不清楚是否常用
- 需求只在 pptx：版本：V1.0产品形态：Web 端数据存储方式：本地保存阶段定位：MVP / 概念验证版
- 需求只在 pptx：左侧侧边栏作为一级导航，顶部为搜索和快捷操作区，主体区域根据页面切换展示相应内容。
- 需求只在 pptx：首页承担"管理仪表盘"的角色，让用户进入后第一时间掌握当前状态。
- 需求只在 pptx：查看和管理所有已记录物品。
- 需求只在 pptx：这是系统的核心管理页，承担长期使用过程中的高频操作。
- 需求只在 pptx：管理系统默认分类和用户自定义分类。
- 需求只在 pptx：提醒中心让系统从"记录工具"升级为"主动管理工具"。
- 需求只在 pptx：帮助用户从整体维度理解自己的物品和消费情况。
- 需求只在 pptx：将零散记录转化为整体认知，提升持续记录动力。
- 需求只在 pptx：承载用户的偏好设置和基础配置。

### FlashingChen__dsh-desktop-hub

段落标题不一致，需求条目 53 / 54 一致（pptx 拆出 78 条）

- 标题只在 Markdown：1.1 DSH 是什么
- 标题只在 Markdown：1.2 生态现状（调研对象）
- 标题只在 Markdown：2.1 用户数据与配置目录（$DSH_HOME）
- 标题只在 Markdown：2.2 DSH harness 如何检测 skills（核心调研项①）
- 标题只在 Markdown：2.3 如何安装 plugin（核心调研项②）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：决策点：插件操作通道；选择（已落地）：主进程 spawn dsh plugin --profile web add；理由：remove；列4：update（进程树托管、输出流回 UI、支持取消）；列5：与 anywhere-labs desktopPnpm.runPlugin() 同构；dsh 是 bundle reconcile 的权威
- 需求只在 pptx：状态：已实现（审计修复完成）（§2 调研结论为实施依据；M0-M6 已按 plan.md 全部落地并通过验证，见 §5；AUDIT_REPORT.md 的 P0-P3 全部修复） 版本：v0.1 · 日期：2026-08-16 应用名：DSH Desktop Hub（已定名并落实，规避社区 dsh-desktop / dsh_desktop 撞名）
- 需求只在 pptx：整体流程：写入 PRD 供审核 → 审核通过后自行制定 plan，按 MVP 拆分，每次只做一件事，以最小可验证的方式推进，自行测试。
- 需求只在 pptx：1.2 生态现状（调研对象）
- 需求只在 pptx：差异化结论：现有桌面端都只做「封装启动」，没有任何产品提供用户要求的三个管理系统的 UI 化整合（Plugin 管理台 / MCP JSON→YAML 转换器 / Skills 管理器）。本项目的定位是 DSH 桌面管理控制台 + 内置 harness，并进一步提供三类扩展市场。
- 需求只在 pptx：本节所有事实来自官方仓库本地 checkout（deepseek-harness @ 0.1.0-rc.5）与参考实现仓库，引用路径即证据位置。
- 需求只在 pptx：2.1 用户数据与配置目录（$DSH_HOME）
- 需求只在 pptx：workspace 根 = 启动 dsh 命令时的目录；该目录下的 .dsh/skills、.agents/skills、AGENTS.md/CLAUDE.md（65,536 字节预算加载）都会进入 agent 上下文。
- 需求只在 pptx：2.2 DSH harness 如何检测 skills（核心调研项①）
- 需求只在 pptx：实现于 packages/skill/（ctx.skills 注册表 + 本地 provider + 模型侧 tool）。
- 需求只在 pptx：对 Skills 系统的启示：管理 = 读写 $DSH_HOME/skills/（用户级）与 workspace 的 .dsh/skills（项目级）；bundled 只读展示。修改后即时生效，无需重启，天然适合 UI 管理。

### Frank-ay__mimo-mcp

段落标题不一致，需求条目 61 / 62 一致（pptx 拆出 82 条）

- 标题只在 Markdown：目标(In Scope)
- 标题只在 Markdown：非目标(Out of Scope,V1 不做)
- 标题只在 Markdown：6.1 总体结构(模块边界)
- 标题只在 Markdown：6.2 技术栈(已定稿)
- 标题只在 Markdown：6.3 复用的现有资产(已经过本机调研)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 21 页
- 需求只在 Markdown：新增 tts_stream(text, voice, *, model, audio_format, opts) -> AsyncIterator[bytes](若 R1 显示不支持流式,则保留 stub 抛 NotSupportedError,此时前端 fallback 一次性)
- 需求只在 pptx：注:本 PRD 为立项基线文档,部分 F7(ASR)/TTS 设计已演进,实际实现以代码与 docs/USAGE.md 为准。
- 需求只在 pptx：项目代号:mimo-mcp 文档归属:docs/PRD.md 撰写日期:2026-04-29(M0 + M1 + 增量任务 1 实施完毕,内容已包含全部实测发现)
- 需求只在 pptx：优先级(已定稿):F1-F8 全部纳入 V1。F7 ASR 云端 API 形态需在 M1 阶段实测确认;若实测云端 API 不存在,F7 在 V1 内 tool/Web 状态显式置为 unavailable,并给出"等待 MiMo 官方开放"的清晰提示——不预置任何本地模型(决定见 §15-Q6)。
- 需求只在 pptx：6.1 总体结构(模块边界)
- 需求只在 pptx：6.2 技术栈(已定稿)
- 需求只在 pptx：6.3 复用的现有资产(已经过本机调研)
- 需求只在 pptx：设计原则:tool 数量目前 11 个,落在 anthropic 推荐的"单工具模式 < 15"范围内,不必引入 search+execute 模式。
- 需求只在 pptx：MIMO_API_KEY=sk-xxx              # 必填 MIMO_BASE_URL=https://api.xiaomimimo.com/v1 MIMO_DEFAULT_TEXT_MODEL=mimo-v2.5-pro MIMO_DEFAULT_VISION_MODEL=mimo-v2.5 MIMO_DEFAULT_TTS_MODEL=mimo-v2.5-tts MIMO_WEB_PORT=7801 MIMO_DATA_DIR=./data
- 需求只在 pptx：10.2 Claude Code 注册(~/.claude/settings.local.json 追加)
- 需求只在 pptx："mcpServers": {  "mimo-mcp": {    "command": "uv",    "args": ["--directory", "/Users/Frank-ay/Desktop/xiaomi-MIMO", "run", "mimo-mcp"],    "env": { "MIMO_API_KEY": "sk-xxx" }  }}

### G1-kiyo__agent

段落标题不一致，需求条目 96 / 107 一致（pptx 拆出 142 条）

- 标题只在 Markdown：利益相关者
- 标题只在 Markdown：版本历史
- 标题只在 Markdown：2.1 产品定位
- 标题只在 Markdown：2.2 核心价值主张
- 标题只在 Markdown：2.3 目标用户
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：生成式AI：Agent智能检索与多轮推理
- 需求只在 Markdown：RAG技术：知识库检索增强问答
- 需求只在 Markdown：协同工作流：群组讨论、审核流程、知识沉淀
- 需求只在 Markdown：AI智能资讯检索（多轮Agent Loop）
- 需求只在 Markdown：RAG知识库（文档入库 + 检索增强）
- 需求只在 Markdown：执行链路可视化（节点流转、日志追踪）
- 需求只在 Markdown：群组协作与讨论（发布、评论、投票）
- 需求只在 Markdown：人工审核与干预（interrupt + resume）
- 需求只在 Markdown：检查点管理与重放（审计、合规）
- 需求只在 Markdown：企业级认证与权限（JWT + RBAC）
- 需求只在 pptx：文档版本：v2.0（企业生产版）编制日期：2026-07-12文档状态：正式版
- 需求只在 pptx：graph TB subgraph 目标用户画像 A[👔 企业AI战略负责人] B[👨‍💻 AI产品经理/技术负责人] C[📊 行业分析师/投资经理] D[👥 团队协作成员] end
- 需求只在 pptx：C --> C1[使用场景：系统性信息收集、深度分析报告] C --> C2[核心需求：RAG知识库检索，支持研究决策]
- 需求只在 pptx：☒ AI智能资讯检索（多轮Agent Loop）
- 需求只在 pptx：☒ RAG知识库（文档入库 + 检索增强）
- 需求只在 pptx：☒ 执行链路可视化（节点流转、日志追踪）
- 需求只在 pptx：☒ 群组协作与讨论（发布、评论、投票）
- 需求只在 pptx：☒ 人工审核与干预（interrupt + resume）
- 需求只在 pptx：☒ 检查点管理与重放（审计、合规）
- 需求只在 pptx：☒ 企业级认证与权限（JWT + RBAC）

### GCWing__OpenBitFun

段落标题不一致，需求条目 38 / 38 一致（pptx 拆出 45 条）

- 标题只在 Markdown：5.1 实际产品变更清单
- 标题只在 Markdown：5.2 页面与面板布局
- 标题只在 Markdown：5.3 关键用例与体验增益
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 pptx：范围：定义 OpenBitFun 加载任意外部目标项目后的产品定位、目标用户、核心体验、产品规格、关键边界、平台入口差异、功能需求和成功指标。 关联文档：external-research.md 提供外部证据，design.md 承接总体架构设计，../architecture/review-lifecycle.md 定义版本化 Review 生命周期，implementation-plan.md 承接阶段落地，traceability-matrix.md 承接覆盖关系检查。
- 需求只在 pptx：用户画像用于选择默认入口、解释语言和提示密度。内部策略画像不是用户侧主概念。体验呈现应聚焦任务状态、弱提示、确认、受限原因、设置项和下一步。
- 需求只在 pptx：5.1 实际产品变更清单
- 需求只在 pptx：5.2 页面与面板布局
- 需求只在 pptx：5.3 关键用例与体验增益
- 需求只在 pptx：组织拒绝 / 受管强制要求
- 需求只在 pptx：允许范围内的会话/任务覆盖

### HowlandMai__EmberIM

段落标题不一致，需求条目 67 / 69 一致（pptx 拆出 84 条）

- 标题只在 Markdown：2.1 角色
- 标题只在 Markdown：2.2 用户故事（核心场景）
- 标题只在 Markdown：F1 注册
- 标题只在 Markdown：F2 登录
- 标题只在 Markdown：F3 登出
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 16 页
- 需求只在 Markdown：普通用户：注册、登录、加好友、建群、单聊/群聊、看历史、收离线消息、感知好友在线状态。
- 需求只在 Markdown：（内部）系统运维者：单机部署、启动服务、配置环境变量、应对异常。
- 需求只在 pptx：阶段：2 / 9 — 需求定义 项目：EmberIM 即时通讯服务端 定位：C/S 架构下的实时通讯服务端（多线程 Reactor + TCP 长连接 + 请求-响应 + 实时推送） 读者：研发 / 测试 / 学习读者。本文档是功能、用户故事与业务规则的唯一基准。
- 需求只在 pptx：EmberIM 是一个可落地的即时通讯服务端，学习用但要求架构完整、可编译、可运行。它属于 C/S 架构：客户端为独立安装的 IM 客户端（App/桌面程序，本仓库只实现服务端），双方通过自定义 TCP 长连接协议通信。
- 需求只在 pptx：服务端职责：接收并维护大量客户端长连接，处理注册/登录/好友/群组/单聊/群聊/历史/在线等业务，负责消息的路由、持久化与实时推送。
- 需求只在 pptx：优先级：P0 为本期必做；P1 为增强（本期不做，列入后续）。
- 需求只在 pptx：F4 会话校验与心跳
- 需求只在 pptx：F9 拉人入群 / 退群
- 需求只在 pptx：F10 群列表 / 群成员列表
- 需求只在 pptx：F11/F12 单聊 / 群聊消息
- 需求只在 pptx：F13 历史消息分页
- 需求只在 pptx：F14 离线消息补推

### JetQiao__football-prediction-skill

段落标题不一致，需求条目 105 / 133 一致（pptx 拆出 151 条）

- 标题只在 Markdown：1.1 一句话定位
- 标题只在 Markdown：1.2 与同类项目的差异（对标基准）
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值
- 标题只在 Markdown：1.5 非目标（本期不做）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：将来若想做实时常驻 App，JSON 已现成可用，零锁定——但当前需求并不需要它。
- 需求只在 Markdown：编排：智能体读 SKILL.md 按流程执行；结构化计算交给脚本（保证可复现、统计严谨），非结构化情报由智能体联网搜集与判断。
- 需求只在 Markdown：语言：脚本用 Python（SciPy 做 Dixon-Coles / 泊松、蒙特卡洛）。
- 需求只在 Markdown：单文件：report_{date}.html，数据以内联 <script type="application/json"> 嵌入。
- 需求只在 Markdown：渲染：原生 JS 生成日期赛单卡片、单场详情展开、按联赛/置信度/价值的筛选排序。
- 需求只在 Markdown：图表：可靠性曲线、收益曲线、比分概率热力图等一律用内联 SVG（零依赖、file:// 可离线打开）。
- 需求只在 Markdown：可选汇总：index.html 列出历史各天报告，形成可浏览归档。
- 需求只在 Markdown：分发：双击打开 / 丢任意静态托管（GitHub Pages 等）皆可，无需构建与服务器。
- 需求只在 Markdown：报告头：日期、生成时间、当日场次数、数据来源与免责声明。
- 需求只在 Markdown：当日精选区：高置信 + 高价值场次置顶（推荐选项、置信度、价值边际、一句话理由）。
- 需求只在 pptx：实现口径以 README、架构文档 与 数据契约 为准；本文保留早期产品调研与完整需求背景。
- 需求只在 pptx：有一定足球知识、希望用数据辅助决策的竞彩购彩者（每天看竞彩赛单的人）。
- 需求只在 pptx：也兼顾大赛期间关注小组 / 淘汰赛走势的球迷。
- 需求只在 pptx：1.5 非目标（本期不做）
- 需求只在 pptx：❌ 不做最佳第三名（best third place）的晋级与对阵推算（组合算法复杂，明确排除）。
- 需求只在 pptx：❌ 不做真实下注 / 资金代操作，仅提供分析建议。
- 需求只在 pptx：❌ 不承诺准确率或盈利，输出为概率性参考。
- 需求只在 pptx：❌ 不做用户账号体系、社交分享（本期）。
- 需求只在 pptx：❌ 不做滚球 / 走地实时预测（本期只做赛前）。
- 需求只在 pptx：本项目最关键的形态决策。结合三大难点（非结构化情报、跨域、全覆盖）综合评估后确定。

### Jonnyan404__clip9

段落标题不一致，需求条目 8 / 8 一致（pptx 拆出 27 条）

- 标题只在 Markdown：（无标题）
- 标题只在 pptx：第 1 页
- 需求只在 pptx：use anydoc::{ConvertError, Format}; use base64::Engine as _; use base64::engine::general_purpose::STANDARD as BASE64;
- 需求只在 pptx：use crate::error::ActionError;
- 需求只在 pptx：/// PDF 的版面分析结论。 #[derive(Debug, Clone, PartialEq, Eq)] pub struct PdfLayout { /// 总页数。 pub page_count: u32, /// 多栏排版的页（1 起）。空 = 没检测到多栏。 pub multi_column_pages: Vec, }
- 需求只在 pptx：/// 文档里的图片集合。 #[derive(Debug)] pub struct ImageSet { /// 找到的图片总数。可能大于 items.len()（见 truncated）。 pub total: usize, /// 真的取出来的那些（按文档顺序）。 pub items: Vec, /// 因为超出 [MAX_IMAGE_TOTAL] 而没取全。 pub truncated: bool, }
- 需求只在 pptx：/// 一张取出来的图片。 #[derive(Debug)] pub struct ImageAsset { /// MIME，例如 image/png。 pub media_type: String, /// 图片原始字节的 base64（不带 data: 前缀 —— 前缀由调用方拼， /// 因为「怎么用」是调用方的事，这里只管把字节安全地放进 JSON）。 pub data_base64: String, /// 原始字节数（给界面显示用，免得前端再解一遍 base64 才知道多大）。 pub bytes: usize, }
- 需求只在 pptx：let format = detect(bytes, filename); let markdown = anydoc::to_markdown_bytes(bytes, format).map_err(explain)?; reject_empty(&markdown)?;
- 需求只在 pptx：let images: Vec<&anydoc::model::Asset> = document .assets .iter() .filter(|asset| asset.media_type.starts_with("image/")) .collect();
- 需求只在 pptx：/// ⚠️ 空结果不能当成功：一份只有图片的 docx、或一个空表格，转出来就是空串。 /// 把它当成功会让调用方铺出一张空白白板，而用户以为「转好了」。 /// 这与 format.rs 的 reject_noop 同源 —— 静默的「成功」比明确的失败糟得多。 fn reject_empty(markdown: &str) -> Result<(), ActionError> { if markdown.trim().is_empty() { return Err(invalid( "没能从这份文档里提取出正文（可能是纯图片或空文档）", )); } Ok(()) }
- 需求只在 pptx：fn invalid(message: impl Into) -> ActionError { ActionError::InvalidInput(message.into()) }
- 需求只在 pptx：#[cfg(test)] mod tests { use super::*;

### Jwz-git__Daygo

段落标题不一致，需求条目 19 / 20 一致（pptx 拆出 23 条）

- 标题只在 Markdown：1.4.1 捕获
- 标题只在 Markdown：1.4.2 分析
- 标题只在 Markdown：1.4.3 呈现
- 标题只在 Markdown：1.4.4 设置
- 标题只在 Markdown：1.4.5 生命周期
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：跟随光标需要显示器枚举、滞后判定和跨调用状态，而截图原语被有意设计成无状态的单次调用
- 需求只在 pptx：本文定义 Daygo 做什么、不做什么。它是范围争议的仲裁依据：任何"顺手加一个功能"的 提议，先回到这里确认它属于哪一节。
- 需求只在 pptx：各需求按 09 §9.7 分配给用户功能模块， 模块可并行推进；本文件继续作为产品范围依据，不因执行方式变化而增删需求。
- 需求只在 pptx：Daygo 的目标是保留工作本身的上下文：在构建什么、排查什么、和谁讨论什么、评审什么。
- 需求只在 pptx：F-C1 曾写成"跟随光标的活跃显示器"。原生契约冻结时把它改成了系统主显示器： 跟随光标需要显示器枚举、滞后判定和跨调用状态，而截图原语被有意设计成无状态的单次调用 （决策）。对单显示器用户没有区别； 多显示器用户在 v1 只会记录到主显示器。是否恢复跟随行为是一个待决产品问题（§1.7）， 不是实现遗漏。

### KaniuBillows__english-anywhere-lab

段落标题不一致，需求条目 107 / 107 一致（pptx 拆出 135 条）

- 标题只在 Markdown：3.1 目标（Goals）
- 标题只在 Markdown：3.2 非目标（Non-Goals）
- 标题只在 Markdown：Persona A：碎片化时间学习者
- 标题只在 Markdown：Persona B：场景导向学习者
- 标题只在 Markdown：Persona C：重启学习者
- 需求只在 pptx：FR-001：支持邮箱/第三方登录
- 需求只在 pptx：FR-002：支持 CEFR 自评 + 快速分级测试
- 需求只在 pptx：FR-003：设置学习目标（领域、每日时长、每周学习天数）
- 需求只在 pptx：FR-004：完成设定后生成首周计划
- 需求只在 pptx：AC-001：新用户 3 分钟内可完成初始化
- 需求只在 pptx：AC-002：计划中至少包含新学、复习、输出三类任务
- 需求只在 pptx：6.2 今日学习页（核心入口）
- 需求只在 pptx：6.3 学习包与内容中心
- 需求只在 pptx：6.6 学习进度与分析
- 需求只在 pptx：6.7 跨端与可用性

### Kerry-yangg__Dotalens

段落标题不一致，需求条目 200 / 231 一致（pptx 拆出 246 条）

- 标题只在 Markdown：2.1 当前产品背景
- 标题只在 Markdown：2.2 OpenDota 数据审计结论
- 标题只在 Markdown：2.3 用户问题
- 标题只在 Markdown：3.1 一句话定位
- 标题只在 Markdown：3.2 核心用户
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：Steam 数字 ID 绑定和最近比赛列表。
- 需求只在 Markdown：比赛解析状态与数据覆盖说明。
- 需求只在 Markdown：已解析比赛与未解析比赛筛选。
- 需求只在 Markdown：独立比赛详情视图。
- 需求只在 Markdown：本地助手手动导入 .dem 和 .dem.bz2。
- 需求只在 Markdown：单任务 replay 解析队列。
- 需求只在 Markdown：1 秒英雄快照：时间、坐标、金钱、经验、补刀、反补、等级、生命状态、装备。
- 需求只在 Markdown：帧级或事件级战斗日志保留。
- 需求只在 Markdown：秒级出装、击杀、死亡、神符、眼位和目标物时间线。
- 需求只在 Markdown：真实 Dota 地图上的英雄轨迹、营地、眼位和事件。
- 需求只在 pptx：本文档定义 Dota Lens 第一版的产品目标、用户流程、数据口径、功能范围、交互结构、技术边界和验收标准。
- 需求只在 pptx：OpenDota parser 内部每秒生成一次 interval 数据，包含英雄坐标、金钱、经验、补刀、反补、状态和装备快照；但公共 API 的聚合过程只保留每分钟曲线，并将前 10 分钟坐标压缩为热力图计数。
- 需求只在 pptx：Dota Lens 是一款面向个人玩家的 Dota 2 单场决策复盘工具，重点解释一名英雄在每个时间段做了什么、获得了什么、错过了什么。
- 需求只在 pptx：7.2 首次使用流程
- 需求只在 pptx：7.3 单场复盘流程
- 需求只在 pptx：7.4 数据处理流程
- 需求只在 pptx：flowchart LR A["小程序或 Web 客户端"] --> B["轻量云端 API"] B --> C["OpenDota / Valve 基础比赛索引"] A --> D["Windows 本地解析助手"] D --> E["用户导入或本地发现 replay"] E --> F["odota/parser 原始事件模式"] F --> G["标准化逐秒快照和事件"] G --> H["刷野、兵线和团战推导引擎"] H --> I["压缩分析包"] I --> B B --> J["对象存储"] B --> A
- 需求只在 pptx：9.1 账号与比赛列表
- 需求只在 pptx：9.3 单英雄逐秒复盘
- 需求只在 pptx：9.5 兵线与漏刀分析

### L20081125__dsh-lite-theme

段落标题不一致，需求条目 9 / 52 一致（pptx 拆出 74 条）

- 标题只在 Markdown：F1 主题系统（Web 端）✅ 已实现
- 标题只在 Markdown：F2 壁纸系统 ✅ 已实现
- 标题只在 Markdown：F3 动效系统 ✅ 已实现（打字机为实验性开关）
- 标题只在 Markdown：F4 实时预览 + 调色 + 另存（工坊）✅ 已实现
- 标题只在 Markdown：F5 主题包导入导出 ✅ 已实现
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 需求只在 Markdown：v1.1 变更：移除 TUI 支持（用户要求仅 Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 Markdown：~~TUI 端~~：v0.2 起已移除（用户决策：仅支持 Web）。
- 需求只在 Markdown：10 套主题全部可切换，切换即时生效
- 需求只在 Markdown：主题选择持久化（localStorage dsh-lite:state），刷新/重启保持
- 需求只在 Markdown：每套主题覆盖背景、前景、强调色、侧边栏、气泡、输入框、边框、代码块、选中态等 40+ token
- 需求只在 Markdown：毛玻璃/半透明质感（背景 token 半透明 + backdrop-filter）
- 需求只在 Markdown：遵循官方 data-ds-dark-theme 机制，与系统深浅色设置不冲突
- 需求只在 Markdown：上传本地图片（jpg/png/webp，≤20MB，自动压缩存储）
- 需求只在 Markdown：内置壁纸库 8 张（SVG 程序生成，樱花/星夜/极光/霓虹/花札/蒸汽波/EVA/誓约）
- 需求只在 Markdown：模糊度滑条（0~50px）、遮罩浓度滑条（0~85%）实时生效
- 需求只在 pptx：版本：v1.1（2026-08-16）｜状态：已评审（4 轮需求反问）+ 实现同步（v0.2） v1.1 变更：移除 TUI 支持（用户要求仅 Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 pptx：TUI 端：v0.2 起已移除（用户决策：仅支持 Web）。
- 需求只在 pptx：开源发布（仅 GitHub，不发布 npm）。
- 需求只在 pptx：F1 主题系统（Web 端）✅ 已实现
- 需求只在 pptx：需求：内置 10 套动漫主题，可一键切换，切换即时生效并持久化。
- 需求只在 pptx：实现方式：每套主题以紧凑 spec（accent/fg/bg/bgA）定义，启动时派生 40+ 官方 --dsw-alias-* token；通过官方 ctx.theme.register() 注册，官方 presenter 以 body 内联变量落地（优先级最高、无闪烁）。
- 需求只在 pptx：☒ 10 套主题全部可切换，切换即时生效
- 需求只在 pptx：☒ 主题选择持久化（localStorage dsh-lite:state），刷新/重启保持
- 需求只在 pptx：☒ 每套主题覆盖背景、前景、强调色、侧边栏、气泡、输入框、边框、代码块、选中态等 40+ token
- 需求只在 pptx：☒ 毛玻璃/半透明质感（背景 token 半透明 + backdrop-filter）

### LoD-Dawn__Fast-Vben-Admin

段落标题不一致，需求条目 135 / 135 一致（pptx 拆出 154 条）

- 标题只在 Markdown：3.1 一句话愿景
- 标题只在 Markdown：3.2 差异化
- 标题只在 Markdown：4.1 已具备能力
- 标题只在 Markdown：4.2 待打磨缺口
- 标题只在 Markdown：6.1 v1.0 目标
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 16 页
- 需求只在 pptx：让开发者拿到项目当天就能开始写业务，而不是先花一周补账号、权限、菜单、日志、上传、通知和部署这些通用基建。
- 需求只在 pptx：只需要纯 API 模板的用户。
- 需求只在 pptx：只需要纯前端 Vben 模板的用户。
- 需求只在 pptx：需要大型 ERP/OA/CRM 成品系统的用户。
- 需求只在 pptx：强依赖 Java Spring Boot 生态、React 生态或复杂低代码平台的团队。
- 需求只在 pptx：7.3 暂不进入范围
- 需求只在 pptx：目标：提供安全、完整、可用于中后台的账号闭环。
- 需求只在 pptx：目标：管理员可维护系统用户，并建立用户、部门、角色关系。
- 需求只在 pptx：目标：形成可复用 RBAC 权限体系，替代单一 is_superuser 判断。
- 需求只在 pptx：目标：菜单、路由和权限码统一维护。

### LordCasser__atlas

段落标题不一致，需求条目 118 / 118 一致（pptx 拆出 129 条）

- 标题只在 Markdown：文件发现
- 标题只在 Markdown：源文件编码与读取
- 标题只在 Markdown：抽取
- 标题只在 Markdown：符号与引用
- 标题只在 Markdown：Resolution
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 8 页
- 需求只在 pptx：Atlas 是一个 local-first Rust-native 代码语义图谱引擎。它扫描本地代码库，基于 tree-sitter 抽取符号、作用域、引用、调用、import/include、数据流和控制流事实，持久化到 .atlas/atlas.db，并通过 CLI 与 MCP 为 LLM Agent 提供搜索、调用分析、依赖分析、影响面分析、上下文构建、变量来源追踪和调用路径查询能力。
- 需求只在 pptx：当前代码已接入 Go、Rust、C#、PHP、Ruby、Kotlin 的 DataflowInterproc frontends。所有 14 种语言均为 DataflowInterproc 级别，具备完整 dataflow 抽取能力（参数、赋值、调用、字段访问、返回）、跨函数 summary 桥接（ArgToParam/ReturnToCall）和 e2e 测试。部分语言的 CFG 和特定跨函数路径仍有个别 gap（见各语言 capability profile limitations）。
- 需求只在 pptx：源文件编码与读取
- 需求只在 pptx：tree-sitter queries + typed language frontend slots -> FileFacts
- 需求只在 pptx：图查询和上下文
- 需求只在 pptx：图查询优先使用 GraphSnapshot 或按需加载的专用图结构，避免每一步访问 SQLite。
- 需求只在 pptx：变量来源追踪与调用路径查询
- 需求只在 pptx：target argument / variable -> local assignment source -> field/access path source -> function return source -> callee parameter -> caller argument -> caller chain / entry candidate
- 需求只在 pptx：Atlas 不做 taint rule / finding 产品能力。Atlas 不包含 taint 代码、taint schema、taint rule/finding 产品能力——这些已从源码和 schema 中完全删除。不进入当前需求、路线图或验收门槛。当前阶段不要求、也不规划漏洞规则三元组、自动端到端漏洞传播扫描、全项目 finding 或内置漏洞规则生态。
- 需求只在 pptx：Level 0: parse/index only, trace unsupported Level 1: symbols + references + calls Level 2: bindings + simple assignments Level 3: field access + call args + returns Level 4: CFG (未来精度增强层，不作为当前 trace MVP 前置门槛) Level 5: lightweight interprocedural summaries

### LubyRuffy__ProxyCraft

段落标题不一致，需求条目 61 / 61 一致（pptx 拆出 63 条）

- 标题只在 Markdown：4.1 代理核心 (Proxy Core)
- 标题只在 Markdown：4.2 HTTPS 支持 (MITM)
- 标题只在 Markdown：4.3 HTTP/2 支持
- 标题只在 Markdown：4.4 Server-Sent Events (SSE) 支持
- 标题只在 Markdown：4.5 流量日志与展示 (Logging & Display)
- 需求只在 pptx：4.4 Server-Sent Events (SSE) 支持
- 需求只在 pptx：4.5 流量日志与展示 (Logging & Display)

### Mark7766__spring-ai-apps

段落标题不一致，需求条目 49 / 84 一致（pptx 拆出 54 条）

- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值
- 标题只在 Markdown：1.5 产品形态
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：学习者：高效、个性化的学习体验，像私人导师一样陪伴，缩短技能掌握时间。
- 需求只在 Markdown：课程开发者：AI 辅助快速创建课程，优化教学设计，扩大内容影响力。
- 需求只在 Markdown：平台：连接学习与创作，构建内容生态，兼顾个人成长和企业培训。
- 需求只在 Markdown：Web 应用，计划扩展至 iOS/Android APP。
- 需求只在 Markdown：包含 AI 对话框、课程播放器、练习模块、开发者编辑器。
- 需求只在 Markdown：支持个人用户和企业版（批量管理和数据分析）。
- 需求只在 Markdown：在线教育需求旺盛：2025 年全球在线教育市场预计超 5000 亿美元，AI 驱动的教育工具增长迅速。
- 需求只在 Markdown：传统课程局限：视频课程缺乏互动、个性化不足，用户完成率低（平均仅 15%）。
- 需求只在 Markdown：开发者痛点：课程创建耗时、教学设计复杂、内容更新滞后。
- 需求只在 Markdown：企业需求：高效、低成本的员工培训，需定制化和隐私保障。
- 需求只在 pptx：版本：1.1日期：2025-04-13作者：Mark
- 需求只在 pptx：4.2 课程开发者功能
- 需求只在 pptx：4.3 平台通用功能
- 需求只在 pptx：说明：用户通过前端交互，请求经后端处理，AI 层调用模型和数据库生成响应，数据存储层确保高效检索和持久化，基础设施层保障系统稳定。
- 需求只在 pptx：8.3 核心代码示例

### Mingyang0018__FastVideo3

段落标题不一致，需求条目 19 / 19 一致（pptx 拆出 34 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 设计目标（按优先级）
- 标题只在 Markdown：1.4 非目标（v1 明确不做）
- 标题只在 Markdown：F1 主题/剧本输入与结构化剧本生成
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 需求只在 pptx：1.4 非目标（v1 明确不做）
- 需求只在 pptx：❌ 不自研、不微调任何生成模型（LoRA 训练需本地 GPU，列入扩展期课题）
- 需求只在 pptx：❌ 不以 90 分钟长片为 v1 交付目标（架构支持，路线图为：30 秒微短剧 → 3 分钟短剧 → 剧集 → 长片）
- 需求只在 pptx：❌ 不做实时交互生成、不做视频流式播放
- 需求只在 pptx：❌ 不做多租户 SaaS 计费系统（预留成本台账接口即可）
- 需求只在 pptx：F1 主题/剧本输入与结构化剧本生成
- 需求只在 pptx：F2 角色与场景资产生成（资产库）
- 需求只在 pptx：F4 镜头视频生成（图生视频）
- 需求只在 pptx：F5 对白语音与口型同步（含双人同屏）
- 需求只在 pptx：F6 转场动画与成片合成

### Neilouo__AI-FortuneTeller

段落标题不一致，需求条目 63 / 103 一致（pptx 拆出 109 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值
- 标题只在 Markdown：2.1 市场规模
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 15 页
- 需求只在 Markdown：打造最有趣、最智能的AI算命体验
- 需求只在 Markdown：让传统命理文化与现代AI技术完美结合
- 需求只在 Markdown：提供情感价值和心理慰藉，而非单纯的算命工具
- 需求只在 Markdown：娱乐价值：有趣的对话体验，不同人格风格选择
- 需求只在 Markdown：情感价值：心理共鸣和情感支持
- 需求只在 Markdown：认知价值：了解传统文化，获得新的思考角度
- 需求只在 Markdown：决策参考：在人生困惑时提供一种参考视角
- 需求只在 Markdown：展示三种人格的介绍和特点
- 需求只在 Markdown：支持用户选择人格
- 需求只在 Markdown：选中后进入对应人格的对话模式
- 需求只在 pptx：版本：v1.0日期：2024年负责人：产品团队
- 需求只在 pptx：3.1.1 人格选择系统
- 需求只在 pptx：☐ 展示三种人格的介绍和特点
- 需求只在 pptx：☐ 支持用户选择人格
- 需求只在 pptx：☐ 选中后进入对应人格的对话模式
- 需求只在 pptx：☐ 人格风格在对话中保持一致
- 需求只在 pptx：3.1.2 八字计算系统
- 需求只在 pptx：☐ 支持公历日期输入
- 需求只在 pptx：☐ 准确计算八字四柱
- 需求只在 pptx：☐ 准确分析五行分布

### NewLifeX__AntJob

段落标题不一致，需求条目 68 / 69 一致（pptx 拆出 76 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2.1 非功能目标
- 标题只在 Markdown：3.1 SYS — 核心调度引擎
- 标题只在 Markdown：3.2 DATA — 数据持久化
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 需求只在 Markdown：WEB-2a 蚂蚁区域注册：Cube 区域"蚂蚁调度"，AntEntityController\<T> 基类支持 appId 导航栏。
- 需求只在 pptx：版本：v5.0 | 日期：2026-10-18 | 从代码逆向整理
- 需求只在 pptx：本文档描述 AntJob 分布式任务调度系统的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：企业只需编写一个 Handler 类，即可获得分布式调度、弹性伸缩、失败重试、数据切片、可视化监控等全部能力——把调度复杂度交给框架，业务开发者只关心"处理一条数据"。
- 需求只在 pptx：编码说明：采用字母前缀方案。存量项目可继续使用 Mx- 编码。
- 需求只在 pptx：3.1 SYS — 核心调度引擎
- 需求只在 pptx：3.4 SRV — 调度中心服务
- 需求只在 pptx：3.5 WEB — 可视化管理后台
- 需求只在 pptx：WEB-2a 蚂蚁区域注册：Cube 区域"蚂蚁调度"，AntEntityController<T> 基类支持 appId 导航栏。

### NewLifeX__NewLife.AI

段落标题不一致，需求条目 136 / 136 一致（pptx 拆出 150 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：1.3 工程分层
- 标题只在 Markdown：2.1 核心目标
- 标题只在 Markdown：2.2 模块编码映射
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 11 页
- 需求只在 pptx：版本：v4.2 | 日期：2026-10-24 | 对齐代码基线：v1.7.2026.1024
- 需求只在 pptx：本文档描述 NewLife.AI 开源项目（NewLife.AI + NewLife.ChatAI）的愿景与核心目标、模块编码和功能方向。完成状态统一维护在功能清单，详细设计在架构设计及各专项文档中展开。
- 需求只在 pptx：2.2 模块编码映射
- 需求只在 pptx：功能清单见 功能清单.md，架构设计见 架构设计.md。
- 需求只在 pptx：本章按模块编码组织功能方向。每个功能点的实现状态、测试和注释在 功能清单 中追踪，详细设计在各专项文档中展开。
- 需求只在 pptx：NewLife.AI 是所有上层能力的基础设施，重点是统一接入不同服务商、协议和模型能力。
- 需求只在 pptx：WebUI 是用户最主要的交互入口，目标是建设标准、稳定、可扩展的 AI Web 对话系统。
- 需求只在 pptx：核心能力：工具 > 技能。 工具决定 AI 能做什么，技能决定 AI 怎么做。能力扩展让 AI 从"会聊天"变成"能做事"。 职责边界：AI 模块（§3.1）定义接口（IChatClient、ToolChatClient、IChatFilter、IToolProvider、MCP 客户端核心等），TOOL 模块提供这些接口的具体实现和深入使用。
- 需求只在 pptx：知识进化是本仓库的基础差异能力。用户记忆让 AI 从"对话工具"初步进化为"越用越懂你"的助手，自动从对话中提取结构化用户记忆。高级进化能力（痛觉、好奇心、蒸馏、融合等）不在本仓库内置，可按需基于 MemoryService 等扩展点实现。
- 需求只在 pptx：API 网关让外部系统以标准协议接入 AI 能力，核心价值是在接口转发之外提供记忆注入与技能增强。v1.6 起默认提供「纯净转发」模式（关闭领域模式时不注入不记录），记忆注入与技能增强需开启网关领域模式。

### NewLifeX__NewLife.Agent

段落标题不一致，需求条目 71 / 74 一致（pptx 拆出 77 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 M1 平台工具类
- 标题只在 Markdown：3.2 M2 配置管理
- 标题只在 Markdown：3.3 M3 服务抽象与跨平台宿主
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：一句话描述：继承 ServiceBase，你的程序就拥有了跨平台服务治理能力。
- 需求只在 Markdown：目标用户：需要长期运行后台服务的 .NET 开发者与运维人员。
- 需求只在 Markdown：核心场景：Windows 服务部署、Linux 守护进程、macOS LaunchAgent、ASP.NET Core 生产托管。
- 需求只在 pptx：本文档描述 NewLife.Agent 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：3.3 M3 服务抽象与跨平台宿主
- 需求只在 pptx：3.4 M4 命令行运维体系
- 需求只在 pptx：3.5 M5 健康监控与自愈
- 需求只在 pptx：核心竞争壁垒
- 需求只在 pptx：文档版本：v2.0创建日期：2026-07-15关联文档：功能清单、架构设计、竞品分析、使用与运维手册

### NewLifeX__NewLife.BACnet

段落标题不一致，需求条目 99 / 100 一致（pptx 拆出 118 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 TRN — 传输层
- 标题只在 Markdown：3.2 COD — 协议编解码
- 标题只在 Markdown：3.3 DSC — 设备发现
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：成为 .NET 生态中功能最完整、最易集成的 BACnet 协议库，让楼宇自动化工程师和 IoT 边缘开发者能够用最少的代码实现设备发现、数据采集、属性写入和事件处理，并无缝对接 NewLife IoT 物联网平台生态，成为楼控系统与 IoT 平台之间的可靠桥梁。
- 需求只在 pptx：本文档描述 NewLife.BACnet 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：以下串口传输实现代码存在但已从编译中排除，需跨平台串口兼容性支持后重新启用： TRN-5 MS/TP (RS485) 串口传输、TRN-6 PTP (RS232) 串口传输、TRN-7 通用串口传输基类、 TRN-8 Ethernet 802.3 直连传输、TRN-9 Windows 管道传输
- 需求只在 pptx：实现 BACnet 各层协议的编码和解码，确保与标准设备的互操作性。
- 需求只在 pptx：在 BACnet 网络中自动发现在线设备。
- 需求只在 pptx：读取和写入 BACnet 设备对象的属性值。
- 需求只在 pptx：订阅设备属性变化，当值发生变化时主动推送通知。
- 需求只在 pptx：处理 BACnet 事件通知、报警摘要，用于楼宇报警管理系统。
- 需求只在 pptx：通过 BACnet 文件服务读写设备上的文件对象。
- 需求只在 pptx：在设备中动态创建和删除 BACnet 对象。
- 需求只在 pptx：将 .NET 应用暴露为 BACnet 设备，供第三方楼控系统读写。

### NewLifeX__NewLife.Cube

段落标题不一致，需求条目 151 / 155 一致（pptx 拆出 155 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 BASE 基础服务
- 标题只在 Markdown：3.2 AUTH 用户认证
- 标题只在 Markdown：3.3 PERM 权限管理
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：通用后台能力：认证、权限、菜单、CRUD、导入导出、日志、配置开箱即用
- 需求只在 Markdown：多前端支持：Vue 为官方前端与核心库载体；仓库内另提供 Angular / Svelte / NaiveUI / ArcoVue / Vuetify / TDesign / MUI / Shadcn 等参考实现，React 皮肤独立为 CubeAntd 仓库；MVC Razor（CubeNC）保持兼容
- 需求只在 Markdown：可扩展架构：通过 EntityController 继承、字段元数据、IModule 插件机制深度定制
- 需求只在 Markdown：超大数据支撑：基于 XCode ORM 的分表、读写分离、二级缓存，支撑单表 100 亿级数据
- 需求只在 pptx：本文档描述魔方（NewLife.Cube）快速开发平台的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：主题皮肤（AdminLTE/ElementUI/LayuiAdmin/Metronic/Metronic8/Tabler/Blazor）已冻结，见 §4 暂缓清单。
- 需求只在 pptx：前端核心以 Vue 皮肤为准；其余前端皮肤为仓库内参考实现，暂不投入，也未发布 NuGet；React 皮肤已独立为 CubeAntd 仓库。
- 需求只在 pptx：3.12 I18N 多语言本地化

### NewLifeX__NewLife.IoT

段落标题不一致，需求条目 57 / 57 一致（pptx 拆出 64 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 SYS — 核心驱动体系
- 标题只在 Markdown：3.2 TSL — 物模型规范
- 标题只在 Markdown：3.3 DEV — 设备接口
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 需求只在 pptx：本文档描述 NewLife.IoT 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计或各模块架构文档中展开。
- 需求只在 pptx：定位核心：平台只调用接口，驱动只实现接口，两者永不直接耦合。
- 需求只在 pptx：物联网接入像文件系统一样简单——平台打开设备得到节点、读取节点得到带质量的数据、写入节点得到回显确认。异步优先、类型安全、零堆分配诊断。
- 需求只在 pptx：3.1 SYS — 核心驱动体系
- 需求只在 pptx：3.6 SER — 串口驱动 (NewLife.IoTSerial)
- 需求只在 pptx：3.7 NET — 网络驱动 (NewLife.IoTSocket)
- 需求只在 pptx：3.8 DB — 数据库驱动 (NewLife.IoTDatabase)

### NewLifeX__NewLife.MQTT

段落标题不一致，需求条目 59 / 59 一致（pptx 拆出 67 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 PROT 协议编解码
- 标题只在 Markdown：3.2 TRAN 传输协议
- 标题只在 Markdown：3.3 CLNT 客户端
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 10 页
- 需求只在 pptx：本文档描述 NewLife.MQTT 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计或各模块架构文档中展开。
- 需求只在 pptx：做 .NET 生态中最完整的 MQTT 协议实现——协议全版本覆盖、客户端与服务端一体、七种传输协议、企业功能免费内置，纯国产自主研发、MIT 开源、零第三方依赖，满足从嵌入式设备到企业级 Broker 的全部 IoT 通信需求。
- 需求只在 pptx：编码说明：模块编码已从 M1-M7 迁移至字母前缀方案：PROT（协议）/ TRAN（传输）/ CLNT（客户端）/ SRV（服务端）/ ENT（企业扩展）/ CLUS（集群）/ SEC（安全增强）。
- 需求只在 pptx：协议层涵盖 MQTT 3.1 / 3.1.1 / 5.0 三个版本的完整报文与属性编解码，是所有上层功能的基础。
- 需求只在 pptx：全功能 MQTT 客户端，面向设备开发者提供极简 API 和自动容错能力。
- 需求只在 pptx：高性能 MQTT Broker，面向平台运维工程师提供全版本兼容、会话管理、安全认证和可扩展架构。
- 需求只在 pptx：企业级功能全部免费内置，无需额外付费。
- 需求只在 pptx：在 SRV-3 基础认证之上，提供连接/消息速率控制和高级认证机制。

### NewLifeX__NewLife.Modbus

段落标题不一致，需求条目 12 / 13 一致（pptx 拆出 16 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 CORE — 协议核心层
- 标题只在 Markdown：3.2 TRAN — 传输变体
- 标题只在 Markdown：3.3 FC — 功能码
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：为 .NET 工业物联网生态提供一套协议最完整、功能码覆盖最全、传输变体最丰富的 Modbus 协议库，支持 IoTEdge 网关及各类工业应用开发，让 .NET 开发者能用最少的代码完成工业设备对接，同时具备充分的可扩展性和可观测性。
- 需求只在 pptx：版本: v4.3 | 更新: 2026-10-24 关联: 功能清单 | 架构设计 | 竞品分析
- 需求只在 pptx：本文档描述 NewLife.Modbus 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计或各模块架构文档中展开。
- 需求只在 pptx：编码说明：采用字母前缀方案，各模块按前置依赖排序（基础→核心→集成→增强→测试）。每个模块下的详细功能点列表见 功能清单.md。
- 需求只在 pptx：3.7 I18N — 多语言本地化

### NewLifeX__NewLife.Remoting

段落标题不一致，需求条目 82 / 83 一致（pptx 拆出 93 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 RPC — RPC 核心框架
- 标题只在 Markdown：3.2 STRM — 流式调用 (Server-Streaming)
- 标题只在 Markdown：3.3 CLNT — 客户端基类
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 需求只在 Markdown：包：NewLife.Remoting；定位：核心通信库；覆盖：RPC 客户端/服务端、协议编解码、连接管理、流式调用、客户端基类、指令下发管线、自动更新、NativeAOT 支持
- 需求只在 pptx：本文档描述 NewLife.Remoting 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：排序原则：协议消息 → 编解码 → 内存管理 → 元数据模型 → 处理流水线 → 连接管理 → 客户端/服务端 → 会话扩展 → 元数据传递 → 重试策略
- 需求只在 pptx：3.2 STRM — 流式调用 (Server-Streaming)
- 需求只在 pptx：提供开箱即用的客户端生命周期管理，调用 UPGD Upgrade 实现自动更新
- 需求只在 pptx：提供下载、解压、覆盖、回滚、重启完整的自动更新链路，被 CLNT 客户端基类的自动升级功能调用
- 需求只在 pptx：提供服务端控制器基类和设备管理服务，依赖 RPC 核心框架和 CMD 指令下发
- 需求只在 pptx：提供云端到设备的指令下发、执行和结果回传完整管线，依赖 RPC 核心框架
- 需求只在 pptx：2026-10 起纳入建设，横切核心库全部模块；范围、实测结论与已知边界详见 AOT兼容性分析
- 需求只在 pptx：2026-10 决策：不拆分新项目，在扩展库内提供 AOT 可用的最小 API 宿主；详见 AOT兼容性分析 §7/§8
- 需求只在 pptx：3.9 L10N — 多语言本地化

### NewLifeX__NewLife.RocketMQ

段落标题不一致，需求条目 63 / 68 一致（pptx 拆出 64 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 痛点
- 标题只在 Markdown：1.3 愿景
- 标题只在 Markdown：3.1 PROTO — 协议通信
- 标题只在 Markdown：3.2 CODEC — 消息编解码
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：NewLife.RocketMQ 是企业级纯托管 .NET RocketMQ 客户端，专为 .NET 生态设计，覆盖 .NET Framework 4.5+ 到 .NET 10。给 .NET 开发者提供一个零外部依赖、双协议支持、多云适配的消息队列客户端。
- 需求只在 Markdown：协议覆盖不全：现有方案多数仅支持单一协议，无法同时兼容 Remoting（4.x Broker）和 gRPC（5.x Proxy）两种接入方式
- 需求只在 Markdown：外部依赖沉重：部分方案依赖 Google.Protobuf、Grpc.Net.Client 等第三方库，增加部署复杂度和包体积
- 需求只在 Markdown：框架兼容不足：大量企业仍运行在 .NET Framework 4.5+，但可用选项极为有限
- 需求只在 Markdown：云厂商适配分散：接入阿里云、华为云、腾讯云需要各自独立的 SDK，缺乏统一接口
- 需求只在 pptx：本文档描述 NewLife.RocketMQ 的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。

### NewLifeX__NewLife.Siemens

段落标题不一致，需求条目 56 / 133 一致（pptx 拆出 156 条）

- 标题只在 Markdown：1.0 项目愿景
- 标题只在 Markdown：1.1 背景与痛点
- 标题只在 Markdown：1.2 目标
- 标题只在 Markdown：3.1 连接管理
- 标题只在 Markdown：3.2 字节级读写
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：提供工业物联网领域最完整、最易用的西门子 PLC S7 协议 .NET 实现，作为 NewLife 开源生态的 IoT 标准驱动组件，让工控工程师能够用几行代码无缝接入任意型号的西门子 PLC，同时支持在 IoTEdge 工业网关中零代码配置化采集。
- 需求只在 Markdown：支持 TCP 连接建立（含 KeepAlive 设置）
- 需求只在 Markdown：完成 COTP ConnectionRequest / ConnectionConfirmed 握手
- 需求只在 Markdown：完成 S7 SetupMessage 协商 PDU 大小
- 需求只在 Markdown：断线后下次读写自动触发重连（GetStream 内部检测）
- 需求只在 Markdown：支持显式 Close() 释放连接
- 需求只在 Markdown：ReadBytes 支持任意长度（超 PDU 限制时自动分多段）
- 需求只在 Markdown：WriteBytes 支持任意长度（超 PDU 限制时自动分多段）
- 需求只在 Markdown：读写失败时抛出包含错误码的 ApiException
- 需求只在 Markdown：支持所有地址区域：DB / Input / Output / Memory / Timer / Counter
- 需求只在 pptx：☒ 支持 TCP 连接建立（含 KeepAlive 设置）
- 需求只在 pptx：☒ 完成 COTP ConnectionRequest / ConnectionConfirmed 握手
- 需求只在 pptx：☒ 完成 S7 SetupMessage 协商 PDU 大小
- 需求只在 pptx：☒ 断线后下次读写自动触发重连（GetStream 内部检测）
- 需求只在 pptx：☒ 支持显式 Close() 释放连接
- 需求只在 pptx：☒ ReadBytes 支持任意长度（超 PDU 限制时自动分多段）
- 需求只在 pptx：☒ WriteBytes 支持任意长度（超 PDU 限制时自动分多段）
- 需求只在 pptx：☒ 读写失败时抛出包含错误码的 ApiException
- 需求只在 pptx：☒ 支持所有地址区域：DB / Input / Output / Memory / Timer / Counter
- 需求只在 pptx：☒ 支持 DB（DBB/DBW/DBD/DBX/STRING）地址格式

### NewLifeX__Stardust

段落标题不一致，需求条目 29 / 30 一致（pptx 拆出 48 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2.1 模块总览
- 标题只在 Markdown：2.2 功能全景图
- 标题只在 Markdown：3.1 SDK 分布式核心 SDK
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：编号：CFG；目标：配置中心；一句话描述：应用从中心读取配置，支持多环境热更新；所属工程：StarServer + SDK + StarWeb；架构文档：SVR-StarServer架构
- 需求只在 pptx：本文档描述星尘（Stardust）分布式服务平台的愿景、核心目标和功能需求。完成状态在功能清单中追踪，详细设计在各模块架构文档中展开。
- 需求只在 pptx：架构文档：SDK-分布式核心SDK架构
- 需求只在 pptx：接入契约：APM-17-监控接入API | 能力矩阵与路线图：SDK/README
- 需求只在 pptx：3.2 SVR 服务端基础能力
- 需求只在 pptx：架构文档：SVR-StarServer架构
- 需求只在 pptx：架构文档：SVR-StarServer架构
- 需求只在 pptx：架构文档：SVR-StarServer架构
- 需求只在 pptx：架构文档：NODE-StarAgent架构 子模块文档：NODE-9-指令下发 | NODE-14-防火墙管理 | NODE-15-StarAgent远程部署 | NODE-16-阿里云DNS动态域名解析 | NODE-17-进程管理 | NODE-18-Web管理面板 | SVR-8-远程命令执行安全
- 需求只在 pptx：架构文档：SVR-StarServer架构
- 需求只在 pptx：3.7 REG 注册中心与服务发现

### NewLifeX__X

段落标题不一致，需求条目 134 / 136 一致（pptx 拆出 138 条）

- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：3.1 M1 基础扩展
- 标题只在 Markdown：3.2 M2 日志与追踪
- 标题只在 Markdown：3.3 M3 定时调度
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 需求只在 Markdown：NewLife.Core 是 NewLife 组件生态的基础核心库，为构建可扩展 .NET 应用程序提供高性能基础设施。支持 .NET Framework 4.5 至 .NET 10.0 全版本。
- 需求只在 Markdown：M5-10 系统配置：SysConfig 基于 Config<T> 的系统名称、版本、显示名称等基本设置管理。
- 需求只在 pptx：版本：v12 | 日期：2026-10-19 | 从代码逆向整理
- 需求只在 pptx：本文档描述 NewLife.Core 核心库的愿景、核心目标和功能方向。完成状态在功能清单中追踪，详细设计在架构设计中展开。
- 需求只在 pptx：成为 .NET 生态中最全面、最高性能的基础类库，让开发者在任何 .NET 版本上都能获得一致、高效的底层能力。
- 需求只在 pptx：M5-10 系统配置：SysConfig 基于 Config 的系统名称、版本、显示名称等基本设置管理。

### PGshen__thinking-map

段落标题不一致，需求条目 100 / 122 一致（pptx 拆出 131 条）

- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 用户痛点
- 标题只在 Markdown：1.5 产品核心价值
- 需求只在 Markdown：ThinkingMap 是一款交互式AI问题解决可视化助手，将AI的思考和问题解决过程转化为可视化的图结构，允许用户在过程中随时干预、提问。
- 需求只在 Markdown：现有AI助手给出答案的过程不透明，用户难以理解和信任
- 需求只在 Markdown：复杂问题需要多步骤思考，但传统AI交互难以清晰展示思路演进
- 需求只在 Markdown：用户想要在思考过程中提供输入和调整方向，而不只是在开始和结束时
- 需求只在 Markdown：现有解决方案缺乏结构化的问题分解和可视化
- 需求只在 Markdown：透明化思考: 可视化AI的问题解决步骤和逻辑
- 需求只在 Markdown：用户控制: 在任何阶段干预和引导思考方向
- 需求只在 Markdown：结构化思维: 将复杂问题分解为可管理的步骤
- 需求只在 Markdown：探索性思考: 支持多种可能的解决路径和分支
- 需求只在 Markdown：可视化工作区正常显示和交互
- 需求只在 pptx：3.1 问题输入与初步分析
- 需求只在 pptx：3.1.1 问题输入界面
- 需求只在 pptx：3.1.2 问题理解确认
- 需求只在 pptx：3.2 可视化工作区
- 需求只在 pptx：3.2.1 可视化思考图展示
- 需求只在 pptx：3.2.2 节点交互功能
- 需求只在 pptx：3.2.3 实时更新机制
- 需求只在 pptx：3.3 操作面板系统
- 需求只在 pptx：3.3.1 面板基础功能
- 需求只在 pptx：信息展示区域

### Peter-cuhk__robot-data-studio

段落标题不一致，需求条目 231 / 254 一致（pptx 拆出 280 条）

- 标题只在 Markdown：3.1 本地优先
- 标题只在 Markdown：3.2 原始数据只读
- 标题只在 Markdown：3.3 可解释而非神秘评分
- 标题只在 Markdown：3.4 统一语义，不做 N×N 转换
- 标题只在 Markdown：3.5 复用优先，但不外包核心资产
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：本地项目创建和目录导入。
- 需求只在 Markdown：ACT/robomimic 风格 HDF5 Reader/Writer。
- 需求只在 Markdown：UMI/Zarr Reader/Writer；针对 UMI 的具体工程版本通过 profile 适配。
- 需求只在 Markdown：Episode 列表、筛选、人工状态标记。
- 需求只在 Markdown：基于 Rerun 的多模态同步回放。
- 需求只在 Markdown：第一批确定性质量规则。
- 需求只在 Markdown：可插拔 VLM 质量规则接口，至少提供一个本地示例适配器和一个 OpenAI-compatible API 适配器。
- 需求只在 Markdown：非破坏式 Pipeline 和基础节点。
- 需求只在 Markdown：坐标系与位姿表达转换。
- 需求只在 Markdown：导出任务、进度、取消、日志和结果报告。
- 需求只在 pptx：版本：V1.0 Draft日期：2026-06-23产品形态：完全开源、本地优先的机器人数据清洗与转换平台首版范围：机械臂与具身操作 Episode 数据，单机数据集不超过 10 GB
- 需求只在 pptx：产品不会把原始数据强制转存到私有数据库。原始文件始终只读，平台只维护项目元数据、本地索引、缓存、处理图和质量报告。首版为浏览器 UI 加本地 Python API，默认不上传任何机器人数据。
- 需求只在 pptx：当前缺少一个可靠且全面的开源平台，把"看数据、判断质量、清洗数据、转换格式、转换坐标系、验证输出"组合为一个端到端工作流。
- 需求只在 pptx：3.2 原始数据只读
- 需求只在 pptx：3.3 可解释而非神秘评分
- 需求只在 pptx：3.4 统一语义，不做 N×N 转换
- 需求只在 pptx：3.5 复用优先，但不外包核心资产
- 需求只在 pptx：支持选择本地目录或文件。
- 需求只在 pptx：禁止浏览器直接承担大文件解析；解析由本地 API 完成。
- 需求只在 pptx：最近项目保存路径引用，不复制数据。

### Poghappy__IhuoniaoN8NFirecralwrules

段落标题不一致，需求条目 22 / 22 一致（pptx 拆出 57 条）

- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：2. 功能需求
- 标题只在 Markdown：2.1 核心功能（Must Have）
- 标题只在 Markdown：2.2 重要功能（Should Have）
- 标题只在 Markdown：2.3 可选功能（Could Have）
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 16 页
- 需求只在 pptx：产品经理（PM）/需求分析师（BA）
- 需求只在 pptx：# 产品需求文档（PRD）## 产品愿景Firecrawl数据采集器是一个基于AI的现代化数据采集平台，为企业和个人用户提供智能、高效、安全的数据采集和分析服务。## 产品目标- 提供简单易用的数据采集工具- 实现AI驱动的智能数据分析- 支持多租户的企业级服务- 确保数据安全和隐私保护## 目标用户- 数据分析师：需要采集和分析数据- 企业用户：需要批量数据采集服务- 开发者：需要API集成数据采集- 研究人员：需要学术数据采集## 非目标- 不提供数据存储服务（仅提供采集和分析）- 不支持实时数据流处理- 不提供数据可视化工具- 不提供数据清洗和预处理服务
- 需求只在 pptx：数据采集管理
- 需求只在 pptx：### 功能描述提供完整的数据采集任务管理功能，支持多种数据源和采集方式。### 功能特性- 创建数据采集任务- 监控采集进度- 管理采集结果- 设置采集参数### 用户界面- 任务列表页面- 任务详情页面- 任务创建向导- 进度监控面板### 技术实现- RESTful API接口- 异步任务处理- 实时状态更新- 错误处理和重试
- 需求只在 pptx：### 功能描述基于AI技术提供智能数据分析和查询功能。### 功能特性- 自然语言查询- 数据自动分类- 内容摘要生成- 相似性搜索### 用户界面- AI查询界面- 分析结果展示- 分类管理页面- 搜索历史记录### 技术实现- OpenAI API集成- Pinecone向量数据库- 自然语言处理- 机器学习模型
- 需求只在 pptx：### 功能描述提供完整的多租户架构，支持企业级用户管理。### 功能特性- 租户数据隔离- 用户权限管理- 资源配额控制- 团队协作功能### 用户界面- 租户管理页面- 用户管理界面- 权限设置页面- 团队协作面板### 技术实现- 多租户数据架构- 基于角色的权限控制- 资源配额管理- 团队协作API
- 需求只在 pptx：### 功能描述提供数据采集结果的可视化展示功能。### 功能特性- 数据图表展示- 采集统计报告- 趋势分析图表- 导出功能### 用户界面- 数据仪表板- 图表展示页面- 报告生成界面- 导出设置页面### 技术实现- 图表库集成- 数据统计计算- 报告生成引擎- 多格式导出
- 需求只在 pptx：### 功能描述提供高级数据分析功能，满足专业用户需求。### 功能特性- 自定义分析规则- 数据关联分析- 预测分析- 异常检测### 用户界面- 分析规则配置- 关联分析界面- 预测结果展示- 异常告警面板### 技术实现- 规则引擎- 机器学习算法- 统计分析库- 告警系统
- 需求只在 pptx：数据存储服务
- 需求只在 pptx：1. 数据采集流程

### Q572071793__word-pinyin

段落标题不一致，需求条目 117 / 120 一致（pptx 拆出 126 条）

- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：2.1 核心功能
- 标题只在 Markdown：2.1.1 拼音转换功能
- 标题只在 Markdown：2.1.2 拼音显示功能
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：教师准备拼音教学材料，需要快速生成带拼音的文本。
- 需求只在 Markdown：制作拼音练习题，需要批量转换大量文本。
- 需求只在 Markdown：编写中文教材，需要专业的拼音标注。
- 需求只在 pptx：2.1.1 拼音转换功能
- 需求只在 pptx：2.1.2 拼音显示功能
- 需求只在 pptx：2.1.3 实时显示功能
- 需求只在 pptx：2.2 文档处理功能
- 需求只在 pptx：2.3 用户界面功能
- 需求只在 pptx：2.3.2 文件上传功能
- 需求只在 pptx：2.4.1 日志记录功能
- 需求只在 pptx：2.4.2 错误处理功能
- 需求只在 pptx：文档版本: v1.0创建日期: 2025年1月5日最后更新: 2025年1月5日作者: 开发团队

### Quirt-studio__Qurit-PPT

段落标题不一致，需求条目 378 / 386 一致（pptx 拆出 471 条）

- 标题只在 Markdown：1.1 版本历史
- 标题只在 Markdown：1.2 文档目的
- 标题只在 Markdown：1.3 相关文档引用
- 标题只在 Markdown：2.1 产品名称与定位
- 标题只在 Markdown：2.2 产品愿景与使命
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 14 页
- 标题只在 pptx：第 16 页
- 需求只在 Markdown：零误差合规: 自动遵循行业规范，实时拦截敏感内容
- 需求只在 Markdown：内容驱动设计: 基于内容特征自动生成专业设计
- 需求只在 Markdown：严谨动态细节: 物理约束的动画系统，服务内容而非装饰
- 需求只在 Markdown：完全自主设计: AI全程自主设计，无需用户选择模板
- 需求只在 Markdown：用户希望获得专业级PPT但缺乏设计技能
- 需求只在 Markdown：合规性和准确性是专业用户的核心痛点
- 需求只在 Markdown：内容驱动的自动设计能显著提升效率
- 需求只在 Markdown：用户愿意为高质量AI服务付费订阅
- 需求只在 pptx：本文档旨在详细定义Qurit PPT产品的功能需求、技术架构和实施计划，为设计、开发、测试团队提供明确的工作指导。
- 需求只在 pptx：1.3 相关文档引用
- 需求只在 pptx：3.1 目标用户画像
- 需求只在 pptx：3.1.1 人口统计特征
- 需求只在 pptx：3.1.2 行为习惯与偏好
- 需求只在 pptx：3.1.3 核心需求与痛点
- 需求只在 pptx：提升工作效率和成果质量
- 需求只在 pptx：降低专业风险
- 需求只在 pptx：获得同行认可
- 需求只在 pptx：3.2 用户场景分析

### RZfive__WorldBase

段落标题不一致，需求条目 59 / 59 一致（pptx 拆出 95 条）

- 标题只在 Markdown：运行时链路（已验证）
- 标题只在 Markdown：discussion 模式的执行结构
- 标题只在 Markdown：① 通信拓扑：纯 hub-and-spoke，无点对点
- 标题只在 Markdown：② 能力：讨论模式下成员被禁用全部工具
- 标题只在 Markdown：③ 共享状态：SharedBoard 是死代码
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 10 页
- 需求只在 pptx：状态 Draft v0.1 · 日期 2026-08-11 · 范围 apps/electron/electron/main-process/ai/group-deliberation.ts 及相关工具/UI
- 需求只在 pptx：当前群组对话是一套以 coordinator 为中枢的并行笔记制——成员间不直接通信、讨论时不许用工具、没有共享状态、轮次是硬同步屏障。本 PRD 定义把它演进为真正的多 Agent 对话所需的产品需求：点对点消息、共享黑板、讨论中工具调用、事件驱动轮次与人在环中。
- 需求只在 pptx：群组对话的运行时已经相当完整——配置、路由、多轮、进度 UI、转写 block 都在。问题不在「有没有」，而在对话拓扑：它是单向的、批量的、经协调者中转的。
- 需求只在 pptx：运行时链路（已验证）
- 需求只在 pptx：discussion 模式的执行结构
- 需求只在 pptx：User ↕ Coordinator  ← planner + synthesizer ↘ ↓ ↙         ↖ ↑ ↗  (笔记批量回传) Member A   Member B   Member C ─ ─         ─ ─        (成员间无链路)
- 需求只在 pptx：每轮：coordinator 用 LLM 决定邀请哪些成员 + focus（调用时禁用全部工具）→ 被选成员并行跑（按 maxParallelWorkers 分批），各自产出内部「笔记」→ 笔记收集 → 下一轮把最近 6 条笔记（≤3000 字符）作为 prior notes 注入。所有轮结束后，笔记汇总成 promptSection 注入 coordinator 的系统提示，由 coordinator 给用户最终答复。
- 需求只在 pptx：做得好的部分 · 保留：@提及 路由、多轮迭代、并行加速、角色隔离 prompt、group_progress/agent_sidechat 实时 UI、转写可见性分级——这套骨架值得保留并在此基础上演进。
- 需求只在 pptx：把现象归到六个根因。每条都已在代码中定位。
- 需求只在 pptx：① 通信拓扑：纯 hub-and-spoke，无点对点

### Rockomate__nextjs_blog

段落标题不一致，需求条目 38 / 39 一致（pptx 拆出 45 条）

- 标题只在 Markdown：1.1 目的
- 标题只在 Markdown：1.2 背景
- 标题只在 Markdown：1.3 定义
- 标题只在 Markdown：2.1 系统功能
- 标题只在 Markdown：2.2 用户界面
- 需求只在 Markdown：系统开发预计耗时6个月，包括需求分析、设计、开发和测试等阶段。
- 需求只在 pptx：随着学生人数的增加（预计2024年在校生达到5000人）和奖学金种类的多样化（目前有20种不同类型的奖学金），传统的手工管理方式已无法满足当前的需求。因此，需要一个自动化的奖学金管理系统来简化流程，提高效率。
- 需求只在 pptx：3.1 学生信息管理
- 需求只在 pptx：3.2 奖学金信息管理
- 需求只在 pptx：3.3 申请提交与审批
- 需求只在 pptx：3.4 奖学金发放管理
- 需求只在 pptx：3.5 报表生成与数据分析
- 需求只在 pptx：4.4 可维护性需求

### SXP-Simon__astrbot_plugin_qq_group_daily_analysis

段落标题不一致，需求条目 174 / 228 一致（pptx 拆出 197 条）

- 标题只在 Markdown：1.1 关联文档
- 标题只在 Markdown：1.2 本文档目的
- 标题只在 Markdown：3.1 产品机会
- 标题只在 Markdown：3.2 用户价值
- 标题只在 Markdown：3.3 工程价值
- 需求只在 Markdown：产品 / 方案负责人：确定目标边界、阶段优先级与质量标准
- 需求只在 Markdown：插件开发者：负责设计、实现、测试、治理与持续演进
- 需求只在 Markdown：群管理员 / 高级用户：在灰度期间提供真实反馈
- 需求只在 Markdown：AstrBot 宿主生态：提供 KV、cron、UMO、persona、message history 等底层能力边界
- 需求只在 Markdown：系统需要为每个群建立独立的长期记忆命名空间。
- 需求只在 Markdown：系统需要能够从 IncrementalBatch 中抽取可复用的 episode 记忆。
- 需求只在 Markdown：核心成员角色
- 需求只在 Markdown：群内角色标签
- 需求只在 Markdown：系统需要在最终总结前检索长期记忆，并将其注入总结 prompt。
- 需求只在 Markdown：系统需要定期清理过期 episode、限制索引规模、重建快照。
- 需求只在 pptx：本文档用于将前置讨论、代码研究、宿主生态 review 和 Phase 1 方案统一收敛为一份项目级 PRD。
- 需求只在 pptx：将插件从"按天生成总结的分析器"，升级为"对每个群拥有持续认知的总结 Agent"。
- 需求只在 pptx：的长期记忆底座。
- 需求只在 pptx：9.1 已完成的文档成果
- 需求只在 pptx：9.2 已确认的技术结论
- 需求只在 pptx：9.3 当前尚未开始的内容
- 需求只在 pptx：原始消息 -> 消息清洗 -> IncrementalBatch -> 记忆提取 -> 长期记忆更新
- 需求只在 pptx：本项目采用"先骨架、后增强；先群级、后细分；先可控、后复杂"的推进策略。
- 需求只在 pptx：12.1 插件内部约束
- 需求只在 pptx：12.3 前置依赖与阻塞项

### SteveTom17__hotpulse

段落标题不一致，需求条目 46 / 62 一致（pptx 拆出 68 条）

- 标题只在 Markdown：1.1 当前实现状态（0.1.0）
- 标题只在 Markdown：2.1 首版技术切分
- 标题只在 Markdown：2.1.1 技术栈决定
- 标题只在 Markdown：2.2 非功能基线
- 标题只在 Markdown：FR-01：工作区与品牌资料
- 需求只在 Markdown：数据连接器层：先实现抖音官方热门视频榜、微博官方/授权关键词检索或榜单供应商；每个连接器独立配置凭据、配额和数据保留策略。
- 需求只在 Markdown：趋势处理层：定时任务拉取、统一字段、语义去重、计算 24 小时增速与跨源信号；保存原始来源链接和采集时间。
- 需求只在 Markdown：决策层：规则优先的风险分类 + LLM 辅助的行业相关性摘要；评分可解释、可人工覆盖。
- 需求只在 Markdown：生成层：用结构化提示词生成多版本脚本、带货文案及图片/表情包制作提示；只在用户明确选择时调用图像或视频生成能力。
- 需求只在 Markdown：审核与导出层：编辑器、必填事实确认、风险确认、AI 标识检查、导出包和不可篡改审计日志。
- 需求只在 Markdown：应用：TypeScript + React 19 + Vinext，兼顾产品界面、服务端接口和 Cloudflare Worker 运行环境。
- 需求只在 Markdown：样式：Tailwind CSS 4 与语义化 CSS 变量；遵循 WCAG 对比度、键盘操作、44px 触控目标和减少动态效果偏好。
- 需求只在 Markdown：数据：Cloudflare D1 + Drizzle ORM；浏览器状态只承载临时界面交互，不作为工作区、审批或审计记录的权威来源。
- 需求只在 Markdown：文件：MVP 仅导出小型 JSON/文本清单；后续图片、视频与 ZIP 等二进制资产使用 R2，D1 只保存元数据。
- 需求只在 Markdown：身份：托管版本优先使用平台提供的已认证用户信息，并在服务端执行工作区授权；不自行拼装未经评估的账号密码系统。
- 需求只在 pptx：产品名（暂定）：热点内容作战台
- 需求只在 pptx：目标用户：美妆、餐饮、本地生活等单一垂直行业的品牌运营、商家、MCN 和代运营团队。
- 需求只在 pptx：首版目标：用户每天在 15 分钟内完成"发现一个相关热点 → 判断是否值得跟进 → 生成并审核一套内容草案 → 导出待发布素材"。首版不承诺自动发布，不承诺实时全网热搜，也不以未经授权的数据抓取为前提。
- 需求只在 pptx：首版建议行业：本地生活/餐饮。理由是热点切入与促销、门店活动和短视频脚本的关联清晰，商品或服务事实能由商家后台提供并核验。
- 需求只在 pptx：1.1 当前实现状态（0.1.0）
- 需求只在 pptx：尚未宣称完成：平台官方实时热搜接入、真实支付网关、自动发布、效果回收报表、企业级 SSO 与精细保留策略。
- 需求只在 pptx：FR-01：工作区与品牌资料
- 需求只在 pptx：需求：管理员创建工作区、邀请成员，并维护品牌资料：行业、目标客群、禁用话题、语气、可核验的商品/门店事实和合规声明。
- 需求只在 pptx：FR-02：授权热点数据接入
- 需求只在 pptx：需求：按计划任务获取至少两个经授权的数据源；保存来源、链接、采集时间、原始标题、热度字段和接口状态。

### StoneLL1__llm-wiki-desktop

段落标题不一致，需求条目 146 / 202 一致（pptx 拆出 158 条）

- 标题只在 Markdown：3.1 用户现状
- 标题只在 Markdown：3.2 核心问题
- 标题只在 Markdown：3.3 产品机会
- 标题只在 Markdown：4.1 MVP 目标
- 标题只在 Markdown：4.2 产品原则
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 14 页
- 标题只在 pptx：第 15 页
- 需求只在 Markdown：导入、来源库、本地与远程媒体、OCR、ASR、平台登录态和 AI 整理的已确认产品决策，以 ../docs/superpowers/specs/2026-07-24-import-source-media-flow-design.md 为唯一可信源。本文中的概览不得被解释为"确认导入后自动编译"。
- 需求只在 Markdown：无项目工作台、新建知识库、打开原生或兼容知识库、目录评估、信任 / 受限 / 只读、兼容启用、修复与进入 Import 的已确认产品决策，以 ../docs/superpowers/specs/2026-07-30-first-run-project-open-workbench-design.md 为唯一可信源。本文中的摘要不得被解释为允许把普通资料文件夹原地初始化成项目。
- 需求只在 Markdown：资料散落在 PDF、网页、公众号文章、PPT、Word、Excel、Markdown 和本地文件夹中。
- 需求只在 Markdown：普通笔记工具依赖手工整理，成本高，长期难以维护。
- 需求只在 Markdown：RAG 工具能问答，但不擅长把知识沉淀成稳定、可编辑、可复用的页面。
- 需求只在 Markdown：图谱工具通常需要用户手动建节点、连线，不适合大量资料导入后的自动探索。
- 需求只在 Markdown：AI Agent 能整理资料，但命令行门槛高，普通用户不容易获得稳定、可恢复、可视化的工作流。
- 需求只在 Markdown：用户需要一个本地桌面应用，把"资料导入、知识整理、图谱探索、问答溯源、HTML 输出、版本恢复"整合成一个可靠闭环。
- 需求只在 Markdown：以 Markdown 文件夹作为长期资产，避免锁定在单一应用。
- 需求只在 Markdown：用 Agent/LLM 自动完成重复整理工作，降低个人知识库维护成本。
- 需求只在 pptx：8.0 无项目工作台
- 需求只在 pptx：8.1 新建知识库流程
- 需求只在 pptx：8.2 打开已有知识库
- 需求只在 pptx：快速评估由后端短期 registry 持有：启动只返回 application-scoped assessmentOperationId，取消命令只接受该 opaque ID；取消不创建项目任务、丢弃未完成快照并保留无项目工作台。完成后返回独立、短期有效的 assessmentId，供打开、信任、兼容启用或修复命令重验。
- 需求只在 pptx：8.3 导入到当前项目
- 需求只在 pptx：8.4 更新 Wiki（编译）流程
- 需求只在 pptx：8.5 图谱探索流程
- 需求只在 pptx：当前实现状态（2026-08-13）：H3–H5 已实现真实 Agent Health route、受保护的 repair task 与 Lint/Workflows 结果入口；只有 deterministic Lint 证明消失的 Finding 才能自动关闭，duplicate_topic、contradiction 等没有 proof 的语义 Finding 保持人工处理。H6 的 full gate 与完整矩阵尚未全绿，因此 Decision Gate H / Batch 7 仍保持阻断。
- 需求只在 pptx：9.4 文章浏览与编辑
- 需求只在 pptx：9.11 设置、隐私与更新

### T-THA__AITravelPlanner

段落标题不一致，需求条目 109 / 200 一致（pptx 拆出 170 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 核心价值
- 标题只在 Markdown：2.1 用户系统模块
- 标题只在 Markdown：2.1.1 注册/登录功能
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：通过 AI 大幅降低旅行规划的时间成本
- 需求只在 Markdown：提供个性化、符合预算的旅行方案
- 需求只在 Markdown：语音交互提升用户体验
- 需求只在 Markdown：云端同步实现多设备无缝衔接
- 需求只在 Markdown：用户可以成功注册账号
- 需求只在 Markdown：用户可以使用邮箱/手机号登录
- 需求只在 Markdown：密码加密存储
- 需求只在 Markdown：登录状态持久化（7天免登录）
- 需求只在 Markdown：支持密码找回流程
- 需求只在 Markdown：用户可以修改个人信息
- 需求只在 pptx：2.1 用户系统模块
- 需求只在 pptx：2.1.1 注册/登录功能
- 需求只在 pptx：☐ 用户可以成功注册账号
- 需求只在 pptx：☐ 用户可以使用邮箱/手机号登录
- 需求只在 pptx：☐ 密码加密存储
- 需求只在 pptx：☐ 登录状态持久化（7天免登录）
- 需求只在 pptx：☐ 支持密码找回流程
- 需求只在 pptx：2.1.2 用户信息管理
- 需求只在 pptx：☐ 用户可以修改个人信息
- 需求只在 pptx：☐ 偏好设置可保存并应用到后续规划

### TY-teo__ChargeWatching

段落标题不一致，需求条目 25 / 67 一致（pptx 拆出 52 条）

- 标题只在 Markdown：3.1 必做（P0）
- 标题只在 Markdown：3.2 应做（P1）
- 标题只在 Markdown：3.3 可做（P2，后续迭代）
- 标题只在 Markdown：3.4 不做（Out of Scope）
- 标题只在 Markdown：9.1 目标
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：菜单栏实时显示
- 需求只在 Markdown：充电中：图标（SF Symbol bolt.fill）+ 数字瓦数，如 ⚡ 67W（图标是 SF Symbols，不是 emoji）
- 需求只在 Markdown：未充电但接电：图标（bolt.slash）+ AC
- 需求只在 Markdown：纯电池放电：图标（battery.50percent）+ 当前 SoC%
- 需求只在 Markdown：无电池（桌面 Mac）：图标（powerplug）+ 系统功耗
- 需求只在 Markdown：下拉详情面板（点击菜单栏图标弹出）
- 需求只在 Markdown：当前状态横幅：充电中 / AC 未充 / 放电中
- 需求只在 Markdown：关键数字（4 项）：充入电池功率、适配器实际输入、系统总功耗、电池 SoC
- 需求只在 Markdown：适配器信息：额定瓦数 + 协商电压电流（如 100W PD, 20V/5A max）
- 需求只在 Markdown：充电曲线：最近 1 小时 sparkline，hover 显示具体数值
- 需求只在 pptx：ChargeWatch 是一款只做一件事的 macOS 菜单栏小工具：让你随时看到 Mac 实时充电功率，并完整记录历史。
- 需求只在 pptx：☐ 菜单栏图标实时显示当前充电瓦数（SF Symbols，无 emoji）
- 需求只在 pptx：☐ 点击图标弹出详情面板，4 个核心数字 + sparkline 全部到位
- 需求只在 pptx：☐ 后台 1Hz 采样写入 SQLite，停止应用后再启动数据不丢
- 需求只在 pptx：☐ 历史窗口可切换今天/本周/本月，正确渲染折线
- 需求只在 pptx：☐ CSV 导出包含全部字段，可在 Numbers 打开
- 需求只在 pptx：☐ 设置中开关开机自启可生效
- 需求只在 pptx：☐ 在我的 MacBook（Apple Silicon）上连续运行 24h 内存 < 50 MB
- 需求只在 pptx：☐ 深色 / 浅色模式下视觉一致
- 需求只在 pptx：☐ 全部源码无 emoji 字符

### Thearetically-speaking__All-you-can-seal

段落标题不一致，需求条目 53 / 53 一致（pptx 拆出 60 条）

- 标题只在 Markdown：FR-1 文件导入（拖拽 + 点击选择）
- 标题只在 Markdown：FR-2 多盘（multi-plate）处理
- 标题只在 Markdown：FR-3 参数面板（可调，默认值沿用现脚本）
- 标题只在 Markdown：FR-4 G-code 改写引擎（Python 脚本逻辑的移植 + 修复）
- 标题只在 Markdown：FR-5 3D 路径预览（核心功能）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 需求只在 pptx：FR-1 文件导入（拖拽 + 点击选择）
- 需求只在 pptx：FR-3 参数面板（可调，默认值沿用现脚本）
- 需求只在 pptx：FR-4 G-code 改写引擎（Python 脚本逻辑的移植 + 修复）
- 需求只在 pptx：FR-5 3D 路径预览（核心功能）
- 需求只在 pptx：FR-6 安全检查（导出前门禁）
- 需求只在 pptx：每项检查带"这是什么、为什么重要"的展开说明。README 中现有的安全警告（垫硅胶垫、通风、不可离人、先空跑）在导出成功页显著展示一次。
- 需求只在 pptx：FR-8 源温度自动识别（去除硬编码 230）

### WrBug__PolyHermes

段落标题不一致，需求条目 108 / 108 一致（pptx 拆出 132 条）

- 标题只在 Markdown：主要用户场景
- 标题只在 Markdown：3.1 回测管理页面
- 标题只在 Markdown：3.1.1 页面布局
- 标题只在 Markdown：3.1.2 列表功能
- 标题只在 Markdown：3.1.3 列表操作
- 标题只在 pptx：第 5 页
- 需求只在 pptx：主要用户场景
- 需求只在 pptx：作为用户,我希望能够创建回测任务,选择特定的 Leader 和跟单配置,以便评估在过去一段时间内使用该策略的收益情况
- 需求只在 pptx：作为用户,我希望能够查看所有历史回测结果,并按收益额或收益率排序,以便找到最优策略
- 需求只在 pptx：作为用户,我希望能够按 Leader 筛选回测记录,以便比较不同 Leader 的表现
- 需求只在 pptx：作为用户,我希望回测结果能够展示详细的交易记录和收益变化,以便深入分析策略表现
- 需求只在 pptx：作为用户,我希望回测在资金不足时能够自动停止,模拟真实交易场景
- 需求只在 pptx：3.1 回测管理页面
- 需求只在 pptx：3.2 新增回测任务
- 需求只在 pptx：跟单配置表单应完全复用现有的跟单配置组件,保持参数一致性
- 需求只在 pptx：3.3 回测详情页面

### Xiangyu-Lou__BlueDrop

段落标题不一致，需求条目 17 / 25 一致（pptx 拆出 37 条）

- 标题只在 Markdown：3.1 系统要求
- 标题只在 Markdown：3.2 外部依赖
- 标题只在 Markdown：3.3 启动校验（强制）
- 标题只在 Markdown：F1: 蓝牙 A2DP Sink 接收
- 标题只在 Markdown：F2: 音频设备枚举与捕获
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：iPhone 可通过蓝牙发现并连接 PC，PC 以 A2DP Sink 身份接收立体声音频
- 需求只在 Markdown：用户可选择物理麦克风、监听耳机、虚拟声卡输出
- 需求只在 Markdown：路由 A：手机音频可从指定耳机播出，无麦克风回音
- 需求只在 Markdown：路由 B：手机音频 + 麦克风混合后可在 VB-Cable Input 端被第三方软件读取
- 需求只在 Markdown：各音量推子和静音开关实时生效
- 需求只在 Markdown：蓝牙断开后 UI 正确提示，重连后自动恢复
- 需求只在 Markdown：内部处理延迟 ≤ 50ms
- 需求只在 Markdown：支持系统 DPI 缩放 (100%~200%)
- 需求只在 pptx：版本： 1.0 日期： 2026-03-24 阶段： Phase 1 — iOS → Windows 单向音频传输
- 需求只在 pptx：聚音 (BlueDrop) 是一款音频路由与混流桌面软件，核心目标是让用户将 iPhone 的媒体音频通过蓝牙 A2DP 传输到 Windows PC，与本地麦克风混合后输出至虚拟麦克风，供 Discord、腾讯会议、Zoom 等通讯软件调用。
- 需求只在 pptx：Phase 1 范围： iPhone (iOS) → Windows (10 2004+ / 11) 单向传输。
- 需求只在 pptx：3.3 启动校验（强制）
- 需求只在 pptx：F2: 音频设备枚举与捕获
- 需求只在 pptx：F3: 双路由音频引擎
- 需求只在 pptx：┌─────────────┐ │  iPhone BT   │──┬──→ 路由 A: 直出物理耳机（本地监听） │  (A2DP Sink) │  │ └─────────────┘  │    ┌─────────────┐ ├──→ │   混音器     │──→ 路由 B: 输出至 VB-Cable Input ┌─────────────┐  │    └─────────────┘     （供通讯软件读取） │  物理麦克风   │──┘ └─────────────┘
- 需求只在 pptx：F4: 音量与通道控制
- 需求只在 pptx：采用左侧导航 + 右侧内容区的卡片式布局（参考 UI 设计参考图）。
- 需求只在 pptx：5.3 连接状态卡片

### Yotoha0303__KnowTrace-Workflow

段落标题不一致，需求条目 136 / 136 一致（pptx 拆出 184 条）

- 标题只在 Markdown：身份与数据范围
- 标题只在 Markdown：US-01 快速保存
- 标题只在 Markdown：US-02 手动分类
- 标题只在 Markdown：US-03 管理分类
- 标题只在 Markdown：US-04 修订内容
- 标题只在 pptx：第 2 页
- 需求只在 pptx：最后核对：2026-08-30，依据 9f408a6。 本行只在内容变更时更新，不随改名/格式化变动——约定见 CONTRIBUTING.md「目录与命名约定」。
- 需求只在 pptx：keyword_set       关键词集合 thought_fragment  想法片段 experience        经历记录 observation       观察记录 question          问题 source_note       资料摘录 mixed             混合内容 unknown           尚未判断
- 需求只在 pptx：Content Type 只描述形态，不表示真假。例如 observation 表示用户记录了一项观察，不代表该观察已被外部验证。
- 需求只在 pptx：身份与数据范围
- 需求只在 pptx：管理员可以查看和管理所有用户创建的 Capture、Category 及其派生内容。
- 需求只在 pptx：普通成员只能管理本人创建的内容，同时可只读查看管理员共享内容；成员之间默认不共享，也不能通过搜索、导出、图片地址或猜测资源 ID 发现彼此私有内容。
- 需求只在 pptx：创建者身份只接受 go-user-system 验证结果，不接受客户端提交的用户 ID 或角色。
- 需求只在 pptx：历史无创建者数据标记为 legacy-local，只对管理员可见。
- 需求只在 pptx：作为使用者，我希望只输入一段内容就能保存，以免整理过程打断想法。
- 需求只在 pptx：作为使用者，我希望给记录指定内容类型和多个主题分类。

### ZJM189__Daily_News

段落标题不一致，需求条目 167 / 183 一致（pptx 拆出 176 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心价值
- 标题只在 Markdown：1.3 产品原则
- 标题只在 Markdown：2.1 普通用户
- 标题只在 Markdown：2.2 管理员
- 需求只在 Markdown：产品首期不做推送渠道，不开放公开注册，不允许普通用户添加外部 URL 信息源。普通用户通过"我的关注"配置个性化规则，影响自己的看板排序和默认筛选。
- 需求只在 Markdown：帮助用户快速了解当天 AI 热点。
- 需求只在 Markdown：把分散来源统一到一个可检索 Web 看板。
- 需求只在 Markdown：通过中文摘要和"为什么重要"降低理解成本。
- 需求只在 Markdown：通过信息库沉淀全量可搜索内容。
- 需求只在 Markdown：通过我的关注提供可解释的个性化排序。
- 需求只在 Markdown：通过管理员后台保障来源、任务、用户和 LLM 配置可维护。
- 需求只在 Markdown：信息优先：页面以扫读、筛选和追溯为主，不做营销型首页。
- 需求只在 Markdown：来源可追溯：每条摘要必须能回到原文。
- 需求只在 Markdown：个性化可解释：先做规则型关注、屏蔽和反馈，不做黑盒推荐。
- 需求只在 pptx：新增 /favorites，用于用户主动保存信息条目。首期包括收藏/取消、单层目录增删改、移动目录、按目录检索筛选和分页；没有目录时直接收藏到根目录。删除目录保留收藏并移回根目录。收藏不影响关注排序或全局简报，管理员也不能查看其他用户的收藏。交互与验收规则见 我的收藏设计。
- 需求只在 pptx：阶段：产品设计
- 需求只在 pptx：4.1 普通用户导航
- 需求只在 pptx：4.3 全局导航体验
- 需求只在 pptx：4.4 主内容区体验
- 需求只在 pptx：4.5 页面职责边界
- 需求只在 pptx：5.1 公开今日简报
- 需求只在 pptx：系统先计算全局 score，再根据用户规则生成 user score。
- 需求只在 pptx：7.5 规则执行顺序

### ZedeX__agentforge

段落标题不一致，需求条目 181 / 181 一致（pptx 拆出 226 条）

- 标题只在 Markdown：文档目的
- 标题只在 Markdown：适用范围
- 标题只在 Markdown：设计总原则
- 标题只在 Markdown：（一）四层业务平面
- 标题只在 Markdown：1. 基础资源层
- 标题只在 pptx：第 9 页
- 需求只在 pptx：本文档为 Agent 智能体平台的完整设计需求规范，用于指导工程化开发，输出可落地的项目工程文件。文档覆盖平台整体架构、核心组件设计、全链路流程、质量保障、成本管控等全部核心模块，所有设计要求均为明确可实现的技术规则。
- 需求只在 pptx：平台后端全量核心服务、Agent 运行时、管控后台、基础中间件集成。
- 需求只在 pptx：采用「四层业务平面 + 两大横向体系」的分层架构，各模块高内聚低耦合，可独立迭代。
- 需求只在 pptx：（一）四层业务平面
- 需求只在 pptx：为全平台提供底层标准化资源能力，屏蔽异构差异。
- 需求只在 pptx：平台核心能力中枢，负责任务全生命周期管控与 Agent 执行驱动。
- 需求只在 pptx：基于核心引擎封装的可复用业务资产层，实现能力产品化。
- 需求只在 pptx：面向终端用户与外部系统的统一入口。
- 需求只在 pptx：（二）两大横向体系
- 需求只在 pptx：（三）完整执行全链路（从用户输入到任务完成）

### ZhengWG__quant_free

段落标题不一致，需求条目 108 / 119 一致（pptx 拆出 125 条）

- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值
- 标题只在 Markdown：2.1 参考项目
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：便捷性：在编码环境中直接管理股票交易，无需切换应用
- 需求只在 Markdown：智能化：基于大模型的策略推荐，辅助投资决策
- 需求只在 Markdown：自动化：支持策略回测和自动化交易执行
- 需求只在 Markdown：✅ 基础VSCode插件框架
- 需求只在 Markdown：✅ 实时行情查看（单市场）
- 需求只在 Markdown：✅ 基础策略推荐（简单规则）
- 需求只在 Markdown：✅ 模拟交易功能
- 需求只在 Markdown：✅ AI策略推荐集成
- 需求只在 Markdown：✅ 实盘交易API对接
- 需求只在 Markdown：✅ 策略回测功能
- 需求只在 pptx：3.1 核心功能模块
- 需求只在 pptx：3.1.1 实时行情监控模块
- 需求只在 pptx：3.1.2 AI策略推荐模块
- 需求只在 pptx：买入/卖出/持有建议
- 需求只在 pptx：持仓周期建议
- 需求只在 pptx：策略理由说明
- 需求只在 pptx：3.1.3 交易执行模块
- 需求只在 pptx：3.1.4 数据可视化模块
- 需求只在 pptx：3.1.5 策略回测模块
- 需求只在 pptx：3.2 辅助功能模块

### ZooHero500__imgsplit

段落标题不一致，需求条目 47 / 47 一致（pptx 拆出 56 条）

- 标题只在 Markdown：需求 1: 图片上传
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：需求 2: 分割线编辑
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：需求 3: 图片分割与下载
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 pptx：需求 1: 图片上传
- 需求只在 pptx：需求 2: 分割线编辑
- 需求只在 pptx：需求 3: 图片分割与下载
- 需求只在 pptx：Objective: 作为访客，我希望直接在落地页使用裁剪功能，无需额外跳转即可完成操作
- 需求只在 pptx：Objective: 作为用户，我希望在操作台中管理多张图片和查看历史记录，以便高效地进行批量操作
- 需求只在 pptx：需求 6: 历史记录管理
- 需求只在 pptx：Objective: 作为用户，我希望系统自动保存我的操作记录，以便随时回顾和继续之前的工作
- 需求只在 pptx：需求 7: 响应式与交互体验
- 需求只在 pptx：Objective: 作为用户，我希望在不同设备上都能获得流畅的操作体验

### aAAaqwq__KGKB

段落标题不一致，需求条目 30 / 40 一致（pptx 拆出 62 条）

- 标题只在 Markdown：1.1 一句话定位
- 标题只在 Markdown：1.2 项目愿景
- 标题只在 Markdown：1.3 核心价值主张
- 标题只在 Markdown：1.4 目标用户
- 标题只在 Markdown：1.5 与现有方案对比
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：支持文本、URL、Markdown三种输入格式
- 需求只在 Markdown：支持标签分类
- 需求只在 Markdown：支持元数据（来源、时间、作者）
- 需求只在 Markdown：使用D3.js或Cytoscape.js渲染图谱
- 需求只在 Markdown：支持节点拖拽和缩放
- 需求只在 Markdown：点击节点显示详情
- 需求只在 Markdown：支持按标签筛选显示
- 需求只在 Markdown：支持手动创建关联
- 需求只在 Markdown：支持定义关联类型（相关、因果、包含等）
- 需求只在 Markdown：关联在图谱中可视化显示
- 需求只在 pptx：项目代号: KGKB优先级: P0 战略级立项人: Daniel Li编写人: 小pm (CPO)创建日期: 2026-03-16目标交付: 2周 MVP
- 需求只在 pptx：基于图谱可视化的可预测关联万物的知识库 — 一个让知识可见、可关联、可预测的下一代知识管理系统。
- 需求只在 pptx：让每个人都能拥有一个"第二大脑"，不仅能存储和检索知识，还能通过图谱可视化发现知识之间的隐藏关联，并通过AI预测未来趋势。
- 需求只在 pptx：1.3 核心价值主张
- 需求只在 pptx：用户类型：AI开发者；痛点：需要本地知识库；核心需求：向量化 + API集成
- 需求只在 pptx：1.5 与现有方案对比
- 需求只在 pptx：2.1 功能优先级矩阵
- 需求只在 pptx：kgkb add "知识内容" --tags "tag1,tag2" --source "url" kgkb query "搜索关键词" --limit 10 kgkb list --tag "tag1" kgkb export --format json
- 需求只在 pptx：☐ 支持文本、URL、Markdown三种输入格式
- 需求只在 pptx：☐ 支持标签分类

### anzx01__cusops

段落标题不一致，需求条目 174 / 196 一致（pptx 拆出 185 条）

- 标题只在 Markdown：3.1 首个 ICP
- 标题只在 Markdown：3.2 非目标用户
- 标题只在 Markdown：6.1 必须做
- 标题只在 Markdown：6.2 暂不做
- 标题只在 Markdown：7.1 Merchant 商家
- 需求只在 Markdown：类型：本地预约型服务商
- 需求只在 Markdown：推荐切入行业：家政/清洁服务
- 需求只在 Markdown：线索来源：网站、广告落地页、社媒私信、电话未接、短信/WhatsApp/微信
- 需求只在 Markdown：客户咨询不能及时回复
- 需求只在 Markdown：晚上、周末、忙碌时段容易漏单
- 需求只在 Markdown：重复问题占用人工
- 需求只在 Markdown：客户信息收集不完整，后续跟进低效
- 需求只在 Markdown：预约、改约、提醒依赖人工
- 需求只在 Markdown：行业模板初始化
- 需求只在 Markdown：业务资料配置
- 需求只在 pptx：AI接待员是面向本地服务商的 24/7 自动接待和预约工具，帮助商家自动回复客户咨询、收集关键信息、判断是否符合服务条件、预约时间，并在不确定或高风险场景下转人工。
- 需求只在 pptx：24/7 AI接待员，帮本地服务商自动回复、筛选客户、预约服务，不漏单。
- 需求只在 pptx：8.1 新商家上线流程
- 需求只在 pptx：目标：首个可用版本在 15 分钟内完成上线。
- 需求只在 pptx：8.2 客户咨询到预约流程
- 需求只在 pptx：MVP 只提供一个行业模板。
- 需求只在 pptx：暂不做复杂自定义权限。
- 需求只在 pptx：风险 1：用户不会配置
- 需求只在 pptx：风险 2：AI 错答或越界
- 需求只在 pptx：风险 3：只做 Web Chat 价值不足

### appstore-discounts__appstore-discounts

段落标题不一致，需求条目 155 / 186 一致（pptx 拆出 243 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 访问地址
- 标题只在 Markdown：1.3 技术选型
- 标题只在 Markdown：2.1 折扣应用列表页（首页）
- 标题只在 Markdown：2.1.1 数据展示规则
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：类别：构建工具；选型：Vite；说明：快速构建，原生 ESM 支持
- 需求只在 Markdown：类别：样式方案；选型：Tailwind CSS；说明：快速开发，响应式支持优秀，tree-shaking 体积小
- 需求只在 Markdown：类别：部署；选型：Cloudflare Pages；说明：支持自定义域名，自动 CI/CD
- 需求只在 Markdown：折扣列表默认按时间倒序展示，按日期分组
- 需求只在 Markdown：首次加载显示 40 条数据，滚动到底部自动加载更多
- 需求只在 Markdown：每个应用卡片展示 Logo、评分、名称、描述、平台标签、优惠信息
- 需求只在 Markdown：价格信息正确显示原价（删除线）和折扣价（高亮）
- 需求只在 Markdown：点击应用卡片跳转到详情页 /{region}/{trackId}
- 需求只在 Markdown：详情页通过 iTunes API 获取并展示完整的应用信息
- 需求只在 Markdown：详情页折线图正确显示历史价格变化（含应用价格和内购价格）
- 需求只在 pptx：2.1 折扣应用列表页（首页）
- 需求只在 pptx：首页即为地区折扣列表页，打开后默认展示 cn（中国大陆）的折扣数据。用户可通过地区选择器切换到其他地区，切换后列表数据整体刷新。
- 需求只在 pptx：2.1.1 数据展示规则
- 需求只在 pptx：2.1.2 应用卡片信息
- 需求只在 pptx：数据来源说明：除优惠信息（折扣数据从存储 JSON 计算得出）外，应用的基础信息（Logo、名称、评分、描述、适配系统、分类等）均通过 iTunes Search API 实时获取。
- 需求只在 pptx：2.1.3 应用信息缓存策略
- 需求只在 pptx：2.1.4 分页加载（API 接口 + 无限滚动）
- 需求只在 pptx：GET /api/discounts/{region}?page=1&size=40&sort=desc Response: { items: DiscountListItem[], total: number, page: number, hasMore: boolean }
- 需求只在 pptx：2.1.6 固定辅助 UI（日期导航、回到顶部、排序按钮）定位
- 需求只在 pptx：2.2.2 页面布局（Tab 页签）

### arana-db__kiwi

段落标题不一致，需求条目 72 / 77 一致（pptx 拆出 84 条）

- 标题只在 Markdown：稳定性、Oracle provenance 与工作连续性
- 标题只在 Markdown：当前兼容、存储、Raft、可观测性与性能
- 标题只在 Markdown：Future Hot Tier 与组合发行（Frozen，仅合同/设计）
- 标题只在 Markdown：含（当前产品主线，Cache OFF）
- 标题只在 Markdown：不含（当前非目标，来源 PROJECT.md L108–L116）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：Redis 8.8.1 可观察语义兼容（Oracle 验证，不依赖热层）。
- 需求只在 Markdown：RocksDB 全量权威存储与真实恢复。
- 需求只在 Markdown：OpenRaft 单 Raft Group 强一致、高可用、成员变更、Snapshot（PROJECT.md 和 SDD M4）。
- 需求只在 Markdown：系统稳定性门禁 G1–G7（SDD M6）。
- 需求只在 Markdown：内嵌 Redis 8.8.1 原生内存热数据层（Embedded Redis Hot Tier）：仅冻结来源/许可证/ABI/正确性/发行接口合同，不进入生产实现；须 M6 通过且用户重新明确批准一个单独的 implementation task 后才解冻（REQ-STABILITY-001/005/006；D009）。
- 需求只在 pptx：唯一权威入口：.planning/SDD.md。本 PRD 消费其中的产品范围、Requirement 和阶段边界，不维护第二套路线或执行状态。 稳定性门禁 G1–G7 引用：docs/quality/system-stability-gate.md。 文档性质：产品视图；Requirement priority 只以 .planning/REQUIREMENTS.md 为准，当前状态只以 .planning/SDD.md、本地 recovery 和 GitHub 实时状态为准。 对齐日期：2026-08-02。
- 需求只在 pptx：约束红线（PROJECT.md L15）：任何 Raft、分片、存储格式、兼容性或未来热层优化，都不得改变 Redis 8.8.1 的可观察语义、已声明的持久化边界和一致性承诺。
- 需求只在 pptx：本节按产品用途聚合 Requirement，便于阅读，不重新定义优先级。 每条 Requirement 的 P0/P1/P2 只以 .planning/REQUIREMENTS.md 为准。
- 需求只在 pptx：稳定性、Oracle provenance 与工作连续性
- 需求只在 pptx：当前兼容、存储、Raft、可观测性与性能
- 需求只在 pptx：Future Hot Tier 与组合发行（Frozen，仅合同/设计）
- 需求只在 pptx：6.1 稳定性门禁 G1–G7（来源 docs/quality/system-stability-gate.md）
- 需求只在 pptx：6.2 REQ 证据规则（来源 REQUIREMENTS.md L5）
- 需求只在 pptx：PRD 只定义产品范围，不维护第二份里程碑、退出门禁或依赖图。项目级 M0-M10 状态、工作包顺序和验收合同以 .planning/SDD.md 为唯一来源。
- 需求只在 pptx：当前（来源 PROJECT.md L6–L7、L84–L91；REQ-LICENSE-001；D002）

### arch-team__devpace

段落标题不一致，需求条目 12 / 166 一致（pptx 拆出 153 条）

- 标题只在 Markdown：S1：首次初始化
- 标题只在 Markdown：S2：日常推进
- 标题只在 Markdown：S3：查看进度
- 标题只在 Markdown：S4：需求插入
- 标题只在 Markdown：S5：需求暂停/砍掉
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：/pace-init 通过对话收集项目信息
- 需求只在 Markdown：自动生成 .devpace/ 目录和所有必需文件
- 需求只在 Markdown：生成的价值功能树结构合理
- 需求只在 Markdown：角色：开发者 场景：新开一个 Claude Code 会话，继续昨天的工作 期望：Claude 自动知道做到哪了，直接继续，不需要我重新解释
- 需求只在 Markdown：Claude 会话开始自动读取 state.md
- 需求只在 Markdown：用 1 句自然语言报告当前状态
- 需求只在 Markdown：用户说"继续"就能从上次断点恢复
- 需求只在 Markdown：/pace-status detail 展开到产品功能级别
- 需求只在 Markdown：/pace-status tree 展示完整价值功能树
- 需求只在 Markdown：角色：开发者 场景：做到一半，发现需要加一个新功能 期望：告诉 Claude 新需求，它自动分析影响、调整计划
- 需求只在 pptx：职责：定义用户场景、功能需求和非功能需求。需求变更时更新本文件。
- 需求只在 pptx：定位：docs/ 体系的需求清单——回答"具体要实现哪些功能"。将 vision.md 的目标和 design.md 的方案拆解为可验收的功能条目。
- 需求只在 pptx：F2：需求变更管理
- 需求只在 pptx：F4：用户入口与引导
- 需求只在 pptx：F6：生命周期扩展
- 需求只在 pptx：S16：主动节奏提醒
- 需求只在 pptx：角色：开发者 场景：在推进模式中长时间工作，Claude 主动检测节奏异常 期望：Claude 自动提醒 CR 滞留、Review 积压、迭代偏移等问题
- 需求只在 pptx：☒ 推进模式中 Claude 主动检测 6 种信号
- 需求只在 pptx：☒ 建议以 1-2 行自然语言输出，不阻断工作流
- 需求只在 pptx：☒ 同一信号在同一会话中只提醒一次

### armylau__tetris_game

段落标题不一致，需求条目 99 / 99 一致（pptx 拆出 109 条）

- 标题只在 Markdown：1.1 项目目标
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：2.1 核心游戏功能
- 标题只在 Markdown：2.1.1 方块系统
- 标题只在 Markdown：2.1.2 方块控制
- 需求只在 pptx：2.1 核心游戏功能
- 需求只在 pptx：2.2.3 游戏结束检测
- 需求只在 pptx：2.4.2 方块保持功能
- 需求只在 pptx：描述: 添加背景音乐
- 需求只在 pptx：游戏进行时的背景音乐
- 需求只在 pptx：菜单背景音乐
- 需求只在 pptx：音量控制功能
- 需求只在 pptx：验收标准: 音乐循环流畅，音量可调
- 需求只在 pptx：3.3 代码质量需求
- 需求只在 pptx：6.3 用户体验验收

### bdim404__Qwen3-TTS-WebUI

段落标题不一致，需求条目 180 / 224 一致（pptx 拆出 237 条）

- 标题只在 Markdown：2.1 音色复用机制
- 标题只在 Markdown：3.1 音色库（VoiceLibrary）
- 标题只在 Markdown：3.2 角色（Character）
- 标题只在 Markdown：3.3 对话项目（Dialogue）
- 标题只在 Markdown：3.4 对话行（DialogueLine）
- 需求只在 Markdown：角色管理（创建、编辑、删除）
- 需求只在 Markdown：对话编辑器（表格式，拖拽排序）
- 需求只在 Markdown：顺序生成 + 实时进度显示
- 需求只在 Markdown：分段音频生成
- 需求只在 Markdown：音频合并（智能间隔）
- 需求只在 Markdown：对话历史列表
- 需求只在 Markdown：单条重试机制
- 需求只在 Markdown：错误显示和手动干预
- 需求只在 Markdown：批量生成模式
- 需求只在 Markdown：音色预览功能
- 需求只在 pptx：2.1 音色复用机制
- 需求只在 pptx：音色库用于持久化存储和管理用户创建的音色。
- 需求只在 pptx：角色代表对话中的发言人，绑定音色和控制指令。
- 需求只在 pptx：对话项目是多轮对话的容器。
- 需求只在 pptx：对话行是单条对话内容。
- 需求只在 pptx：独立页面：/dialogues 路由
- 需求只在 pptx：4.2 对话编辑器（表格式）
- 需求只在 pptx：4.3 生成控制面板
- 需求只在 pptx：4.4 音色库管理界面
- 需求只在 pptx：4.5 角色管理界面

### bugkiwi__elons-job

段落标题不一致，需求条目 40 / 58 一致（pptx 拆出 148 条）

- 标题只在 Markdown：1.1 一句话描述
- 标题只在 Markdown：1.2 核心原则
- 标题只在 Markdown：1.3 MVP 不做
- 标题只在 Markdown：用户可见描述
- 标题只在 Markdown：Jev Question
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：安装后自动进入 Onboarding
- 需求只在 Markdown：用户可以保存 TypeSafe API Key
- 需求只在 Markdown：默认有 2 条过滤规则
- 需求只在 Markdown：用户可以新增过滤规则
- 需求只在 Markdown：用户可以修改 threshold
- 需求只在 Markdown：用户可以关闭规则
- 需求只在 Markdown：Tweet Detail 页面自动识别评论
- 需求只在 Markdown：高置信度命中自动隐藏
- 需求只在 Markdown：隐藏评论可展开查看
- 需求只在 Markdown：API 失败时不隐藏评论
- 需求只在 pptx：Chrome Extension 产品需求与技术设计版本：MVP v0.1平台：Chrome / Chromium，Manifest V3目标站点：X（x.com）判别服务：TypeSafe Jev
- 需求只在 pptx："Elon的工作"是一个只针对 X 评论区的 Chrome 插件：自动识别色情、性暗示、擦边和色情引流评论，并将高置信度命中的评论隐藏。
- 需求只在 pptx：CM比我👆好看的没我骚🖤❤️比我骚的没我好看1789699386154
- 需求只在 pptx：长数字联系方式 / ID
- 需求只在 pptx：引导进一步联系
- 需求只在 pptx：这条评论是否属于用户不想看到的色情 / 性暗示 / 色情引流内容？
- 需求只在 pptx：首次安装后自动打开 Onboarding 页面。
- 需求只在 pptx：安装插件 ↓ 输入 TypeSafe API Key ↓ 测试连接 ↓ 确认默认过滤规则 ↓ 可选：新增自定义规则 ↓ 完成
- 需求只在 pptx：为了让用户理解简单，MVP 默认只暴露两个规则。
- 需求只在 pptx：用户可见描述

### caesarloo__obsidian-svn

段落标题不一致，需求条目 91 / 91 一致（pptx 拆出 93 条）

- 标题只在 Markdown：包含范围 (MVP)
- 标题只在 Markdown：不包含范围 (本期)
- 标题只在 Markdown：4.1 仓库配置
- 标题只在 Markdown：4.2 状态刷新
- 标题只在 Markdown：4.3 状态视图
- 需求只在 pptx：12.1 功能需求验收标准
- 需求只在 pptx：12.2 非功能需求验收标准

### calderbuild__MD_Audit

段落标题不一致，需求条目 73 / 100 一致（pptx 拆出 102 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标
- 标题只在 Markdown：1.3 核心价值主张
- 标题只在 Markdown：2.1 核心用户角色
- 标题只在 Markdown：2.2 用户工作流
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 15 页
- 需求只在 Markdown：原生Markdown支持: 无需转换，直接分析.md文件
- 需求只在 Markdown：双引擎分析: 规则引擎（快速、准确）+ AI引擎（深度、智能）
- 需求只在 Markdown：可执行建议: 提供具体的代码示例和修改建议，而非泛泛而谈
- 需求只在 Markdown：配置化规则: 支持自定义SEO规则阈值，适应不同场景
- 需求只在 Markdown：Markdown报告: 输出人类可读的Markdown格式报告，便于分享和存档
- 需求只在 Markdown：技术博主: 使用Markdown撰写技术文章，需要优化SEO以提升文章曝光
- 需求只在 Markdown：文档工程师: 维护产品文档站（如GitBook、VuePress），需确保文档SEO友好
- 需求只在 Markdown：内容运营: 管理静态博客（如Hugo、Jekyll），需批量检查内容质量
- 需求只在 Markdown：用户使用CLI命令分析Markdown文件：python main.py analyze article.md --keyword "Python SEO"
- 需求只在 Markdown：Agent解析Frontmatter（元数据）和正文内容
- 需求只在 pptx：文档版本: v1.0 创建日期: 2025-11-27 负责人: Claude Code (PM) 开发团队: Codex
- 需求只在 pptx：---title: "Markdown SEO最佳实践"description: "深度解析Markdown内容的SEO优化技巧，提升搜索排名"tags: [SEO, Markdown, 内容优化]---
- 需求只在 pptx：应成功解析为字典: {"title": "Markdown SEO最佳实践", "description": "深度解析..."}
- 需求只在 pptx：优先级: P0（必需） 描述: 将Markdown正文转换为HTML DOM树，便于结构分析
- 需求只在 pptx：# 主标题示例图片链接文本
- 需求只在 pptx：FR-1.3: 关键词自动提取
- 需求只在 pptx：优先级: P1（重要） 描述: 当用户未提供关键词时，自动从内容中提取Top关键词
- 需求只在 pptx：过滤掉 "http://", "www.", "class=", "" 等技术术语
- 需求只在 pptx：3.2 评分维度与逻辑
- 需求只在 pptx：STRUC_02: 图片Alt属性检查

### cholf5__skynet

段落标题不一致，需求条目 166 / 166 一致（pptx 拆出 172 条）

- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 29 页
- 标题只在 pptx：第 67 页
- 需求只在 pptx：目的：交付一个功能层面上尽量还原 Skynet（cloudwu/skynet）语义、但在接口层采用 C# 强类型 + Interface + SourceGenerator + MessagePack 的轻量 Actor 框架。核心原则是 极简内核、插件化扩展、把复杂性留给用户（而不是强制框架行为）。 目标交付物是一个可开源的 GitHub 仓库 + 可发布到 NuGet 的组件集合，含样例服务与压测脚本，能被编程 Agent 自动实现。
- 需求只在 pptx：文字架构草图（可交给 Agent 生成图片）： Client <-> GateServer (SessionActor) <-> Cluster Transport <-> ActorHost (ActorSystem) [=> Actor Instances + Registry + Plugins]
- 需求只在 pptx：SourceGenerator 与 server dispatch 将 methodName 与 payload 解耦，避免反射查找。
- 需求只在 pptx：public interface IClusterRegistry{    Task RegisterNodeAsync(NodeInfo node);    Task UnregisterNodeAsync(NodeId id);    Task<NodeInfo[]> ListNodesAsync();    Task<NodeInfo> ResolveActorHandleAsync(long handle);    Task<long?> LookupUniqueServiceAsync(string name);}
- 需求只在 pptx：/Skynet /src /Skynet.Core /Skynet.Msgpack /Skynet.SourceGen /Skynet.Cluster /Skynet.Samples /tests /docs /benchmarks /scripts (docker, launch scripts) README.md LICENSE (MIT)
- 需求只在 pptx：public interface ILoginActor{    Task<LoginResult> LoginAsync(LoginRequest req);}var login = ActorSystem.GetActor<ILoginActor>("login");var r = await login.LoginAsync(new LoginRequest{Account="u1"});

### cnjack__jcode

段落标题不一致，需求条目 111 / 111 一致（pptx 拆出 131 条）

- 标题只在 Markdown：4.1 用户目标
- 标题只在 Markdown：4.2 平台目标
- 标题只在 Markdown：7.1 生成并预览报告
- 标题只在 Markdown：7.2 查看会话交付物
- 标题只在 Markdown：7.3 Desktop 深度使用
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 18 页
- 标题只在 pptx：第 19 页
- 需求只在 pptx：Artifact 是由 Agent 或未来的用户操作显式登记、属于某个 JCode 会话、实际内容存放在该会话工作区中的文件。
- 需求只在 pptx：Web 产品中的 task_id 与 Recorder 的 session UUID 是同一个标识；文档后续写作 task_id/session_id。Artifact 的最小身份由 task_id/session_id + normalized_relative_path 决定。同一会话再次展示同一路径时，更新同一个 Artifact，并增加 revision；会话记录保留登记历史，界面默认展示最新登记。
- 需求只在 pptx：本地 revision 是"显式登记代数"，不是文件内容快照。JSONL 只记录元数据，Viewer 每次都重新校验并读取工作区当前文件；因此文件在未再次登记时发生变化，revision 不会自动增加，但 Viewer 仍会看到当前内容。只有 Phase 3 Cloud 分享会把某个 revision 的内容复制为不可变密文快照。
- 需求只在 pptx：7.1 生成并预览报告
- 需求只在 pptx：用户说："分析这些数据，给我一个交互式 HTML 报告。"
- 需求只在 pptx：7.2 查看会话交付物
- 需求只在 pptx：用户在 Desktop 预览 PDF 后，选择"在默认应用中打开"或"在 Finder 中显示"。原生层只接受已经由服务端验证过的 Artifact ID，不能由 WebView 直接打开任意路径。
- 需求只在 pptx：7.4 后台任务完成
- 需求只在 pptx：自动化任务使用与 Web chat 相同的 ToolTransportWeb Artifact 工具计划。生成 Artifact 时，系统记录产物并在 automation run 列表和对应 session/task 上显示未查看状态，但不会切换用户正在查看的会话或右侧面板。用户进入 automation-run 详情后，通过该页面自己的 Artifacts 入口打开列表和 Viewer；查看后清除该 run 的未读状态。
- 需求只在 pptx：Artifact 分享是独立、明确的单文件授权。它不自动打开该会话的 Cloud sync，也不上传会话历史、其他 Artifact 或整个 workspace。

### cuixbo__OnePanel

段落标题不一致，需求条目 138 / 162 一致（pptx 拆出 159 条）

- 标题只在 Markdown：6.1 包含内容
- 标题只在 Markdown：6.2 不包含内容
- 标题只在 Markdown：7.1 快速查看常用命令
- 标题只在 Markdown：7.2 临时补充工作记录
- 标题只在 Markdown：7.3 跨桌面持续参考
- 需求只在 Markdown：系统状态栏图标入口。
- 需求只在 Markdown：点击状态栏图标显示/隐藏面板。
- 需求只在 Markdown：一个全局快捷键显示/隐藏面板。
- 需求只在 Markdown：单一主文档的纯文本编辑。
- 需求只在 Markdown：内容自动保存到本地。
- 需求只在 Markdown：窗口支持拖动、自由调节大小。
- 需求只在 Markdown：窗口支持"悬浮 / 固定"两种状态。
- 需求只在 Markdown：面板焦点状态下按 ESC 隐藏。
- 需求只在 Markdown：支持跨 Mission Control 桌面唤起。
- 需求只在 Markdown：面板唤起后，切换桌面时始终可见。
- 需求只在 pptx：8.2 用户故事列表
- 需求只在 pptx：9.4 页面边界说明
- 需求只在 pptx：应用启动后在 macOS 系统状态栏显示一个仅图标入口。用户点击图标时，可切换 OnePanel 面板的显示和隐藏状态。
- 需求只在 pptx：应用仅提供一个主记录面板。面板主体为纯文本编辑区域，用户可直接输入、修改、删除内容。
- 需求只在 pptx：10.3 自动保存与本地存储
- 需求只在 pptx：所有编辑内容自动保存到本地应用私有文件中，无需用户手动点击保存按钮。
- 需求只在 pptx：当 OnePanel 面板处于焦点状态时，用户按下 ESC，面板立即隐藏。
- 需求只在 pptx：MVP 提供最小设置页，用于管理少量必要配置。
- 需求只在 pptx：全局快捷键设置。
- 需求只在 pptx：窗口默认行为相关设置。

### dasi0227__QA-Agent

段落标题不一致，需求条目 143 / 169 一致（pptx 拆出 219 条）

- 标题只在 Markdown：2.1 项目名称
- 标题只在 Markdown：2.2 产品定位
- 标题只在 Markdown：2.3 当前核心问题
- 标题只在 Markdown：2.4 核心价值主张
- 标题只在 Markdown：3.1 目标用户
- 需求只在 Markdown：如何把用户资料稳定沉淀为结构清晰、长期可用的训练资产，而不是一次性生成结果。
- 需求只在 Markdown：如何在资产底座稳定之后，再逐步接入真正可用的 Agent 能力，而不是一开始就让系统承担过大的智能链路复杂度。
- 需求只在 Markdown：资料必须是系统的主证据源，而不是可有可无的输入附件。
- 需求只在 Markdown：问答集必须是可编辑、可持续训练、可长期复用的核心资产，而不是一次性文本输出。
- 需求只在 Markdown：系统演进必须遵循阶段化规律，先做底座，再做智能链路，不再走首版大而全路线。
- 需求只在 Markdown：把用户已有资料转成结构化、可复用的问答训练资产。
- 需求只在 Markdown：让用户围绕同一份问答集持续练习，而不是每次重新开始。
- 需求只在 Markdown：在资产稳定的前提下，逐步引入生成、反馈、评分与记忆能力，形成真正可持续的面试训练工作台。
- 需求只在 Markdown：项目总结文档
- 需求只在 Markdown：中间件学习笔记
- 需求只在 pptx：本文适用范围为 QA_Agent 当前这一轮重新收敛后的产品设计，不再默认首版一次性交付完整的生成、反馈、评估、记忆闭环，而是按照"核心资产 -> RAG -> 生成 Agent -> 反馈 Agent -> 评估 Agent -> Memory"的顺序逐步推进。
- 需求只在 pptx：5.1 前端技术选型
- 需求只在 pptx：5.2 后端技术选型
- 需求只在 pptx：5.3 后端选型原则
- 需求只在 pptx：用于承载主业务数据。当前核心资产如账户、画像、问答集、题目、练习会话等数据，都更适合作为标准业务数据稳定落在 MySQL 中。
- 需求只在 pptx：5.4 技术组合结论
- 需求只在 pptx：保存用户的求职方向与基本背景
- 需求只在 pptx：组成生成、反馈、评分的默认提示词上下文
- 需求只在 pptx：允许用户对智能体行为做基础自定义
- 需求只在 pptx：成为后续长期记忆沉淀的高优先级显式输入

### davidhoo__MarkdownReader

段落标题不一致，需求条目 126 / 163 一致（pptx 拆出 184 条）

- 标题只在 Markdown：4.1 窗口会话（Window Session）
- 标题只在 Markdown：4.2 资源
- 标题只在 Markdown：4.3 活动窗口
- 标题只在 Markdown：4.4 空白窗口
- 标题只在 Markdown：5.1 应用级共享状态
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 20 页
- 需求只在 Markdown：当前根目录或单文件模式；
- 需求只在 Markdown：当前选中文件；
- 需求只在 Markdown：AppViewModel、FileTreeViewModel、DocumentViewModel；
- 需求只在 Markdown：文档内容缓存、脏状态和文件监控；
- 需求只在 Markdown：显示模式、滚动位置、查找状态和缩放状态；
- 需求只在 Markdown：Sidebar、Outline、设置页、命令面板和全屏状态；
- 需求只在 Markdown：该会话使用的 undo/redo 历史。
- 需求只在 Markdown：能够作为窗口打开目标的本地 Markdown 文件、纯文本文件或目录。
- 需求只在 Markdown：当前 key window。菜单快捷键和文档级命令必须路由到该窗口；隐藏窗口、非 key window 和系统 Panel 不得响应。
- 需求只在 Markdown：尚未打开文件或目录、未创建待保存 Untitled 文档的主窗口。空白窗口显示 Welcome 页面，可以被下一次打开操作复用。
- 需求只在 pptx：目标版本：待定
- 需求只在 pptx：产品模型：Word 式文档多窗口
- 需求只在 pptx：5.1 应用级共享状态
- 需求只在 pptx：应用级设置发生变化时，所有窗口应按现有规则同步更新。
- 需求只在 pptx：5.2 窗口级独立状态
- 需求只在 pptx：首期只恢复最后一次活动窗口，不恢复上次退出时的全部窗口。
- 需求只在 pptx：6.2 新建窗口与新建文件
- 需求只在 pptx：当应用没有可见主窗口时执行"新建文件"，应先创建或恢复一个主窗口，再在其中创建 Untitled 文档。
- 需求只在 pptx：6.3 打开文件或目录
- 需求只在 pptx：如果活动窗口是空白窗口，复用该窗口打开资源。

### davidhoo__buddy

段落标题不一致，需求条目 280 / 348 一致（pptx 拆出 378 条）

- 标题只在 Markdown：1.1 目标用户
- 标题只在 Markdown：1.2 核心问题
- 标题只在 Markdown：1.3 产品目标
- 标题只在 Markdown：1.4 非目标
- 标题只在 Markdown：1.5 产品成功指标
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：初始化 Electron + electron-vite + React 19 + TypeScript + Tailwind 4
- 需求只在 Markdown：主/预加载/渲染进程能各自构建并打包通过
- 需求只在 Markdown：IPC bridge 跑通一个 ping/pong demo
- 需求只在 Markdown：pnpm install && pnpm dev 能启动空白窗口
- 需求只在 Markdown：pnpm build 输出可启动的 .app
- 需求只在 Markdown：Claude stream-json 模式：PTY 启动 → stdin 写入 prompt + \x04（Ctrl+D）→ 成功解析完整 JSON stream → 捕获 session_id → 无 ANSI 残留干扰
- 需求只在 Markdown：stderr 权限提示关键词检测（PTY 合并 stdout/stderr 下的检测策略）
- 需求只在 Markdown：记录 PTY 输出中的 ANSI 转义码样本，评估清洗成本
- 需求只在 Markdown：通过 → Phase 4 使用 PTY 方案
- 需求只在 Markdown：未通过 → Phase 4 使用 spawn 管道方案（与 buddy-python 一致），终端标签页使用独立 Shell PTY
- 需求只在 pptx：Buddy 是一个 macOS 原生桌面应用，采用 Electron 构建。界面完全参照 Codex Desktop App 的三栏布局——左侧 Sidebar、中间 Chat、右侧面板（含运行状态 / 文件 / 审查 / 终端四个标签页）；业务逻辑完整移植自 buddy-python 的收敛式 AI 工程协作功能。
- 需求只在 pptx：核心理念：两个 AI Actor（执行方 + Reviewer）轮流工作，每轮结束后给人 30 秒校准窗口，结果逐步收敛至正确。
- 需求只在 pptx：已经在日常开发中使用 Claude Code、Codex CLI、OpenCode 或 Kimi CLI 的个人开发者
- 需求只在 pptx：需要让 AI 反复实现 / 审查 / 修正，并希望保留人工校准窗口的工程师
- 需求只在 pptx：在多个本地项目之间切换，希望 AI 协作过程可恢复、可审计、可迁移的高级用户
- 需求只在 pptx：希望观察 AI 工程协作过程、导出对话和运行证据的技术负责人
- 需求只在 pptx：需要在 macOS 上用桌面界面管理 buddy-python 任务的既有用户
- 需求只在 pptx：目标：保持数据兼容；说明：与 buddy-python 共用 ~/Library/Application Support/buddy/，字段语义兼容；v0.1 验收信号：buddy-python 创建的任务可被 macOS 打开，macOS 创建的任务可被 buddy-python 推进
- 需求只在 pptx：目标：降低操作负担；说明：桌面 UI 常驻展示当前任务、状态、倒计时、下一 actor 和错误原因；v0.1 验收信号：用户不需要读 JSON 文件即可判断下一步操作
- 需求只在 pptx：不提供云端同步、团队协作后台或远程任务队列

### davidhoo__jsonpath

段落标题不一致，需求条目 52 / 93 一致（pptx 拆出 142 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值主张
- 标题只在 Markdown：2.1 已实现功能
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：length("café") 返回 4（含重音字符）
- 需求只在 Markdown：length([]) 返回 0（数组行为不变）
- 需求只在 Markdown：现有测试全部通过
- 需求只在 Markdown：新增 Unicode 字符串测试用例
- 需求只在 Markdown：对于 {"name": "root", "child": {"name": "child1"}}，$..name 返回 ["root", "child1"]
- 需求只在 Markdown：对于 {"value": 1}，$..value 包含根节点的 value
- 需求只在 Markdown：现有递归下降测试全部通过
- 需求只在 Markdown：括号可以覆盖默认优先级
- 需求只在 Markdown：! 对复合表达式的求值正确（De Morgan 定律）
- 需求只在 Markdown：RFC 9535 测试套件中相关用例通过
- 需求只在 pptx：产品名称： jsonpath — Go 语言 JSONPath 查询库当前版本： v2.0.2文档版本： 1.0最后更新： 2026-05-06文档状态： 草稿
- 需求只在 pptx：1.4 核心价值主张
- 需求只在 pptx：2.2 已知合规性缺陷（审计结果）
- 需求只在 pptx：来源：AUDIT_REPORT_2026.md、RFC9535_COMPLIANCE_REPORT.md
- 需求只在 pptx：jsonpath.go          — 公共 API（Query 函数） parser.go            — JSONPath 表达式解析器 segments.go          — 段类型定义和求值逻辑 functions.go         — 内置函数注册和实现 types.go             — 内部类型定义 errors.go            — 错误类型 stringCompare.go     — 本地化字符串比较 cmd/jp/              — CLI 工具
- 需求只在 pptx：以 bug fix 名义发布行为修正和新增语法，不改变任何 API 签名，用户无需修改代码。
- 需求只在 pptx：FR-2.1.1 修复 length() 字符串计算
- 需求只在 pptx：length() 函数对字符串参数应返回 Unicode 字符数（rune count），而非字节数。
- 需求只在 pptx：length("日本語") → 9  （按字节：UTF-8 编码每个汉字 3 字节）
- 需求只在 pptx：length("日本語") → 3  （按 Unicode 字符）

### dotnet9__Vex

段落标题不一致，需求条目 6 / 6 一致（pptx 拆出 11 条）

- 标题只在 Markdown：Markdown 和表格专项
- 标题只在 Markdown：数据失败处理专项
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 10 页
- 需求只在 pptx：不为旧原型增加兼容层。项目文件中的其他 RID、旧打包脚本及浏览器模拟流程不扩大正式交付范围。
- 需求只在 pptx：表格列宽依据表头和正文内容分配，短名称列收窄，长解释列获得空间；不能默认等分，也不应为填满区域拉宽短列。空间不足时换行或在表格内部横向滚动。使用"负责方 / 职责 / 示例"等长短内容混合样本，检查单视图、三视图及深浅模式。
- 需求只在 pptx：数据失败处理专项
- 需求只在 pptx：98% 是明确目标，不作为未经测量的宣传结论。当前数值只覆盖 Windows 安装器指定十张截图，完整应用和跨平台实机边界见验收文档。
- 需求只在 pptx：各模式的运行方法见 开发与验证。源码目录和数据流见概要设计，具体方法及失败分支见详细设计。

### dtsola__xiaoyaoprivatebill

段落标题不一致，需求条目 52 / 114 一致（pptx 拆出 63 条）

- 标题只在 Markdown：P0功能（必须有）
- 标题只在 Markdown：核心数据功能
- 标题只在 Markdown：核心分析功能
- 标题只在 Markdown：交易查询功能
- 标题只在 Markdown：演示模式
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：账单解析与导入：支持上传支付宝(CSV)和微信(XLSX/CSV)账单文件
- 需求只在 Markdown：多文件合并：支持同时上传多个账单文件并合并分析
- 需求只在 Markdown：数据自动识别：自动识别账单来源（支付宝/微信）
- 需求只在 Markdown：数据标准化：将不同平台的账单格式统一处理
- 需求只在 Markdown：会话管理：基于会话的数据处理，30分钟超时自动清理
- 需求只在 Markdown：年度分析：年度消费趋势、收支比例、分类占比
- 需求只在 Markdown：月度分析：月度消费明细、环比变化、趋势图
- 需求只在 Markdown：分类分析：按消费类别的统计、趋势、占比分析
- 需求只在 Markdown：时间分析：每日热力图、时段分布、工作日/周末对比
- 需求只在 Markdown：消费洞察：消费画像、商家分析、习惯识别
- 需求只在 pptx：为 使用支付宝/微信进行日常消费的广大人群 提供 数据完全本地处理、跨平台整合分析 的 账单分析工具
- 需求只在 pptx：用户访问首页 ↓ 选择【上传账单】或【演示模式】 ↓ ├─ 演示模式 → 加载示例数据 → 直接查看分析 │ └─ 上传账单 → 选择文件 → 上传 → 账单解析 ↓ 数据清洗和标准化 ↓ 主界面（年度分析页） ↓ 用户选择分析维度 ↓ ┌───────┼───────┐ ↓       ↓       ↓       ↓ 年度   月度   分类   时间   洞察   交易 分析   分析   分析   分析   分析   记录 ↓ 查看详细数据和可视化图表 ↓ 获取消费洞察和建议 ↓ 会话结束（30分钟）→ 数据自动清理
- 需求只在 pptx：功能：欢迎页面、产品介绍、入口引导
- 需求只在 pptx：功能：年度财务概览和趋势分析
- 需求只在 pptx：功能：月度消费明细分析
- 需求只在 pptx：功能：消费分类详细统计
- 需求只在 pptx：功能：时间维度消费模式分析
- 需求只在 pptx：功能：智能消费分析和建议
- 需求只在 pptx：功能：交易明细查询
- 需求只在 pptx：功能：数据管理和设置

### dtsola__xiaoyaosearch-dingding-export-md

段落标题不一致，需求条目 44 / 65 一致（pptx 拆出 61 条）

- 标题只在 Markdown：📦 个人知识备份
- 标题只在 Markdown：🔄 笔记工具迁移
- 标题只在 Markdown：🏛️ 企业知识归档
- 标题只在 Markdown：📊 技术文档本地化
- 标题只在 Markdown：🚀 离职文档交接
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 17 页
- 需求只在 Markdown：插件安装与激活：支持 Chrome/Edge 浏览器扩展安装
- 需求只在 Markdown：页面检测与注入：自动检测钉钉文档页面并注入插件功能
- 需求只在 Markdown：文档列表加载：获取并展示当前页面的文档/文件夹列表
- 需求只在 Markdown：单选/多选功能：支持选择单个或多个文档进行导出
- 需求只在 Markdown：文件夹级联选择：选择文件夹时自动选中所有子项
- 需求只在 Markdown：批量下载：支持同时下载多个选中的文档
- 需求只在 Markdown：目录结构保持：下载后的文件保持原有的文件夹层级
- 需求只在 Markdown：下载进度显示：实时显示每个文件的下载状态
- 需求只在 Markdown：导出格式配置：用户可自定义各类型文档的默认导出格式
- 需求只在 Markdown：错误处理与提示：网络错误、导出失败等异常情况友好提示
- 需求只在 pptx：💡 本工具是 小遥搜索 生态的扩展工具
- 需求只在 pptx：小遥搜索 —— 听懂你的话、看懂你的图，用 AI 找到本地任何文件。让搜索像聊天一样简单。
- 需求只在 pptx：为 钉钉文档用户 提供 批量导出知识库并转换为通用格式 的 浏览器插件
- 需求只在 pptx：插件激活流程
- 需求只在 pptx：用户访问钉钉文档 → 点击扩展图标 → 注入内容脚本 → 检测页面类型 → 加载文档列表 → 显示插件界面
- 需求只在 pptx：文档导出流程
- 需求只在 pptx：用户选择文档/文件夹 → 点击"下载选中" → 选择本地保存目录 → 递归处理选中项 → 调用钉钉导出API → 轮询任务状态 → 下载到本地 → 更新进度显示 → 完成/失败提示
- 需求只在 pptx：获取认证信息 → 获取文档列表 → 用户选择文档 → 上传文档元数据 → 创建导出任务 → 轮询任务状态 → 获取OSS下载链接 → 写入本地文件
- 需求只在 pptx：主界面品牌元素
- 需求只在 pptx：┌─────────────────────────────────┐ │ 🔍 小遥搜索 - 钉钉导出工具 v1.0.0 │ ├─────────────────────────────────┤ │ 💡 配合小遥搜索，实现本地AI搜索   │ │    了解更多 →                    │ ├─────────────────────────────────┤ │ 我的文档                          │ │ ████████████████░░ 80%           │ └─────────────────────────────────┘

### dtsola__xiaoyaosearch-feishu-export-md

段落标题不一致，需求条目 27 / 99 一致（pptx 拆出 53 条）

- 标题只在 Markdown：场景1：个人用户备份文档
- 标题只在 Markdown：场景2：迁移到其他笔记工具
- 标题只在 Markdown：场景3：企业知识库归档
- 标题只在 Markdown：场景4：技术文档版本控制
- 标题只在 Markdown：场景5：自动化备份
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 12 页
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：交互式引导用户输入飞书App ID和App Secret
- 需求只在 Markdown：生成配置文件 ~/.feishu-export/config.json
- 需求只在 Markdown：验证配置有效性（测试API连接）
- 需求只在 Markdown：配置查看 (feishu-export config get)
- 需求只在 Markdown：显示当前配置信息（脱敏处理）
- 需求只在 Markdown：配置更新 (feishu-export config set)
- 需求只在 Markdown：更新单个配置项
- 需求只在 Markdown：支持重置配置
- 需求只在 Markdown：支持存储多个飞书应用配置
- 需求只在 Markdown：通过 --profile 参数切换
- 需求只在 pptx：4.1 首次使用流程
- 需求只在 pptx：用户安装工具 ↓ feishu-export init ↓ 交互式输入App ID & Secret ↓ 验证API连接 ↓ 配置保存成功 ↓ feishu-export doc <doc_id> (首次导出测试)
- 需求只在 pptx：4.2 日常导出流程
- 需求只在 pptx：用户执行导出命令 ↓ 读取配置文件和参数 ↓ 获取 tenant_access_token ↓ 遍历文档列表 ↓ 并发请求文档内容 ↓ 转换Markdown格式 ↓ 是否下载图片/附件？ ├─ 是 → 下载资源 → 更新引用 └─ 否 → 保留原始链接 ↓ 写入本地文件 ↓ 显示导出报告
- 需求只在 pptx：4.3 错误处理流程
- 需求只在 pptx：捕获异常 ↓ 判断错误类型 ├─ 认证失败 → 提示重新配置 → 退出 ├─ 权限不足 → 记录失败ID → 继续 ├─ 网络错误 → 重试（最多3次） ├─ API限流 → 等待后重试 └─ 未知错误 → 记录日志 → 跳过 ↓ 生成错误报告
- 需求只在 pptx：5.3 命令详细说明
- 需求只在 pptx：初始化配置，交互式引导用户输入。
- 需求只在 pptx：feishu-export init [--profile <name>]
- 需求只在 pptx：导出单个文档。

### entropy-cloud__nop-entropy

段落标题不一致，需求条目 22 / 24 一致（pptx 拆出 37 条）

- 标题只在 Markdown：核心需求
- 标题只在 Markdown：其他需求说明
- 标题只在 Markdown：1. 业务目标与范围
- 标题只在 Markdown：2. 用户角色与场景
- 标题只在 Markdown：3. 核心功能需求
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 需求只在 Markdown：需求编号：按章节+序号分级（如FR2.1=功能需求3.2节第1条）。
- 需求只在 Markdown：来源：标注原始文档章节及问题编号（如3.1-Q4）。
- 需求只在 pptx：其他需求说明
- 需求只在 pptx：1. 业务目标与范围
- 需求只在 pptx：需求编号：SR2；需求描述：不包含：版本协作/用户权限管理、应用部署/移动端支持、团队协作功能；来源：1.范围边界；类型：范围；优先级：-；验收标准：-
- 需求只在 pptx：2. 用户角色与场景
- 需求只在 pptx：角色：需求分析工程师；使用场景：细化原始需求，设计业务用例和测试用例；关键需求：AI生成结果支持重新生成或改进；待澄清问题：需团队共享功能
- 需求只在 pptx：3. 核心功能需求
- 需求只在 pptx：3.1 智能需求输入
- 需求只在 pptx：3.3 模型编辑与调整
- 需求只在 pptx：3.4 应用生成与导出
- 需求只在 pptx：4. 非功能性需求

### fanfan-de__anybox

段落标题不一致，需求条目 66 / 109 一致（pptx 拆出 86 条）

- 标题只在 Markdown：4.1 快速收集
- 标题只在 Markdown：4.2 今日执行
- 标题只在 Markdown：4.3 待安排工作
- 标题只在 Markdown：4.4 对话中调用计划能力
- 标题只在 Markdown：4.5 Agent 执行任务
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：安排在今天的任务。
- 需求只在 Markdown：今天截止但未完成的任务。
- 需求只在 Markdown：等待用户确认的 Agent 建议。
- 需求只在 Markdown：准备资料或草稿。
- 需求只在 Markdown：启动一次有审计记录的执行。
- 需求只在 Markdown：将明确、重复的执行要求转为 Automation。
- 需求只在 Markdown：Planner Todo 领域模型、存储、查询与迁移。
- 需求只在 Markdown：今天、Inbox、即将到来、未安排、全部、待确认、已完成和项目视图。
- 需求只在 Markdown：任务快速创建、编辑、完成、筛选和删除/恢复策略。
- 需求只在 Markdown：日历作为二级视图，支持排期任务拖拽和右侧详情编辑。
- 需求只在 pptx：本文档是"计划"模块当前的产品权威入口。历史 Calendar-first 方案仅保留为决策背景，不再指导新功能实现。
- 需求只在 pptx：以待办事项为核心、以时间安排为可选属性、由 Agent 协助规划和执行的个人工作管理模块。
- 需求只在 pptx：用户先回答"我要做什么"，再决定"什么时候做、是否交给 Agent、是否形成自动化"。日历是任务的排期视图，不是主数据源，也不是默认首页。
- 需求只在 pptx：计划 ├─ 待办事项：工作的主对象 ├─ 排期：待办事项的可选时间属性 ├─ 日历：排期与外部事件的时间视图 ├─ Agent：建议、拆解和执行 └─ Automation：经用户确认后的持续或定时执行
- 需求只在 pptx："计划"作为顶层模块，与 Workspace、Agents、Automations 等入口平级。
- 需求只在 pptx：计划 ├─ 今天（默认） ├─ Inbox ├─ 即将到来 ├─ 未安排 ├─ 全部 ├─ 待确认 ├─ 已完成 ├─ 项目 └─ 日历视图
- 需求只在 pptx：默认使用紧凑列表，优先展示标题、状态、排期、截止时间、项目和优先级。日历、按日程列表等视图是同一批数据的不同呈现，不建立第二套任务对象。
- 需求只在 pptx：5.4 视觉与交互约束
- 需求只在 pptx：Todo 是计划模块的主对象。
- 需求只在 pptx：时间字段在领域层和本地 API 中统一使用 Unix epoch milliseconds；展示层负责时区格式化。

### flycalm__md-reader-miniprogram

段落标题不一致，需求条目 105 / 158 一致（pptx 拆出 177 条）

- 标题只在 Markdown：3.1 MVP 目标
- 标题只在 Markdown：3.2 成功指标
- 标题只在 Markdown：3.3 非目标
- 标题只在 Markdown：4.1 目标用户
- 标题只在 Markdown：4.2 核心场景
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：开发者工具以场景值 1173 启动成功。
- 需求只在 Markdown：Android 真机从微信聊天 .md 文件进入成功。
- 需求只在 Markdown：iOS 真机从微信聊天 .md 文件进入成功。
- 需求只在 Markdown：小程序冷启动、热启动和二次打开新文件均正确。
- 需求只在 Markdown：小程序内选择聊天文件成功。
- 需求只在 Markdown：成功阅读后首页出现最近记录，冷启动后仍可重新打开。
- 需求只在 Markdown：默认展示 3 条，展开后可滚动查看全部记录并可正常收起。
- 需求只在 Markdown：单条删除和一键清空同步删除本地副本，不影响聊天原文件。
- 需求只在 Markdown：单条删除默认需要确认；勾选"以后不再确认"并完成删除后，后续单条删除不再弹窗，取消时不保存该偏好。
- 需求只在 Markdown：中英文混排文档。
- 需求只在 pptx：文档版本：v1.5文档状态：已确认确认日期：2026-07-16产品形态：微信小程序暂定名称：MD 阅读器MVP 目标：让用户在微信聊天中方便、可靠地阅读 Markdown 文件
- 需求只在 pptx：具体性能目标在首轮真机测试后校准。
- 需求只在 pptx：不承诺点击文件后自动默认进入本小程序。微信仅提供"用小程序打开"入口，最终选择权由用户和微信客户端控制。
- 需求只在 pptx：不提供完整 Markdown 编辑器。
- 需求只在 pptx：不提供多人协作、评论或版本管理。
- 需求只在 pptx：不提供账号体系和跨设备同步。
- 需求只在 pptx：不提供 Word、图片或 HTML 等其他格式转换。
- 需求只在 pptx：不依赖服务端上传和解析文件。
- 需求只在 pptx：7.1 聊天素材打开
- 需求只在 pptx：7.2 主动选择聊天文件

### franklinxkk__ai-delivery-spec

段落标题不一致，需求条目 0 / 0 一致（pptx 拆出 20 条）

- 标题只在 Markdown：（无标题）
- 标题只在 pptx：第 1 页
- 标题只在 pptx：第 3 页
- 需求只在 pptx：#!/usr/bin/env python3 """Bounded stage-artifact checks; never infer intent or progress from prose."""
- 需求只在 pptx：from future import annotations
- 需求只在 pptx：import argparse import hashlib import json import re import sys from dataclasses import dataclass from pathlib import Path from typing import Any
- 需求只在 pptx：from cli_support import dependency_message, shell_command, input_error_detail
- 需求只在 pptx：try: import yaml except ModuleNotFoundError as exc: # pragma: no cover - clean-machine path message = dependency_message(getattr(exc, "name", "PyYAML/jsonschema"), "en-US" in sys.argv) print(message, file=sys.stderr) raise SystemExit(4) from exc
- 需求只在 pptx：if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8") if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
- 需求只在 pptx：STAGES = ("frame", "explore", "intake", "clarify", "specify", "review", "baseline", "change", "acceptance") EARLY_PROFILES = ("frame", "explore", "clarify") STAGE_INDEX = {name: index for index, name in enumerate(STAGES)}
- 需求只在 pptx：@dataclass class Artifact: path: Path text: str metadata: dict[str, Any] kind: str stage: str confidence: str = "declared"
- 需求只在 pptx：def sha256(path: Path) -> str: digest = hashlib.sha256() with path.open("rb") as stream: for chunk in iter(lambda: stream.read(65536), b""): digest.update(chunk) return digest.hexdigest()
- 需求只在 pptx：class ArtifactFormatError(ValueError): pass

### gitxuzhefeng__timelines

段落标题不一致，需求条目 105 / 127 一致（pptx 拆出 260 条）

- 标题只在 Markdown：（无标题）
- 标题只在 Markdown：一期迭代：核心闭环与单机可用 (MVP)
- 标题只在 Markdown：二期迭代：多模态 AI 深度赋能与智能洞察 (V1.0)
- 标题只在 Markdown：三期迭代：全平台协同与探索商业化团队版 (V2.0)
- 标题只在 Markdown：版本目标
- 标题只在 pptx：第 1 页
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 需求只在 Markdown：开发环境准备 工具 用途 要求 Node.js 18+ 前端开发、API 服务 必须 Rust 1.70+ Tauri 客户端核心 必须 pnpm / npm 包管理 推荐 pnpm Git 版本控制 必须 VS Code 开发 IDE 推荐 Docker 本地数据库/服务 可选 检查命令： node --version    # 需要 >= 18 rustc --version   # 需要 >= 1.70 pnpm --version
- 需求只在 Markdown：GET /api/v1/data/daily // Query Parameters interface DailyQueryParams { date: string;  // YYYY-MM-DD userId?: string;  // 自己的不需要传 }
- 需求只在 Markdown：推送配置 3.10.2 设置项定义 interface AppSettings { // 追踪设置 tracking: { enabled: boolean; pauseOnLock: boolean;      // 锁屏时暂停 pauseOnIdle: boolean;      // 空闲时暂停 idleThreshold: number;     // 空闲阈值（分钟） };
- 需求只在 Markdown：方向：AI 渠道；V1.x：仅 Claude API；V2.0：支持 Claude / DeepSeek / Qwen 多渠道
- 需求只在 Markdown：可成功配置并调用 DeepSeek API 进行分析
- 需求只在 Markdown：可成功配置并调用 Qwen API 进行分析
- 需求只在 Markdown：API Key 加密存储，界面显示脱敏（仅展示后 4 位）
- 需求只在 Markdown：连接测试按钮正确反馈成功/失败状态
- 需求只在 Markdown：主渠道超时（>10s）时自动切换到备用渠道
- 需求只在 Markdown：渠道切换记录写入日志
- 需求只在 pptx：🦞 TimeLens - AI 个人时间追踪应用 产品定位 一句话描述：AI 驱动的个人时间透视镜，自动记录电脑使用情况，智能分析并生成每日总结。 目标用户：程序员、设计师、知识工作者、自由职业者、学生
- 需求只在 pptx：技术架构 客户端 (Tauri)
- 需求只在 pptx：商业模式 版本 价格 功能 免费版 ¥0 基础追踪 + 简单周报 付费版 ¥30/月 AI 每日总结 + 洞察 + 多设备 企业版 定制 团队时间管理
- 需求只在 pptx：里程碑 [] MVP：本地追踪 + 飞书推送（2周） [] V1.0：AI 分类 + 每日报告（1个月） [] V1.5：生产力分析 + 对比功能（2个月） [] V2.0：公开发布
- 需求只在 pptx：技术架构设计
- 需求只在 pptx：Windows: GetForegroundWindow + GetWindowText 数据结构： struct WindowEvent { timestamp: i64, // Unix ms app_name: String, // "VSCode" app_bundle: Option, // "com.microsoft.VSCode" window_title: String, // "main.ts - myproject" duration_ms: i64, // 持续时间 is_active: bool, // 是否正在使用 }
- 需求只在 pptx：记录格式：[时间] App名称 - 窗口标题
- 需求只在 pptx：只输出 JSON 格式： {"categories": {...}, "insights": [...], "suggestions": [...]}
- 需求只在 pptx：-- 用户设置表 CREATE TABLE settings ( key TEXT PRIMARY KEY, value TEXT );
- 需求只在 pptx：-- 每日统计缓存 CREATE TABLE daily_stats ( date TEXT PRIMARY KEY, -- YYYY-MM-DD total_ms INTEGER, stats_json TEXT, -- 分类统计 JSON ai_insights TEXT, created_at INTEGER );

### grapeot__opencode_android_client

段落标题不一致，需求条目 107 / 112 一致（pptx 拆出 146 条）

- 标题只在 Markdown：1.1 它不是什么
- 标题只在 Markdown：1.2 核心交互范式
- 标题只在 Markdown：Steer 范式
- 标题只在 Markdown：Markdown 作为交互窗口
- 标题只在 Markdown：文件卡片预览（非代码编辑器）
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：约 60% 的时间在阅读 Markdown——AI 的分析报告、调研文章、设计文档、带有嵌入式截图的部署结果。这是"审"的环节。
- 需求只在 Markdown：约 25% 的时间在与 AI 对话——通过语音下达新指令、纠正方向、追问细节。这是"领"的环节。
- 需求只在 Markdown：约 10% 的时间在 Session 间切换——追踪不同项目、不同方向的进展，判断哪个需要介入。这是"多线统领"。Session 辨识度（一眼区分哪些是活跃的、哪些是已完成的）因此成为一个真实的 UX 痛点。
- 需求只在 Markdown：约 5% 的时间在 Files Tab——它本质上是一个兜底入口，绝大部分文件访问都是通过 Chat 窗口中的 tool/patch 卡片跳转完成的。
- 需求只在 Markdown：基于这个时间分布，产品优化的优先级应该是：Markdown 渲染质量 > 语音输入流畅度 > Session 辨识度 > 文件树功能。
- 需求只在 pptx：Product Requirements Document · v1.1 · Mar 2026
- 需求只在 pptx：核心设计原则：轻量、快速、以阅读和交互为主。所有繁重的配置（Provider 密钥、MCP 服务、workspace 设置）都在电脑端完成，Android 端只做必要的交互和消费。
- 需求只在 pptx：但比技术架构更根本的，是这个 App 要解决的核心交互问题：如何让 AI 把它做出的最关键决策浮出水面，供人类审查，并在必要时通过语音快速介入纠正——我们把这个模式叫做 Steer（统领）。AI 负责执行和探索，人类负责判断和方向。App 的价值不只是在"看一眼 AI 在干嘛"的监控，更在于它是一个轻量的决策审查与方向控制终端——用户每次打开都在阅读 Markdown 报告、查看嵌入的截图和产物、通过语音下达新的方向性指令。它不是浏览工具，是统领工具。
- 需求只在 pptx：围绕 Steer 这个范式，App 把重心放在了三个交互载体上：Markdown 对话窗口（AI 向人类汇报和展示产物的主要途径）、文件卡片预览（快速查看 AI 修改了什么，以文档而非代码为主）、语音输入（用户在远离键盘时仍能高效下达方向性指令）。代码语法高亮不是优先级——因为用户要审的不是代码本身，而是 AI 做决策的理由和结果。
- 需求只在 pptx：这个 App 不试图做以下事情：在手机上编辑代码、在手机上运行 OpenCode server、替代完整的 Web UI。它的价值在于"AI 在干活的任何时刻掏出手机，阅读它刚刚完成的 Markdown 分析报告或者代码改动，觉得方向不对就立刻通过语音让它换一条路"这种场景。
- 需求只在 pptx：1.2 核心交互范式
- 需求只在 pptx：Markdown 作为交互窗口
- 需求只在 pptx：文件卡片预览（非代码编辑器）
- 需求只在 pptx：Android Client 与 iOS Client 共享同一套产品范式和视觉语言（Quiet Tech），两者在功能上追求对等——Steer 范式、Markdown 交互窗口、文件卡片预览、语音输入、模型/Agent 切换、Host Profiles 与 SSH Tunnel 等核心体验在两个平台上保持一致。差异仅在于平台实现手段（Jetpack Compose / Material 3 vs SwiftUI、JSch vs Citadel/SwiftNIO）。详细的平台差异对照见下文"与 iOS 版本的差异"章节。
- 需求只在 pptx：1.4 核心能力总览

### guobin211__local-db

段落标题不一致，需求条目 137 / 147 一致（pptx 拆出 162 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心特性
- 标题只在 Markdown：1.3 技术架构
- 标题只在 Markdown：2.1 数据库下载安装
- 标题只在 Markdown：2.2 数据库运行管理
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：local-db 是一个跨平台的数据库管理工具，旨在简化本地开发环境中多种数据库的安装、配置和管理流程。通过提供统一的图形化界面，让开发者能够快速搭建和管理本地数据库环境。
- 需求只在 Markdown：多数据库支持：MySQL、PostgreSQL、MongoDB、Redis、Qdrant、SurrealDB
- 需求只在 Markdown：GUI操作：图形化界面（GUI）
- 需求只在 Markdown：统一管理：集中式的数据库安装、配置、启停、备份管理
- 需求只在 Markdown：开发友好：快速部署、一键启停、配置持久化
- 需求只在 Markdown：前端技术栈：React + TypeScript + TailwindCSS + Zustand
- 需求只在 Markdown：数据持久化：Tauri Store 插件
- 需求只在 Markdown：2026-01-11：初始版本，完善需求文档
- 需求只在 Markdown：2026-01-11：更新数据持久化方案，采用 Tauri Store 插件
- 需求只在 Markdown：2026-01-11：删除开机自启动章节，改为由 Rust 后端在应用启动时自动启动配置的数据库
- 需求只在 pptx：2.1 数据库下载安装
- 需求只在 pptx：2.2 数据库运行管理
- 需求只在 pptx：2.3 数据库配置管理
- 需求只在 pptx：2.4 数据库备份恢复
- 需求只在 pptx：2.6 数据库列表查看
- 需求只在 pptx：3.1 各平台的具体实现方案参考
- 需求只在 pptx：使用二进制包和 MSI 安装包
- 需求只在 pptx：统一存储路径：D:.local-db
- 需求只在 pptx：使用官方二进制包
- 需求只在 pptx：统一存储路径：~/.local-db

### gwwen05__CodeCompass

段落标题不一致，需求条目 61 / 106 一致（pptx 拆出 68 条）

- 标题只在 Markdown：产品名称
- 标题只在 Markdown：一句话介绍
- 标题只在 Markdown：解决的问题
- 标题只在 Markdown：P1: 小王 — Java 初学者
- 标题只在 Markdown：P2: 老李 — Java 后端开发
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：信息过载：一个中型项目可能有几百个类、几千个方法，不知道从哪开始看
- 需求只在 Markdown：调用链不透明：IDE 只能看单步跳转，难以理解完整的调用链路
- 需求只在 Markdown：业务逻辑分散：一个业务流程可能跨越多个模块、多个类，手动梳理成本高
- 需求只在 Markdown：缺乏结构化指导：新人对项目的学习没有路线图，只能随机阅读
- 需求只在 Markdown：文档缺失或过时：项目文档往往不完整、过时、或根本不存在
- 需求只在 Markdown：CodeCompass 通过 AI Agent 自动分析代码库，将代码转化为可查询的知识图谱，让开发者可以像对话一样理解代码。
- 需求只在 Markdown：年龄: 22，应届毕业生
- 需求只在 Markdown：技能: 基础 Java，Spring Boot 基础，无生产级项目经验
- 需求只在 Markdown：痛点: 第一次面对真实项目代码，不知道从哪开始
- 需求只在 Markdown：目标: 理解项目结构，从真实代码中学习
- 需求只在 pptx：产品需求文档 | Product Requirements Document
- 需求只在 pptx：版本: v0.1.0-draft | 日期: 2026-07-22 | 作者: gwwen
- 需求只在 pptx：FR1: 仓库分析 (Repository Understanding)
- 需求只在 pptx：FR4: 业务理解 (Business Understanding)
- 需求只在 pptx：核心功能：调用链图 + 业务分析
- 需求只在 pptx：核心功能：多 Agent 协作 + 学习路径
- 需求只在 pptx：核心功能：完整的企业级代码理解平台

### hackmagic__opennavicat

段落标题不一致，需求条目 31 / 122 一致（pptx 拆出 155 条）

- 标题只在 Markdown：0.0 对标基线与修订记录
- 标题只在 Markdown：0.1 目标
- 标题只在 Markdown：0.2 非目标
- 标题只在 Markdown：0.3 范围决策（2026-09-29 已定）
- 标题只在 Markdown：0.4 统一验收原则
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：现有 CLI、GUI 主流程仍可用。
- 需求只在 Markdown：核心模块之间不出现反向依赖 —— docs/module_dependency_matrix.md（scripts/build_dependency_matrix.py 自动生成），261 条顶层导入边、0 违规（2026-10-06，含 ClickHouse / Oracle 驱动与 Phase 6 流水线）（2026-09-30，含 ClickHouse / Oracle 驱动）。
- 需求只在 Markdown：至少 1 个连接器迁移到新分层 —— 全部 9 个 connector 现居 open_navicat/drivers/，dal/base_connector.py 与 dal/*_connector.py 保留兼容 shim。
- 需求只在 Markdown：已落地的新模块有模块说明 —— open_navicat/drivers/README.md（职责表、接入新引擎的两步流程、package 必填 / super().init() / 单线程 executor 桥接等约定与坑）。types / sql / formats / platform 尚未成模块，待各自 Phase 落地时补。
- 需求只在 Markdown：至少 1 个 CLI 命令、1 个 GUI 调用路径迁移到新分层 —— CLI：conn engines|add|test|open 全走注册表 + dsn.py；GUI：connection_dialog.py 的引擎下拉框 / 端口默认值 / 测试错误展示改走 drivers.registry 与 drivers.dsn。
- 需求只在 Markdown：新增模块的单元测试覆盖率不低于项目当前基线（基线：289 passed / 16 skipped，装 pytest-asyncio 前是 243/62；当前 556 passed）。
- 需求只在 Markdown：连接失败、超时、SQL 错误、AI 错误均使用统一错误对象（open_navicat/errors.py）；插件错误 ONV-PLG-001 已定义，待 Phase 8 接入。
- 需求只在 Markdown：CLI 展示结构化错误（conn add --test / conn test）；GUI 连接对话框"测试连接"失败时展示 NavicatError.render()（错误码 + 脱敏说明）。
- 需求只在 Markdown：错误码保持稳定，不复用、不改义（ONV-<域>-<序号>，见 ERROR_CATALOG 常量表）。
- 需求只在 Markdown：至少 1 类错误支持本地化展示。
- 需求只在 pptx：对标仓库：t8y2/dbx本仓库：hackmagic/OpenNavicat目标：把 OpenNavicat 从"单体工具"升级为"可扩展、可安全分发、AI/CLI/MCP 一致的核心平台"。
- 需求只在 pptx：0.0 对标基线与修订记录
- 需求只在 pptx：2026-09：按上述 commit 复核；修正包名、补充"运行时体积""专用浏览器与消息中间件""连接配置导入"等遗漏需求；标注已有实现，避免重复立项。
- 需求只在 pptx：这份文档把前面的差距分析拆成可执行需求，并给出验收标准。
- 需求只在 pptx：不要求一次性复刻 DBX 的全部功能。
- 需求只在 pptx：不要求改变主语言或放弃 Python。
- 需求只在 pptx：不要求一步到位做插件商店、Marketplace、供应链体系。
- 需求只在 pptx：0.3 范围决策（2026-09-29 已定）
- 需求只在 pptx：DBX 源码只作逻辑参考，不复制实现。
- 需求只在 pptx：0.4 统一验收原则

### hexianWeb__Third-Person-MC

段落标题不一致，需求条目 11 / 40 一致（pptx 拆出 34 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心体验流程
- 标题只在 Markdown：1.3 在线预览
- 标题只在 Markdown：3.1 无限地形系统
- 标题只在 Markdown：3.1.1 Chunk 管理
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：Chunk 动态加载/卸载正常工作
- 需求只在 Markdown：相同 Seed 生成一致的地形
- 需求只在 Markdown：多生态平滑过渡
- 需求只在 Markdown：地形振幅与 FBM 参数可调节
- 需求只在 Markdown：Chunk 随机事件系统实现
- 需求只在 Markdown：角色移动流畅，动画衔接自然
- 需求只在 Markdown：相机跟随不穿透地形
- 需求只在 Markdown：攻击 Combo 连击正常
- 需求只在 Markdown：越肩切换动画平滑
- 需求只在 Markdown：所有 HUD 组件正确渲染
- 需求只在 pptx：3.1 无限地形系统
- 需求只在 pptx：3.1.4 Chunk 随机事件（新功能）
- 需求只在 pptx：☒ Chunk 动态加载/卸载正常工作
- 需求只在 pptx：☒ 相同 Seed 生成一致的地形
- 需求只在 pptx：☒ 多生态平滑过渡
- 需求只在 pptx：☒ 地形振幅与 FBM 参数可调节
- 需求只在 pptx：☐ Chunk 随机事件系统实现
- 需求只在 pptx：3.2 第三人称角色控制
- 需求只在 pptx：☒ 角色移动流畅，动画衔接自然
- 需求只在 pptx：☒ 相机跟随不穿透地形

### iflytek__skillhub

段落标题不一致，需求条目 109 / 119 一致（pptx 拆出 132 条）

- 标题只在 Markdown：背景
- 标题只在 Markdown：业务问题
- 标题只在 Markdown：目标用户
- 标题只在 Markdown：价值主张
- 标题只在 Markdown：核心功能
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：在技能详情页与审核详情页中新增常驻文件浏览侧边栏。
- 需求只在 Markdown：将现有平铺 files 列表重构为目录树，支持文件夹展开 / 合并。
- 需求只在 Markdown：点击文件节点后，通过弹窗预览文件内容。
- 需求只在 Markdown：支持 Markdown 文档渲染、常见文本文件源码预览，以及大文件 / 不支持文件类型的不可预览提示。
- 需求只在 Markdown：对不可预览文件提供下载入口。
- 需求只在 Markdown：桌面端使用右侧侧边栏布局，移动端将文件浏览区域下沉到主内容区域下方。
- 需求只在 Markdown：按版本浏览文件树与文件预览，并结合权限控制设计访问策略。
- 需求只在 Markdown：侧边栏搜索过滤、最近打开文件、选中文件高亮等增强交互。
- 需求只在 Markdown：对 JSON / YAML / TS / JS 等文本文件提供更完整的语法高亮能力。
- 需求只在 Markdown：超大文本文件受控截断预览，基于服务端预览接口返回结构化元数据。
- 需求只在 pptx：2026-10-09 更新：本文件记录早期侧栏方案。审核详情页现采用顶部摘要和页级 Tab，文件树移入"内容与文件"Tab；下文有关审核页常驻右侧栏及其三个内层 Tab 的条款不再适用。技能市场详情页的侧栏需求仍按本文件执行。审核页最新行为见 审核指南。
- 需求只在 pptx：当前技能详情页 space/global/skill-writer 与审核详情区块都提供"概览 / 文件 / 版本"三个 Tab，但文件区域仅展示平铺文件列表，无法在页面内浏览目录层级或直接查看文件内容。
- 需求只在 pptx：技能详情页已经具备按路径读取单个文件内容的能力，可用于 README 加载；审核详情页目前仅返回 files、documentationPath、documentationContent，还不具备按任意文件路径读取正文的能力。
- 需求只在 pptx：用户需要在不下载整个 zip 包的前提下，快速查看 skill 包含的目录结构与具体文件内容，提升详情浏览和审核判断效率。
- 需求只在 pptx：浏览技能详情的普通用户
- 需求只在 pptx：管理技能的作者 / 命名空间成员
- 需求只在 pptx：在审核中心查看技能内容的审核人员与管理员
- 需求只在 pptx：用户交互流程
- 需求只在 pptx：页面布局要求
- 需求只在 pptx：文件预览行为

### jaylinwang__zen

段落标题不一致，需求条目 72 / 72 一致（pptx 拆出 91 条）

- 标题只在 Markdown：用户已确认
- 标题只在 Markdown：本文提出的第一版默认值
- 标题只在 Markdown：第一版目标
- 标题只在 Markdown：第一版不包含
- 标题只在 Markdown：两端分工建议
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 11 页
- 需求只在 pptx：版本：v0.5 草案 日期：2026-10-21 项目名：zen；应用显示名：禅 来源：用户对阶段性计时、专注声音、结束觉察和自主放弃的需求说明；最新范围为个人自用的 Mac 与 iPhone 应用，采用本地文件存储，文件同步由用户自行处理，暂不考虑 Apple Watch。
- 需求只在 pptx：核心体验：一键开始 → 专注 → 结束觉察 → 可靠保存到本地。
- 需求只在 pptx：产品保持轻量，以"禅"和关注当下为体验方向。应用提供时间边界和记录，不判断用户是否真正专注；修行的感受由使用者自己体会。
- 需求只在 pptx：本文提出的第一版默认值
- 需求只在 pptx：跨端关系与文件同步边界
- 需求只在 pptx：Mac 端首次打开选择一个独立数据目录，展示文件存放方式。目录取消选择则留在设置引导，不静默写入其他位置。完成选择后显示开始按钮；可直接使用默认时长，无需建立项目或任务。
- 需求只在 pptx：4.2 未选任务直接开始
- 需求只在 pptx：示例："修复博客移动端导航""阅读 SwiftUI 文档""整理职业选择思路"。
- 需求只在 pptx：4.3 开始前选择名称
- 需求只在 pptx：放弃只影响当前一轮，其他已完成记录和待补记保持不变。界面不对放弃作惩罚性评价。旧版本已有的放弃记录保留并可手动删除，不计入累计；不批量清理用户文件。已完成、异常中断和待补记记录也可在详情中手动删除；确认后移除对应本地文件和草稿，并更新累计时间。

### jerryjiao__dsh-wewrite

段落标题不一致，需求条目 91 / 95 一致（pptx 拆出 117 条）

- 标题只在 Markdown：2.1 主要画像：技术型公众号号主（核心，占预期 80%+）
- 标题只在 Markdown：2.2 次要画像：重度内容创业者（v0.1 服务其单账号场景）
- 标题只在 Markdown：2.3 核心场景（3 个）
- 标题只在 Markdown：3.1 竞品矩阵（调研日期 2026-08-18）
- 标题只在 Markdown：3.2 热门榜数据源可用性（场景 B 的供给面）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：身份：开发者 / AI 从业者 / 独立博主，25-40 岁，运营科技、AI、开发向公众号（周更 2-7 篇）。
- 需求只在 Markdown：环境：本机已装 DSH（~/.dsh/ 已存在，已配模型插件与 API key），会用命令行但不享受折腾配置。
- 需求只在 Markdown：技术水平：高。能读懂报错、会配环境变量；但期待「装完即用」，不接受为了发一篇文章研究半天 IP 白名单。
- 需求只在 Markdown：核心诉求：把我自己的模型订阅变成内容生产力；写作风格稳定可复现；发出前我必须能过目（默认只进草稿箱）。
- 需求只在 pptx：谁：已经在用 DSH（本地 AI Agent harness，91k+ stars，npx @deepseek-ai/dsh web 即起）的技术博主、独立开发者、内容创业者——他们运营微信公众号，且已经为本机配置好了大模型供应商。
- 需求只在 pptx：现在怎么解决、为什么不行：Jerry 自己用一条私有 skill 管线（workspace-writer/wewrite，经真实生产使用检验）解决了这个问题，但它是个人工作流，不是产品——没有配置界面、没有安装路径、没有对外文档。dsh-wewrite 要做的就是把这条已验证的管线产品化给所有 DSH 用户：一条命令安装，界面里配好凭据和供应商，之后「给主题出一篇」或「每天 4 点自动跑」。
- 需求只在 pptx：3.1 竞品矩阵（调研日期 2026-08-18）
- 需求只在 pptx：3.2 热门榜数据源可用性（场景 B 的供给面）
- 需求只在 pptx：源：imsyy/DailyHotApi；可用性：✅ 开源自托管（约 2.7k+ star）；说明：聚合微博/知乎/百度/抖音/B站/头条/豆瓣/V2EX/GitHub 等热榜，JSON+RSS，Docker/Vercel 一键部署；产品内置支持用户填自建实例 URL，不内置第三方公共实例（公共实例无 SLA 且合规主体不明）
- 需求只在 pptx：结论：选题数据源供给无风险；合规姿态是「用户自备聚合源 URL + 公开 HN API」。
- 需求只在 pptx：3.3 我们的差异化（用户为什么选 dsh-wewrite）
- 需求只在 pptx：4.1 P0 视觉门禁（workspace 全局，违反=退回重做）
- 需求只在 pptx：4.2 安全默认（产品价值观，不可谈判）
- 需求只在 pptx：RICE 口径：Reach=受影响用户占比（1-10）；Impact=单用户影响（0.25/0.5/1/2/3）；Confidence=确信度（100%=源管线已验证/80%=有竞品佐证/50%=直觉）；Effort=人月（1=半天 ... 10=3 个月+）。Score = R×I×C/E。

### jnMetaCode__agency-orchestrator

段落标题不一致，需求条目 42 / 42 一致（pptx 拆出 61 条）

- 标题只在 Markdown：P0 — MVP（v0.1）
- 标题只在 Markdown：F1: Workflow YAML 定义
- 标题只在 Markdown：F2: DAG 执行引擎
- 标题只在 Markdown：F3: LLM Connector 接口
- 标题只在 Markdown：F4: CLI 入口
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 13 页
- 需求只在 pptx：基于 agency-agents 角色定义的轻量多智能体编排引擎 —— 用 YAML 定义工作流，自动调度 AI 角色协作完成复杂任务。
- 需求只在 pptx：现状： 用户手动拆任务 → 手动复制粘贴上下文 → 手动汇总结果 目标： 写一个 YAML 文件 → 引擎自动编排执行 → 输出最终结果
- 需求只在 pptx：analyze ──→ tech_review ──→ final_summary └→ design_review ──┘ (tech 和 design 并行)
- 需求只在 pptx：抽象的 LLM 调用层。MVP 只做 1 个 provider（Claude 或 OpenAI，取决于用户基数），其他 v0.2 加。
- 需求只在 pptx：interface LLMConnector {  chat(systemPrompt: string, userMessage: string): Promise<LLMResult>;}interface LLMResult {  content: string;  usage: { input_tokens: number; output_tokens: number };}
- 需求只在 pptx：# 执行工作流npx agency-orchestrator run workflow.yaml --input prd_content=@prd.md# 验证工作流定义（不执行）npx agency-orchestrator validate workflow.yaml# 查看执行计划（DAG 可视化）npx agency-orchestrator plan workflow.yaml# 列出可用角色npx agency-orchestrator roles --agents-dir ./agents
- 需求只在 pptx：F5: 执行过程输出
- 需求只在 pptx：🔄 [1/4] analyze — product/product-manager ✅ 完成 (3.2s, 856 tokens)
- 需求只在 pptx：ao-output/产品需求评审-20260321-163000/ ├── summary.md          # 最终步骤的输出 ├── steps/ │   ├── 1-analyze.md │   ├── 2-tech_review.md │   ├── 3-design_review.md │   └── 4-final_summary.md └── metadata.json       # 执行耗时、token 用量等
- 需求只在 pptx：F6: 人工介入 / 审批节点

### jnMetaCode__openshorts

段落标题不一致，需求条目 41 / 57 一致（pptx 拆出 66 条）

- 标题只在 Markdown：2.1 用户故事（M1 验收用）
- 标题只在 Markdown：2.2 竞品对照
- 标题只在 Markdown：3.1 口播短视频（默认线，免费可跑通）
- 标题只在 Markdown：3.2 AI 短剧（差异化线）
- 标题只在 Markdown：5.1 MVP（M1，能发的第一条片）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：口播科普模板：话题 → 脚本 → 素材库配画面 → 免费 TTS → 字幕 → BGM → 1080×1920 mp4
- 需求只在 Markdown：画面来源切换（素材库 / AI 配图 / 云端出片）— 项目级默认 + 镜头级覆盖
- 需求只在 Markdown：花费预览（openshorts estimate；短剧线 drama --plan 逐镜报价，界面「确认花费，出片」）
- 需求只在 Markdown：四步界面：输入 → 选模板与来源 → 看预览与花费 → 出片/下载
- 需求只在 Markdown：中文界面、中文 TTS 音色（Edge TTS 免费默认，其余走 AO type: tts）
- 需求只在 Markdown：发布规格：封面图、标题 3 选 1、话题标签、平台尺寸预设（抖音/视频号/B 站/Shorts）
- 需求只在 Markdown：「AI 短剧」模板（复用 AO 短剧流水线）
- 需求只在 Markdown：本地生成适配器：sd.cpp（Metal / CUDA），硬件检测 → 推荐档位 → 按需下载 GGUF → 出片；预期时长与画质在界面明说
- 需求只在 Markdown：看图验收结果在界面可见，一键"按未满足项重出"
- 需求只在 Markdown：项目历史、重跑某一镜、更换来源重出
- 需求只在 pptx：版本：v2.1 · 2026-08-30 · 状态：已定案，进入 M0（v2.1：自审后补齐模板规格、免费路径前提、合规、竞品对照、用户故事）
- 需求只在 pptx：开源、本地优先的短视频生产线：文案进，成片出。
- 需求只在 pptx：2.1 用户故事（M1 验收用）
- 需求只在 pptx：3.1 口播短视频（默认线，免费可跑通）
- 需求只在 pptx：3.2 AI 短剧（差异化线）
- 需求只在 pptx：5.1 MVP（M1，能发的第一条片）
- 需求只在 pptx：勾选状态 2026-09-11 与 03-开发计划 对账：[x] 已做并真跑验证，[~] 部分完成，[ ] 未做。
- 需求只在 pptx：☒ 口播科普模板：话题 → 脚本 → 素材库配画面 → 免费 TTS → 字幕 → BGM → 1080×1920 mp4
- 需求只在 pptx：☒ 画面来源切换（素材库 / AI 配图 / 云端出片）— 项目级默认 + 镜头级覆盖
- 需求只在 pptx：☒ 花费预览（openshorts estimate；短剧线 drama --plan 逐镜报价，界面「确认花费，出片」）

### junerver__ComposeHooks

段落标题不一致，需求条目 24 / 45 一致（pptx 拆出 45 条）

- 标题只在 Markdown：1.1 谁在依赖这个
- 标题只在 Markdown：1.2 当前的问题
- 标题只在 Markdown：1.3 期望收益
- 标题只在 Markdown：2.1 核心需求（P0）
- 标题只在 Markdown：2.2 次要需求（P1）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：useState / useGetState / useLatestState（状态）
- 需求只在 Markdown：useContext / createContext（上下文）
- 需求只在 Markdown：Palette 计划建设在线文档站点，目标是在浏览器中提供组件的真实可交互预览（可点击、可调参的 Compose 组件）。这需要为 Palette 的 palette 模块启用 wasmJs target，用 Compose Multiplatform 编译到 WebAssembly 运行在浏览器里。
- 需求只在 Markdown：ID：R2；需求：核心状态 hooks 全部可用；说明：下表"必须在 wasmJs 可用"的 hooks 不能因平台限制降级或编译失败。
- 需求只在 Markdown：V1：hooks/build.gradle.kts 中存在 wasmJs { browser() } target。
- 需求只在 Markdown：V2：./gradlew :hooks:publishToMavenLocal 成功，且产物包含 wasmJs klib（2.4.0-beta-1, 963KB）。
- 需求只在 Markdown：V3：本地 Maven 中 hooks2 新版本的 .module 文件包含 wasmJs variant。
- 需求只在 Markdown：V4：§3.1 列出的核心 hooks 在 wasmJs target 下编译通过（./gradlew :hooks:compileKotlinWasmJs）。
- 需求只在 Markdown：V5：§3.1 核心 hooks 在 wasmJs 下功能正确（hooks/src/wasmJsTest 已覆盖 201 项测试，含 WasmJsSmokeTest + 继承自 commonTest 的 Fetch/Redux/Debounce/Form/Table）。
- 需求只在 Markdown：V6：§3.2 的 hooks 要么在 wasmJs 可用，要么在 API 文档中明确标注"wasmJs 不支持/降级"。（待阶段 2 处理；当前 useRequest/useForm/useRedux 依赖的 KClass 仅作 Map 键，wasmJs 下可用，反射调用已隔离在 commonJvmAndroid。）
- 需求只在 pptx：提出日期：2026-06-29 提出方：Palette 组件库（xyz.junerver.compose.palette） 优先级：P0（阻塞下游文档站的在线交互预览能力） 状态：✅ 已完成（2.4.0-beta-1，2026-06-29）
- 需求只在 pptx：闭环验证：hooks2 2.4.0-beta-1 已在 Maven Central 发布（含 wasmJs 变体）。Palette 已升级 并验证 :palette:compileKotlinWasmJs BUILD SUCCESSFUL（走远程 Maven Central，非本地缓存）。 反射隔离设计（commonMain 只用 stdlib KClass，反射调用隔离在 commonJvmAndroid）经验证有效。 下游 Palette 已为 palette + 3 子模块启用 wasmJs target，仅修 1 处 PlatformActivity actual。
- 需求只在 pptx：3.1 ✅ 预期可直接可用（纯 Compose 状态逻辑，无平台依赖）
- 需求只在 pptx：3.2 ⚠️ 需要验证/可能需轻量适配
- 需求只在 pptx：3.3 ❓ 平台强依赖，需明确 wasmJs 行为
- 需求只在 pptx：4.1 ⚠️ kotlin.reflect（KClass / KFunction / KProperty）
- 需求只在 pptx：这是最大的移植风险点。 共 11 处 import 分布在 10 个文件（见 §3.2/3.3）。
- 需求只在 pptx：4.2 ✅ arrow-kt（arrow-core / arrow-functions）
- 需求只在 pptx：4.4 ✅ kotlinx-datetime / kotlinx-coroutines / kotlinx-collections-immutable
- 需求只在 pptx：4.5 ✅ usePersistent / useRequest 的注入式架构

### konghanghang__openlist-strm

段落标题不一致，需求条目 143 / 161 一致（pptx 拆出 182 条）

- 标题只在 Markdown：1.1 项目简介
- 标题只在 Markdown：1.2 核心价值
- 标题只在 Markdown：1.3 技术栈
- 标题只在 Markdown：2.1 核心功能
- 标题只在 Markdown：2.1.1 Alist 集成
- 标题只在 pptx：2. 查询任务状态
- 标题只在 pptx：3. 获取配置列表
- 标题只在 pptx：4. Webhook 接收（可选）
- 标题只在 pptx：5. 健康检查
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：免挂载：无需挂载网盘，通过 STRM 文件直接播放
- 需求只在 Markdown：节省空间：本地只存储小体积的 STRM 文件
- 需求只在 Markdown：灵活调度：每个配置独立定时任务，可视化 Cron 编辑器
- 需求只在 Markdown：高性能：Go 语言实现，每配置独立并发控制
- 需求只在 Markdown：MediaWarp 集成：支持 302 重定向代理，优化播放体验
- 需求只在 Markdown：Web UI 管理：无需编辑配置文件，所有配置通过 Web UI 管理
- 需求只在 Markdown：前端：Vue.js 3 + Element Plus + Vite
- 需求只在 Markdown：部署：单二进制文件（前端嵌入）/ Docker
- 需求只在 Markdown：STRM 文件格式说明
- 需求只在 Markdown：tefuirZ/alist-strm - Python 实现的 STRM 生成工具
- 需求只在 pptx：功能描述：将 Alist 路径映射到本地 STRM 目录
- 需求只在 pptx：管理方式：通过 Web UI 管理，存储在 SQLite 数据库
- 需求只在 pptx：target：本地 STRM 目标路径
- 需求只在 pptx：extensions：媒体扩展名列表（如：mp4, mkv, mp3）
- 需求只在 pptx：concurrent：并发数（默认 3，推荐 1-5）
- 需求只在 pptx：strm_mode：STRM 模式（alist_path / http_url）
- 需求只在 pptx：cron_expr：Cron 表达式（可选，为空则不启用定时）
- 需求只在 pptx：2.2.1 定时任务（Cron）✨ 已优化
- 需求只在 pptx：2.2.3 API 触发（差异化功能 🌟）
- 需求只在 pptx：POST /api/generate { "path": "/media/movies", "mode": "incremental" }

### kunhuang12345__wuthering-waves-automation

段落标题不一致，需求条目 272 / 303 一致（pptx 拆出 305 条）

- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 技术栈
- 标题只在 Markdown：2.1 核心功能模块
- 标题只在 Markdown：2.1.1 日常任务自动化
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：核心框架: LangChain + AutoGPT架构
- 需求只在 Markdown：图像识别: OpenCV 4.8+, PIL, EasyOCR
- 需求只在 Markdown：自动化控制: PyAutoGUI, win32api, pynput
- 需求只在 Markdown：决策模型: 强化学习算法
- 需求只在 Markdown：数据存储: SQLite + Redis缓存
- 需求只在 Markdown：Web框架: FastAPI (可选的管理界面)
- 需求只在 Markdown：项目结构搭建
- 需求只在 Markdown：基础自动化控制实现
- 需求只在 Markdown：图像识别基础功能
- 需求只在 Markdown：配置管理系统
- 需求只在 pptx：2.1 核心功能模块
- 需求只在 pptx：2.1.1 日常任务自动化
- 需求只在 pptx：2.1.2 资源收集自动化
- 需求只在 pptx：功能描述: 自动收集游戏中的各种资源
- 需求只在 pptx：2.1.3 角色养成自动化
- 需求只在 pptx：功能描述: 自动管理角色养成相关操作
- 需求只在 pptx：功能描述: 自动执行战斗相关操作
- 需求只在 pptx：功能描述: 自动执行探索相关操作
- 需求只在 pptx：2.2 智能决策模块
- 需求只在 pptx：2.2.1 任务优先级管理

### kyre-99__MacDynamicIslandPet

段落标题不一致，需求条目 35 / 183 一致（pptx 拆出 51 条）

- 标题只在 Markdown：2.1 总目标
- 标题只在 Markdown：2.2 用户感知目标
- 标题只在 Markdown：3.1 少而准，不堆上下文
- 标题只在 Markdown：3.2 先组织，再生成
- 标题只在 Markdown：3.3 事实、关系、自我解释分层
- 需求只在 Markdown：用户通常什么时候愿意互动
- 需求只在 Markdown：用户偏好的语气
- 需求只在 Markdown：哪些话题容易获得回应
- 需求只在 Markdown：哪些行为会让小人更靠近或更失落
- 需求只在 Markdown：最近关系变化摘要
- 需求只在 Markdown：当前身份与关系状态
- 需求只在 Markdown：当前内部状态
- 需求只在 Markdown：当前观察与环境
- 需求只在 Markdown：最近几轮对话
- 需求只在 Markdown：召回的 1~3 条高相关记忆
- 需求只在 pptx：3.1 少而准，不堆上下文
- 需求只在 pptx：每次生成只给模型必要且高命中的信息，不再简单堆叠全文记忆。
- 需求只在 pptx：3.2 先组织，再生成
- 需求只在 pptx：任何对话、自言自语、主动评论前，都先构建"工作记忆"。
- 需求只在 pptx：3.3 事实、关系、自我解释分层
- 需求只在 pptx：优先兼容现有代码，不做一次性推翻重构。
- 需求只在 pptx：struct PetInternalState: Codable {    var mood: String    var energy: Int    var socialNeed: Int    var attachmentLevel: Int    var frustration: Int    var curiosityFocus: String?    var currentGoal: String?    var unfinishedThought: String?    var lastInteractionAt: Date?    var updatedAt: Date}
- 需求只在 pptx：struct RelationshipSnapshot: Codable {    var stageSummary: String    var preferredTone: String?    var favoriteTopics: [String]    var sensitiveTopics: [String]    var interactionPatterns: [String]    var petInterpretations: [String]    var updatedAt: Date}
- 需求只在 pptx：struct WorkingMemoryContext {    var identitySummary: String    var relationshipSummary: String    var internalStateSummary: String    var environmentSummary: String    var recentConversationSummary: String    var recalledMemories: [String]    var unfinishedThought: String?}
- 需求只在 pptx：8.4 ConversationAnalysisManager

### lhxone__TeacherDesk

段落标题不一致，需求条目 86 / 86 一致（pptx 拆出 91 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 设计原则
- 标题只在 Markdown：2.1 V1 范围（本期）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 pptx：3.6 随机抽签 / 分组
- 需求只在 pptx：3.6.1 随机点名（抽签）
- 需求只在 pptx：3.7 成绩管理与分析
- 需求只在 pptx：3.7.3 班级维度分析
- 需求只在 pptx：3.7.4 学生维度分析

### liamyueng__xu-ai-news-rag

段落标题不一致，需求条目 87 / 119 一致（pptx 拆出 108 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 产品愿景
- 标题只在 Markdown：2.1 核心用户故事
- 标题只在 Markdown：2.2 场景描述
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：作为一名金融分析师，我希望系统能够自动从investing.com等财经网站抓取最新新闻，这样我就不需要手动收集信息了。
- 需求只在 Markdown：作为一名投资顾问，我希望能够通过自然语言查询相关的新闻信息，系统能够理解我的问题并返回最相关的内容。
- 需求只在 Markdown：作为一名内容管理员，我希望能够管理知识库中的内容，包括查看、编辑、删除和批量导入数据。
- 需求只在 Markdown：作为一名研究人员，我希望系统能够对新闻数据进行聚类分析，展示热点话题和关键词分布。
- 需求只在 Markdown：功能描述: 定时从investing.com等财经网站抓取新闻
- 需求只在 Markdown：每小时自动抓取一次
- 需求只在 Markdown：支持去重功能
- 需求只在 Markdown：功能描述: 提供用户注册、登录、权限管理
- 需求只在 Markdown：密码加密存储
- 需求只在 Markdown：功能描述: 增删改查知识库内容
- 需求只在 pptx：版本: 1.0日期: 2025年10月9日作者: Xu
- 需求只在 pptx：随着信息技术的快速发展，新闻资讯呈现爆炸式增长。传统的新闻获取和管理方式已无法满足用户对于个性化、智能化信息处理的需求。本项目旨在构建基于大语言模型的智能新闻知识库系统，通过自动化新闻抓取、语义理解和智能检索，为用户提供高效的新闻信息管理和查询服务。
- 需求只在 pptx：主要用户: 金融分析师、投资顾问、财经记者
- 需求只在 pptx：次要用户: 投资者、财经爱好者、研究人员
- 需求只在 pptx：管理员用户: 系统管理员、内容管理员
- 需求只在 pptx：打造智能化的新闻知识库平台，通过AI技术实现新闻内容的自动采集、智能分析和精准检索，帮助用户在海量信息中快速找到有价值的内容，提升信息获取和决策效率。
- 需求只在 pptx：4.3 算法边界与可解释性
- 需求只在 pptx：☐ 所有P0功能100%完成
- 需求只在 pptx：☐ 所有P1功能80%完成
- 需求只在 pptx：☐ 通过全部核心功能测试

### liangyimingcom__BRClient

段落标题不一致，需求条目 153 / 236 一致（pptx 拆出 272 条）

- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 产品愿景
- 标题只在 Markdown：1.4 产品原则
- 标题只在 Markdown：2.1 功能优先级定义
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：核心定位: AWS Bedrock专用客户端
- 需求只在 Markdown：目标用户: 企业技术团队、AI开发者、内容创作者
- 需求只在 Markdown：差异化: 专注、简洁、开源、跨平台
- 需求只在 Markdown：简单至上: 降低使用门槛，开箱即用
- 需求只在 Markdown：性能优先: 快速响应，流畅体验
- 需求只在 Markdown：安全可靠: 数据本地存储，隐私保护
- 需求只在 Markdown：开放生态: 开源协议，插件扩展
- 需求只在 Markdown：可输入和保存AWS凭证
- 需求只在 Markdown：配置保存后可正常调用API
- 需求只在 Markdown：凭证本地加密存储
- 需求只在 pptx：2.1 功能优先级定义
- 需求只在 pptx：2.2.1 用户管理模块
- 需求只在 pptx：功能描述: 用户配置AWS访问凭证和区域设置
- 需求只在 pptx：☐ 可输入和保存AWS凭证
- 需求只在 pptx：☐ 配置保存后可正常调用API
- 需求只在 pptx：☐ 凭证本地加密存储
- 需求只在 pptx：☐ 错误配置有明确提示
- 需求只在 pptx：F1.2 用户偏好设置 (P1)
- 需求只在 pptx：功能描述: 用户个性化设置
- 需求只在 pptx：☐ 设置可保存和恢复

### lintsinghua__oops

段落标题不一致，需求条目 51 / 82 一致（pptx 拆出 84 条）

- 标题只在 Markdown：1.1 官方需求长期悬而未决
- 标题只在 Markdown：1.2 竞品（2026-10-14 快照）
- 标题只在 Markdown：2.1 一句话定位
- 标题只在 Markdown：2.2 Slogan
- 标题只在 Markdown：2.3 设计信条（所有决策的裁判）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：US-1 作为 P1，我在 Claude Code 的 auto mode 下让 Agent 用 bash 批量改了文件，我希望 oops undo 能把这一轮的改动全部撤回，即使官方 /rewind 做不到。
- 需求只在 Markdown：US-2 作为 P1，我希望安装后执行一条 oops init，它自动检测本机装了哪些 Agent，我确认一次就全部接上，全程 30 秒内完成；不想用了，oops init --undo 就能干净地撤掉接入。
- 需求只在 Markdown：US-3 作为 P1，撤销前我想先看到会发生什么：哪些文件恢复、哪些删除、哪些还原，再确认执行。
- 需求只在 Markdown：US-4 作为 P3，Agent 删除了被 .gitignore 忽略的 .env，我希望能找回来。
- 需求只在 Markdown：US-5 作为 P2，我希望 oops list 能显示每一轮是哪个 Agent、什么时间、prompt 摘要、改了几个文件。
- 需求只在 Markdown：US-6 作为 P1，我希望 oops 永远不拖慢 Agent。开不开 oops，我感觉不到区别。
- 需求只在 Markdown：US-7 作为 P1，我在撤销时如果某些文件在这一轮之后被我改过，我希望 oops 不要覆盖它们，并告诉我怎么处理。
- 需求只在 Markdown：US-8 作为 P1，撤销本身出错或者我后悔了，我希望 oops redo 一定能回到撤销前的状态。
- 需求只在 Markdown：US-9 作为 P4，我希望所有命令都支持 --json，非交互环境下行为确定（不会卡在确认提示上）。
- 需求只在 Markdown：US-10 作为 P5 / P8 场景用户，没有 hooks 的 Agent 我也能用 oops run -- <cmd> 或 oops snap 获得保护。
- 需求只在 pptx：版本：v1.0（供开发 agent 实现用） · 日期：2026-10-14 · 状态：可开工 姊妹文档：DESIGN.md（用户旅程、交互原则、技术方案、CLI 命令设计、UI/UX 规范） 技术选型已定：Go + Bubble Tea / Lip Gloss，单二进制 CLI。
- 需求只在 pptx：oops 是所有编程 Agent 共用的撤销键：工作在文件系统层，Agent 用什么方式改的文件、文件有没有进 git，都能撤回。
- 需求只在 pptx：2.3 设计信条（所有决策的裁判）
- 需求只在 pptx：2.4 非目标（明确不做）
- 需求只在 pptx：不替代 git，也不做版本管理或协作。
- 需求只在 pptx：不回滚工作区之外的副作用：数据库、网络请求、全局安装的包、工作区外的文件（v0.2 起会给出警告）。
- 需求只在 pptx：不回滚 Agent 的对话上下文（那是 Agent 自己的事）。v0.2 会在撤销后把"文件已被撤回"这一事实告知 Agent。
- 需求只在 pptx：不做云同步，没有账号体系，默认不收集遥测。
- 需求只在 pptx：MVP 不包含：步骤级（单个工具调用级）撤销、Agent 上下文同步、Web 视图、MCP。（交互式时间线 TUI 已纳入 MVP，见 F12。）
- 需求只在 pptx：5.2 v0.2 — 目标：更细的粒度，更好的体验，口碑传播

### lonnnnnng__fluxdown

段落标题不一致，需求条目 36 / 56 一致（pptx 拆出 36 条）

- 标题只在 Markdown：桌面端 CLI
- 标题只在 Markdown：桌面端 GUI
- 标题只在 Markdown：移动端 App
- 标题只在 Markdown：立即下载
- 标题只在 Markdown：队列下载
- 需求只在 Markdown：detect：识别输入源协议。
- 需求只在 Markdown：support：输出协议运行时支持状态。
- 需求只在 Markdown：doctor：检查内建和外部后端可用性。
- 需求只在 Markdown：download：立即执行单个下载并输出 JSON 摘要。
- 需求只在 Markdown：add、list、start、run、pause、resume、remove：管理本地下载队列。
- 需求只在 Markdown：download 和 add 支持可选 --sha256；配置后下载完成必须校验最终文件，直连下载校验失败返回错误，队列任务校验失败进入 failed。
- 需求只在 Markdown：download、add、start、run 支持 --hls-variant-index（从 0 开始）和 --hls-keep-ts；前两者保存 HLS 任务配置，后两者可在本次执行中指定 variant 或启用 TS 输出。
- 需求只在 Markdown：通过 --store 覆盖默认队列文件路径。
- 需求只在 Markdown：输入下载源、输出目录和可选文件名。
- 需求只在 Markdown：可选输入 SHA-256；配置后下载完成必须校验最终文件，校验失败进入 failed。

### maczh__mgin

段落标题不一致，需求条目 24 / 94 一致（pptx 拆出 42 条）

- 标题只在 Markdown：1.1 已就绪能力（a285b65 已完成，不重复列入待办）
- 标题只在 Markdown：1.2 分类盘点表
- 标题只在 Markdown：1.3 一段话总结
- 标题只在 Markdown：P0（v2.0 必须做，重在理顺骨架）
- 标题只在 Markdown：P1（v2.1 应做，重在能力补齐；本轮建议纳入）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：做什么：脚手架 cmd/scaffold.go 生成的 router/controller/service/dao/model 五层统一收纳到 internal/ 下；在框架内明确 pkg/（对外可导入，如 client、registry、errcode、i18n、health、models）与 internal/（框架内部实现，如 db、mgin、config 内部细节）的边界，并写明各包归属。
- 需求只在 Markdown：mgin new 生成的工程含 internal/router|controller|service|dao|model；旧式顶层平铺工程 go build 仍通过（框架不强依赖 internal/）；
- 需求只在 Markdown：提供一份 pkg/ vs internal/ 包归属表，纳入 README；
- 需求只在 Markdown：go vet ./... 针对脚手架与框架相关包干净。
- 需求只在 Markdown：理由：当前脚手架把五层平铺在顶层（实测 scaffold.go 写 write("router/router.go", ...)），无 internal 边界，随业务增长包耦合失控，域间易越界直连（见 mgin-architecture-options.md §3.6）。
- 需求只在 Markdown：mgin.go 中不再出现逐组件的 if Contains(Used,...) 初始化/关闭链；
- 需求只在 Markdown：新增一个组件只需 Register(plugin) 而不改 Init；
- 需求只在 Markdown：现有 MginPlugin（s3 等）可经适配器平滑升级到新 Plugin 接口，行为不变；
- 需求只在 Markdown：既有 17 个测试用例仍通过（据 a285b65）。
- 需求只在 Markdown：理由：MginPlugin 仅三方法且只 s3 注册（mgin.go:19,38,140 实测），生命周期逻辑散落硬编码，是扩展成本最高的部位。
- 需求只在 pptx：mgin 是"单进程、单 gin.Engine、HTTP+HTTPS 同启"的框架 + 基础设施胶水层。v2 不是重写得像 Spring Cloud，而是在保留全部既有能力的前提下，把散落的职责收拢成清晰的扩展点、标准化契约与可插拔插件体系，并补齐微服务必备能力。a285b65 已把"健康探针 / client.Call 韧性 / HTTPS 优雅关闭"三块短板补齐，本 PRD 的 P0/P1/P2 在它之上继续推进。
- 需求只在 pptx：下列结论均来自对 v2-arch 分支源码的实测（app.go / mgin.go / client/client.go / client/resilience.go / client/breaker.go / registry/registry.go / db/dao/* / config/configure.go / cmd/scaffold.go / health/health.go / go.mod）。函数名、配置项名、接口签名均与源码一致，未编造。
- 需求只在 pptx：1.1 已就绪能力（a285b65 已完成，不重复列入待办）
- 需求只在 pptx：典型迁移案例（旧项目升级到 v2 的 diff 示意）
- 需求只在 pptx：案例 1：存量工程零代码改动，仅启用新能力
- 需求只在 pptx：// main.go（旧）  app := mgin.NewApp("application.yml", "demo", "1.0.0", true)  app.Run()  // main.go（v2，业务代码零改动）  app := mgin.NewApp("application.yml", "demo", "1.0.0", true)+ app.EnableHealth()          // 可选：暴露 /health/live|ready|startup  app.Run()
- 需求只在 pptx：# application.yml（v2 新增，旧键全部保留）go:  framework:    shutdownTimeout: 10       # 框架级；旧 go.application.shutdownTimeout 仍可读取  health:    enabled: true             # 探针开关（v2 新增）  application:                 # 旧键原样保留，向后兼容    name: demo    port: 8080
- 需求只在 pptx：案例 2：新增一个数据源/组件（旧式改 Init，新式注册 Plugin）
- 需求只在 pptx：// 旧式：需要在 mgin.go 的 Init() 里加一整段 if Contains(...) 链（破坏框架）// 新式（v2）：组件自己实现 Plugin 接口并注册，框架 Init 由注册表驱动，无需改框架代码func init() {    mgin.Register(myPlugin{})   // 仅此一行，不改 mgin.go}
- 需求只在 pptx：☐ go vet ./... 干净（针对 v2 新增/修改的包）。

### mapleLeafOfficial__Skillhub

段落标题不一致，需求条目 109 / 119 一致（pptx 拆出 131 条）

- 标题只在 Markdown：背景
- 标题只在 Markdown：业务问题
- 标题只在 Markdown：目标用户
- 标题只在 Markdown：价值主张
- 标题只在 Markdown：核心功能
- 需求只在 Markdown：在技能详情页与审核详情页中新增常驻文件浏览侧边栏。
- 需求只在 Markdown：将现有平铺 files 列表重构为目录树，支持文件夹展开 / 合并。
- 需求只在 Markdown：点击文件节点后，通过弹窗预览文件内容。
- 需求只在 Markdown：支持 Markdown 文档渲染、常见文本文件源码预览，以及大文件 / 不支持文件类型的不可预览提示。
- 需求只在 Markdown：对不可预览文件提供下载入口。
- 需求只在 Markdown：桌面端使用右侧侧边栏布局，移动端将文件浏览区域下沉到主内容区域下方。
- 需求只在 Markdown：按版本浏览文件树与文件预览，并结合权限控制设计访问策略。
- 需求只在 Markdown：侧边栏搜索过滤、最近打开文件、选中文件高亮等增强交互。
- 需求只在 Markdown：对 JSON / YAML / TS / JS 等文本文件提供更完整的语法高亮能力。
- 需求只在 Markdown：超大文本文件受控截断预览，基于服务端预览接口返回结构化元数据。
- 需求只在 pptx：当前技能详情页 space/global/skill-writer 与审核详情区块都提供"概览 / 文件 / 版本"三个 Tab，但文件区域仅展示平铺文件列表，无法在页面内浏览目录层级或直接查看文件内容。
- 需求只在 pptx：技能详情页已经具备按路径读取单个文件内容的能力，可用于 README 加载；审核详情页目前仅返回 files、documentationPath、documentationContent，还不具备按任意文件路径读取正文的能力。
- 需求只在 pptx：用户需要在不下载整个 zip 包的前提下，快速查看 skill 包含的目录结构与具体文件内容，提升详情浏览和审核判断效率。
- 需求只在 pptx：浏览技能详情的普通用户
- 需求只在 pptx：管理技能的作者 / 命名空间成员
- 需求只在 pptx：在审核中心查看技能内容的审核人员与管理员
- 需求只在 pptx：用户交互流程
- 需求只在 pptx：页面布局要求
- 需求只在 pptx：文件预览行为
- 需求只在 pptx：数据与接口需求

### molix-shu__find-seafood

段落标题不一致，需求条目 79 / 84 一致（pptx 拆出 97 条）

- 标题只在 Markdown：3.1 包含
- 标题只在 Markdown：3.2 暂不包含
- 标题只在 Markdown：4.1 普通用户
- 标题只在 Markdown：4.2 内容管理员
- 标题只在 Markdown：5.1 拍照识别熟海鲜流程
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：熟海鲜拍照识别
- 需求只在 Markdown：熟海鲜文字搜索
- 需求只在 Markdown：基础安全提醒
- 需求只在 Markdown：用户点亮餐馆星星
- 需求只在 Markdown：查看某种海鲜对应的推荐餐馆
- 需求只在 pptx：识鲜地图是一款面向普通消费者的熟海鲜识别、食用建议与本地美食地图小程序。
- 需求只在 pptx：5.1 拍照识别熟海鲜流程
- 需求只在 pptx：5.2 文字搜索海鲜流程
- 需求只在 pptx：flowchart TD A[用户进入首页] --> B[输入海鲜名称/别名] B --> C[系统检索海鲜库] C --> D{是否有匹配结果} D -->|精确匹配| E[进入海鲜详情页] D -->|多个相似结果| F[展示搜索结果列表] D -->|无结果| G[提示暂无资料] F --> H[用户选择目标海鲜] H --> E G --> I[引导用户拍照识别或反馈新增] E --> J[查看食用建议] E --> K[查看美食地图]
- 需求只在 pptx：5.3 查看海鲜详情流程
- 需求只在 pptx：flowchart TD A[进入海鲜详情页] --> B[查看基础信息] B --> C[查看可食用部位] C --> D[查看不建议食用部位] D --> E[查看推荐吃法] E --> F[查看剥壳/处理技巧] F --> G[查看安全提醒] G --> H{用户下一步} H -->|想找店| I[进入美食地图] H -->|想推荐| J[添加餐馆推荐] H -->|结束| K[返回首页/历史]
- 需求只在 pptx：详情页信息结构
- 需求只在 pptx：5.4 美食地图查看流程
- 需求只在 pptx：flowchart TD A[进入美食地图] --> B{是否从海鲜详情进入} B -->|是| C[默认筛选当前海鲜] B -->|否| D[展示附近热门点亮] C --> E[加载地图点位] D --> E E --> F[用户点击餐馆点位] F --> G[展示餐馆推荐卡片] G --> H[查看星星数/标签/评价/图片] H --> I{用户操作} I -->|导航去店| J[打开地图导航] I -->|我也点亮| K[进入点亮流程] I -->|切换海鲜| L[更新筛选条件] L --> E
- 需求只在 pptx：5.5 点亮餐馆星星流程

### mufflegyro__dsh-bottom-info-bar

段落标题不一致，需求条目 50 / 50 一致（pptx 拆出 65 条）

- 标题只在 Markdown：FR-1 花费按服务商账户隔离（Bug 修复）
- 标题只在 Markdown：FR-2 余额严格跟随当前服务商（Bug 修复）
- 标题只在 Markdown：FR-3 智谱适配器（GLM Coding Plan 订阅额度，零设置）
- 标题只在 Markdown：FR-4 Kimi 适配器（API 余额，零设置）
- 标题只在 Markdown：FR-5 OpenRouter 适配器（credits 余额，零设置）
- 需求只在 pptx：FR-1 花费按服务商账户隔离（Bug 修复）
- 需求只在 pptx：FR-2 余额严格跟随当前服务商（Bug 修复）
- 需求只在 pptx：FR-3 智谱适配器（GLM Coding Plan 订阅额度，零设置）
- 需求只在 pptx：FR-4 Kimi 适配器（API 余额，零设置）
- 需求只在 pptx：FR-5 OpenRouter 适配器（credits 余额，零设置）
- 需求只在 pptx：FR-6 阶跃星辰适配器（API 余额，零设置）
- 需求只在 pptx：FR-7 未适配服务商优雅降级
- 需求只在 pptx：与 v1.6 合并一次发布（v1.7.0）。原则：只显示官方真实返回的余额/额度/套餐/账单；任何本地估算显示一律不做。
- 需求只在 pptx：FR-8 OpenAI / ChatGPT 订阅卡（真实订阅信息，纯本地）
- 需求只在 pptx：FR-9 小米 MiMo（真实余额 + 套餐额度，零设置）

### openyida__openyida

段落标题不一致，需求条目 0 / 0 一致（pptx 拆出 0 条）

- 标题只在 Markdown：（无标题）
- 标题只在 pptx：第 1 页

### phodal__routa

段落标题不一致，需求条目 0 / 0 一致（pptx 拆出 3 条）

- 标题只在 Markdown：（无标题）
- 标题只在 pptx：第 1 页
- 需求只在 pptx：import type { ExtendedTranslationDictionarySections } from "../types-extended"; import { zhTail } from "./zh-tail";
- 需求只在 pptx：errors: { generic: "出了点问题", saveFailed: "保存失败", loadFailed: "加载失败", deleteFailed: "删除失败", },
- 需求只在 pptx：kanbanBoard: { repos: "仓库", noReposLinked: "未关联仓库。", cards: "张卡片", manualLane: "手动泳道", manualLaneOnly: "仅手动泳道", },

### qtgf520__kai-qt

段落标题不一致，需求条目 98 / 114 一致（pptx 拆出 121 条）

- 标题只在 Markdown：5.1 重新生成消息按钮
- 标题只在 Markdown：5.2 修改消息内容按钮
- 标题只在 Markdown：5.3 复制消息按钮
- 标题只在 Markdown：5.4 删除消息按钮
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 18 页
- 需求只在 Markdown：1. 更改提供商名称 ✅ 已有：renameServiceInstance + displayName 持久化，设置页可编辑，全局生效（v3.2.2 已实现）
- 需求只在 Markdown：2. 思考强度按钮 ✅ 已实现：设置页「思考强度」选择器（默认/低/中低/中/高/最高），写入 reasoning_effort 请求体（v3.2.3+）
- 需求只在 Markdown：3. 流式输出开关 ✅ 已实现：设置页「流式输出」开关，关闭时 stream=false 整体渲染（v3.2.3+）
- 需求只在 Markdown：4. 提示词字数上限 ✅ 已满足：输入框无字符硬截断，文件上限 200KB（20 万字符级），超长内容完整发送
- 需求只在 Markdown：5.1 重新生成 ✅ 已有：BotMessage onRegenerate 按钮，保留上下文重新请求
- 需求只在 Markdown：5.2 修改消息 ✅ 已实现：用户消息下方「编辑」按钮，就地变输入框，保存后截断旧回复并自动重新生成（v3.2.3-3）
- 需求只在 Markdown：5.3 复制消息 ✅ 已有：BotMessage 复制按钮（含代码块复制）
- 需求只在 Markdown：5.4 删除消息 ✅ 已实现：每条消息操作栏「删除」按钮（AI 消息 × 图标 / 用户消息文字），删除单条及其配套工具行，自动保存（v3.2.3-2）
- 需求只在 Markdown：6. 上下文压缩 ✅ 已有：compactHistoryIfNeeded（70% 阈值自动摘要 + 保留最近 4 轮）
- 需求只在 Markdown：7. Skill 功能 ✅ 已有：完整 skills 包（SkillManager/Registry/Marketplaces/前端 SkillsSection）
- 需求只在 pptx：用途：本文件供 AI 编码助手直接阅读并按条目实现。每条需求均含【目标】【位置】【行为】【验收标准】。 项目假设：Kai2 9000 为开源 AI 助手客户端（参考 Kai 9000 架构），前端 UI + 设置层 + Provider/Model 抽象层 + 工具/MCP 层 + 本地推理层。 代码标记约定：[NEED_IMPLEMENT] 表示需 AI 填充实现；[CONFIG_KEY] 表示需新增的设置项 key。
- 需求只在 pptx：5.1 重新生成消息按钮
- 需求只在 pptx：5.2 修改消息内容按钮
- 需求只在 pptx：5.3 复制消息按钮
- 需求只在 pptx：5.4 删除消息按钮
- 需求只在 pptx：使用说明：AI 编码时，请逐条（按编号）实现并在代码/PR 中标注对应编号（如 // [REQ-5.1]），实现完一条即在下方 [进度] 打勾，便于追踪。
- 需求只在 pptx：更改提供商名称 ✅ 已有：renameServiceInstance + displayName 持久化，设置页可编辑，全局生效（v3.2.2 已实现）
- 需求只在 pptx：思考强度按钮 ✅ 已实现：设置页「思考强度」选择器（默认/低/中低/中/高/最高），写入 reasoning_effort 请求体（v3.2.3+）
- 需求只在 pptx：流式输出开关 ✅ 已实现：设置页「流式输出」开关，关闭时 stream=false 整体渲染（v3.2.3+）
- 需求只在 pptx：提示词字数上限 ✅ 已满足：输入框无字符硬截断，文件上限 200KB（20 万字符级），超长内容完整发送

### raceychan__lihil

段落标题不一致，需求条目 75 / 76 一致（pptx 拆出 92 条）

- 标题只在 Markdown：5.1 客户端加入 topic
- 标题只在 Markdown：5.2 客户端发送命令
- 标题只在 Markdown：5.3 服务端推送事件
- 标题只在 Markdown：5.4 断线恢复
- 标题只在 Markdown：5.5 长任务清理
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：字段：ref；类型：string | null；必填：否；说明：若是请求响应，必须回填客户端 ref
- 需求只在 pptx：作为 Web/iOS 客户端，我发送带 ref 的 join 消息后，希望收到带同一个 ref 的明确响应，知道 join 是成功、失败、还是已经加入。
- 需求只在 pptx：5.2 客户端发送命令
- 需求只在 pptx：作为客户端，我发送 send_message、cancel、approve_tool 等命令后，希望服务端响应能和请求配对，而不是只能依赖后续事件流猜测命令是否成功。
- 需求只在 pptx：5.3 服务端推送事件
- 需求只在 pptx：作为业务 channel 作者，我希望在 channel 中启动流式任务后，客户端 leave 或断开连接时，Lihil 自动取消并清理这些任务。
- 需求只在 pptx：{  "topic": "session:abc",  "event": "join",  "payload": {},  "ref": "1",  "join_ref": null}
- 需求只在 pptx：{  "topic": "session:abc",  "event": "reply",  "payload": {    "status": "ok",    "response": {}  },  "ref": "1",  "join_ref": "1",  "event_id": "evt_123",  "seq": 12}
- 需求只在 pptx：字段：ref；类型：string ／ null；必填：否；说明：若是请求响应，必须回填客户端 ref
- 需求只在 pptx：{  "status": "ok",  "response": {}}
- 需求只在 pptx：{  "status": "error",  "error": {    "code": "topic_not_found",    "message": "Topic not found",    "detail": {}  }}

### rzx007__nanobot-ts

段落标题不一致，需求条目 67 / 97 一致（pptx 拆出 74 条）

- 标题只在 Markdown：1.1 产品目标
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 技术选型
- 标题只在 Markdown：1.4 成功指标
- 标题只在 Markdown：2.1 主要用户角色
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：类别：LLM SDK；选择：@ai-sdk (Vercel AI SDK)；理由：统一的提供商接口，支持 OpenAI、Anthropic、OpenRouter 等
- 需求只在 Markdown：需求：在多个聊天应用(WhatsApp, Feishu, Email)上有一个智能助手
- 需求只在 Markdown：场景：快速查询信息、编写代码、执行任务
- 需求只在 Markdown：关键功能：消息路由、工具调用、记忆管理
- 需求只在 Markdown：需求：快速集成 AI 代理到现有应用
- 需求只在 Markdown：场景：添加新的聊天渠道、自定义工具、修改 Agent 行为
- 需求只在 Markdown：关键功能：插件系统、工具 API、事件钩子
- 需求只在 Markdown：需求：研究 AI 代理架构，修改核心逻辑
- 需求只在 Markdown：场景：测试新的提示词策略、实验记忆算法
- 需求只在 Markdown：关键功能：代码可读性、清晰的架构、易于修改
- 需求只在 pptx：版本: 0.1.0 日期: 2026-02-25 作者: Nanobot TypeScript 团队 状态: 进行中
- 需求只在 pptx：// 实现自定义渠道class CustomChannel extends BaseChannel {  async start(): Promise<void> {    // 连接到平台  }  async stop(): Promise<void> {    // 断开连接  }  async send(msg: OutboundMessage): Promise<void> {    // 发送消息到平台  }}// 注册渠道（自动）// ChannelManager 会根据配置自动加载
- 需求只在 pptx：8.2 为什么选择 Pino 作为日志库？
- 需求只在 pptx：8.3 为什么使用 Zod 进行配置验证？
- 需求只在 pptx：8.4 为什么选择 Vitest 作为测试框架？
- 需求只在 pptx：9.1 关键测试用例
- 需求只在 pptx：9.2 测试覆盖率目标

### sameencai__KarvisForYou

段落标题不一致，需求条目 130 / 130 一致（pptx 拆出 174 条）

- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 与 Karvis-opensource 的关系
- 标题只在 Markdown：1.4 核心原则
- 标题只在 Markdown：2.1 角色定义
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 pptx：版本：v1.0 日期：2026-02-15 状态：Draft
- 需求只在 pptx：KarvisForAll 是一个独立项目，从 Karvis-opensource fork 后进行多用户改造。不追求与原版保持同步，而是在原版功能集的基础上做减法和适配。
- 需求只在 pptx：2.2 管理员特有操作
- 需求只在 pptx：2.3 普通用户操作
- 需求只在 pptx：3.1 用户生命周期
- 需求只在 pptx：F1：自动注册与欢迎引导
- 需求只在 pptx：触发条件：一个新的企微用户 ID 首次向 Karvis 发送消息。
- 需求只在 pptx：users/{user_id}/ ├── 00-Inbox/ │   ├── Quick-Notes.md │   ├── Todo.md │   └── .ai-life-state.json ├── 01-Daily/ ├── 02-Notes/ │   ├── 读书笔记/ │   ├── 影视笔记/ │   ├── 情感日记/ │   ├── 工作笔记/ │   ├── 生活趣事/ │   └── 语音日记/ └── _Karvis/ ├── memory/memory.md ├── user_config.json └── logs/decisions.jsonl
- 需求只在 pptx：{  "users": {    "zhangsan": {      "created_at": "2026-02-15T10:30:00+08:00",      "last_active": "2026-02-15T18:45:00+08:00",      "nickname": "小明",      "status": "active",      "message_count_today": 12,      "total_messages": 156    }  }}
- 需求只在 pptx：字段说明： | 字段 | 类型 | 说明 | |---|---|---| | created_at | string | 用户首次消息时间（ISO 8601） | | last_active | string | 最后活跃时间 | | nickname | string | 用户设置的昵称 | | status | string | active / suspended（管理员可控） | | message_count_today | int | 今日已发消息数（UTC+8 零点重置） | | total_messages | int | 累计消息总数 |

### sarahwangy__knowho

段落标题不一致，需求条目 17 / 66 一致（pptx 拆出 94 条）

- 标题只在 Markdown：P0 — 核心层（先做，撑起产品价值）
- 标题只在 Markdown：🟠 EPIC-01：快速添加人
- 标题只在 Markdown：🟠 EPIC-02：个人档案页
- 标题只在 Markdown：🟠 EPIC-03：生日 / 重要日期提醒
- 标题只在 Markdown：🟠 EPIC-04：互动时间线
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 Markdown：从打开到提交 ≤ 30秒（实测）
- 需求只在 Markdown：移动端（375px）一屏内可完成
- 需求只在 Markdown：姓名为唯一必填项，其余可跳过
- 需求只在 Markdown：提交后跳转到该人的档案页
- 需求只在 Markdown：接口返回 201，包含 contact_id
- 需求只在 Markdown：姓名为空时返回 400 + 错误信息
- 需求只在 Markdown：数据落库，可通过 GET /api/contacts/:id 查询
- 需求只在 Markdown：预设标签在新建表单中可直接点选
- 需求只在 Markdown：可新建自定义标签并即时使用
- 需求只在 Markdown：标签列表页可按标签筛选联系人
- 需求只在 pptx：产品名： Knowho定位： 帮助社区里的普通人记住每一个新认识的人——名字、习惯、生日、故事。负责人： Sarah（IT Developer）文档版本： v0.1 草稿日期： 2026-05-31
- 需求只在 pptx："Know who you met. Show up like you remembered."
- 需求只在 pptx：现有 Personal CRM 工具（Clay、Monica、Dex）都面向职场人脉管理，界面复杂、学习成本高。Knowho 专注社区生活圈——读书会、健身群、邻居、社群——帮普通人在30秒内记录一个新认识的人，并在下次见面前自动提醒你"她上次说她女儿在学钢琴"。
- 需求只在 pptx：核心指标（MVP阶段）
- 需求只在 pptx：格式：[KNW-XXX] 编号 · 标题 · 描述 · 验收标准 · 估时
- 需求只在 pptx：P0 — 核心层（先做，撑起产品价值）
- 需求只在 pptx：[KNW-001] 设计"添加联系人"表单 UI
- 需求只在 pptx：☐ 从打开到提交 ≤ 30秒（实测）
- 需求只在 pptx：☐ 移动端（375px）一屏内可完成
- 需求只在 pptx：☐ 姓名为唯一必填项，其余可跳过

### shangbian__Enterprise-Brain-Platform

段落标题不一致，需求条目 23 / 23 一致（pptx 拆出 209 条）

- 标题只在 Markdown：（无标题）
- 标题只在 pptx：第 1 页
- 需求只在 pptx：企业大脑服务平台 需求说明书
- 需求只在 pptx：天云聚合网络科技有限公司 版权所有
- 需求只在 pptx：一、修订记录 版本 日期 修改人 审批人 备注 V1.0.0 2025-04-11 系统 系统 根据输入内容生成初始文档
- 需求只在 pptx：二、适用业务范围 本需求说明书适用于"企业大脑服务平台"的开发与实施。该平台旨在为企业，特别是制造行业的中小企业，提供一套集成的、AI驱动的解决方案，通过连接企业现有数据源（如ERP、MES、IoT设备等），实现数据采集、治理、分析、知识管理和智能应用，最终赋能企业进行数据驱动的决策，提升运营效率、控制风险、沉淀知识。平台重点关注标准化、轻量化、大模型深度应用和弹性商业模式，以应对市场挑战。
- 需求只在 pptx：四、整体业务流程图
- 需求只在 pptx：前台：用户交互界面，包括PC端（浏览器）和移动端（各类办公App），提供知识问答、智能软件、智能问数、办公助手等功能。
- 需求只在 pptx：AI工具中心：提供开发和编排AI应用的核心工具，如提示工厂、思维链编排、Agent开发、算子中心、Workflow、可视化开发。
- 需求只在 pptx：后台：支撑平台运行的基础设施和管理平台，包括知识管理、模型管理、数据管理、用户中心、任务调度、AI能力开放平台。 各层之间通过接口和数据流进行交互，共同构成企业大脑服务。
- 需求只在 pptx：五、需求详细说明
- 需求只在 pptx：5.1 2025年目标与战略 5.1.1需求描述 为应对2025年市场挑战，企业大脑平台确立以"标准化"为核心突破方向，结合技术架构轻量化、大模型深度赋能、弹性商业模式创新，并通过分阶段实施保障战略落地，构建差异化竞争力。 5.1.2业务流程（战略实施步骤）

### shikanon__cookies

段落标题不一致，需求条目 94 / 94 一致（pptx 拆出 107 条）

- 标题只在 Markdown：非目标
- 标题只在 Markdown：系统边界
- 标题只在 Markdown：Project 关联
- 标题只在 Markdown：一级导航
- 标题只在 Markdown：策略工作区内导航
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 需求只在 pptx：对话是主交互，结构化 Brief 和策略是对话逐步形成的可编辑产物，而不是独立表单流程。
- 需求只在 pptx：完整的 L0 至 L3 导航分布、路由与交互规则见 四大模块导航与信息架构；子板块功能、必要性、价值和展示形式见 四大模块子板块分析。本 PRD 维护业务职责。
- 需求只在 pptx：需求与策略是独立垂直系统，路由前缀为 /strategy/*。它拥有需求对话、Brief、研究产物、策略、实验方案和评审记录；只通过 共享基座 使用用户组织、Provider、知识库、Codex/Skills、任务、审批和审计。
- 需求只在 pptx：策略工作区内导航
- 需求只在 pptx：进入一个 StrategyWorkspace 后，二级导航固定为：概览 → 对话 → Brief → 研究 → 策略 → 实验 → 评审 → 变更记录。工作区内切换不跳转到创意、素材或投放页面；跨系统交接通过"发送到创意""创建投放草稿"等明确动作完成。
- 需求只在 pptx：6.1 助手回复结构
- 需求只在 pptx：运行卡展示 Skill 名称、目的、状态、读取的数据范围、产物和错误恢复。涉及外部研究、敏感资料或写操作时，按权限策略先请求授权。
- 需求只在 pptx：状态：待运行 → 运行中 → 等待用户 → 已完成 → 部分完成/失败/已取消。
- 需求只在 pptx：8.1 创意任务级策略
- 需求只在 pptx：任务级策略是已批准通用策略面向一次具体 Creative Route 的可选增强层，不是第二套独立策略，也不能绕过 StrategyPackage 成为新的 Creative 输入根。

### skywind3000__toys

段落标题不一致，需求条目 76 / 76 一致（pptx 拆出 82 条）

- 标题只在 Markdown：输出
- 标题只在 Markdown：请求（仿 PHP 超全局变量命名）
- 标题只在 Markdown：响应
- 标题只在 Markdown：第二期扩展（暂不实现）
- 标题只在 Markdown：说明
- 标题只在 pptx：第 2 页
- 需求只在 pptx：Flask 端向 .mako 模板暴露的函数/对象，设计对标 PHP 的超全局变量与常用函数。命名空间原则：PHP 靠 $ 前缀让变量与函数天然分域，Python 单命名空间没有这层保护，注入名分三类——
- 需求只在 pptx：请求（仿 PHP 超全局变量命名）
- 需求只在 pptx：第二期扩展（暂不实现）
- 需求只在 pptx：注入名作用域（模板编写约定）
- 需求只在 pptx：违反时的失败形态：编译正常通过（注入名是合法标识符），运行时函数被调用才抛 NameError——且若该函数只在特定分支（如 ?debug=1）被调用，平时页面一切正常，极具迷惑性。
- 需求只在 pptx：站点本地模块 import

### staklab__jianji

段落标题不一致，需求条目 306 / 321 一致（pptx 拆出 326 条）

- 标题只在 Markdown：4.1 已有工程基础
- 标题只在 Markdown：4.2 已有 UI 覆盖
- 标题只在 Markdown：4.3 待补齐能力
- 标题只在 Markdown：5.1 访客
- 标题只在 Markdown：5.2 普通用户
- 需求只在 Markdown：路由与页面结构。
- 需求只在 Markdown：用户资料设置。
- 需求只在 Markdown：文档基础创建、编辑、保存。
- 需求只在 Markdown：数据表基础字段和记录。
- 需求只在 Markdown：可查看/可编辑权限。
- 需求只在 Markdown：文档版本记录。
- 需求只在 Markdown：基础实时在线状态。
- 需求只在 Markdown：邮箱账号绑定。
- 需求只在 Markdown：站内提醒和邮件提醒。
- 需求只在 Markdown：完整编辑器工具栏。
- 需求只在 pptx：简记是一个轻量但完整的开源文档协作平台。它不追求完全复刻大型商业套件复杂度，而是参考语雀的知识组织体验、腾讯文档的共享协作体验、现代协作文档的现代编辑体验，以及结构化数据表的数据视图能力，形成适合自托管场景的文档中心。
- 需求只在 pptx：4.1 已有工程基础
- 需求只在 pptx：登录后可创建、编辑、收藏、共享文档，使用数据表、工作台、邮箱、日历和个人设置。
- 需求只在 pptx：拥有文档或空间的最高权限，可管理协作者、设置分享链接、调整用户权限、转移所有权、删除或归档文档。
- 需求只在 pptx：通过邀请链接或指定邮箱加入协作，根据权限可查看或编辑文档，并可在协作界面看到其他协作者的在线状态和编辑进度。
- 需求只在 pptx：可进入管理后台，管理用户、用户组、角色权限、系统邮箱配置、验证码策略、系统审计和部署参数。
- 需求只在 pptx：/login /register /forgot-password /app/dashboard /app/docs /app/docs/:docId /app/tables /app/tables/:tableId /app/mail /app/calendar /app/recent /app/settings /app/profile /admin/users /admin/groups /admin/settings /share/:shareToken
- 需求只在 pptx：工作台应以仪表盘形式展示用户当天最重要的工作，不展示会议纪要、项目计划、个人百科等默认卡片。
- 需求只在 pptx：7.2 文档中心模块
- 需求只在 pptx：文档中心参考语雀的知识库组织方式和腾讯文档/现代协作文档的编辑协作方式。

### superman1006__MeetMind

段落标题不一致，需求条目 37 / 67 一致（pptx 拆出 70 条）

- 标题只在 Markdown：修订记录
- 标题只在 Markdown：1.1 文档目的
- 标题只在 Markdown：1.2 读者对象
- 标题只在 Markdown：1.3 优先级定义
- 标题只在 Markdown：1.4 术语表
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 10 页
- 需求只在 Markdown：没有用户体系：无注册/登录、无权限、所有会话全局共享，无法多人使用。
- 需求只在 Markdown：没有工具治理：Agent 可调用文件读取、进程查看等工具，但无权限策略、无风险分级、无沙箱、无人工审批，存在安全隐患。
- 需求只在 Markdown：容错薄弱：进行中的讨论一旦中断（关闭会话/进程退出）即丢失，无 checkpoint / 恢复 / 重发能力。
- 需求只在 Markdown：编排单一：只有"架构师 + 各 Agent 自主选下一个"一种路由模式，缺少面向不同需求类型的固定工作流。
- 需求只在 Markdown：运维不友好：模型 URL / Key / 名称 / 温度等只能改 .env 重启，无法在前端配置。
- 需求只在 Markdown：能力有缺口：会话标题需手动改、无 todolist、RAG 无 query 改写、不支持文件作为消息输入、无上下文用量与压缩策略。
- 需求只在 Markdown：对用户：把"开一次跨职能需求评审会"压缩成一次对话，几分钟内得到结构化结论 + 分工待办。
- 需求只在 Markdown：对团队：每个 Agent 绑定本职知识库与工具，输出贴合角色、可直接落地。
- 需求只在 Markdown：对平台：可扩展的工具 / 工作流 / 知识库体系，使其能从需求评审扩展到更多协作场景。
- 需求只在 Markdown：M1 用户与账户体系：FR-M1-01 ~ FR-M1-05
- 需求只在 pptx：多 Agent RAG 协作会议系统 · Product Requirements Document
- 需求只在 pptx：如果你是第一次看产品文档，先读这一节。下面是本文里反复出现的几类"代号"分别代表什么、怎么读。
- 需求只在 pptx：一句话记忆：P 看多重要、M 看属于哪个模块、FR-Mx-NN 是某条需求的身份证号、R 看第几批做、G 是目标。
- 需求只在 pptx：产品经理、前后端研发、测试、架构师、项目管理。
- 需求只在 pptx：3.2 关键成功指标（北极星 & 辅助指标）
- 需求只在 pptx：4.2 核心使用场景
- 需求只在 pptx：需求评审（主场景）：PM 抛出一个产品需求，5 个 Agent 从架构、前后端、测试、产品角度讨论，产出方案与分工。
- 需求只在 pptx：技术方案讨论：架构师主导，针对一个技术问题组织多角色评估。
- 需求只在 pptx：快速问答：用户只是简单提问，架构师一句话回答并结束（已支持的"反喧宾夺主 / 一句话结束"逻辑）。
- 需求只在 pptx：带资料的讨论：用户上传 PRD/设计稿/文档（md/pdf/word/txt），Agent 基于文件内容讨论（待实现）。

### terryso__ccpet

段落标题不一致，需求条目 40 / 44 一致（pptx 拆出 60 条）

- 标题只在 Markdown：版本: 0.1
- 标题只在 Markdown：目标 (Goals)
- 标题只在 Markdown：背景 (Background Context)
- 标题只在 Markdown：变更日志 (Change Log)
- 标题只在 Markdown：功能性需求 (Functional Requirements)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：界面应当是环境式 (ambient) 的、令人愉悦的、且几乎无形的。它应该感觉像是 IDE 原生的一部分，而不是一个外挂。用户只需一瞥，就能理解宠物的状态，无需主动投入注意力。
- 需求只在 Markdown：主要交互 (Passive): 核心交互是被动的。宠物对用户的编码活动做出反应，用户无需进行任何直接点击或操作。
- 需求只在 Markdown：次要交互 (Command-based): 唯一的主动操作是通过 IDE 的命令面板执行的（例如，"领养新宠物"），MVP 阶段不设任何图形化配置界面。
- 需求只在 Markdown：建议: 我们应确保状态栏的文本对屏幕阅读器是友好的（例如，可以读出"宠物状态：开心，能量值85%"）。ASCII 字符本身应选择高对比度的样式。
- 需求只在 pptx：功能性需求 (Functional Requirements)
- 需求只在 pptx：非功能性需求 (Non-Functional Requirements)
- 需求只在 pptx：本项目将采用单一代码仓库 (Polyrepo) 的形式。由于这是一个独立的 IDE 扩展，因此无需复杂的 Monorepo 结构。
- 需求只在 pptx：采用纯本地化/无服务器 (Serverless) 架构。所有应用逻辑、计算和数据存储均在用户本地的客户端（IDE扩展环境）中完成，不依赖任何远程后端服务器。
- 需求只在 pptx：测试策略应至少覆盖单元测试和集成测试 (Unit + Integration)。单元测试用于验证核心逻辑（如能量条算法），集成测试用于验证扩展与模拟的 Claude Code API 之间的交互。
- 需求只在 pptx：史诗 1: MVP - 核心宠物体验 (Epic 1: MVP - Core Pet Experience)
- 需求只在 pptx：目标: 建立并发布一个功能完整的状态栏宠物 MVP，包含其核心的能量条生命周期和与用户编码活动的互动机制，以验证产品的核心吸引力。
- 需求只在 pptx：史诗 1: MVP - 核心宠物体验 (Epic 1: MVP - Core Pet Experience)
- 需求只在 pptx：史诗目标 (Epic Goal): 这个史诗将交付一个完整的、端到端的用户体验。它涵盖了从扩展的初始设置、能量条的核心逻辑、所有宠物状态的转换，到最终的重生循环。完成这个史诗后，产品将准备好进行首次用户验证。
- 需求只在 pptx：Story 1.1: 宠物的首次亮相 (Pet's First Appearance)

### terryso__mcp-pinterest

段落标题不一致，需求条目 96 / 96 一致（pptx 拆出 128 条）

- 标题只在 Markdown：Epic-1: MVP Core Functionality (v0.1)
- 标题只在 Markdown：Epic-2: Server Configuration Enhancements
- 标题只在 Markdown：Epic-N: Future Enhancements (Beyond Scope of v0.1/v0.2)
- 标题只在 Markdown：1.1 项目目标
- 标题只在 Markdown：1.2 范围
- 标题只在 pptx：第 2 页
- 需求只在 pptx：Epic-1: MVP Core Functionality (v0.1)
- 需求只在 pptx：此 Epic 包含了实现 Pinterest MCP 服务器基本搜索和下载功能的初始用户故事。
- 需求只在 pptx：Epic-2: Server Configuration Enhancements
- 需求只在 pptx：此 Epic 专注于提高服务器的可配置性，例如下载目录和文件名。
- 需求只在 pptx：Epic-N: Future Enhancements (Beyond Scope of v0.1/v0.2)
- 需求只在 pptx：包括 Pinterest 认证、更丰富的搜索、下载前确认、异步处理等未来可能的功能。
- 需求只在 pptx：(当前版本主要是 Tool 的输入输出定义，已在用户故事中描述)
- 需求只在 pptx：(基于 architecture.md 描述的主要组件)
- 需求只在 pptx：本项目旨在开发一个遵循模型上下文协议 (Model Context Protocol, MCP) 的服务器。该服务器的核心功能是提供与 Pinterest 平台交互的能力，允许 MCP 客户端（如 IDE、AI 助手等）通过标准化的接口搜索 Pinterest 图片，获取图片信息，并将图片下载到指定位置。
- 需求只在 pptx：当前版本 (v0.1) 的范围聚焦于实现基本的 Pinterest 图片搜索和下载功能，无需用户认证。

### terryso__tv-recommender-mcp-server

段落标题不一致，需求条目 88 / 88 一致（pptx 拆出 110 条）

- 标题只在 Markdown：Epic-1: 核心推荐工具 MVP
- 标题只在 Markdown：Epic-2: 增强与扩展 (Future Enhancement)
- 标题只在 Markdown：Epic-3: 个性化与集成 (Future Enhancement)
- 标题只在 Markdown：Epic-4: 可视化与探索 (Future Enhancement)
- 标题只在 Markdown：Potential Tool Response Structure (Conceptual)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 17 页
- 需求只在 pptx：Epic-1: 核心推荐工具 MVP
- 需求只在 pptx：(包含 MVP 范围内的所有核心功能和故事)
- 需求只在 pptx：Epic-2: 增强与扩展 (Future Enhancement)
- 需求只在 pptx：Epic-3: 个性化与集成 (Future Enhancement)
- 需求只在 pptx：(包含连接 Trakt.tv、智能追剧进度管理等用户个性化功能)
- 需求只在 pptx：Epic-4: 可视化与探索 (Future Enhancement)
- 需求只在 pptx：(包含系列/宇宙可视化等)
- 需求只在 pptx：{ Mermaid Diagrams, visual aids, citations, external URLs - Placeholder }
- 需求只在 pptx：{ Key data structures returned by tools or used internally - Placeholder }
- 需求只在 pptx：{ Diagram the folder and file organization structure - Placeholder }

### tyrchen__index-tts-rs

段落标题不一致，需求条目 35 / 40 一致（pptx 拆出 49 条）

- 标题只在 Markdown：1.1 双核产品形态
- 标题只在 Markdown：FR-1：两阶段解耦与 .itts_voice 音色包管理（Voice Snapshot System）
- 标题只在 Markdown：FR-2：多语种文本前端与精细发音控制（Multilingual Frontend）
- 标题只在 Markdown：FR-3：高性能合成与流式音频输出（Synthesis & Streaming）
- 标题只在 Markdown：FR-4：Rust Library Crate (index-tts-rs-core) 集成体验
- 标题只在 pptx：第 6 页
- 需求只在 Markdown：指标项：Daemon 热态请求响应开销；原版 Python index-tts-2.5-mlx：不支持（每次重跑进程）；index-tts-rs 目标值：$\le$ 5 ms；核心实现手段：Unix Domain Socket + 内存常驻 DashMap 音色池
- 需求只在 Markdown：DSP 特征（mel_spectrogram、campplus_fbank、w2v_features）：余弦相似度 $\ge 0.9999$，最大绝对误差 $< 10^{-4}$。
- 需求只在 Markdown：SpeakerContext 各张量：余弦相似度 $\ge 0.9995$。
- 需求只在 Markdown：Greedy GPT 生成的 Semantic Codes：100% 序列一致（或在浮点边界步重合率 $\ge 99\%$）。
- 需求只在 Markdown：CFM Mel 频谱（给定相同初始噪声 z）与 BigVGAN 输出波形：余弦相似度 $\ge 0.999$，听感完全无退化、无拼接爆音。
- 需求只在 pptx：1.1 双核产品形态
- 需求只在 pptx：FR-1：两阶段解耦与 .itts_voice 音色包管理（Voice Snapshot System）
- 需求只在 pptx：FR-2：多语种文本前端与精细发音控制（Multilingual Frontend）
- 需求只在 pptx：FR-3：高性能合成与流式音频输出（Synthesis & Streaming）
- 需求只在 pptx：FR-4：Rust Library Crate (index-tts-rs-core) 集成体验
- 需求只在 pptx：FR-5：面向 AI Agent 的 CLI、常驻 Daemon 与 MCP Server
- 需求只在 pptx：4.1 性能与资源指标（以 Apple Silicon M2/M3/M4 Max/Pro MBP 为基准）
- 需求只在 pptx：指标项：Daemon 热态请求响应开销；原版 Python index-tts-2.5-mlx：不支持（每次重跑进程）；index-tts-rs 目标值：5 ms；核心实现手段：Unix Domain Socket + 内存常驻 DashMap 音色池
- 需求只在 pptx：4.2 数值精度与音质验收标准
- 需求只在 pptx：DSP 特征（mel_spectrogram、campplus_fbank、w2v_features）：余弦相似度 ，最大绝对误差 。

### tyxben__AI_novel

段落标题不一致，需求条目 140 / 168 一致（pptx 拆出 166 条）

- 标题只在 Markdown：1.1 现状
- 标题只在 Markdown：1.2 问题
- 标题只在 Markdown：1.3 新策略
- 标题只在 Markdown：US-1: 快速预览生成结果
- 标题只在 Markdown：US-2: 编辑布局后实时反馈
- 需求只在 Markdown：9 阶段流水线：文档分析 → 内容提取 → 内容增强 → 演示计划 → 大纲生成 → 内容创作 → 设计编排 → 配图生成 → PPT 渲染
- 需求只在 Markdown：40+ Pydantic 数据模型（SlideSpec / SlideContent / SlideDesign / ColorScheme / FontSpec / DecorationSpec 等）
- 需求只在 Markdown：5 个视觉主题（modern / business / creative / tech / education）
- 需求只在 Markdown：12 种布局类型（title_hero / section_divider / text_left_image_right / data_highlight / timeline / comparison 等）
- 需求只在 Markdown：任务队列集成（_run_ppt_outline / _run_ppt_continue）
- 需求只在 Markdown：Web UI 有 PPT Tab（但按钮禁用中）
- 需求只在 Markdown：布局调整困难，需要手动计算每个元素的 left / top / width / height
- 需求只在 Markdown：预览困难：用户无法在生成前看到最终效果
- 需求只在 Markdown：调试成本高：每次调整都需要重新生成完整 .pptx 文件
- 需求只在 Markdown：装饰元素（渐变 / 形状 / 分割线）实现复杂
- 需求只在 pptx：US-1: 快速预览生成结果
- 需求只在 pptx：作为 PPT 创作者 我想要 在生成 PPTX 之前先预览 HTML 版幻灯片 以便于 快速确认内容和布局是否符合预期，无需等待完整渲染
- 需求只在 pptx：US-2: 编辑布局后实时反馈
- 需求只在 pptx：作为 PPT 创作者 我想要 修改大纲中的布局类型后立即看到效果 以便于 快速迭代设计方案
- 需求只在 pptx：作为 PPT 创作者 我想要 将确认后的 HTML 幻灯片导出为 .pptx 文件 以便于 在 PowerPoint / Keynote 中演示或进一步编辑
- 需求只在 pptx：作为 PPT 创作者 我想要 所有页面自动应用统一的主题风格 以便于 保持视觉专业性和一致性
- 需求只在 pptx：FR-1: HTML 幻灯片渲染器
- 需求只在 pptx：描述：新建 src/ppt/html_renderer.py，替换现有 ppt_renderer.py 的职责。
- 需求只在 pptx：描述：新建 src/ppt/html_to_pptx.py，将 HTML 幻灯片转换为 PPTX 文件。
- 需求只在 pptx：描述：新建 src/ppt/image_agent.py，为幻灯片自动搜索或生成配图。

### weiwei929__wireguard_plus

段落标题不一致，需求条目 79 / 102 一致（pptx 拆出 107 条）

- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 项目愿景
- 标题只在 Markdown：2.1 目标用户
- 标题只在 Markdown：2.2 用户痛点
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：每种伪装模式能够正常转换WireGuard流量
- 需求只在 Markdown：伪装后的流量能够绕过基本的DPI检测
- 需求只在 Markdown：支持动态切换伪装模式
- 需求只在 Markdown：性能损失控制在30%以内
- 需求只在 Markdown：界面响应式设计，支持桌面和移动端
- 需求只在 Markdown：操作流程直观，新用户5分钟内能创建隧道
- 需求只在 Markdown：配置文件生成正确，客户端能正常连接
- 需求只在 Markdown：实时数据更新延迟不超过5秒
- 需求只在 Markdown：密钥生成符合WireGuard安全标准
- 需求只在 Markdown：IP地址分配无冲突
- 需求只在 pptx：个人用户: 需要绕过网络限制的隐私保护用户
- 需求只在 pptx：开发者: 需要学习网络工具开发的技术人员
- 需求只在 pptx：系统管理员: 需要为组织部署VPN服务的IT人员
- 需求只在 pptx：开源贡献者: 希望参与网络安全工具开发的社区成员
- 需求只在 pptx：3.1.1 流量伪装引擎
- 需求只在 pptx：功能描述: 提供多种WireGuard流量伪装技术的统一接口
- 需求只在 pptx：☐ 每种伪装模式能够正常转换WireGuard流量
- 需求只在 pptx：☐ 伪装后的流量能够绕过基本的DPI检测
- 需求只在 pptx：☐ 支持动态切换伪装模式
- 需求只在 pptx：☐ 性能损失控制在30%以内

### wgcairui__airplay-receiver

段落标题不一致，需求条目 97 / 209 一致（pptx 拆出 164 条）

- 标题只在 Markdown：产品名称
- 标题只在 Markdown：产品愿景
- 标题只在 Markdown：目标用户
- 标题只在 Markdown：主要目标
- 标题只在 Markdown：关键指标
- 标题只在 pptx：第 13 页
- 需求只在 Markdown：视频质量支持最高3392×2400@144Hz
- 需求只在 Markdown：应用启动时间 < 3秒
- 需求只在 Markdown：电池续航影响 < 15%/小时
- 需求只在 Markdown：背景: 软件工程师，经常需要多屏调试代码
- 需求只在 Markdown：需求: 将MacBook代码扩展到平板，提高开发效率
- 需求只在 Markdown：痛点: 外接显示器不便携，咖啡厅无法使用双屏
- 需求只在 Markdown：背景: UI/UX设计师，使用Mac进行设计工作
- 需求只在 Markdown：需求: 平板作为第二屏显示参考素材或预览效果
- 需求只在 Markdown：痛点: 需要大屏预览设计稿，iPad连接复杂
- 需求只在 Markdown：背景: 经常出差开会，需要展示PPT和数据
- 需求只在 pptx：1. AirPlay服务发现与连接
- 需求只在 pptx：功能描述: 自动发现并连接Mac设备的AirPlay请求
- 需求只在 pptx：☐ Mac能在AirPlay列表中发现OPPO Pad
- 需求只在 pptx：☐ 连接成功率>95%（同一网络环境下）
- 需求只在 pptx：☐ 支持自动连接，无需额外验证步骤
- 需求只在 pptx：☐ 支持记住已配对设备，后续快速连接
- 需求只在 pptx：2. 视频流接收与渲染
- 需求只在 pptx：功能描述: 接收并显示Mac传输的视频流
- 需求只在 pptx：☐ 支持1080p、4K分辨率切换
- 需求只在 pptx：☐ 延迟控制在50ms以内

### wordflowlab__novel-writer-openspec

段落标题不一致，需求条目 36 / 68 一致（pptx 拆出 112 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心价值主张
- 标题只在 Markdown：1. 清晰的上下文管理
- 标题只在 Markdown：2. 严格的规格格式
- 标题只在 Markdown：3. 自动化验证机制
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 13 页
- 标题只在 pptx：第 14 页
- 需求只在 Markdown：借鉴理念：specs/（真相）+ changes/（提案）的双轨制结构
- 需求只在 Markdown：独立工具：使用 novelspec 命令，独立命名空间，避免与 OpenSpec 冲突
- 需求只在 Markdown：定制化：针对小说创作优化规格格式、验证规则和工作流
- 需求只在 Markdown：novelspec/specs/ 存储已确定的设定（角色、世界观、大纲）
- 需求只在 Markdown：novelspec/changes/ 管理待创作的章节和设定变更
- 需求只在 Markdown：AI 明确知道"当前真相"和"工作任务"
- 需求只在 Markdown：使用 Requirements + Scenarios 格式，让规格可验证
- 需求只在 Markdown：SHALL/MUST 关键词明确约束强度
- 需求只在 Markdown：ADDED/MODIFIED/REMOVED 清晰管理设定演进
- 需求只在 Markdown：novelspec validate 自动检查一致性
- 需求只在 pptx：版本：1.0日期：2025-01-22状态：Draft
- 需求只在 pptx：本文档定义 Novel-Writer-OpenSpec 产品的核心需求和技术规格。该产品借鉴 OpenSpec 方法论，将 specs/（真相）+ changes/（提案）的双轨结构应用于小说创作领域，通过结构化管理和自动化验证提升 AI 辅助创作的效率和质量。
- 需求只在 pptx：2.1 目录结构设计
- 需求只在 pptx：独立命名空间：使用 novelspec/ 而非 openspec/，避免冲突
- 需求只在 pptx：无 constitution：创作原则整合到 project.md，而非单独 spec（OpenSpec 没有 constitution 概念）
- 需求只在 pptx：清晰分离：specs/（真相）和 changes/（提案）严格分离
- 需求只在 pptx：结构化归档：archive/ 保留完整历史和变更意图
- 需求只在 pptx：2.2 规格文件格式
- 需求只在 pptx：2.3 工作流程设计
- 需求只在 pptx：Stage 1: 创建变更提案（详细示例）

### wordflowlab__novel-writer

段落标题不一致，需求条目 81 / 115 一致（pptx 拆出 138 条）

- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 核心价值
- 标题只在 Markdown：1.5 开发方法论
- 标题只在 pptx：第 14 页
- 标题只在 pptx：第 15 页
- 需求只在 Markdown：参考 Spec-Kit 方法论的 AI 智能小说创作平台，采用规格驱动创作(Spec-Driven Writing)的理念，通过结构化的工作流程（风格设定→故事大纲→章节规划→任务分解→内容创作）来组织小说项目的创建和管理。专注于为中文内容创作者提供智能化的小说写作辅助能力，支持多种文体风格、角色管理、世界观构建等功能。
- 需求只在 Markdown：降低创作门槛：通过 AI 辅助简化创作流程，帮助新手快速上手
- 需求只在 Markdown：提升写作效率：结构化管理，避免写作瓶颈和剧情混乱
- 需求只在 Markdown：保证内容质量：AI 智能建议，保持风格一致性和逻辑连贯性
- 需求只在 Markdown：激发创作灵感：提供创意建议，突破思维定式
- 需求只在 Markdown：版本管理便捷：Git 集成，轻松管理创作版本
- 需求只在 Markdown：规格优先：先定义创作风格和故事框架，再进行具体写作
- 需求只在 Markdown：分阶段执行：遵循 style → story → outline → chapters → write 的渐进式流程
- 需求只在 Markdown：模板驱动：使用标准化模板确保创作的一致性
- 需求只在 Markdown：AI 增强：每个阶段都有 AI 智能辅助，提升创作质量
- 需求只在 pptx：2.0 工作流命令（参考 Spec-Kit 方法论）
- 需求只在 pptx：Novel Writer 提供两类命令：工作流命令和 CLI 工具命令。
- 需求只在 pptx：2.1 创作风格设定（/constitution）
- 需求只在 pptx：设定小说的整体创作风格和准则，建立创作的基本原则，贯穿整个作品。
- 需求只在 pptx：输入参数:  - style_type: 文体风格（网文/文学/轻小说）  - narrative: 叙事视角  - tone: 文字基调  - principles: 创作原则列表输出格式:  - 生成 .specify/memory/writing-constitution.md  - 包含完整的风格规范文档
- 需求只在 pptx：2.2 故事大纲创建（/specify）
- 需求只在 pptx：创建完整的故事设定，包括主题、角色、世界观等核心要素。
- 需求只在 pptx：输入参数:  - description: 故事描述  - genre: 类型（科幻/奇幻/现实/历史等）  - length: 预计字数输出格式:  - 创建 stories/[编号-名称]/specify.md  - 使用 story-template.md 模板  - 自动生成带编号的目录结构
- 需求只在 pptx：将故事大纲细化为具体的章节结构，制定详细的创作计划。
- 需求只在 pptx：输入参数:  - total_chapters: 总章节数  - volume_structure: 卷册结构  - pacing_plan: 节奏规划输出格式:  - 生成 stories/[编号]/plan.md  - 包含详细的章节大纲  - 动态卷册管理（不限制固定卷数）

### wth461694678__text-block-timer

段落标题不一致，需求条目 74 / 75 一致（pptx 拆出 97 条）

- 标题只在 Markdown：1.1 需求来源
- 标题只在 Markdown：1.2 核心痛点
- 标题只在 Markdown：1.3 目标
- 标题只在 Markdown：3.1 In Scope（核心计时器功能）
- 标题只在 Markdown：3.2 Out of Scope（其他功能，已单独建文档）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：Obsidian 用户在日常笔记中记录任务、会议、学习等活动，需要一种轻量级、零侵入的方式来追踪各项活动的耗时。现有的计时工具要么是独立应用（需要在 Obsidian 外操作），要么使用独立数据库（数据与笔记割裂）。用户希望计时数据直接嵌入笔记文本，随笔记一同迁移、版本控制。
- 需求只在 pptx：文档版本: v1.0 | 创建日期: 2026-03-02 | 状态: 补充归档 | 优先级: P0
- 需求只在 pptx：本文档为已上线功能的补充归档 PRD，描述 Text Block Timer 插件的核心计时器功能——即 Sidebar 和 Delete Enhancement 之外的所有功能。
- 需求只在 pptx：零侵入计时：计时器以 HTML span 形式内嵌 Markdown，不影响笔记的纯文本可读性
- 需求只在 pptx：多触发方式：支持命令面板（快捷键）、右键菜单、Checkbox 状态联动三种触发方式
- 需求只在 pptx：实时显示：运行中计时器每秒更新时长，编辑器内直观可见
- 需求只在 pptx：三层持久化：Markdown HTML span ↔ JSON 数据库 ↔ IndexedDB，三层数据保持一致
- 需求只在 pptx：崩溃安全：Obsidian 异常退出后，下次启动自动恢复/结算运行中计时器
- 需求只在 pptx：跨天支持：运行中计时器跨越午夜时自动拆分日统计
- 需求只在 pptx：高度可配：插入位置、时间格式、显示样式、颜色、图标等均可自定义
- 需求只在 pptx：国际化：支持 en/zh/zhTW/ja/ko 五种语言

### wukun2005-gif__patentExaminator

段落标题不一致，需求条目 118 / 128 一致（pptx 拆出 212 条）

- 标题只在 Markdown：B-008 产品方向基线
- 标题只在 Markdown：v0.1.0 功能矩阵
- 标题只在 Markdown：2.1 审查员的典型痛点
- 标题只在 Markdown：2.2 AI 介入的机会点
- 标题只在 Markdown：2.3 产品边界声明
- 标题只在 pptx：第 3 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 10 页
- 标题只在 pptx：第 11 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：文档阅读与摘要：AI 可以快速提取申请文件的技术方案要素、权利要求结构、声称的技术效果。
- 需求只在 Markdown：AI 交互式解读：审查员上传完整申请文件后，AI 以对话方式帮助其快速理解专利——用通俗语言解释技术方案、梳理发明要点、指出关键创新之处。审查员可随时追问（"这个技术方案的核心创新在哪里？""这段描述是否清楚？"），AI 在对话上下文中持续解答。这是审查员"舒了好大一口气"的核心体验——不是结构化拆解，而是理解。
- 需求只在 Markdown：特征拆解：AI 可以按三步法框架输出结构化的 claim chart，并标注说明书出处。
- 需求只在 Markdown：文献对照：AI 可以将权利要求技术特征与用户上传的对比文件逐项比对，标注公开状态和引用出处，并识别区别特征候选。
- 需求只在 Markdown：时间轴自动校验：AI 可以自动核查每篇对比文件的公开日与申请日/优先权日的先后关系，过滤不可用文件。
- 需求只在 Markdown：OCR 解析：对扫描版 PDF 申请文件先做 OCR 再解析，避免审查员手动转换格式。
- 需求只在 Markdown：不接入任何内部检索系统，对比文件由审查员自行检索后上传。
- 需求只在 Markdown：不替代发文系统、OA 格式、法条引用、正式三步法论证，APP 产出是审查员起草 OA 的素材。
- 需求只在 Markdown：不作出新颖性、创造性、授权或驳回的法律结论，所有候选判断均须审查员确认。
- 需求只在 Markdown：~~反馈系统~~：已删除（用户要求），满意度评估改为 Metrics 体系自动指标（Groundedness、Faithfulness 等）
- 需求只在 pptx：B-008 产品方向基线
- 需求只在 pptx：复审文件导入 → 审查意见解析（opinion-analysis） → 答辩理由映射（argument-analysis） → Claim Chart（以修改后权利要求为准） → 新颖性复核 / 创造性复核 / 缺陷复查 → 复审意见草稿（reexam-draft） → 导出
- 需求只在 pptx：原初审式"从零生成审查意见素材"不属于当前版本范围；保留的 Claim Chart、新颖性、创造性和文献管理能力均作为复审回应链路的上游事实材料。
- 需求只在 pptx：本节描述一位审查员从打开工具到获得有用输出的完整理想流程，帮助理解产品体验目标。
- 需求只在 pptx：背景： 审查员手上有一件电子领域发明专利申请（扫描 PDF 格式），以及从检索系统检索到的两篇对比文件（一篇专利、一篇期刊论文）。想在开会前 30 分钟内整理出权利要求技术特征和初步文献对照结果。
- 需求只在 pptx：Step 1 — 打开工具 审查员在浏览器里输入内网地址，工具秒开。顶部显示"演示模式"横幅，她点击切换为"真实模式"，弹出安全提示，她确认 API Key 已配置，点击继续。
- 需求只在 pptx：Step 2 — 新建案件 点击"新建案件"，填写申请号、发明名称、申请日（关键）。工具提示"是否主张优先权"，她选否。
- 需求只在 pptx：Step 3 — 上传申请文件（扫描 PDF） 她直接把扫描版 PDF 拖入上传区。工具检测到无文字层，自动启动 OCR，进度条显示"正在识别文字内容..."（约 15–30 秒，基于现代硬件）。OCR 完成后提示"已识别 XX 页，请确认文字质量"，她快速扫了一眼，点击确认。
- 需求只在 pptx：Step 3.5 — AI 解读申请文件（核心体验） 她点击"解读此专利"。APP 弹出发送确认框，她确认后约 15 秒，AI 返回一份通俗易懂的专利解读：技术方案概述、发明要解决的问题、关键技术手段、独立权利要求的核心保护范围。她读完后追问："这个技术方案和现有技术相比的创新点主要在哪？"AI 在对话上下文中给出分析。她心里有了底，继续下一步。这个环节是审查员"舒了好大一口气"的关键——先理解，再拆解。
- 需求只在 pptx：Step 4 — 上传对比文件 她点击"选择文件夹"，授权 APP 访问她的检索结果文件夹，两篇文件自动导入。APP 提取两篇文件的公开日，自动完成时间轴校验：一篇通过（绿色 ✅），一篇公开日与申请日同日（橙色 ⚠️ 标注"同日公开·不可用于新颖性评价"）。

### xgwangdl__wikiknowledge

段落标题不一致，需求条目 95 / 95 一致（pptx 拆出 107 条）

- 标题只在 Markdown：2.1 本期做
- 标题只在 Markdown：2.2 本期不做
- 标题只在 Markdown：FR-01 注册与登录（P0）
- 标题只在 Markdown：FR-02 知识库管理（P0）
- 标题只在 Markdown：FR-03 文档上传与异步解析（P0）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 需求只在 pptx：文档解析 -> 切片 -> 向量化 -> 入库检索 -> 提示词组装 -> 流式回答 -> 引用来源 -> 反馈 -> 评估
- 需求只在 pptx：权限建议用简单的 ROLE_USER / ROLE_ADMIN，通过 JWT 携带角色，接口用注解或拦截器校验。
- 需求只在 pptx：FR-03 文档上传与异步解析（P0）
- 需求只在 pptx：FR-04 切片与向量化策略（P0）
- 需求只在 pptx：FR-12 可观测性与运维（P1）
- 需求只在 pptx：graph TB FE[Vue 3 前端] --> API[REST / SSE API] API --> AUTH[认证与限流] AUTH --> SVC[业务服务层] SVC --> RAG[RAG 服务] SVC --> KB[知识库/文档服务] SVC --> CHAT[会话服务] RAG --> VS[(pgvector)] RAG --> LLM[Spring AI ChatModel] RAG --> REDIS[(Redis 缓存/限流)] KB --> QUEUE[异步任务] QUEUE --> VS QUEUE --> DB[(PostgreSQL)]
- 需求只在 pptx：POST /api/auth/register POST /api/auth/login POST /api/auth/refresh
- 需求只在 pptx：知识库与文档
- 需求只在 pptx：GET    /api/knowledge-bases POST   /api/knowledge-bases GET    /api/knowledge-bases/{id} PUT    /api/knowledge-bases/{id} DELETE /api/knowledge-bases/{id}
- 需求只在 pptx：GET    /api/sessions POST   /api/sessions GET    /api/sessions/{id}/messages DELETE /api/sessions/{id}

### xi-lie5__Story-Platform

段落标题不一致，需求条目 159 / 164 一致（pptx 拆出 174 条）

- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 核心价值
- 标题只在 Markdown：2.1 普通用户
- 标题只在 Markdown：2.2 管理员
- 需求只在 Markdown：StoryForge是一个基于AI技术的交互式故事创作与阅读平台，允许用户创建、编辑、发布和阅读具有多分支结局的互动故事。
- 需求只在 Markdown：AI辅助创作：利用AI技术辅助用户进行故事创作
- 需求只在 Markdown：多分支叙事：支持创建具有多个选择分支和结局的互动故事
- 需求只在 Markdown：社区分享：用户可以发布作品供其他用户阅读和体验
- 需求只在 Markdown：可视化编辑：提供直观的故事节点图谱编辑工具
- 需求只在 pptx：3.1 用户认证模块
- 需求只在 pptx：3.3 故事浏览模块
- 需求只在 pptx：3.4 故事阅读模块
- 需求只在 pptx：3.5 故事创作模块
- 需求只在 pptx：3.5.1 故事创建工具
- 需求只在 pptx：3.6 作品管理模块
- 需求只在 pptx：3.7 个人中心模块
- 需求只在 pptx：3.8.1 管理员控制台
- 需求只在 pptx：所有页面通用
- 需求只在 pptx：4.2 认证状态管理

### xiaodong-l__amazon-1688-selector

段落标题不一致，需求条目 6 / 88 一致（pptx 拆出 108 条）

- 标题只在 Markdown：版本名称
- 标题只在 Markdown：版本目标
- 标题只在 Markdown：核心价值
- 标题只在 Markdown：FR-001: 数据库集成
- 标题只在 Markdown：需求描述
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 Markdown：数据持久化 - 从 CSV 文件升级为数据库存储
- 需求只在 Markdown：历史追踪 - 记录商品数据变化历史
- 需求只在 Markdown：趋势对比 - 支持周/月/季度数据对比分析
- 需求只在 Markdown：查询优化 - 支持复杂查询和数据导出
- 需求只在 Markdown：支持 SQLite (默认，零配置)
- 需求只在 Markdown：支持 PostgreSQL (生产环境)
- 需求只在 Markdown：通过配置切换数据库类型
- 需求只在 Markdown：数据库连接池管理
- 需求只在 Markdown：定义数据模型类
- 需求只在 Markdown：支持异步操作 (asyncpg)
- 需求只在 pptx：版本: v2.2.0制定时间: 2026-03-27预计发布: 2026-05-31优先级: 🔴 高工作量: ~40 小时状态: 📋 需求设计中
- 需求只在 pptx：☐ 支持 SQLite (默认，零配置)
- 需求只在 pptx：☐ 支持 PostgreSQL (生产环境)
- 需求只在 pptx：☐ 通过配置切换数据库类型
- 需求只在 pptx：☐ 数据库连接池管理
- 需求只在 pptx：☐ 定义数据模型类
- 需求只在 pptx：☐ 支持异步操作 (asyncpg)
- 需求只在 pptx：☐ 数据库迁移工具 (Alembic)
- 需求只在 pptx：☐ 数据库连接配置 (.env)
- 需求只在 pptx：☐ 连接池参数配置

### xiaojilele-glitch__WhyBuddy

段落标题不一致，需求条目 88 / 88 一致（pptx 拆出 102 条）

- 标题只在 Markdown：US-1: 定义审计事件类型和关键操作
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：US-2: 采集和记录审计事件
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：US-3: Append-Only Log 存储和防篡改
- 需求只在 pptx：US-1: 定义审计事件类型和关键操作
- 需求只在 pptx：US-2: 采集和记录审计事件
- 需求只在 pptx：US-3: Append-Only Log 存储和防篡改
- 需求只在 pptx：US-4: 时间戳验证和可信时间源
- 需求只在 pptx：US-5: 审计链完整性验证
- 需求只在 pptx：US-6: 审计日志查询和搜索
- 需求只在 pptx：US-7: 审计日志导出和报告
- 需求只在 pptx：US-8: 审计日志保留和归档
- 需求只在 pptx：US-9: 审计链与数据血缘的集成
- 需求只在 pptx：US-10: 异常检测和告警

### yangyunice__WorkMesh

段落标题不一致，需求条目 279 / 363 一致（pptx 拆出 312 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 产品目标
- 标题只在 Markdown：2.1 产品目标
- 标题只在 Markdown：P0 (Must Have - 本版本必须实现)
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 标题只在 pptx：第 12 页
- 需求只在 Markdown：🎯 场景导向: 针对个人用户碎片化、高频次的使用习惯设计
- 需求只在 Markdown：🔄 生态融合: 就业、订单、布道三大业务闭环
- 需求只在 Markdown：📱 多端适配: 移动端网页、H5、PWA、可封装为 iOS/Android 原生应用
- 需求只在 Markdown：🔗 体系共用: 与 PC 端、企业端、管理端共用账号、数据库、订单和审核体系
- 需求只在 Markdown：核心业务闭环: 实现就业、订单、布道三条核心链路的移动端完整支持
- 需求只在 Markdown：高频操作优化: 首页快捷入口、状态切换、消息通知等高频功能易用性达标
- 需求只在 Markdown：多端数据同步: 与 PC 端、企业端、管理端数据实时同步，状态一致
- 需求只在 Markdown：用户体验优化: AI 推荐、智能匹配、个性化首页等提升用户体验的功能
- 需求只在 Markdown：离线能力: PWA 离线缓存、关键数据本地存储
- 需求只在 Markdown：性能优化: 首屏加载 < 2s，操作响应 < 500ms
- 需求只在 pptx：文档版本: v1.0创建日期: 2025-05-31产品经理: 许清楚 (Xu)产品名称: Personal Portal 移动端文档状态: 待评审
- 需求只在 pptx：提升用户活跃度: 通过移动端便捷操作，提升用户日均使用时长和打开频次
- 需求只在 pptx：促进交易转化: 简化就业/接单/布道流程，提高订单成交率
- 需求只在 pptx：构建成长闭环: 通过技能学习和认证，提升用户价值和平台粘性
- 需求只在 pptx：3.1 用户角色定义
- 需求只在 pptx：用户画像: 22-35 岁，灵活用工群体，希望通过平台找到合适的工作机会
- 需求只在 pptx：用户画像: 25-40 岁，有一技之长的自由职业者，希望通过平台接单赚钱
- 需求只在 pptx：用户画像: 28-45 岁，行业专家或资深从业者，希望分享技能获得收益
- 需求只在 pptx：用户画像: 18-30 岁，希望提升技能的在校学生或职场新人
- 需求只在 pptx：机会中心相关

### yaomindong1996__forge-admin

段落标题不一致，需求条目 156 / 173 一致（pptx 拆出 199 条）

- 标题只在 Markdown：1.1 文档目的
- 标题只在 Markdown：1.2 功能背景
- 标题只在 Markdown：1.3 功能目标
- 标题只在 Markdown：FR1. 编码规则主表管理（CRUD）
- 标题只在 Markdown：FR2. 分段明细配置
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 6 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 标题只在 pptx：第 9 页
- 需求只在 Markdown：应用中心菜单下可见「编码规则」页面
- 需求只在 Markdown：可新增/编辑/删除/启停编码规则
- 需求只在 Markdown：分段明细可在弹窗内增删改排序
- 需求只在 Markdown：五种段类型（DATE/FIXED/SEQ/VARIABLE/SYS_VAR）均可正确配置生成
- 需求只在 Markdown：SEQ 段5种进制转换正确，溢出时报错
- 需求只在 Markdown：SEQ 段可配置是否去除易混淆字符（I/O/Z），开启后字母进制不含这些字符
- 需求只在 Markdown：流水号按年/月/日/时重置正确
- 需求只在 Markdown：流水号按分组字段独立计数正确
- 需求只在 Markdown：不重置规则跨周期持续递增
- 需求只在 Markdown：保存时实时预览编码格式与示例值
- 需求只在 pptx：文档版本：1.0 编写日期：2026-07-16 状态：已实现
- 需求只在 pptx：FR1. 编码规则主表管理（CRUD）
- 需求只在 pptx：需求描述：系统管理员可对编码规则主记录进行新增、修改、删除、分页查询、查看详情及启用/停用操作。
- 需求只在 pptx：FR2. 分段明细配置
- 需求只在 pptx：FR3. 五种段类型支持
- 需求只在 pptx：下表针对 SEQ 段的 5 种进制，分别给出「规则配置 + 前 5 个生成序列 + 溢出边界」的完整示例，便于直观理解每种进制的递增与进位规则。
- 需求只在 pptx：FR4. 流水号重置与分组计数
- 需求只在 pptx：下表覆盖「重置周期」与「分组字段」两个维度的全部组合，每行给出规则配置、计数 key 结构与生成序列示例。
- 需求只在 pptx：计数 key 结构说明：sys-code-rule:{租户ID}:{规则ID}:seg{段序号}:{分组值}:{周期}
- 需求只在 pptx：FR5. 编码实时预览

### young-nights__ota-upgrade-of-qi-charger-based-on-can

段落标题不一致，需求条目 90 / 90 一致（pptx 拆出 139 条）

- 标题只在 Markdown：1.1 功能目标
- 标题只在 Markdown：1.2 系统架构
- 标题只在 Markdown：1.3 术语定义
- 标题只在 Markdown：1.4 版本字符串（编译期常量）
- 标题只在 Markdown：2.1 单 App 升级机制（备份区暂存 + BOOT 搬运）
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 4 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 pptx：1.4 版本字符串（编译期常量）
- 需求只在 pptx：2.1 单 App 升级机制（备份区暂存 + BOOT 搬运）
- 需求只在 pptx：描述: Boot + App + 备份区单 App 升级模式。OTA 写入备份区，BOOT 校验后搬运至 App 区；运行中固件不被直接覆盖。
- 需求只在 pptx：2.2 APP 下载 + 自复位切区（MCU1）/ UART 转发（MCU2）
- 需求只在 pptx：描述: 擦写与下载在运行中的 APP 完成。Bootloader 12KB 只做选区+验签+跳转，无 UDS。MCU1 与 MCU2 共用 UDS 下载 SID，由 2E 20 10 选择目标。
- 需求只在 pptx：2.2.1 MCU1（APP 固件）下载流程
- 需求只在 pptx：2.2.2 MCU2（Qi 芯片）IAP 流程（统一 UDS 路径）
- 需求只在 pptx：已删除的旧路径：DID 0x2130（Qi IAP 控制）/ 0x2131（Qi IAP 数据）写服务已移除，不可再用。
- 需求只在 pptx：2.3 镜像安全校验
- 需求只在 pptx：描述: 下载完成后对镜像做完整性、来源、地址合法性校验。

### yuhui0531__md2ppt

段落标题不一致，需求条目 70 / 89 一致（pptx 拆出 79 条）

- 标题只在 Markdown：用户类型
- 标题只在 Markdown：典型诉求
- 标题只在 Markdown：用户故事 1
- 标题只在 Markdown：用户故事 2
- 标题只在 Markdown：用户故事 3
- 需求只在 Markdown：已经在外部工具中写好了逐页生图 prompt 的用户
- 需求只在 Markdown：从系统导出的 prompt ZIP 经过外部修改后，希望重新导入的用户
- 需求只在 Markdown：希望跳过"内容解析与 prompt 生成"阶段，只做精修和出图的用户
- 需求只在 Markdown：快速把一批 .md prompt 导入系统
- 需求只在 Markdown：在系统内继续人工修改 prompt
- 需求只在 Markdown：对整套 prompt 做统一风格检查
- 需求只在 Markdown：批量生图并导出 PPT
- 需求只在 Markdown：支持导入一个 ZIP
- 需求只在 Markdown：支持导入多个 .md
- 需求只在 Markdown：导入后自动创建项目
- 需求只在 pptx：作为一个已经准备好逐页 prompt 的用户，我希望直接上传一个 ZIP 或多个 .md 文件，这样我就不用重新从 Markdown 原文开始生成。
- 需求只在 pptx：作为一个导入 prompt 的用户，我希望系统在导入后自动补全页面结构信息，并且在这个过程中看到进度条和状态说明，这样我能知道系统正在处理什么，而不是误以为卡住。
- 需求只在 pptx：7.1 导入项目定义
- 需求只在 pptx：7.2 导入项目初始数据
- 需求只在 pptx：7.3 结构补全 / 大纲提取
- 需求只在 pptx：7.5 工作台按钮策略
- 需求只在 pptx：导入项目进入工作台后，不应完全复用"Markdown 生成型项目"的所有按钮语义。
- 需求只在 pptx：该操作只更新结构化字段，不改写 prompt。
- 需求只在 pptx：每个文件全文直接保存到 slide.prompt。

### yuqie6__WorkMirror

段落标题不一致，需求条目 125 / 132 一致（pptx 拆出 153 条）

- 标题只在 Markdown：0.1 文档关系与口径（UI）
- 标题只在 Markdown：0.2 现状对照（alpha.2）
- 标题只在 Markdown：2.1 目标用户（Phase 1）
- 标题只在 Markdown：2.2 非目标用户（明确不支持）
- 标题只在 Markdown：3.1 UI/UX 设计约束（v0.2 必须落地）
- 标题只在 pptx：第 2 页
- 需求只在 Markdown：Local-first & Privacy by default：数据本地；敏感项默认最小化/可脱敏
- 需求只在 Markdown：内置本地 HTTP Server（随机端口，监听 127.0.0.1）
- 需求只在 Markdown：内置 Web UI（React/Vite SPA）：运行时优先加载同目录 frontend/dist/，否则回退内嵌资源
- 需求只在 Markdown：端口发现：写入 ./data/http_base_url.txt
- 需求只在 Markdown：云同步/账号体系/社交分享
- 需求只在 Markdown：复杂目标管理（TODO/OKR/习惯）
- 需求只在 Markdown：托盘 → 打开面板
- 需求只在 pptx：最后更新：2025-12-17对应版本：v0.2.0-alpha.2（见 CHANGELOG.md）
- 需求只在 pptx：把当前"能跑的个人工具"收敛为可长期交付的产品：对非作者用户也能安装即用、结果可解释、失败可诊断、可持续升级不炸数据。
- 需求只在 pptx：0.1 文档关系与口径（UI）
- 需求只在 pptx：下一版优先级将转向：更细粒度的证据覆盖率指标、可回放的语义升级策略与诊断闭环。
- 需求只在 pptx：复盘镜 WorkMirror：自动把你每天/每周的真实工作学习行为整理成可追溯的证据链回顾，并给出下一步建议（默认本地、可离线）。
- 需求只在 pptx：1. Local-first & Privacy by default：数据本地；敏感项默认最小化/可脱敏
- 需求只在 pptx：3.1 UI/UX 设计约束（v0.2 必须落地）
- 需求只在 pptx：行为采集 → Session（切分/聚合/摘要） → Skill 归因 → Weekly 回顾 → 证据链展开 → 系统状态可诊断
- 需求只在 pptx：6.3 会话语义来源（v0.2 P0，补齐"口径"）
- 需求只在 pptx：6.2 权威路径（必须遵守）

### ywq2019__ai_test_agent

段落标题不一致，需求条目 104 / 111 一致（pptx 拆出 136 条）

- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 技术架构选型
- 标题只在 Markdown：1.3 整体功能架构
- 标题只在 Markdown：2.1 权限规范
- 标题只在 Markdown：2.2 编码规范
- 需求只在 Markdown：基础开发框架：django vue3（前后端分离开源框架，支持列级别权限、多终端认证、插件化扩展）
- 需求只在 Markdown：后端技术栈：Python3.9+/3.11+、Django、Django REST Framework、SimpleJWT、Celery（定时任务）、Redis、MySQL8.0+
- 需求只在 Markdown：前端技术栈：Vue3、CompositionAPI、TypeScript、Vite、Element Plus、Pinia
- 需求只在 Markdown：自动化核心组件：Playwright（UI自动化执行引擎）
- 需求只在 Markdown：AI能力支撑：主流大模型（Deepseek、通义千问等）对接适配
- 需求只在 Markdown：平台整体分为基础系统模块、核心测试业务模块、AI智能扩展模块、自动化调度模块、报告统计模块五大板块，完全基于基础框架插件化开发，不改动底层原生架构，支持后续功能迭代扩展。
- 需求只在 Markdown：Docker \& Docker Compose：支持容器化快速部署
- 需求只在 pptx：复用系统原生操作日志、异常日志能力，记录所有新增、编辑、删除、用例执行、套件调度、AI调用、定时任务操作，包含操作人、操作时间、操作内容、IP、执行结果等信息。
- 需求只在 pptx：3.1 项目管理模块
- 需求只在 pptx：3.2 UI用例管理模块
- 需求只在 pptx：核心基础模块，用于标准化管理所有UI自动化测试用例，支撑套件组装、手动执行、自动调度，全程记录用例迭代及执行历史。
- 需求只在 pptx：3.2.1 核心字段属性
- 需求只在 pptx：3.3 UI测试套件管理模块
- 需求只在 pptx：3.3.1 核心字段属性
- 需求只在 pptx：3.3.2 核心功能需求
- 需求只在 pptx：3.4 套件用例执行管理模块
- 需求只在 pptx：3.4.1 手动执行功能

### zhewu43__FocusFlight_wxminiprogram

段落标题不一致，需求条目 132 / 151 一致（pptx 拆出 174 条）

- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 核心价值
- 标题只在 Markdown：2.1 核心功能模块
- 标题只在 Markdown：2.1.1 用户系统
- 需求只在 Markdown：创新的航班式专注时间设定
- 需求只在 Markdown：简单直观的操作体验
- 需求只在 Markdown：基于真实地理位置的时间计算
- 需求只在 Markdown：创新的航班式专注时间设定
- 需求只在 Markdown：简单直观的操作体验
- 需求只在 Markdown：基于真实地理位置的时间计算
- 需求只在 Markdown：小程序基础结构搭建
- 需求只在 Markdown：页面路由配置
- 需求只在 Markdown：城市数据和距离计算
- 需求只在 Markdown：航班选择功能
- 需求只在 pptx：2.1 核心功能模块
- 需求只在 pptx：功能描述： 基于微信账号的用户登录和信息管理
- 需求只在 pptx：2.1.2 航班选择系统
- 需求只在 pptx：功能描述： 模拟航班预订界面，选择起始地和目的地
- 需求只在 pptx：功能描述： 执行专注任务的核心功能
- 需求只在 pptx：2.1.4 社交分享系统
- 需求只在 pptx：功能描述： 用户专注成果分享功能
- 需求只在 pptx：功能描述： 个性化设置和偏好管理
- 需求只在 pptx：2.1.5 社交分享系统
- 需求只在 pptx：功能描述： 用户专注成果分享功能

### zxmqq1234__web3-pawID

段落标题不一致，需求条目 58 / 58 一致（pptx 拆出 70 条）

- 标题只在 Markdown：3.1 创建身份：
- 标题只在 Markdown：3.2 宠物总览：
- 标题只在 Markdown：3.3 家庭与族谱：
- 标题只在 Markdown：3.4 生命档案：
- 标题只在 Markdown：3.5 成长资产：
- 标题只在 pptx：第 2 页
- 标题只在 pptx：第 5 页
- 标题只在 pptx：第 7 页
- 标题只在 pptx：第 8 页
- 需求只在 pptx：版本：V1.1｜用途：PawID Web3 项目的当前范围与需求说明，可作为后续开发与路演的统一口径。
- 需求只在 pptx：依据：用户提供的产品方案。保留宠物数字身份、AI 形象、人宠绑定、共同监护、族谱、成长资产、防丢和服务生态；下述路由、样式、数值、示例人物及状态规则为本项目的具体设计。
- 需求只在 pptx：当前项目状态（2026-09-05）：GitHub main 分支已完成合并；公网前端 http://web3.yrq666.xyz/ 已上线；MOJO 项目提交 399 处于 pending 状态。Monad 钱包与状态内核已实现；Registry 合约代码已实现，但尚未完成 Monad 测试网真实部署与验证，VITE_MONAD_REGISTRY_ADDRESS 尚未配置；JWS 生图代理代码已实现，生产端点与新 Key 尚未部署配置；Foundry 尚未在本地运行。上述未完成项在本文中一律保持待完成表述，不虚构能力。
- 需求只在 pptx：采用"品牌入口 + 宠物工作台 + 公开访问页面"。宠物工作台通过顶部宠物切换器维持当前宠物，切换标签不丢失宠物 ID。
- 需求只在 pptx：补充：不再单独创建消息中心、个人中心、后台管理。消息入口用顶栏抽屉，展示邀请结果、积分奖励和寻宠线索，并跳转对应宠物及标签。
- 需求只在 pptx：规则：上一步保留输入；处理中禁用重复提交；创建成功只执行一次，展示身份卡及轻量庆祝动效，然后点击"进入它的数字世界"打开总览。创建草稿在刷新后恢复，退出创建时可选择保留或清除。
- 需求只在 pptx：监护家庭：主监护人卡置顶，共同监护人并排，下方为待处理邀请。
- 需求只在 pptx：宠物族谱：默认展示以当前宠物为中心的三代局部图谱；父母在上方、祖父母再上一层、兄弟姐妹与当前宠物同层。
- 需求只在 pptx：数据同步边界：同源、同浏览器多标签页通过存储事件同步；不同设备没有共享本地数据，不能实时通知主人。内置示例宠物的二维码可在另一设备展示示例资料；自建宠物和邀请在另一设备无法解析时展示"此内容仅在创建它的浏览器可用"并提供"体验示例"。现场互动统一使用"打开访客预览/以受邀者身份打开"完成，不承诺跨设备实时同步。
- 需求只在 pptx：每张卡展示服务对象、解决的问题及未来收费方式或公益属性；弹窗中提供"感兴趣/取消意向"按钮并本地保存。此处仅表达产品与商业价值，不生成订单、不展示虚构合作机构或真实认证。

## pdf

### Bytepute__endpointForge

段落标题一致，需求条目 155 / 170 一致（pdf 拆出 167 条）

- 需求只在 Markdown：method: GET, POST, PUT, PATCH, or DELETE
- 需求只在 Markdown：User enters a route path beginning with /.
- 需求只在 Markdown：/projects/$projectId/controllers/$controllerId/endpoints/$endpointId: endpoint detail page with response preview and edit/delete actions.
- 需求只在 Markdown：Login and registration call /auth/login and /auth/register.
- 需求只在 Markdown：On 401, the client tries /auth/refresh-token once and retries the failed request.
- 需求只在 Markdown：GET /route-groups/project/:projectId
- 需求只在 Markdown：GET /endpoints/route-group/:routeGroupId
- 需求只在 Markdown：Create controllers with base paths beginning with /.
- 需求只在 Markdown：Validate endpoint path begins with /.
- 需求只在 Markdown：Support GET, POST, PUT, PATCH, and DELETE.
- 需求只在 pdf：method:GET,POST,PUT,PATCH, or DELETE
- 需求只在 pdf：User enters a route path beginning with/.
- 需求只在 pdf：Login and registration call/auth/login and/auth/register.
- 需求只在 pdf：On 401, the client tries/auth/refresh-token once and retries the failed request.
- 需求只在 pdf：Create controllers with base paths beginning with/.
- 需求只在 pdf：Validate endpoint path begins with/.
- 需求只在 pdf：Support GET,POST,PUT,PATCH, and DELETE.
- 需求只在 pdf：Endpoint URL copy currently builds window.location.origin+"/api"+ endpoint.path; it does not include the controller base path in the endpoint detail page. Future work should confirm the intended public mock URL shape.
- 需求只在 pdf：Endpoint details are loaded from the endpoint list by controller rather than directly from GET/endpoints/:id, even though the service supports direct endpoint fetching.
- 需求只在 pdf：Controller cards display endpoint count from controller.endpoints.length, but the service currently maps endpoints to an empty array because the backend route- group response does not include endpoints.

### GoForthTechnology__RoomBooker

段落标题一致，需求条目 12 / 30 一致（pdf 拆出 30 条）

- 需求只在 Markdown：User Story 1 (Guest Access): As a guest user, I want to view the room calendar and submit a booking request without creating an account, so I can reserve a space with minimal friction.
- 需求只在 Markdown：User Story 2 (Guest Booking Confirmation): As a guest user who has submitted a request, I want to provide my email and receive a confirmation link so that I can verify my booking and manage it later.
- 需求只在 Markdown：User Story 3 (Account Creation): As a user, I want to be able to sign up or log in (with email or Google) to have a centralized place to view and manage all my past and upcoming bookings.
- 需求只在 Markdown：User Story 4 (Logout): As an authenticated user, I want to be able to log out of the application to protect my account.
- 需求只在 Markdown：User Story 5 (View Rooms): As any user (guest or authenticated), I want to see a clear, calendar-based view of all available rooms and their schedules so I can easily find an open slot.
- 需求只在 Markdown：User Story 6 (Submit Booking Request): As any user, I want to be able to select an available room and time slot to create a new booking. If I am a guest, I will be prompted for my email address.
- 需求只在 Markdown：User Story 7 (View My Bookings): As an authenticated user, I want to have a dedicated section where I can view all of my upcoming and past reservations.
- 需求只在 Markdown：User Story 8 (Cancel a Booking): As any user, I want to be able to cancel a booking I've made. (Guests will use the link from their confirmation email, authenticated users will do it from their account).
- 需求只在 Markdown：Performance: The calendar view should load in under 2 seconds, and booking confirmations should feel instantaneous.
- 需求只在 Markdown：Security: All user data and authentication tokens must be handled securely. Communication with Firebase services must be over HTTPS.
- 需求只在 pdf：User Story 1 (Guest Access):As a guest user, I want to view the room calendar and submit a booking request without creating an account, so I can reserve a space with minimal friction.
- 需求只在 pdf：User Story 2 (Guest Booking Confirmation):As a guest user who has submitted a request, I want to provide my email and receive a confirmation link so that I can verify my booking and manage it later.
- 需求只在 pdf：User Story 3 (Account Creation):As a user, I want to be able to sign up or log in (with email or Google) to have a centralized place to view and manage all my past and upcoming bookings.
- 需求只在 pdf：User Story 4 (Logout):As an authenticated user, I want to be able to log out of the application to protect my account.
- 需求只在 pdf：User Story 5 (View Rooms):As any user (guest or authenticated), I want to see a clear, calendar-based view of all available rooms and their schedules so I can easily find an open slot.
- 需求只在 pdf：User Story 6 (Submit Booking Request):As any user, I want to be able to select an available room and time slot to create a new booking. If I am a guest, I will be prompted for my email address.
- 需求只在 pdf：User Story 7 (View My Bookings):As an authenticated user, I want to have a dedicated section where I can view all of my upcoming and past reservations.
- 需求只在 pdf：User Story 8 (Cancel a Booking):As any user, I want to be able to cancel a booking I've made. (Guests will use the link from their confirmation email, authenticated users will do it from their account).
- 需求只在 pdf：Performance:The calendar view should load in under 2 seconds, and booking confirmations should feel instantaneous.
- 需求只在 pdf：Security:All user data and authentication tokens must be handled securely. Communication with Firebase services must be over HTTPS.

### JulioBorges__gantry

段落标题一致，需求条目 13 / 25 一致（pdf 拆出 24 条）

- 需求只在 Markdown：Agents + code > agents alone. Every decision that must not be improvised — what is ready, what must be proven, whether gates pass, when an issue is done — is made by a workflow script. Agents never re-decide what a script decided.
- 需求只在 Markdown：Fail closed. An uncertain critic, a missing result, a dirty tree, a gate that could not run: not done.
- 需求只在 Markdown：One authority per fact. An issue's Status: line and checkboxes, written only by the roadmap script, say where work stands. The run log says how it got there. The dashboard shows both and changes neither.
- 需求只在 Markdown：Never weaken verification. No test is skipped, disabled, mocked-away or deleted to get green, and no delivery that did so is accepted.
- 需求只在 Markdown：The operator's checkout stays free. A run offers a dedicated worktree before it creates anything.
- 需求只在 Markdown：Honest capabilities. Each harness's capabilities are declared in a file and exercised on the fixture; a run report states the support tier it ran at. Gantry never advertises a guarantee it cannot measure.
- 需求只在 Markdown：If /gantry encounters an older incomplete scope, it may delegate the missing planning work to this same workflow, but it must preserve the approval stop. The documented default remains the explicit /gantry-plan → approval → /gantry lifecycle.
- 需求只在 Markdown：deny edits to ROADMAP.md, to an issue's Status: line or to its criteria checkboxes by any tool other than the roadmap script;
- 需求只在 Markdown：deny git push --force and test-skip patterns being committed;
- 需求只在 Markdown：record SubagentStart/SubagentStop, phase transitions and compaction events (PreCompact, session.compacted) into the run log.
- 需求只在 pdf：Agents + code > agents alone.Every decision that must not be improvised — what is ready, what must be proven, whether gates pass, when an issue is done — is made by a workflow script. Agents never re-decide what a script decided.
- 需求只在 pdf：Fail closed.An uncertain critic, a missing result, a dirty tree, a gate that could not run: not done.
- 需求只在 pdf：One authority per fact.An issue's Status:line and checkboxes, written only by the roadmap script, say where work stands. The run log says how it got there. The dashboard shows both and changes neither.
- 需求只在 pdf：Never weaken verification.No test is skipped, disabled, mocked-away or deleted to get green, and no delivery that did so is accepted.
- 需求只在 pdf：The operator's checkout stays free.A run offers a dedicated worktree before it creates anything.
- 需求只在 pdf：Honest capabilities.Each harness's capabilities are declared in a file and exercised on the fixture; a run report states the support tier it ran at. Gantry never advertises a guarantee it cannot measure.
- 需求只在 pdf：If/gantry encounters an older incomplete scope, it may delegate the missing planning work to this same workflow, but it must preserve the approval stop. The documented default remains the explicit/gantry-plan→ approval →/gantry lifecycle.
- 需求只在 pdf：deny edits to ROADMAP.md, to an issue's Status:line or to its criteria checkboxes by any tool other than the roadmap script;
- 需求只在 pdf：deny git push--force and test-skip patterns being committed;
- 需求只在 pdf：record SubagentStart/SubagentStop, phase transitions and compaction events (PreCompact,session.compacted) into the run log.

### MrThief123__care-compass

段落标题一致，需求条目 24 / 62 一致（pdf 拆出 35 条）

- 需求只在 Markdown：Role (app)：Carer；Real-world people：Registered nurse, enrolled nurse, support worker, including temporary staff；Context：Shift worker on a shared laptop; one organisation, many clients；Status：CONFIRMED
- 需求只在 Markdown：ID：REQ-03；Area：Access；Requirement：Authorisation enforced by the database (RLS) on every read and write.；Priority · Status：MUST · CONFIRMED；Sources：FR-5.5; NFR-3; ADR-01–03; TM-2808；Implemented by：F0-04, F0-06, INT-05
- 需求只在 Markdown：ID：REQ-08；Area：Access；Requirement：Staff are identified by name (and optional reference); organisations differ on showing full surname or initial.；Priority · Status：MUST · CONFIRMED (display AMBIGUOUS, OQ-13)；Sources：CIS5 Rostering & Q&A; UI-D33；Implemented by：ADM-02
- 需求只在 Markdown：ID：REQ-09；Area：Access；Requirement：MFA is not mandatory for any role, including Admin (PD-040, reaffirmed by CHG-010 on 2026-09-24).；Priority · Status：SHOULD · CONFIRMED (PD-040, CHG-010)；Sources：NFR-3; ADR-03; TM-2108；Implemented by：F0-07
- 需求只在 Markdown：ID：REQ-12；Area：Client record；Requirement：The client's name and avatar anchor Family page headers; the signed-in user is shown separately.；Priority · Status：MUST · CONFIRMED；Sources：UI-D16; DD §1；Implemented by：F0-15
- 需求只在 Markdown：ID：REQ-13；Area：Scheduling；Requirement：Care events (Care Need Items) can be one-off or recurring, with no limit on number.；Priority · Status：MUST · CONFIRMED；Sources：BRIEF I, items 1–3; FR-1.3, FR-2.1, FR-2.6; US C-5；Implemented by：F0-09, F0-11, FAM-06
- 需求只在 Markdown：ID：REQ-14；Area：Scheduling；Requirement：Schedules are perpetual: recurrences carry forward indefinitely without re-entry and can be changed later.；Priority · Status：MUST · CONFIRMED；Sources：BRIEF item 3; CIS5 Perpetual; FR-2.4；Implemented by：F0-09, F0-11, FAM-04, FAM-06, FAM-07
- 需求只在 Markdown：ID：REQ-15；Area：Scheduling；Requirement：A single occurrence can be cancelled or modified without affecting the series.；Priority · Status：SHOULD · CONFIRMED (UI AMBIGUOUS, OQ-11)；Sources：BRIEF item 3; FR-2.5; US C-6；Implemented by：F0-09, F0-11, FAM-07
- 需求只在 Markdown：ID：REQ-16；Area：Scheduling；Requirement：Calendar offers day, week and month views, defaulting to week, with normal conventions.；Priority · Status：MUST · CONFIRMED；Sources：CM-0309; UI-D6, D12；Implemented by：UI-01, FAM-01, FAM-04
- 需求只在 Markdown：ID：REQ-18；Area：Scheduling；Requirement：Family and Carers can create events and mark tasks Done; no approval step (CHG-009).；Priority · Status：MUST · CONFIRMED；Sources：CM-0309; UI-D26; CIS5 Q&A (superseded supervisor confirmation)；Implemented by：F0-11, FAM-05, FAM-06, CAR-06, CAR-07, INT-03
- 需求只在 pdf：9% availability , daily backups, 1-hour redeploy. REQ-N12 Non-Money MUST ·ADR-01;F0-12 functional stored as CONFIRM ADR-02 exact ED decimals; multi-table financial writes are atomic.
- 需求只在 pdf：Client set-up— admin adds client with family contact (design) or family registers the client (CIS3/CM-1908) — AMBIGUOUS (OQ-07).
- 需求只在 pdf：Schedule care— family (or carer on shift) enters an event with date, recurrence, description, documents; it appears on calendars indefinitely.
- 需求只在 pdf：Roster— admin selects staff and client, picks date and time slot, sees a soft overlap warning, assigns shift; carer is notified.
- 需求只在 pdf：Deliver care— carer on shift opens Home/Calendar, ticks tasks; family sees "Done · Aisha R.".
- 需求只在 pdf：Monitor— family Home shows today, overdue, recent activity and budgets; admin Home shows overdue across all clients.
- 需求只在 pdf：Budget— funds recorded per bucket; spending deducts automatically; threshold emails sent automatically.
- 需求只在 pdf：Change organisation— family chooses a new organisation, confirms consequences; history retained, nurses and future shifts cleared, old organisation loses access immediately.
- 需求只在 pdf：Handover— client receives plain-English guides and runbooks.
- 需求只在 pdf：Missing sources required: Client Information Sheet No 4 (budgeting); workshop decks W3, w4-5; UI Spec v1 §7 /care-compass-spec-v3.md;CLAUDE-CODE- HANDOFF.md; Domain Model PDF; wireframes PDF; Figma pages 02–06 via MCP (OQ-19). Place them in docs/sources/when obtained.

### ScionResearch__multi-material-printer

段落标题不一致，需求条目 16 / 102 一致（pdf 拆出 38 条）

- 标题只在 Markdown：4.1 Logical Components (Refined)
- 标题只在 Markdown：4.2 State Definitions (Added)
- 标题只在 Markdown：4.3 Data Persistence (Added)
- 标题只在 Markdown：5.1 Feature 1: System Configuration
- 标题只在 Markdown：5.2 Feature 2: Recipe Management
- 需求只在 Markdown：Web Interface (SPA or server-rendered hybrid) – real-time dashboard, configuration, control.
- 需求只在 Markdown：Flask Backend – REST + Server-Sent Events (SSE) or WebSocket push (implementation decision) for status streaming.
- 需求只在 Markdown：Print Manager Service – long-running supervisor (loop interval: 2–5 s) executing recipe logic.
- 需求只在 Markdown：Shared Status Module – single source of truth (in-memory + persisted snapshot file on graceful shutdown).
- 需求只在 Markdown：MMU Control – abstracts GPIO / pump actuation / safety interlocks.
- 需求只在 Markdown：Printer Comms – abstraction over uart-wifi with retry + backoff.
- 需求只在 Markdown：Logging Module – structured logging (JSON lines + human-readable rolling log).
- 需求只在 Markdown：Configuration Files: canonical; edits atomically written via temp + rename.
- 需求只在 Markdown：Runtime Cache: in-memory dict; periodically (every 60 s) snapshot to runtime_status.json.
- 需求只在 Markdown：Logs: logs/app.log (rotating, 10 MB * 5). Material change events also mirrored to logs/material_events.jsonl.
- 需求只在 pdf：1 Feature 1: System Configuration
- 需求只在 pdf：User Story (Ben):"As a Student, I want a single place to configure the printer's IP address and the physical profiles of our pumps so that I can set up new hardware easily."
- 需求只在 pdf：2 Feature 2: Recipe Management
- 需求只在 pdf：User Story (Elena):"As a research scientist, I want to create, save, and load a recipe that specifies which material to use at which layer number, so I can design my experiments."
- 需求只在 pdf：3 Feature 3: Automated Multi-Material Print Execution
- 需求只在 pdf：User Story (Ben):"As a Student, after selecting a file on the printer and loading a recipe, I want to press a single 'Start' button and have the system manage the entire multi- material print process automatically."
- 需求只在 pdf：4 Feature 4: Real-Time Monitoring and Control
- 需求只在 pdf：User Story (Elena):"As a researcher, while a multi-material print is running, I want to see a live dashboard with the printer's status, current layer, active material, and a log of events, so I can have confidence my experiment is proceeding correctly."
- 需求只在 pdf：5 Feature 5: Manual Hardware Control & Diagnostics
- 需求只在 pdf：User Story (Ben):"As a Student, I need to be able to run any pump manually for a specific amount of time to prime the lines or perform maintenance."

### closedloop-technologies__climbhill

段落标题一致，需求条目 112 / 125 一致（pdf 拆出 125 条）

- 需求只在 Markdown：Run-centered engine. A standalone Run is executable and auditable without loading a Job.
- 需求只在 Markdown：Git owns revisions. Commits and branches represent content history; ClimbHill stores semantic lineage as metadata.
- 需求只在 Markdown：One primary Focus. A Run changes one declared surface with a resolved writable scope.
- 需求只在 Markdown：External evaluation. Every optimization is judged by evidence outside the surface being optimized.
- 需求只在 Markdown：Scoped autonomy. Work may continue within an Authorization Envelope; widening the envelope requires authority.
- 需求只在 Markdown：Recommendation is not authority. Agentic Continuation Analysis cannot authorize or execute itself.
- 需求只在 Markdown：Least change first. Prefer lower-scope diagnostic or optimization actions when they can produce useful evidence.
- 需求只在 Markdown：Failure is not evaluator error. Alignment requires evidence outside the evaluator being challenged.
- 需求只在 Markdown：Filesystem is canonical. Version-controlled YAML and Markdown are the source of truth; SQLite is a rebuildable cache.
- 需求只在 Markdown：Partial work remains evidence. Failure, cancellation, budget termination, and stale reasoning remain inspectable.
- 需求只在 pdf：Run-centered engine.A standalone Run is executable and auditable without loading a Job.
- 需求只在 pdf：Git owns revisions.Commits and branches represent content history; ClimbHill stores semantic lineage as metadata.
- 需求只在 pdf：One primary Focus.A Run changes one declared surface with a resolved writable scope.
- 需求只在 pdf：External evaluation.Every optimization is judged by evidence outside the surface being optimized.
- 需求只在 pdf：Scoped autonomy.Work may continue within an Authorization Envelope; widening the envelope requires authority.
- 需求只在 pdf：Recommendation is not authority.Agentic Continuation Analysis cannot authorize or execute itself.
- 需求只在 pdf：Least change first.Prefer lower-scope diagnostic or optimization actions when they can produce useful evidence.
- 需求只在 pdf：Failure is not evaluator error.Alignment requires evidence outside the evaluator being challenged.
- 需求只在 pdf：Filesystem is canonical.Version-controlled YAML and Markdown are the source of truth; SQLite is a rebuildable cache.
- 需求只在 pdf：Partial work remains evidence.Failure, cancellation, budget termination, and stale reasoning remain inspectable.

### cloud-ai-summit-cz__ai

段落标题一致，需求条目 32 / 46 一致（pdf 拆出 35 条）

- 需求只在 Markdown：Target demo date: December 8, 2025
- 需求只在 Markdown：Scenario：Complete research with recommendation；Given：User asks "Should Cofilot expand to Vienna?"；When：Research completes；Then：All checklist items addressed; synthesized report with clear recommendation；Automated Test?：Yes
- 需求只在 Markdown：ID：FR9；Requirement：User Interaction；Description：Agents can pause to ask user clarifying questions; user responses influence research
- 需求只在 Markdown：Submits research question via web portal
- 需求只在 Markdown：Observes agents working collaboratively in real-time
- 需求只在 Markdown：Responds to clarifying questions when prompted
- 需求只在 Markdown：Receives comprehensive research report with recommendation
- 需求只在 Markdown：Views research query submission
- 需求只在 Markdown：Observes agent reasoning, tool usage, and collaboration
- 需求只在 Markdown：Sees scratchpad evolving with findings
- 需求只在 pdf：Target demo date:December 8, 2025
- 需求只在 pdf：Static JSON files for mock data: o Market statistics and trends o Competitor profiles o Location/neighborhood data o Cofilot company profile
- 需求只在 pdf：Azure AI Search index for: o Regulatory and compliance rules (semantic search) o Coffee culture and preferences (semantic search)

### e6a5__zenta

段落标题一致，需求条目 57 / 65 一致（pdf 拆出 64 条）

- 需求只在 Markdown：zenta export should produce clean output suitable for awk, grep, sort
- 需求只在 Markdown：❌ Adding task management features ("I'll just add a simple todo list...")
- 需求只在 Markdown：❌ Complex configuration systems with dozens of options
- 需求只在 Markdown：❌ Web dashboards or GUI components
- 需求只在 Markdown：❌ Cloud sync, accounts, or external service dependencies
- 需求只在 Markdown：❌ AI features that require large models or internet connectivity
- 需求只在 Markdown：❌ Notification systems that are intrusive or attention-grabbing
- 需求只在 Markdown：Optional interactive setup for preferences
- 需求只在 pdf：zenta export should produce clean output suitable for awk,grep,sort
- 需求只在 pdf：❌Adding task management features ("I'll just add a simple todo list...")
- 需求只在 pdf：❌Complex configuration systems with dozens of options
- 需求只在 pdf：❌Web dashboards or GUI components
- 需求只在 pdf：❌Cloud sync, accounts, or external service dependencies
- 需求只在 pdf：❌AI features that require large models or internet connectivity
- 需求只在 pdf：❌Notification systems that are intrusive or attention-grabbing

### hasanraiyan__resume

段落标题一致，需求条目 11 / 15 一致（pdf 拆出 15 条）

- 需求只在 Markdown：Today → Mark attendance (primary screen)
- 需求只在 Markdown：Calendar → View and edit history
- 需求只在 Markdown：Analytics → Charts, reports, safe bunks, predictions
- 需求只在 Markdown：Semester → Subjects, timetable, holidays, settings
- 需求只在 pdf：Today→ Mark attendance (primary screen)
- 需求只在 pdf：Calendar→ View and edit history
- 需求只在 pdf：Analytics→ Charts, reports, safe bunks, predictions
- 需求只在 pdf：Semester→ Subjects, timetable, holidays, settings

### intervalrain__OpenClaw.Net

段落标题不一致，需求条目 11 / 46 一致（pdf 拆出 45 条）

- 标题只在 Markdown：PRD：C# Agent Platform（OpenClaw.NET）
- 标题只在 Markdown：1. 產品背景與目標
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：2. 產品定位
- 标题只在 Markdown：2.1 產品一句話描述
- 标题只在 pdf：PRD：C#Agent Platform（OpenClaw.NET）
- 标题只在 pdf：1.產品背景與目標
- 标题只在 pdf：1.1背景
- 标题只在 pdf：2.產品定位
- 标题只在 pdf：2.1產品一句話描述
- 需求只在 Markdown：高階軟體工程師 / 平台工程師
- 需求只在 Markdown：企業內部 AI / Agent 平台團隊
- 需求只在 Markdown：想自託管 Agent、避免 SaaS Lock-in 的團隊
- 需求只在 Markdown：純 Prompt 工具（無實際任務執行）
- 需求只在 Markdown：Strongly Typed First（所有 Tool / Skill 皆可編譯期檢查）
- 需求只在 Markdown：接收外部輸入並轉為統一 AgentEvent
- 需求只在 Markdown：可在 CLI 完成複雜任務（多 tool）
- 需求只在 Markdown：新增 Skill 不需改核心程式
- 需求只在 Markdown：容器內運行 headless browser（Playwright/Puppeteer）
- 需求只在 Markdown：透過 VNC/noVNC 或 X11 forwarding 提供遠端可視化
- 需求只在 pdf：高階軟體工程師/平台工程師
- 需求只在 pdf：企業內部AI / Agent平台團隊
- 需求只在 pdf：想自託管Agent、避免SaaS Lock-in的團隊
- 需求只在 pdf：純Prompt工具（無實際任務執行）
- 需求只在 pdf：Strongly Typed First（所有Tool / Skill皆可編譯期檢查）
- 需求只在 pdf：接收外部輸入並轉為統一AgentEvent MVP支援
- 需求只在 pdf：Execution Timeout非目標（第一版）
- 需求只在 pdf：可在CLI完成複雜任務（多tool）
- 需求只在 pdf：新增Skill不需改核心程式
- 需求只在 pdf：容器內運行headless browser（Playwright/Puppeteer）

### jpbullalayao__pokemon-vgc-calc-mcp

段落标题不一致，需求条目 0 / 14 一致（pdf 拆出 10 条）

- 标题只在 Markdown：7.1 Input Schema ($input)
- 标题只在 Markdown：7.2 Output Schema ($output)
- 需求只在 Markdown：ID：FR1；Requirement：Core Tool: calculateDamage；Details：The MCP server shall expose one primary tool with the tool_id: calculateDamage.
- 需求只在 Markdown：ID：FR3；Requirement：Calculation Logic；Details：All damage calculation logic must be performed by the smogon/damage-calc npm package. The server will act as a wrapper, translating MCP input into the format required by the package and formatting its output.
- 需求只在 Markdown：ID：FR5；Requirement：Error Handling；Details：If the input is invalid (e.g., non-existent Pokémon, invalid move), the server should return a structured MCP error message with a clear description of the problem, not a 500 server error.
- 需求只在 Markdown：ID：TR4；Requirement：Deployment；Specification：The project must be configured for "zero-config" deployment on Vercel. This includes a vercel.json file if necessary to handle routing.
- 需求只在 Markdown：ID：TR6；Requirement：Code Repository；Specification：The project will be maintained in a Git repository.
- 需求只在 Markdown：The input will be a JSON object with three main properties: attacker, defender, and field.
- 需求只在 Markdown：API Uptime: > 99.9% on the Vercel platform.
- 需求只在 Markdown：Average Latency: < 500ms per request for standard calculations.
- 需求只在 Markdown：Adoption: Number of unique IP addresses or applications making requests to the server (if logging is implemented).
- 需求只在 Markdown：Accuracy: 0 calculation discrepancies when compared with the official Smogon Web Calculator for identical inputs.
- 需求只在 pdf：Field:Active weather, terrain, and global modifiers (e.g., Beads of Ruin, Aurora Veil). FR3 Calculation Logic All damage calculation logic must be performed by the
- 需求只在 pdf：The input will be a JSON object with three main properties:attacker,defender, and field.
- 需求只在 pdf：API Uptime:> 99.9% on the Vercel platform.
- 需求只在 pdf：Average Latency:< 500ms per request for standard calculations.
- 需求只在 pdf：Adoption:Number of unique IP addresses or applications making requests to the server (if logging is implemented).
- 需求只在 pdf：Accuracy:0 calculation discrepancies when compared with the official Smogon Web Calculator for identical inputs.
- 需求只在 pdf：findBestMove Tool:A new tool that takes an attacker and defender and calculates the damage for all of the attacker's viable moves to find the most damaging one.
- 需求只在 pdf：coverage Tool:A tool that analyzes a Pokémon's moveset against common metagame threats.
- 需求只在 pdf：Support for Pokémon Sets:Integrate with a database or a simple JSON store to allow users to use shorthand for common Smogon sets (e.g.,"Lando-T-Scarf").
- 需求只在 pdf：Caching:Implement a simple in-memory or Vercel Edge cache to return instant results for frequently repeated calculations.

### profullstack__coinpayportal

段落标题一致，需求条目 201 / 201 一致（pdf 拆出 204 条）

- 需求只在 pdf：environment mode: o sandbox o production
- 需求只在 pdf：enabled payment methods: o crypto only o card only o crypto + card
- 需求只在 pdf：platform-specific adapters: o packages/coinpay-sdk o plugins/woocommerce o plugins/whmcs

### rahilp__gatewright

段落标题一致，需求条目 26 / 29 一致（pdf 拆出 28 条）

- 需求只在 Markdown：The agent. Not a person, but the tracker's most frequent caller. Needs: cheap state, clear next action, a way to record evidence and discovered work, and hard rules it can't accidentally break.
- 需求只在 Markdown：ID：R4；Requirement：gw move enforces stage exit rules from stages.json (evidence required, deps must be at or past a stage)；Acceptance：Move to Built with no evidence → non-zero exit and reason; with evidence → succeeds
- 需求只在 Markdown：ID：D4；Decision：License: MIT.；Rationale：This is a CLI people will vendor and fork. Apache-2.0's patent grant buys nothing here and adds adoption friction.
- 需求只在 pdf：The agent.Not a person, but the tracker's most frequent caller. Needs: cheap state, clear next action, a way to record evidence and discovered work, and hard rules it can't accidentally break.
- 需求只在 pdf：dren allows ired_for, which the pipeline preset sets —

### sudo-Harshk__Skillify

段落标题不一致，需求条目 34 / 56 一致（pdf 拆出 55 条）

- 标题只在 Markdown：3.11 LOW — No .env.example File
- 标题只在 pdf：3.11 LOW — No.env.example File
- 需求只在 Markdown：Issue: The file backend/.env was committed to the repository. It contains the live GEMINI_API_KEY. Any person with access to the git history can extract and abuse this key, incurring costs or exhausting the quota.
- 需求只在 Markdown：Remove the .env file from git history using git filter-repo or BFG Repo Cleaner.
- 需求只在 Markdown：Add .env to .gitignore if not already present (it is, but verify it was not bypassed).
- 需求只在 Markdown：Create a .env.example file listing every required environment variable with placeholder values and a comment explaining each one. This becomes the canonical reference for any new developer setting up the project.
- 需求只在 Markdown：Change the fallback behavior so that if ALLOWED_ORIGINS is empty or not set, the server refuses to start and logs a clear error: ALLOWED_ORIGINS must be set. Example: https://yourdomain.com.
- 需求只在 Markdown：Document the expected value format in .env.example.
- 需求只在 Markdown：Issue: POST /questions/generate makes a live call to the Gemini API on every request. There is no rate limiting or request throttling. A malicious or runaway client can exhaust the API quota within minutes.
- 需求只在 Markdown：Add IP-based rate limiting on the /questions/generate and /questions/evaluate endpoints.
- 需求只在 Markdown：Use @fastify/rate-limit (official Fastify plugin) to implement this — do not roll a custom solution.
- 需求只在 Markdown：API key / model not available → "Question generation is temporarily unavailable. Please try again in a few minutes."
- 需求只在 pdf：Issue:The file backend/.env was committed to the repository. It contains the live GEMINI_API_KEY. Any person with access to the git history can extract and abuse this key, incurring costs or exhausting the quota.
- 需求只在 pdf：Remove the.env file from git history using git filter-repo or BFG Repo Cleaner.
- 需求只在 pdf：Add.env to.gitignore if not already present (it is, but verify it was not bypassed).
- 需求只在 pdf：Create a.env.example file listing every required environment variable with placeholder values and a comment explaining each one. This becomes the canonical reference for any new developer setting up the project.
- 需求只在 pdf：Change the fallback behavior so that if ALLOWED_ORIGINS is empty or not set, the server refuses to start and logs a clear error:ALLOWED_ORIGINS must be set. Example:https://yourdomain.com.
- 需求只在 pdf：Document the expected value format in.env.example.
- 需求只在 pdf：Issue:POST/questions/generate makes a live call to the Gemini API on every request. There is no rate limiting or request throttling. A malicious or runaway client can exhaust the API quota within minutes.
- 需求只在 pdf：Add IP-based rate limiting on the/questions/generate and /questions/evaluate endpoints.
- 需求只在 pdf：Use@fastify/rate-limit (official Fastify plugin) to implement this — do not roll a custom solution.
- 需求只在 pdf：Issue:App.tsx manages 11 useState hooks in a single component. The quiz state (subject, chapter, questions, answers, timer, results) is spread across individual hooks with no clear grouping. As we add features (difficulty levels, history, etc.), this will become unmanageable.

### wjsutton__tableau-public-mcp

段落标题不一致，需求条目 44 / 84 一致（pdf 拆出 71 条）

- 标题只在 Markdown：Step 1: Create Tool Directory
- 标题只在 Markdown：Step 2: Define Tool Factory
- 标题只在 Markdown：Step 3: Add to Tool Registry
- 标题只在 Markdown：Step 4: Update Tool Name Types
- 标题只在 Markdown：Step 5: Write Tests
- 标题只在 pdf：✅Completed Steps
- 标题只在 pdf：🚀Ready for Use
- 标题只在 pdf：📦Optional Future Steps
- 标题只在 pdf：✅Completed Implementation
- 标题只在 pdf：🎯Critical Success Factors
- 需求只在 Markdown：constructor(params: ToolParams<Args>): Initialises the tool
- 需求只在 Markdown：ListToolsRequestSchema - Returns the list of available tools with their schemas
- 需求只在 Markdown：CallToolRequestSchema - Handles tool execution requests
- 需求只在 Markdown：Tool Callback Return: Tool callbacks return Ok<CallToolResult>, and you must extract the .value property when returning from the request handler.
- 需求只在 Markdown：Error Handling: All errors should be caught within tool callbacks and returned as Ok results with isError: true, rather than throwing exceptions.
- 需求只在 Markdown：get_user_profile - User profile data
- 需求只在 Markdown：get_workbooks_list - List user's workbooks
- 需求只在 Markdown：get_workbook_details - Single workbook metadata
- 需求只在 Markdown：search_visualizations - Search across Tableau Public
- 需求只在 Markdown：get_viz_of_day - Featured visualizations
- 需求只在 pdf：constructor(params:ToolParams<Args>): Initialises the tool
- 需求只在 pdf：Tool Callback Return: Tool callbacks return Ok<CallToolResult>, and you must extract the.value property when returning from the request handler.
- 需求只在 pdf：Error Handling: All errors should be caught within tool callbacks and returned as Ok results with isError:true, rather than throwing exceptions.
- 需求只在 pdf：Parameter explanations with.describe()
- 需求只在 pdf：✅Initialized the project with package.json and all dependencies
- 需求只在 pdf：✅Set up base infrastructure: Tool class, server setup, API client, utilities
- 需求只在 pdf：✅Implemented all 16 tools with full test coverage
- 需求只在 pdf：✅Documented usage in comprehensive README.md with examples
- 需求只在 pdf：✅Built and verified- TypeScript compilation successful
- 需求只在 pdf：✅Project configuration (package.json, tsconfig.json, vitest.config.ts, .gitignore)

### 01MVP__blog-starter

段落标题不一致，需求条目 0 / 7 一致（pdf 拆出 87 条）

- 标题只在 Markdown：01mvp-blog-starter 最终需求文档
- 标题只在 Markdown：1. 项目定位
- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 一句话定位
- 标题只在 Markdown：1.3 项目本质
- 标题只在 pdf：01mvp-blog-starter最终需求文档
- 标题只在 pdf：1.项目定位
- 标题只在 pdf：1.1项目名称
- 标题只在 pdf：1.2一句话定位
- 标题只在 pdf：1.3项目本质
- 需求只在 Markdown：01mvp-blog-starter 是一个基于 Cloudflare 全家桶的个人永久博客 CMS，既支持小白用户通过后台可视化写作，也支持 AI Skill / OpenAPI 自动化发布和维护。
- 需求只在 Markdown：Cloudflare 官方已经提供 TanStack Start 部署支持。已有 TanStack Start 项目可以直接执行 wrangler deploy，Wrangler 会自动检测 TanStack Start 并生成必要配置。(Cloudflare Docs)
- 需求只在 Markdown：Cloudflare 也已经支持 TanStack Start 通过 Cloudflare Vite plugin 部署，并且可以用 create-cloudflare 创建 TanStack Start 项目。(Cloudflare Docs)
- 需求只在 Markdown：Cloudflare Email Sending 等能力作为增强模块。Cloudflare Email Service 的文档显示 Email Sending 属于 public beta，并支持 Workers binding / REST API 等方式发送事务邮件；因此本项目将其设计为可选增强，而不是核心依赖。(Cloudflare Docs)
- 需求只在 Markdown：评论功能必须自研，基于 D1。
- 需求只在 Markdown：且部署记录必须来自 Skill 模拟真实用户流程，不能手工搭建后补材料。
- 需求只在 Markdown：目标：模板站 blog.01mvp.com 可以作为完整博客 CMS 使用。
- 需求只在 pdf：01mvp-blog-starter是一个基于Cloudflare全家桶的个人永久博客CMS，既支持小白用户通过后台可视化写作，也支持AI Skill / OpenAPI自动化发布和维护。
- 需求只在 pdf：一个可复用的Cloudflare-native博客CMS模板
- 需求只在 pdf：一个AI可以使用的Skill，用来自动创建新的博客站点
- 需求只在 pdf：一个统一部署在blog.01mvp.com的模板演示站
- 需求只在 pdf：Cloudflare官方已经提供TanStack Start部署支持。已有TanStack Start项目可以直接执行wrangler deploy，Wrangler会自动检测TanStack Start并生成必要配置。(Cloudflare Docs)
- 需求只在 pdf：Cloudflare也已经支持TanStack Start通过Cloudflare Vite plugin部署，并且可以用create-cloudflare创建TanStack Start项目。(Cloudflare Docs)
- 需求只在 pdf：AI优先使用Cloudflare对应Skill，必要时再使用Wrangler/ Cloudflare API/MCP操作
- 需求只在 pdf：AI引导用户授权登录
- 需求只在 pdf：AI引导用户创建最小权限API Token
- 需求只在 pdf：只有实在无法自动操作时，才让用户手动进Dashboard

### 259876lr__yolo-sop

段落标题不一致，需求条目 18 / 48 一致（pdf 拆出 43 条）

- 标题只在 Markdown：产品需求文档（PRD）- 基于YOLO26的SOP工序检测系统
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：产品需求文档（PRD）-基于YOLO26的SOP工序检测系统
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品背景
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：特性：边缘端优化；描述：专为边缘设备设计；业务价值：支持本地部署，降低硬件成本
- 需求只在 Markdown：特性：多任务统一；描述：检测/跟踪/分割/姿态估计；业务价值：支持复杂工序识别场景
- 需求只在 Markdown：特性：跨平台支持；描述：支持Windows/Linux/Mac；业务价值：部署灵活
- 需求只在 Markdown：特性：自定义手势；描述：支持自定义手势分类；业务价值：适应不同SOP需求
- 需求只在 Markdown：功能ID：F1.1；功能名称：摄像头接入；功能描述：支持USB摄像头、网络摄像头（RTSP/RTMP）接入；优先级：P0
- 需求只在 Markdown：功能ID：F1.2；功能名称：视频文件上传；功能描述：支持上传本地视频文件进行分析；优先级：P1
- 需求只在 Markdown：功能ID：F1.3；功能名称：多路视频支持；功能描述：支持同时接入多个视频源；优先级：P2
- 需求只在 Markdown：功能ID：F1.4；功能名称：视频预处理；功能描述：自动调整分辨率、帧率，支持ROI裁剪；优先级：P1
- 需求只在 Markdown：功能ID：F4.2；功能名称：告警方式；功能描述：支持声音告警、界面提示、消息推送；优先级：P1
- 需求只在 Markdown：功能ID：F4.3；功能名称：告警级别；功能描述：支持不同级别的告警（警告、严重、紧急）；优先级：P1
- 需求只在 pdf：YOLO26核心优势特性描述业务价值One-Stage, One-Box无需NMS后处理推理速度提升30%+，降低系统延迟边缘端优化专为边缘设备设计支持本地部署，降低硬件成本CPU性能提升优化CPU推理无GPU环境也能实时运行多任务统一检测/跟踪/分割/姿态估支持复杂工序识别场景计MediaPipe Hands手势识别优势特性描述业务价值21关键点检测精确检测手部21个关高精度手势识别键点轻量化设计专为移动端/边缘设备CPU实时运行，无需GPU优化跨平台支持支持Windows/Linux/部署灵活Mac自定义手势支持自定义手势分类适应不同SOP需求
- 需求只在 pdf：2.1视频采集模块功能ID功能名称功能描述优先级F1.1 P0摄像头接入支持USB摄像头、网络摄像头（RTSP/ RTMP）接入F1.2 P1视频文件上传支持上传本地视频文件进行分析F1.3 P2多路视频支持支持同时接入多个视频源F1.4 P1视频预处理自动调整分辨率、帧率，支持ROI裁剪
- 需求只在 pdf：2.2实时检测模块功能ID功能名称功能描述优先级F2.1 P0目标检测使用YOLO26实时检测画面中的目标（工人、工具、零件等）F2.2 P0手部定位使用YOLO26检测手部区域，为手势识别提供ROI F2.3 P0手势识别使用MediaPipe在ROI区域内识别手势类型F2.4 P0工序识别基于手势和目标检测结果识别当前执行的工序类型F2.5 P1目标跟踪跟踪工人和工具的位置变化F2.6 P0检测结果可视化在视频画面上实时绘制检测框、手部关键点和手势标签
- 需求只在 pdf：2.3 SOP分析模块功能ID功能名称功能描述优先级F3.1 P0 SOP流程配置配置标准作业流程的步骤序列F3.2 P0工序顺序验证验证工序执行顺序是否符合SOP F3.3 P1工序时长检测检测每个工序的执行时长是否在合理范围F3.4 P0工序遗漏检测检测是否有工序被遗漏F3.5 P1异常行为识别识别非标准操作行为
- 需求只在 pdf：2.4异常告警模块功能ID功能名称功能描述优先级F4.1 P0实时告警检测到异常时实时触发告警F4.2 P1告警方式支持声音告警、界面提示、消息推送F4.3 P1告警级别支持不同级别的告警（警告、严重、紧急）F4.4 P1告警记录记录所有告警事件，支持查询和
- 需求只在 pdf：2.5数据统计模块功能ID功能名称功能描述优先级F5.1 P0实时统计实时显示检测统计数据F5.2 P1历史数据查询按时间、工位、工序等条件查询历史数据F5.3 P0合规率统计统计SOP合规率、各工序执行情况F5.4 P2趋势分析分析合规率变化趋势
- 需求只在 pdf：2.6报告生成模块功能ID功能名称功能描述优先级F6.1 P1自动报告自动生成日报、周报、月报F6.2 P2自定义报告支持自定义报告模板和内容F6.3 P1报告导出支持导出PDF、Excel格式
- 需求只在 pdf：2.7 Web管理平台功能ID功能名称功能描述优先级F7.1 P0实时监控页面显示实时视频流功能ID功能名称功能描述优先级和检测结果F7.2 P1历史回放页面回放历史视频和检测记录F7.3 P1统计分析页面展示各类统计图表F7.4 P0系统配置页面配置系统参数、SOP流程、告警规则F7.5 P1用户管理页面管理用户账号和权限
- 需求只在 pdf：2.8模型训练平台功能ID功能名称功能描述优先级F8.1 P1数据上传上传训练数据和标注文件F8.2 P2数据标注提供在线标注工
- 需求只在 pdf：指标要求说明mAP@0.5≥ 85%检测精度在标准测试集上的精度GPU ≥ 45 FPS, CPU ≥推理速度单路视频流处理速度30 FPS ≤ 200ms系统延迟从视频采集到结果输出的延迟并发能力支持4路视频同时处理单服务器并发处理能力指标要求说明响应时间Web页面加载≤3s页面首次加载时间

### 5kyfkr__siyuan-plugin-task-horizon

段落标题不一致，需求条目 121 / 148 一致（pdf 拆出 147 条）

- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：2. 目标用户
- 标题只在 Markdown：3. 使用场景
- 标题只在 Markdown：4. 范围
- 标题只在 Markdown：4.1 本期必须覆盖
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：2.目标用户
- 标题只在 pdf：3.使用场景
- 标题只在 pdf：4.范围
- 标题只在 pdf：4.1本期必须覆盖
- 需求只在 Markdown：导入导出：滴答清单 CSV 导入、当前分组任务导出、汇总 Markdown/Excel 类能力。
- 需求只在 Markdown：content / markdown：任务标题和原始 Markdown。
- 需求只在 Markdown：parentTaskId / children：父子任务关系。
- 需求只在 Markdown：h2 / h2Id / h2Path：所属标题，标题层级可配置。
- 需求只在 Markdown：priority：重要性，支持高/中/低/无，对应 A/B/C/none。
- 需求只在 Markdown：自定义分组：手动添加文档 ID，可选择包含子文档。
- 需求只在 Markdown：逾期风险任务。
- 需求只在 Markdown：移动端和 Dock 使用浮动工具条，不遮挡多选条。
- 需求只在 Markdown：移动端支持长按 1 秒新建日程或拖动已有日程。
- 需求只在 Markdown：备注编辑，支持 Markdown 工具。
- 需求只在 pdf：导入导出：滴答清单CSV导入、当前分组任务导出、汇总Markdown/Excel类能力。
- 需求只在 pdf：content/markdown：任务标题和原始Markdown。
- 需求只在 pdf：parentTaskId/children：父子任务关系。
- 需求只在 pdf：h2/h2Id/h2Path：所属标题，标题层级可配置。
- 需求只在 pdf：priority：重要性，支持高/中/低/无，对应A/B/C/none。
- 需求只在 pdf：自定义分组：手动添加文档ID，可选择包含子文档。
- 需求只在 pdf：移动端和Dock使用浮动工具条，不遮挡多选条。
- 需求只在 pdf：移动端支持长按1秒新建日程或拖动已有日程。
- 需求只在 pdf：备注编辑，支持Markdown工具。
- 需求只在 pdf：附件区：图片、PDF、普通文件、文档链接、块链接；支持粘贴剪贴板附件或文档ID。

### AlanDXiang__Google_ADK_Chat

段落标题不一致，需求条目 8 / 55 一致（pdf 拆出 53 条）

- 标题只在 Markdown：Google ADK 本地Web大模型交互平台项目需求文档
- 标题只在 Markdown：1. 引言
- 标题只在 Markdown：1.1 项目背景与意义
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 项目范围
- 标题只在 pdf：Google ADK本地Web大模型交互平台项目需求文档
- 标题只在 pdf：1.引言
- 标题只在 pdf：2.总体设计
- 标题只在 pdf：3.详细功能需求
- 标题只在 pdf：4.非功能性需求
- 需求只在 Markdown：Web技术 (HTML/CSS/JavaScript + Python Web框架)：用于构建用户友好的本地Web界面。
- 需求只在 Markdown：描述：应用需包含一个本地Web服务器，用户可以通过浏览器访问指定端口（例如 http://localhost:8000）来打开UI界面。
- 需求只在 Markdown：验收标准：成功启动后，在浏览器输入地址能正确加载和显示UI。
- 需求只在 Markdown：描述：UI界面应包含一个输入框供用户输入文本，一个展示区域显示用户与大模型的对话历史。
- 需求只在 Markdown：验收标准：用户可以顺畅地输入文本并发送；对话历史能够清晰、有序地展示。
- 需求只在 Markdown：FR1.3: 大模型集成与对话
- 需求只在 Markdown：描述：用户在UI界面输入问题后，系统应能将问题发送给通过 .env 或环境变量配置的大模型，并将模型的响应结果展示在UI界面上。
- 需求只在 Markdown：验收标准：能够成功调用配置的大模型API并获取响应；响应内容正确显示在对话界面。
- 需求只在 Markdown：FR1.4: 基础对话管理
- 需求只在 Markdown：描述：支持简单的多轮对话上下文（具体实现依赖于ADK和大模型本身的能力）。
- 需求只在 pdf：1项目背景与意义
- 需求只在 pdf：随着大型语言模型（LLM）技术的飞速发展，其在各个领域的应用潜力日益凸显。为了更便捷地利用和扩展这些模型的能力，我们需要一个灵活、易用且功能强大的开发与交互平台。本项目旨在基于Google的Agent Development Kit (ADK)，构建一个本地化的Web应用，使用户能够方便地与大模型进行对话，并能灵活配置和扩展模型及相关工具。这不仅能加速AI应用的开发迭代，更能激发创新思维，探索大模型应用的更多可能性。
- 需求只在 pdf：本地化Web界面：提供一个在本地运行的Web用户界面，用于与大模型进行实时对话。
- 需求只在 pdf：灵活的模型配置：通过.env文件及环境变量，轻松配置大模型的连接参数（如base_url,model,api_key等）。
- 需求只在 pdf：可定制的MCP工具：支持用户自定义添加和修改ADK中的模型中心处理（MCP）工具，增强应用的扩展性。
- 需求只在 pdf：Python为核心：项目主要采用Python语言进行开发，充分利用其在AI领域的生态优势。
- 需求只在 pdf：包含范围：o本地Web服务器的搭建与UI界面的基础实现。o通过UI界面发送用户输入到大模型，并展示模型返回结果。o实现从.env文件和环境变量读取模型配置信息的功能，并确保环境变量的优先性。o提供添加和修改MCP工具的机制和接口文档。o使用Python作为主要的后端开发语言。
- 需求只在 pdf：暂不包含范围（可作为未来迭代）：o复杂的用户认证与授权系统。o多用户并发处理的深度优化。o高级数据分析与可视化功能。o移动端应用的适配。
- 需求只在 pdf：ADK项目主页:https://github.com/google/adk-python
- 需求只在 pdf：ADK项目说明文档:https://google.github.io/adk-docs/

### Ariestar__obsidian-dragger

段落标题不一致，需求条目 35 / 150 一致（pdf 拆出 156 条）

- 标题只在 Markdown：1. 一句话目标
- 标题只在 Markdown：2. 背景
- 标题只在 Markdown：3. 用户目标
- 标题只在 Markdown：3.1 桌面端
- 标题只在 Markdown：3.2 移动端：未开启长按文本拖拽
- 标题只在 pdf：1.一句话目标
- 标题只在 pdf：2.背景
- 标题只在 pdf：3.用户目标
- 标题只在 pdf：3.1桌面端
- 标题只在 pdf：3.2移动端：未开启长按文本拖拽
- 需求只在 Markdown：桌面端不需要 mobile drag mode。
- 需求只在 Markdown：不需要右上角 mobile drag mode。
- 需求只在 Markdown：不应因为没有开启 mobile drag mode 而禁止手柄拖拽。
- 需求只在 Markdown：如果当前设置不是"始终显示手柄"，移动端应由 platform 实现自己的手柄触达策略，而不是让 drag 层知道移动端差异。
- 需求只在 Markdown：移动端手柄触达策略可以和桌面 hover 不同，但最终仍翻译成 source = handle 的同一种 interaction event。
- 需求只在 Markdown：由于文本长按容易误触，此模式需要 mobile drag mode 作为外部开关。
- 需求只在 Markdown：关闭 mobile drag mode 时，所有依赖文本长按拖拽的移动端子模式必须退出并清理 UI。
- 需求只在 Markdown：platform 负责 hit-test、timer、移动阈值和坐标解析，然后提交事件。
- 需求只在 Markdown：drag 负责根据当前 state 和 event 决定状态转换。
- 需求只在 Markdown：hold_start 表示用户按住了一个可交互对象，但还没开始拖。
- 需求只在 pdf：桌面端不需要mobile drag mode。
- 需求只在 pdf：不需要右上角mobile drag mode。
- 需求只在 pdf：不应因为没有开启mobile drag mode而禁止手柄拖拽。
- 需求只在 pdf：如果当前设置不是"始终显示手柄"，移动端应由platform实现自己的手柄触达策略，而不是让drag层知道移动端差异。
- 需求只在 pdf：移动端手柄触达策略可以和桌面hover不同，但最终仍翻译成source=handle的同一种interaction event。
- 需求只在 pdf：由于文本长按容易误触，此模式需要mobile drag mode作为外部开关。
- 需求只在 pdf：关闭mobile drag mode时，所有依赖文本长按拖拽的移动端子模式必须退出并清理UI。
- 需求只在 pdf：platform负责hit-test、timer、移动阈值和坐标解析，然后提交事件。
- 需求只在 pdf：drag负责根据当前state和event决定状态转换。
- 需求只在 pdf：hold_start表示用户按住了一个可交互对象，但还没开始拖。

### ChrisChen667788__wind-comic

段落标题不一致，需求条目 16 / 183 一致（pdf 拆出 171 条）

- 标题只在 Markdown：AI-Comic-Studio v2.0 产品升级 PRD（OiiOii 同构竞品反击战）
- 标题只在 Markdown：一、现状基线 vs OiiOii 差距盘点
- 标题只在 Markdown：1.1 当前 ai-comic-studio 前端基线
- 标题只在 Markdown：1.2 OiiOii 已具备而我方缺失的能力
- 标题只在 Markdown：1.3 我方独有 OiiOii 没有的护城河（不能丢）
- 标题只在 pdf：AI-Comic-Studio v2.0产品升级PRD（OiiOii同构竞品反击战）
- 标题只在 pdf：一、现状基线vs OiiOii差距盘点
- 标题只在 pdf：1.1当前ai-comic-studio前端基线
- 标题只在 pdf：1.2 OiiOii已具备而我方缺失的能力
- 标题只在 pdf：1.3我方独有OiiOii没有的护城河（不能丢）
- 需求只在 Markdown：✅ Seedance 2.0 走 即梦官方 API（非 fal.ai）
- 需求只在 Markdown：✅ 风格库缩略图采用 Midjourney API 批量生图（复用现有 mj service）
- 需求只在 Markdown：✅ 上线 Beta 邀请码闸（Sprint 0 内交付）
- 需求只在 Markdown：✅ 暂不做 4K；新增分辨率设置选项，上限 720P（提供 360P / 480P / 720P 三档）
- 需求只在 Markdown：✅ 5 大创作模式 全部保留，按 Sprint 0/1 分阶段交付
- 需求只在 Markdown：配色：保留现有黑色主题（与 OiiOii 浅色形成区隔），主色 #7C3AED（Purple-600）
- 需求只在 Markdown：字体：保留现有 Inter / 思源黑体
- 需求只在 Markdown：卡片：圆角 16px，hover 上浮 4px + 投影
- 需求只在 Markdown：模式卡片：每张 200×260px，含 emoji icon + 标题 + 时长说明 + "开始 →"
- 需求只在 Markdown：顶部新增"托管 / 对话"切换器
- 需求只在 pdf：✅Seedance 2.0走即梦官方API（非fal.ai）
- 需求只在 pdf：✅风格库缩略图采用Midjourney API批量生图（复用现有mj service）
- 需求只在 pdf：✅上线Beta邀请码闸（Sprint 0内交付）
- 需求只在 pdf：✅暂不做4K；新增分辨率设置选项，上限720P（提供360P / 480P / 720P三档）
- 需求只在 pdf：✅5大创作模式全部保留，按Sprint 0/1分阶段交付
- 需求只在 pdf：2.1新首页/(借鉴OiiOii的"模式入口"理念)
- 需求只在 pdf：配色：保留现有黑色主题（与OiiOii浅色形成区隔），主色#7C3AED（Purple-600）
- 需求只在 pdf：字体：保留现有Inter /思源黑体
- 需求只在 pdf：卡片：圆角16px，hover上浮4px +投影
- 需求只在 pdf：模式卡片：每张200×260px，含emoji icon +标题+时长说明+"开始→"

### Cicada0719__moeplay-tauri

段落标题不一致，需求条目 10 / 87 一致（pdf 拆出 72 条）

- 标题只在 Markdown：萌游 (moeplay-tauri) 规则系统与观看体验修复 — 产品需求文档
- 标题只在 Markdown：1. 背景与目标
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标
- 标题只在 Markdown：1.3 成功指标
- 标题只在 pdf：萌游(moeplay-tauri)规则系统与观看体验修复—产品需求文档
- 标题只在 pdf：1.背景与目标
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2目标
- 标题只在 pdf：1.3成功指标
- 需求只在 Markdown：指标：历史记录同步端到端成功率（双设备验证）；基线（现状）：不支持；目标值：≥ 95%（冲突可解决）
- 需求只在 Markdown：指标：漫画双页模式渲染帧率（1080p，中等配置）；基线（现状）：不支持；目标值：≥ 50 FPS，翻页延迟 < 100ms
- 需求只在 Markdown：作为高级用户，我希望能导入/导出第三方规则文件（兼容 kazumi 风格的规则格式），以便自行扩展源而不必等待官方更新。
- 需求只在 Markdown：重构规则（源）子系统，所有内容类型（番剧/漫画/小说）共用一套规则生命周期：加载 → 校验 → 执行（搜索/详情/章节/播放地址解析）→ 错误上报。规则执行在独立隔离环境中运行（前端沙箱或 Rust 侧 quickjs/boa 引擎），单条规则异常不得影响应用主体。
- 需求只在 Markdown：Given 一条语法错误的规则文件，When 应用加载规则，Then 该规则被标记为"无效"并在源列表中置灰，应用其余功能正常运行，日志中记录具体错误行信息。
- 需求只在 Markdown：Given 一条规则在解析播放地址时抛出异常，When 用户点击播放，Then 界面展示"该源解析失败，建议切换源"的可操作提示（含"切换源"按钮），应用不崩溃、不白屏。
- 需求只在 Markdown：Given 20 条规则同时加载，When 其中 5 条超时（>10s），Then 超时的 5 条被单独标记失败，其余 15 条正常可用。
- 需求只在 Markdown：修复源切换 bug：切换源时必须保留当前内容的上下文（条目标识、集/话/章序号、播放进度），并在新源中自动定位到对应位置；若新源无该集数，则定位到最近可用集并提示用户。
- 需求只在 Markdown：Given 用户在源 A 观看某番第 5 集、进度 12:30，When 切换到源 B 且源 B 存在第 5 集，Then 播放器加载源 B 第 5 集并从 12:30（±10s 容差）续播。
- 需求只在 Markdown：Given 源 B 仅有 1~3 集，When 用户从源 A 第 5 集切换到源 B，Then 播放器定位到第 3 集并 Toast 提示"当前源暂无第 5 集，已跳转至最新一集"。
- 需求只在 pdf：指标基线（现状）目标值≥ 80%内置源健康检查通过率<30%（多数失效）（每日CI探测）≥ 90%源切换后首次播放成功不稳定率（手动测试抽样，每类源各10个条目）源切换异常导致的崩溃频发0（全部降级为可恢复/白屏次数错误提示）0%100%超清画质下控制栏3秒自动隐藏成功率历史记录同步端到端成不支持≥95%（冲突可解决）功率（双设备验证）漫画双页模式渲染帧率不支持≥ 50 FPS，翻页延迟< 100ms（1080p，中等配置）—旧版本历史数据迁移成100%（含失败回滚）功率
- 需求只在 pdf：作为高级用户，我希望能导入/导出第三方规则文件（兼容kazumi风格的规则格式），以便自行扩展源而不必等待官方更新。
- 需求只在 pdf：重构规则（源）子系统，所有内容类型（番剧/漫画/小说）共用一套规则生命周期：加载→校验→执行（搜索/详情/章节/播放地址解析）→错误上报。规则执行在独立隔离环境中运行（前端沙箱或Rust侧quickjs/boa引擎），单条规则异常不得影响应用主体。
- 需求只在 pdf：Given一条语法错误的规则文件，When应用加载规则，Then该规则被标记为"无效"并在源列表中置灰，应用其余功能正常运行，日志中记录具体错误行信息。
- 需求只在 pdf：Given一条规则在解析播放地址时抛出异常，When用户点击播放，Then界面展示"该源解析失败，建议切换源"的可操作提示（含"切换源"按钮），应用不崩溃、不白屏。
- 需求只在 pdf：Given 20条规则同时加载，When其中5条超时（>10s），Then超时的5条被单独标记失败，其余15条正常可用。
- 需求只在 pdf：修复源切换bug：切换源时必须保留当前内容的上下文（条目标识、集/话/章序号、播放进度），并在新源中自动定位到对应位置；若新源无该集数，则定位到最近可用集并提示用户。
- 需求只在 pdf：Given用户在源A观看某番第5集、进度12:30，When切换到源B且源B存在第5集，Then播放器加载源B第5集并从12:30（±10s容差）续播。
- 需求只在 pdf：Given源B仅有1~3集，When用户从源A第5集切换到源B，Then播放器定位到第3集并Toast提示"当前源暂无第5集，已跳转至最新一集"。
- 需求只在 pdf：Given连续快速切换源3次，When切换进行中，Then仅最后一次切换生效（前序请求被取消，无竞态导致的串源播放）。

### DTrader-store__formula-ts

段落标题不一致，需求条目 49 / 146 一致（pdf 拆出 109 条）

- 标题只在 Markdown：Formula-TS 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 核心价值主张
- 标题只在 pdf：Formula-TS产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定义
- 标题只在 pdf：1.2产品愿景
- 标题只在 pdf：1.3核心价值主张
- 需求只在 Markdown：兼容性: 完全兼容通达信公式语法，降低用户学习成本
- 需求只在 Markdown：高性能: 支持大规模数据计算（10000+ 数据点），增量计算延迟 < 100ms
- 需求只在 Markdown：同构设计: 同时支持浏览器和 Node.js 环境
- 需求只在 Markdown：易于集成: 简洁的 API 设计，开箱即用
- 需求只在 Markdown：可扩展性: 灵活的函数注册机制，易于添加自定义函数
- 需求只在 Markdown：教育工作者: 教授技术分析课程，需要演示工具
- 需求只在 Markdown：个人投资者: 具备编程能力，希望自建分析工具
- 需求只在 Markdown：词法分析：将公式文本转换为 Token 流
- 需求只在 Markdown：语法分析：构建抽象语法树 (AST)
- 需求只在 Markdown：能正确解析 MA、MACD、KDJ 等经典指标公式
- 需求只在 pdf：兼容性:完全兼容通达信公式语法，降低用户学习成本
- 需求只在 pdf：高性能:支持大规模数据计算（10000+数据点），增量计算延迟< 100ms
- 需求只在 pdf：同构设计:同时支持浏览器和Node.js环境
- 需求只在 pdf：易于集成:简洁的API设计，开箱即用
- 需求只在 pdf：可扩展性:灵活的函数注册机制，易于添加自定义函数
- 需求只在 pdf：教育工作者:教授技术分析课程，需要演示工具
- 需求只在 pdf：个人投资者:具备编程能力，希望自建分析工具
- 需求只在 pdf：词法分析：将公式文本转换为Token流
- 需求只在 pdf：语法分析：构建抽象语法树(AST)
- 需求只在 pdf：支持通达信基础语法：o变量声明（:=）o输出声明（:）o算术运算符（+,-,*,/）o比较运算符（>,<,>=,<=,=,<>）o逻辑运算符（AND,OR）o函数调用o括号表达式

### FLYFISH567__ItemMemo

段落标题不一致，需求条目 96 / 116 一致（pdf 拆出 116 条）

- 标题只在 Markdown：物品价值记录网页版 PRD
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品简介
- 标题只在 Markdown：1.3 产品目标
- 标题只在 pdf：物品价值记录网页版PRD
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品名称
- 标题只在 pdf：1.2产品简介
- 标题只在 pdf：1.3产品目标
- 需求只在 Markdown：理性消费用户
- 需求只在 Markdown：精致生活 / 收纳管理用户
- 需求只在 Markdown：数码 / 家居 / 装备爱好者
- 需求只在 Markdown：年轻上班族 / 学生
- 需求只在 Markdown：需要一个轻量工具帮助自己管理生活和消费。
- 需求只在 Markdown：缺少一个兼顾"物品管理 + 成本分析 + 提醒"的工具
- 需求只在 Markdown：产品闭环完整：录入 → 查看 → 提醒 → 复盘
- 需求只在 Markdown：新增物品弹窗 / 面板
- 需求只在 Markdown：操作按钮（标记完成 / 稍后提醒）
- 需求只在 Markdown：价格必填且大于等于 0
- 需求只在 pdf：理性消费用户希望知道买的东西到底值不值，愿意做消费复盘。
- 需求只在 pdf：精致生活/收纳管理用户有整理习惯，愿意把生活物品数字化管理。
- 需求只在 pdf：数码/家居/装备爱好者购买金额高、物品使用周期长，更关心长期价值。
- 需求只在 pdf：年轻上班族/学生需要一个轻量工具帮助自己管理生活和消费。
- 需求只在 pdf：缺少一个兼顾"物品管理+成本分析+提醒"的工具
- 需求只在 pdf：产品闭环完整：录入→查看→提醒→复盘
- 需求只在 pdf：新增物品弹窗/面板
- 需求只在 pdf：操作按钮（标记完成/稍后提醒）
- 需求只在 pdf：价格必填且大于等于0
- 需求只在 pdf：AI自然语言录入

### FlashingChen__dsh-desktop-hub

段落标题不一致，需求条目 1 / 54 一致（pdf 拆出 54 条）

- 标题只在 Markdown：DSH Desktop Hub — 产品需求文档（PRD）
- 标题只在 Markdown：0. 原始需求（未改动）
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：1.1 DSH 是什么
- 标题只在 Markdown：1.2 生态现状（调研对象）
- 标题只在 pdf：DSH Desktop Hub —产品需求文档（PRD）
- 标题只在 pdf：0.原始需求（未改动）
- 标题只在 pdf：1.背景
- 标题只在 pdf：1.1 DSH是什么
- 标题只在 pdf：1.2生态现状（调研对象）
- 需求只在 Markdown：DSH 最近发布，其理念是一切皆插件，因此我们需要构建一个桌面端，在桌面端内集成所有功能，用户无需安装 Node、CS 等运行环境，双击打开桌面端即可进入 DSH harness。
- 需求只在 Markdown：插件系统（Plugin）：负责管理、安装和移除本机 DSH 的所有插件；
- 需求只在 Markdown：MCP 系统：将普通 JSON 格式转换为 DeepSeek 所需的 YAML 格式；
- 需求只在 Markdown：Skills 系统：负责管理 DeepSeek 可用的 skills；
- 需求只在 Markdown：第四个系统暂不做，目前只保留以上几个系统。
- 需求只在 Markdown：当前的使用门槛正是用户要解决的痛点：必须自己安装 Node.js（+ pnpm），再执行命令启动；没有开箱即用的桌面入口。
- 需求只在 Markdown：项目：mcporter；Stars：—；定位：第三方 MCP 配置管理工具，支持 mcporter config import claude-code；与本项目关系：验证了「JSON MCP 配置 → 目标格式」转换的行业惯例
- 需求只在 Markdown：项目根 = 向上找最近含 .git 的祖先目录；找不到则用 cwd。
- 需求只在 Markdown：skill 身份：kebab-case 名称（^[a-z0-9]+(?:-[a-z0-9]+)*$）。两种形态：目录包 <name>/SKILL.md 或扁平文件 <name>.md。
- 需求只在 Markdown：frontmatter 元数据：name、description、可选 disable-model-invocation、user-invocable（缺省均视为 true）。模型只看到 name + description，绝不暴露正文/路径。
- 需求只在 pdf：插件系统（Plugin）：负责管理、安装和移除本机DSH的所有插件；
- 需求只在 pdf：MCP系统：将普通JSON格式转换为DeepSeek所需的YAML格式；
- 需求只在 pdf：Skills系统：负责管理DeepSeek可用的skills；
- 需求只在 pdf：第四个系统暂不做，目前只保留以上几个系统。整体流程：写入PRD供审核→审核通过后自行制定plan，按MVP拆分，每次只做一件事，以最小可验证的方式推进，自行测试。
- 需求只在 pdf：1.0-rc.6（2026-08-16实测；developer preview，官方声明会有破坏性变更）项值底层框架Cordis（时空可组合的插件框架）Node.js^22.19.0||>=24.0.0+运行时依赖pnpm 11.7.0 npm包@deepseek-ai/dsh（bin:dsh）npx@deepseek-ai/dsh web→启动方式本地Web UI
- 需求只在 pdf：当前的使用门槛正是用户要解决的痛点：必须自己安装Node.js（+pnpm），再执行命令启动；没有开箱即用的桌面入口。
- 需求只在 pdf：项目根=向上找最近含.git的祖先目录；找不到则用cwd。
- 需求只在 pdf：skill身份：kebab-case名称（^[a-z0-9]+(?:-[a-z0-9]+)*$）。两种形态：目录包<name>/SKILL.md或扁平文件<name>.md。
- 需求只在 pdf：frontmatter元数据：name、description、可选disable-model- invocation、user-invocable（缺省均视为true）。模型只看到name+ description，绝不暴露正文/路径。
- 需求只在 pdf：模型侧消费：面向模型的skill({name})工具；会话早期以user-role <system-reminder>注入<available_skills>目录；目录digest变化才追加替换（增量注入，不浪费token）。

### Frank-ay__mimo-mcp

段落标题不一致，需求条目 1 / 62 一致（pdf 拆出 55 条）

- 标题只在 Markdown：MiMo MCP Server — 产品需求文档(PRD v1.0)
- 标题只在 Markdown：1. 背景(Context)
- 标题只在 Markdown：2. 目标与非目标
- 标题只在 Markdown：非目标(Out of Scope,V1 不做)
- 标题只在 Markdown：3. 目标用户与典型使用场景
- 标题只在 pdf：MiMo MCP Server —产品需求文档(PRD v1.0)
- 标题只在 pdf：1.背景(Context)
- 标题只在 pdf：2.目标与非目标
- 标题只在 pdf：非目标(Out of Scope,V1不做)
- 标题只在 pdf：3.目标用户与典型使用场景
- 需求只在 Markdown：实现语言:Python 3.11 + FastMCP(用 uv 管理依赖)
- 需求只在 Markdown：Transport:仅 stdio(Claude Code + Codex 双注册)
- 需求只在 Markdown：Web 前端栈:Vite + React + shadcn/ui(独立打包,本地 127.0.0.1)
- 需求只在 Markdown：MVP 范围:全功能 F1-F8(Chat / 图像 / 视频 / TTS / 声音克隆 / 声音设计 / ASR / Dashboard 全部纳入 V1)
- 需求只在 Markdown：ASR 兜底:仅云端,无本地兜底,云端缺失则 F7 显式 unavailable
- 需求只在 Markdown：阶段：V1 (MVP,本次交付)；内容：F1-F8 全量(含 ASR);stdio MCP + 本地 Web;支持 Claude Code/Codex 双注册;voice 库 SQLite 持久化
- 需求只在 Markdown：层：HTTP Client；选型：httpx (async)；理由：与 FastMCP/FastAPI 异步生态一致,支持流式
- 需求只在 Markdown：voices(voice_id PK, name, source[default|clone|design], reference_path, voice_prompt, status, created_at)
- 需求只在 Markdown：sessions(id PK, kind, payload_json, created_at)(Web 沙盒会话)
- 需求只在 Markdown：audit_log(id PK, ts, channel[mcp|web], tool, model, input_tokens, output_tokens, latency_ms, status, error)
- 需求只在 pdf：实现语言:Python 3.11 + FastMCP(用uv管理依赖)
- 需求只在 pdf：Transport:仅stdio(Claude Code + Codex双注册)
- 需求只在 pdf：Web前端栈:Vite + React + shadcn/ui(独立打包,本地127.0.0.1)
- 需求只在 pdf：MVP范围:全功能F1-F8(Chat /图像/视频/ TTS /声音克隆/声音设计/ ASR / Dashboard全部纳入V1)
- 需求只在 pdf：ASR兜底:仅云端,无本地兜底,云端缺失则F7显式unavailable
- 需求只在 pdf：阶段内容V1 (MVP,本次交付) F1-F8全量(含ASR);stdio MCP +本地Web;支持Claude Code/Codex双注册;voice库SQLite持久化V1.1流式TTS;Web端批量任务队列;ASR长音频分片;Web国际化V2 HTTP/SSE远程transport;OAuth;多用户音色库;与Void/lay- screenwriter/libtv等skill串联工作流模板
- 需求只在 pdf：│├──run_mcp.sh#stdio启动脚本(Codex因TOML不支持env
- 需求只在 pdf：文件系统(data/artifacts/) o voice_refs/<voice_id>.wav参考音频o tts/<yyyymmdd>/<uuid>.wav合成产物o uploads/<yyyymmdd>/<uuid>.{jpg|mp4|...}用户上传
- 需求只在 pdf：保留策略:V1不自动清理,Web提供"清理30天前"按钮。
- 需求只在 pdf：安全:API Key仅出现在.env(.gitignore)、不写日志;Web UI默认仅127.0.0.1监听,不暴露公网;克隆素材本地保存,前端禁止外链。

### G1-kiyo__agent

段落标题不一致，需求条目 97 / 107 一致（pdf 拆出 106 条）

- 标题只在 Markdown：AI 资讯社交协作平台
- 标题只在 Markdown：2.1 产品定位
- 标题只在 Markdown：2.2 核心价值主张
- 标题只在 Markdown：2.3 目标用户
- 标题只在 Markdown：2.4 产品范围
- 标题只在 pdf：AI资讯社交协作平台
- 标题只在 pdf：2.1产品定位
- 标题只在 pdf：2.2核心价值主张
- 标题只在 pdf：2.3目标用户
- 标题只在 pdf：2.4产品范围
- 需求只在 Markdown：AI智能资讯检索（多轮Agent Loop）
- 需求只在 Markdown：RAG知识库（文档入库 + 检索增强）
- 需求只在 Markdown：执行链路可视化（节点流转、日志追踪）
- 需求只在 Markdown：群组协作与讨论（发布、评论、投票）
- 需求只在 Markdown：人工审核与干预（interrupt + resume）
- 需求只在 Markdown：检查点管理与重放（审计、合规）
- 需求只在 Markdown：企业级认证与权限（JWT + RBAC）
- 需求只在 Markdown：技术点：Function Calling；成熟度：⭐⭐⭐⭐⭐；风险：低；应对策略：主流模型均支持
- 需求只在 Markdown：用户输入问题后，AI Agent自主决策是否需要搜索、搜索什么、何时结束并生成答案。
- 需求只在 Markdown：故障恢复 < 5分钟
- 需求只在 pdf：LangGraph状态低官方稳定API机Function Calling⭐⭐⭐⭐⭐低主流模型均支持
- 需求只在 pdf：subgraph企业必须["5.审计合规(企业必须)"] E1[执行回放] E2[审计日志] E3[确定性验证]
- 需求只在 pdf：需求描述：用户输入问题后，AI Agent自主决策是否需要搜索、搜索什么、何时结束并生成答案。
- 需求只在 pdf：3.1群组发布与推送
- 需求只在 pdf：4.1话题自动归档
- 需求只在 pdf：6.2权限控制（RBAC）角色权限范围管理员全部权限管理者查看、创建、审核、审计分析师查看、创建普通成员查看访客仅查看公开内容
- 需求只在 pdf：故障恢复<5分钟
- 需求只在 pdf：C-->D{需要工具?} D-->|是|E[Tools节点Function Call]
- 需求只在 pdf：C-->F{需要审核?} F-->|是|G[Admin节点interrupt]

### GCWing__OpenBitFun

段落标题不一致，需求条目 2 / 38 一致（pdf 拆出 5 条）

- 标题只在 Markdown：OpenBitFun 可配置开发体验产品需求
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：2. 产品目标
- 标题只在 Markdown：3. 用户画像
- 标题只在 Markdown：4. 核心体验路径
- 标题只在 pdf：OpenBitFun可配置开发体验产品需求
- 标题只在 pdf：1.背景
- 标题只在 pdf：2.产品目标
- 标题只在 pdf：3.用户画像
- 标题只在 pdf：4.核心体验路径
- 需求只在 Markdown：路径：执行安全；触发：高权限 shell、网络、凭据、MCP、hook、删除、跨目录写；体验呈现：安全确认、范围、后果、可选隔离路径；系统动作：安全边界独立判定 allow/ask/deny/应急放行
- 需求只在 Markdown：规格：检查建议；用户可见结果：推荐检查、不可运行原因、替代验证和跳过后果；产品约束：推荐检查不等同阻断；强制检查必须有配置、确定性失败或用户显式升级来源
- 需求只在 Markdown：规格：沙箱与执行位置；用户可见结果：本机/远程/容器/ACP/MCP/插件/浏览器动作的位置、隔离等级组合、降级原因和可选替代路径；产品约束：只有真实隔离存在时才展示"沙箱允许"；权限确认不能包装成系统级沙箱
- 需求只在 Markdown：规格：阶段性收益；用户可见结果：当前阶段用户能得到的体验变化、必要技术前置、延期边界和质量一致性说明；产品约束：不用完整模块边界代替阶段收益；后台技术能力必须说明服务哪个用户场景
- 需求只在 Markdown：规格：团队配置；用户可见结果：配置来源、优先级、冲突状态和生效范围；产品约束：团队配置需要可解释；冲突规则先提示或降级，不静默选择高风险路径
- 需求只在 Markdown：产品入口与组件：安全确认面板；变更：展示命令/文件/域名/凭据、授权范围、执行位置、沙箱等级、后果、允许一次/会话/拒绝/隔离选项；默认状态：仅安全动作触发；触发条件：shell、网络、凭据、删除、跨目录写、发布
- 需求只在 Markdown：用例：未知网络命令或外部访问；质量要求：安全高敏；触发条件：shell、网络、凭据、删除、跨目录写或发布动作触发安全边界；体验变化：弹出安全确认面板，展示命令、域名、目的、授权范围、后果和隔离选项；用户收益：用户能快速判断是否允许执行，并控制授权范围；验收点：用户确认后只在声明范围内生效；拒绝或隔离路径可继续任务
- 需求只在 Markdown：用例：受管路径或团队规则命中；质量要求：团队定义；触发条件：变更命中 CODEOWNERS、CI、路径规则、受保护分支或组织策略；体验变化：折叠展示团队规则来源、优先级、强制项和冲突处理；用户收益：用户知道为什么需要额外检查，并能定位负责人或规则来源；验收点：阻断来源可追踪；风险接受和强制检查有记录
- 需求只在 Markdown：用例：远程或云端执行；质量要求：按任务风险；触发条件：SSH、容器、Dev Container、远程工作区或云端异步任务；体验变化：在任务头和安全确认中固定显示执行主机、路径映射、端口/网络边界和不可用能力；用户收益：用户能分清本地与远程能力差异，减少误操作和无效验证；验收点：不可支持能力有替代路径；网络和端口范围可确认
- 需求只在 Markdown：边界：内部策略与用户语言；产品判定：内部策略画像可以存在；用户侧不直接学习内部模式名，只看到自然语言状态、原因和操作
- 需求只在 pdf：组织拒绝/受管强制要求>安全边界>最近确认的路径或团队规则>工作区配置>允许范围内的会话/任务覆盖>全局/用户默认值
- 需求只在 pdf：PR就绪度采用率P2+验证团队协作价值强制检查精度P2+控制低价值门禁不可支持状态恢复率验证替代路径是否能帮助用户继续推进跨入口语义一致率验证不同平台是否保留相同任务状态、安全范围和验证摘要关键用例验收覆盖率验证主要体验用例是否有可回放用例、预期交互和用户收益说明
- 需求只在 pdf：本表的P0/P1指SDLC Harness的默认开发体验阶段。插件运行时主线的P0以../architecture/product-architecture.md为准：插件可用性必须由真实生产入口和端到端调用证明；SDLC Harness不用空接口、静态候选或未预算界面贡献代替该执行闭环。

### HowlandMai__EmberIM

段落标题不一致，需求条目 26 / 69 一致（pdf 拆出 61 条）

- 标题只在 Markdown：产品需求文档（PRD · Product Requirements Document）
- 标题只在 Markdown：1. 引言与项目定位
- 标题只在 Markdown：2. 用户角色与使用场景
- 标题只在 Markdown：2.1 角色
- 标题只在 Markdown：2.2 用户故事（核心场景）
- 标题只在 pdf：产品需求文档（PRD· Product Requirements Document）
- 标题只在 pdf：1.引言与项目定位
- 标题只在 pdf：2.用户角色与使用场景
- 标题只在 pdf：2.1角色
- 标题只在 pdf：2.2用户故事（核心场景）
- 需求只在 Markdown：业务规则：用户名 8–32 字符且仅由英文字母与数字组成（a-z A-Z 0-9），全局唯一；口令 8–64 字符，字符集仅限 ASCII 可打印字符（英文字母/数字及常见符号），至少含 1 个字母与 1 个数字；禁止非 ASCII 字符、空格、制表符/换行/回车等空白与控制字符（服务端强制）；口令+随机盐经 PBKDF2-HMAC-SHA256 生成散列；明文口令绝不落盘/不进日志/不回显；口令仅经 TLS 一次性传输，服务端校验长度/强度；两次确认在客户端完成，服务端仅接收一个口令字段；注册成功即签发会话凭据（自动登录）。
- 需求只在 Markdown：验收标准：① 新用户名注册成功并可登录；② 重复用户名被拒绝且返回明确错误码；③ 用户名长度（<8 或 >32）或含非法字符（非英文字母/数字），或口令长度/强度（<8、>64、缺字母或数字、含非 ASCII、含空格/制表/换行等空白与控制字符）不符均被拒并返回对应错误码；④ 数据库中仅存散列与盐，检索不到明文；⑤ 日志无明文口令。
- 需求只在 Markdown：业务规则：按用户名取该用户盐重算散列比对；口令长度超上限（>64）直接拒绝（上限为硬约束）；连续失败超过阈值触发限流；成功后用 CSPRNG 生成会话凭据（token），写入 Redis 带过期，客户端仅持 token。
- 需求只在 Markdown：验收标准：① 正确口令登录成功并返回 token；② 错误口令被拒并返回对应错误码；③ 高频失败被限流；④ token 过期后被拒绝。
- 需求只在 Markdown：业务规则：使当前 token 失效（Redis 删除/置失效）；服务端认为该会话登出。
- 需求只在 Markdown：验收标准：登出后原 token 无法再通过鉴权。
- 需求只在 Markdown：业务规则：所有非注册/登录命令需携带有效 token；客户端定时发送心跳（HEARTBEAT）；服务端对超过 heartbeat_timeout（默认 60s，可配）未活跃的连接判定超时并断开；心跳可顺带续期。
- 需求只在 Markdown：验收标准：① 无有效 token 的请求被拒；② 正常心跳下连接保持；③ 停止心跳超过超时阈值后服务端主动断开该连接并广播离线。
- 需求只在 Markdown：验收标准：① A 申请 B，B 未处理时 A/B 均看到待处理状态；② B 同意后 A、B 双向成为好友且出现在彼此好友列表；③ B 拒绝则关系不建立；④ 重复申请被拒绝。
- 需求只在 Markdown：验收标准：A 删除 B 后，A、B 的好友列表互不再出现对方。
- 需求只在 pdf：业务规则：用户名8–32字符且仅由英文字母与数字组成（a-z A-Z 0-9），全局唯一；口令8–64字符，字符集仅限ASCII可打印字符（英文字母/数字及常见符号），至少含1个字母与1个数字；禁止非ASCII字符、空格、制表符/换行/回车等空白与控制字符（服务端强制）；口令+随机盐经PBKDF2-HMAC-SHA256生成散列；明文口令绝不落盘/不进日志/不回显；口令仅经TLS一次性传输，服务端校验长度/强度；两次确认在客户端完成，服务端仅接收一个口令字段；注册成功即签发会话凭据（自动登录）。
- 需求只在 pdf：验收标准：①新用户名注册成功并可登录；②重复用户名被拒绝且返回明确错误码；③用户名长度（<8或>32）或含非法字符（非英文字母/数字），或口令长度/强度（<8、>64、缺字母或数字、含非ASCII、含空格/制表/换行等空白与控制字符）不符均被拒并返回对应错误码；④数据库中仅存散列与盐，检索不到明文；⑤日志无明文口令。
- 需求只在 pdf：业务规则：按用户名取该用户盐重算散列比对；口令长度超上限（>64）直接拒绝（上限为硬约束）；连续失败超过阈值触发限流；成功后用CSPRNG生成会话凭据（token），写入Redis带过期，客户端仅持token。
- 需求只在 pdf：验收标准：①正确口令登录成功并返回token；②错误口令被拒并返回对应错误码；③高频失败被限流；④token过期后被拒绝。
- 需求只在 pdf：业务规则：使当前token失效（Redis删除/置失效）；服务端认为该会话登出。
- 需求只在 pdf：验收标准：登出后原token无法再通过鉴权。
- 需求只在 pdf：业务规则：所有非注册/登录命令需携带有效token；客户端定时发送心跳（HEARTBEAT）；服务端对超过heartbeat_timeout（默认60s，可配）未活跃的连接判定超时并断开；心跳可顺带续期。
- 需求只在 pdf：验收标准：①无有效token的请求被拒；②正常心跳下连接保持；③停止心跳超过超时阈值后服务端主动断开该连接并广播离线。
- 需求只在 pdf：验收标准：①A申请B，B未处理时A/B均看到待处理状态；②B同意后A、B双向成为好友且出现在彼此好友列表；③B拒绝则关系不建立；④重复申请被拒绝。
- 需求只在 pdf：验收标准：A删除B后，A、B的好友列表互不再出现对方。

### JetQiao__football-prediction-skill

段落标题不一致，需求条目 20 / 133 一致（pdf 拆出 119 条）

- 标题只在 Markdown：竞彩足球智能预测系统 — 需求文档
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 一句话定位
- 标题只在 Markdown：1.2 与同类项目的差异（对标基准）
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：竞彩足球智能预测系统—需求文档
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1一句话定位
- 标题只在 pdf：1.2与同类项目的差异（对标基准）
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：v0.3：产品形态从"纯前端"调整为"Skill + 自包含 HTML 报告"（见 §2）；确认覆盖竞彩当日全部场次（情报分层强制）。
- 需求只在 Markdown：v0.4：完成数据源调研并落地（§3.5/§3.6，含可复用的 SportteryAPI 与免费历史数据 football-data.co.uk）；补全 HTML 报告结构（§7.3）、成功指标与验收（§12）、风险登记（§13）、术语表（§14）。文档已基本完整。
- 需求只在 Markdown：v0.6：合并原 v0.6 评估基础与 v0.7 模型演进；加入多预测时点、多赛季数据体检、分层 Dixon-Coles、多窗口验证、稳定性晋级协议、训练模型卡和自更新命令。
- 需求只在 Markdown：更精准：用统计学正确的模型 + 市场锚定 + 可度量的回测，而非"拍脑袋专业感"。
- 需求只在 Markdown：赛制推演：大赛期间附带小组排名 + 淘汰赛对阵推演（含"算计对阵"博弈）。
- 需求只在 Markdown：跨域 CORS：竞彩官网 / 赔率站 / 新闻站大多禁止浏览器跨域请求。
- 需求只在 Markdown：核心 = Skill：SKILL.md + 脚本（拉竞彩赛单/赔率、Dixon-Coles 计算、回测）。智能体编排： 拉当天赛单 → 全部场次跑脚本算 B 级预测 → 对重点场联网搜情报做 A 级深度分析 → 产出结果。 一举解决 CORS、情报采集、专业分析 三大难题。
- 需求只在 Markdown：prediction_{date}.json：机器可读，供回测与跨天累积。
- 需求只在 Markdown：report_{date}.html：自包含单文件 HTML 报告——数据以内联 <script> JSON 嵌入，原生 JS 渲染卡片/筛选/排序，图表用内联 SVG（零依赖、可离线）。双击即开，无需服务器/构建/部署。
- 需求只在 Markdown：彻底免前端工程：不需要 npm / Vite / Vue/React / 开发服务器 / 部署流水线；数据在生成时已"烤进"HTML，打开时不发请求 → 运行时无 CORS。
- 需求只在 pdf：v0.3：产品形态从"纯前端"调整为"Skill+自包含HTML报告"（见§2）；确认覆盖竞彩当日全部场次（情报分层强制）。
- 需求只在 pdf：v0.4：完成数据源调研并落地（§3.5/§3.6，含可复用的SportteryAPI与免费历史数据football-data.co.uk）；补全HTML报告结构（§7.3）、成功指标与验收（§12）、风险登记（§13）、术语表（§14）。文档已基本完整。
- 需求只在 pdf：v0.6：合并原v0.6评估基础与v0.7模型演进；加入多预测时点、多赛季数据体检、分层Dixon-Coles、多窗口验证、稳定性晋级协议、训练模型卡和自更新命令。实现口径以README、架构文档与数据契约为准；本文保留早期产品调研与完整需求背景。
- 需求只在 pdf：更精准：用统计学正确的模型+市场锚定+可度量的回测，而非"拍脑袋专业感"。
- 需求只在 pdf：赛制推演：大赛期间附带小组排名+淘汰赛对阵推演（含"算计对阵"博弈）。
- 需求只在 pdf：跨域CORS：竞彩官网/赔率站/新闻站大多禁止浏览器跨域请求。
- 需求只在 pdf：核心= Skill：SKILL.md+脚本（拉竞彩赛单/赔率、Dixon-Coles计算、回测）。智能体编排：拉当天赛单→全部场次跑脚本算B级预测→对重点场联网搜情报做A级深度分析→产出结果。一举解决CORS、情报采集、专业分析三大难题。
- 需求只在 pdf：输出（每次运行产两个文件）：o prediction_{date}.json：机器可读，供回测与跨天累积。o report_{date}.html：自包含单文件HTML报告——数据以内联<script>JSON嵌入，原生JS渲染卡片/筛选/排序，图表用内联SVG（零依赖、可离线）。双击即开，无需服务器/构建/部署。
- 需求只在 pdf：彻底免前端工程：不需要npm / Vite / Vue/React /开发服务器/部署流水线；数据在生成时已"烤进"HTML，打开时不发请求→运行时无CORS。
- 需求只在 pdf：数据/Key：智能体在工具侧抓取，免浏览器跨域；付费源/LLM Key由运行环境保管。📌这是一份"每日快照报告"模式：每天跑一次Skill →一个可离线、可转发、可存档的HTML。将来若想做实时常驻App，JSON已现成可用，零锁定——但当前需求并不需要它。

### Jonnyan404__clip9

段落标题一致，需求条目 0 / 8 一致（pdf 拆出 22 条）

- 需求只在 Markdown：#[test] fn csv_converts_to_a_markdown_table() { let csv = b"name,qty\napple,3\npear,5\n"; let out = to_markdown(csv, Some("fruit.csv")).expect("CSV 应当能转"); assert!(out.contains("apple"), "结果里应当有数据：{out}"); assert!(out.contains('|'), "CSV 应当转成表格：{out}"); }
- 需求只在 Markdown：// 正文一个字都不能丢（也不许变成乱码）。 for expected in [ "产品需求文档", "这是一份中文需求文档，用来验证标题层级能不能被识别。", "背景", "用户反馈白板功能缺失，需要补齐。", "验收标准", "标题要变成树形节点，正文要成为卡片。", ] { assert!( out.contains(expected), "转出来的 Markdown 里没有「{expected}」：\n{out}" ); }
- 需求只在 Markdown：/// CSV 没有签名 —— 不给出名字就认不出来。这条差异要可见，不能靠猜。 #[test] fn csv_without_a_filename_is_unsupported() { let csv = b"name,qty\napple,3\n"; let error = to_markdown(csv, None).expect_err("无名 CSV 应当认不出来"); assert!( matches!(error, ActionError::InvalidInput(ref message) if message.contains("格式")), "{error}" ); }
- 需求只在 Markdown：#[test] fn empty_input_is_rejected_before_parsing() { let error = to_markdown(b"", Some("empty.docx")).expect_err("空文件应当报错"); assert!( matches!(error, ActionError::InvalidInput(ref message) if message.contains("空的")), "{error}" ); }
- 需求只在 Markdown：assert!( !converted.markdown.contains("!["), "上游开始输出 Markdown 图片了？那 extract_images 这趟解析可以撤掉：\n{}", converted.markdown ); assert!( converted.markdown.contains("图之后还有一段文字"), "正文不能少" );
- 需求只在 Markdown：let images = converted .images .expect("docx 应当读得出文档模型（PDF 才是 None）"); assert_eq!(images.total, 1, "应当找到 1 张图"); assert_eq!(images.items.len(), 1, "预算足够，不该截断"); assert!(!images.truncated);
- 需求只在 Markdown：fn a_document_without_images_reports_an_empty_set_not_none() { let converted = convert(&chinese_docx(), Some("需求.docx")).expect("应当能转"); let images = converted.images.expect("docx 读得出文档模型"); assert_eq!(images.total, 0); assert!(images.items.is_empty()); assert!(!images.truncated); }
- 需求只在 Markdown：// 预算刚好够：一张都不截 let (items, truncated) = cap_images(&refs[..1], 10); assert!(!truncated); assert_eq!(items.len(), 1, "预算正好等于大小应当装得下（边界不是越界）");
- 需求只在 pdf：///格式判定：内容优先、扩展名兜底（与上游anydoc::to_markdown同一条规矩）。/// ///理由：扩展名是用户可改的、内容不是——一份.txt里装着docx，///按内容转是对的；反过来按扩展名硬套只会得到「malformed」这种看不懂的报错。/// ⚠️CSV没有签名，所以它必须有名字才认得出来。fn detect(bytes: &[u8], filename: Option<&str>)
- 需求只在 pdf：> Option { Format::from_bytes(bytes).or_else(|| { filename .and_then(extension_of) .and_then(Format::from_extension) }) }
- 需求只在 pdf：let out=to_markdown(csv, Some("fruit.csv")).expect("CSV应当能转"); assert!(out.contains("apple"),"结果里应当有数据：{out}"); assert!(out.contains('|'), "CSV应当转成表格：{out}");
- 需求只在 pdf：/// ⚠️★中文（CJK）必须能转——包括标题层级。
- 需求只在 pdf：求.docx")).expect("中文docx应当能转");
- 需求只在 pdf："用户反馈白板功能缺失，需要补齐。",
- 需求只在 pdf：/// ⚠️styles.xml必须带上：w:pStyle引用的样式得在styles.xml里声明* *，///否则Word/解析器会当成一个不存在的样式——而anydoc正是靠它判标题层级的///（Heading1→#）。少了它，标题会全部退化成正文，而用例会红（这正是我们要的）。
- 需求只在 pdf：let error=to_markdown(csv,None).expect_err("无名CSV应当认不出来");
- 需求只在 pdf："应当按内容当成PDF处理：{error}"
- 需求只在 pdf：let error=to_markdown(b"",Some("empty.docx")).expect_err("空文件应当报错");

### Jwz-git__Daygo

段落标题不一致，需求条目 1 / 20 一致（pdf 拆出 9 条）

- 标题只在 Markdown：01 产品需求
- 标题只在 Markdown：1.1 问题陈述
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 核心用户故事
- 标题只在 Markdown：1.4 功能需求
- 标题只在 pdf：01产品需求
- 标题只在 pdf：1.1问题陈述
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：1.3核心用户故事
- 标题只在 pdf：1.4功能需求
- 需求只在 Markdown：2026-10-13 实现边界复核：本文列的是需求，生产空闲采样、搜索、录制后即时日报和通知点击 唤回仍有缺口，Linux 尚无录制闭环。手动停止不跨重启保存是当前已接受的初版行为， 持久化语义须另行决定；不把 idle 的运行时含义推断为重启后的用户偏好。 v1 不交付 agent / chat 的范围保持，但默认生产入口尚未收口，不能据文档推断安装包已排除。 结构 / 聚合测试通过也不等于识别与摘要准确率已量化；责任与完成标准见 09 §9.1.2。
- 需求只在 Markdown：手动计时器（Toggl 一类）要求用户记得启停，而人恰恰在专注时最不可能记得。
- 需求只在 Markdown：应用级时间统计（Screen Time 一类）只知道哪个应用在前台，不知道你在那个应用里 做了什么。"VS Code 3 小时"对复盘几乎没有信息量。
- 需求只在 Markdown：#：U1；作为用户，我希望：打开应用就能看到今天的活动时间线，不需要事先做任何配置动作；以便：不必为了记录而中断工作
- 需求只在 Markdown：#：U8；作为用户，我希望：关掉窗口后记录继续，需要时从状态栏叫回来；以便：应用不占用屏幕空间
- 需求只在 Markdown：跟随光标需要显示器枚举、滞后判定和跨调用状态，而截图原语被有意设计成无状态的单次调用
- 需求只在 Markdown：ID：F-C6；需求：睡眠、锁屏、屏保期间停止捕获，事件结束后自动恢复；验收标准：恢复是自动的，不需要用户干预
- 需求只在 Markdown：ID：F-C7；需求：用户主动关闭记录后，系统事件不得自动恢复它；验收标准：idle（用户关闭）与 paused（系统事件）是不同状态
- 需求只在 Markdown：ID：F-V6；需求：全部界面文案经 i18n，支持简体中文与英文；验收标准：缺 key 在类型检查阶段失败，不在运行时回退
- 需求只在 Markdown：ID：F-S1；需求：自定义 provider：名称、协议、接口地址、模型、密钥；验收标准：协议 v1 支持 openai（Chat Completions）、openai_responses、anthropic（Messages）三种
- 需求只在 pdf：2026-10-13实现边界复核：本文列的是需求，生产空闲采样、搜索、录制后即时日报和通知点击唤回仍有缺口，Linux尚无录制闭环。手动停止不跨重启保存是当前已接受的初版行为，持久化语义须另行决定；不把idle的运行时含义推断为重启后的用户偏好。v1不交付agent / chat的范围保持，但默认生产入口尚未收口，不能据文档推断安装包已排除。结构/聚合测试通过也不等于识别与摘要准确率已量化；责任与完成标准见09 §9.1.2。
- 需求只在 pdf：手动计时器（Toggl一类）要求用户记得启停，而人恰恰在专注时最不可能记得。
- 需求只在 pdf：应用级时间统计（Screen Time一类）只知道哪个应用在前台，不知道你在那个应用里做了什么。"VS Code 3小时"对复盘几乎没有信息量。
- 需求只在 pdf：ID需求验收标准F-V1按逻辑日展示时间线，逻辑日边界为凌晨4含标题、摘要、分类、点时长F-V2卡片可展开查看该时段帧按需解码，不阻塞列的帧条表渲染F-V3可修改卡片的分类与标删除是软删除题，可删除卡片F-V4每日摘要：亮点、完成按日历日聚合（与时间项、阻塞项线的逻辑日不同，见03 §3.2）F-V5每周视图：跟踪时长、合计一律排除System专注时长、分类占比分类F-V6全部界面文案经缺key在类型检查阶i18n，支持简体中文与段失败，不在运行时回英文退F-V7浅色/深色/跟随系统跟随系统时随系统切换实时生效三态主题
- 需求只在 pdf：ID需求验收标准F-S1自定义provider：名协议v1支持openai称、协议、接口地址、（Chat模型、密钥Completions）、openai_responses、
- 需求只在 pdf：（Messages）三种F-S2主/备用provider路备用为空时表示不回由退；备用不得与主相同F-S3密钥写入系统钥匙串，任何接口都不返回密钥只写不读内容；UI只知道"是否已配置" ID需求验收标准F-S4 provider连接测试一次真实调用，返回结果不回显密钥或完整请求体F-S5屏蔽应用名单按bundle identifier F-S6录制磁盘占用上限超限按整个分段清理最旧数据F-S7分类体系可增删改、可分类名称是卡片的外键调顺序与颜色语义，重命名需要同步已有卡片F-S8开机自启、Dock图标
- 需求只在 pdf：F-L3 Cmd+Q / Dock软退软退出与关窗继续录制；真退出/重启/关出、窗口关闭、状态栏真退出、更新重启、系机完成或安全移交当前统关机是不同事件分段F-L4自动更新实现待定设计；更新重启不得丢失未收尾的分
- 需求只在 pdf：类别要求隐私见07。屏幕数据只发往用户明确配置的provider；屏蔽名单与脱敏占位帧两层保护都必须存在资源占用空闲态CPU占用不应稳定高于个位数百分比；捕获间隔10秒时不应产生可感知的输入延迟类别要求数据安全单一写入方；异常退出不得损坏数据库；未收尾的分段必须可恢复或被安全丢弃可观测性静默丢数据是缺陷。解析失败、跳过的卡片、失败批次都必须计数并可在诊断界面看到可测试性Go Core必须能在无macOS、无GUI的环境中构建与测试（CGO_ENABLED=0）国际化全部用户可见文案经i18n；后端错误message不本地化，前端按错误码映射文案

### KaniuBillows__english-anywhere-lab

段落标题不一致，需求条目 54 / 107 一致（pdf 拆出 120 条）

- 标题只在 Markdown：English Anywhere Lab - PRD（v0.4）
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 背景与问题定义
- 标题只在 Markdown：3. 产品目标与非目标
- 标题只在 Markdown：3.1 目标（Goals）
- 标题只在 pdf：English Anywhere Lab -PRD（v0.4）
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.背景与问题定义
- 标题只在 pdf：3.产品目标与非目标
- 标题只在 pdf：3.1目标（Goals）
- 需求只在 Markdown：状态：Draft -> 可进入设计与开发拆分
- 需求只在 Markdown：FR-006：支持"10 分钟快学"和"20 分钟完整模式"
- 需求只在 Markdown：AC-003：进入今日学习页到开始任务 <= 2 次点击
- 需求只在 Markdown：FR-010：支持 AI 一键生成学习包（词汇、对话、练习、测验）
- 需求只在 Markdown：AC-006：AI 生成失败可自动重试一次并返回错误原因
- 需求只在 Markdown：AC-007：到期卡片可在 1 秒内加载
- 需求只在 Markdown：FR-016：AI 提供反馈（准确性、流畅度、词汇建议）
- 需求只在 Markdown：AC-009：每次学习至少有 1 个输出任务可选
- 需求只在 Markdown：AC-010：反馈在 5 秒内返回（P95）
- 需求只在 Markdown：AC-011：看板数据按天聚合，刷新延迟 <= 5 分钟
- 需求只在 pdf：状态：Draft->可进入设计与开发拆分
- 需求只在 pdf：FR-006：支持"10分钟快学"和"20分钟完整模式"
- 需求只在 pdf：AC-003：进入今日学习页到开始任务<= 2次点击
- 需求只在 pdf：FR-010：支持AI一键生成学习包（词汇、对话、练习、测验）
- 需求只在 pdf：AC-006：AI生成失败可自动重试一次并返回错误原因
- 需求只在 pdf：AC-007：到期卡片可在1秒内加载
- 需求只在 pdf：FR-016：AI提供反馈（准确性、流畅度、词汇建议）
- 需求只在 pdf：AC-009：每次学习至少有1个输出任务可选
- 需求只在 pdf：AC-010：反馈在5秒内返回（P95）
- 需求只在 pdf：AC-011：看板数据按天聚合，刷新延迟<= 5分钟

### Kerry-yangg__Dotalens

段落标题不一致，需求条目 124 / 231 一致（pdf 拆出 223 条）

- 标题只在 Markdown：Dota Lens 产品需求文档（PRD）
- 标题只在 Markdown：1. 文档目的
- 标题只在 Markdown：2. 背景与问题
- 标题只在 Markdown：2.1 当前产品背景
- 标题只在 Markdown：2.2 OpenDota 数据审计结论
- 标题只在 pdf：Dota Lens产品需求文档（PRD）
- 标题只在 pdf：1.文档目的
- 标题只在 pdf：2.背景与问题
- 标题只在 pdf：2.1当前产品背景
- 标题只在 pdf：2.2 OpenDota数据审计结论
- 需求只在 Markdown：一名玩家打完一场 Dota 2 比赛后，能够选中自己的英雄，按秒回看移动、刷野、补刀、经济、装备、战斗和视野事件，并看懂某段决策带来了什么收益、又放弃了什么机会。
- 需求只在 Markdown：最近比赛大部分没有 OpenDota 深度解析，进入详情后只能看到基础数据。
- 需求只在 Markdown：OpenDota 公共 API 无法回答"第几分钟在哪里刷野"。
- 需求只在 Markdown：OpenDota 公共 API 无法精确回答"这段刷野赚了多少钱"。
- 需求只在 Markdown：当前地图时间滑块容易让用户误以为 lane_pos 是全场带时间的轨迹。
- 需求只在 Markdown：愿意在 Windows 游戏电脑上运行一个本地解析助手的个人用户。
- 需求只在 Markdown：指标：支持当前版本正常 replay 的解析成功率；MVP 目标：≥ 90%
- 需求只在 Markdown：系统换算并校验账号 ID。
- 需求只在 Markdown：每场比赛显示数据状态：完整、OpenDota 深度、仅基础、等待 replay、解析中、失败。
- 需求只在 Markdown：若只有基础数据，页面引导用户在电脑端打开本地助手并导入 replay。
- 需求只在 pdf：一名玩家打完一场Dota 2比赛后，能够选中自己的英雄，按秒回看移动、刷野、补刀、经济、装备、战斗和视野事件，并看懂某段决策带来了什么收益、又放弃了什么机会。
- 需求只在 pdf：最近比赛大部分没有OpenDota深度解析，进入详情后只能看到基础数据。
- 需求只在 pdf：OpenDota公共API无法回答"第几分钟在哪里刷野"。
- 需求只在 pdf：OpenDota公共API无法精确回答"这段刷野赚了多少钱"。
- 需求只在 pdf：当前地图时间滑块容易让用户误以为lane_pos是全场带时间的轨迹。
- 需求只在 pdf：愿意在Windows游戏电脑上运行一个本地解析助手的个人用户。
- 需求只在 pdf：MVP目标指标≥ 95%本地replay导入成功率≥ 90%支持当前版本正常replay的解析成功率≥ 98%逐秒快照完整率≥ 98%关键事件带时间戳比例100%数据来源标识覆盖率100%估算指标带置信度比例
- 需求只在 pdf：系统换算并校验账号ID。
- 需求只在 pdf：每场比赛显示数据状态：完整、OpenDota深度、仅基础、等待replay、解析中、失败。
- 需求只在 pdf：若只有基础数据，页面引导用户在电脑端打开本地助手并导入replay。

### L20081125__dsh-lite-theme

段落标题不一致，需求条目 1 / 52 一致（pdf 拆出 11 条）

- 标题只在 Markdown：PRD — dsh-lite-theme：DeepSeek Harness 动漫美化主题插件
- 标题只在 Markdown：1. 项目定位
- 标题只在 Markdown：2. 用户画像与使用场景
- 标题只在 Markdown：3. 功能需求（含验收标准与实现状态）
- 标题只在 Markdown：F1 主题系统（Web 端）✅ 已实现
- 标题只在 pdf：PRD —dsh-lite-theme：DeepSeek Harness动漫美化主题插件
- 标题只在 pdf：1.项目定位
- 标题只在 pdf：2.用户画像与使用场景
- 标题只在 pdf：3.功能需求（含验收标准与实现状态）
- 标题只在 pdf：F1主题系统（Web端）✅已实现
- 需求只在 Markdown：v1.1 变更：移除 TUI 支持（用户要求仅 Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 Markdown：Web 端（dsh web）：深度主题化——10 套动漫主题、壁纸系统、炫技级动效、实时预览调色（工坊）、主题包导入导出
- 需求只在 Markdown：桌面端：对接社区现成 Electron 壳（如 ChisaAlter/Deepseek-Harness-Desktop），加载 Web UI 自动继承主题，插件内提供兼容性说明（docs/DESKTOP.md）
- 需求只在 Markdown：~~TUI 端~~：v0.2 起已移除（用户决策：仅支持 Web）。
- 需求只在 Markdown：10 套主题全部可切换，切换即时生效
- 需求只在 Markdown：主题选择持久化（localStorage dsh-lite:state），刷新/重启保持
- 需求只在 Markdown：每套主题覆盖背景、前景、强调色、侧边栏、气泡、输入框、边框、代码块、选中态等 40+ token
- 需求只在 Markdown：毛玻璃/半透明质感（背景 token 半透明 + backdrop-filter）
- 需求只在 Markdown：遵循官方 data-ds-dark-theme 机制，与系统深浅色设置不冲突
- 需求只在 Markdown：上传本地图片（jpg/png/webp，≤20MB，自动压缩存储）
- 需求只在 pdf：版本：v1.1（2026-08-16）｜状态：已评审（4轮需求反问）+实现同步（v0.2）v1.1变更：移除TUI支持（用户要求仅Web）；上传/壁纸可见性修复；安装脚本落地
- 需求只在 pdf：Web端（dsh web）：深度主题化——10套动漫主题、壁纸系统、炫技级动效、实时预览调色（工坊）、主题包导入导出
- 需求只在 pdf：桌面端：对接社区现成Electron壳（如ChisaAlter/Deepseek-Harness-Desktop），加载Web UI自动继承主题，插件内提供兼容性说明（docs/DESKTOP.md）
- 需求只在 pdf：TUI端：v0.2起已移除（用户决策：仅支持Web）。
- 需求只在 pdf：基底：毛玻璃（backdrop-filter:blur +saturate）面板、半透明侧边栏、渐变光晕
- 需求只在 pdf：动效：微交互过渡140~200ms ease-out；粒子/视差为氛围层，不干扰内容阅读
- 需求只在 pdf：圆角：卡片10~16px，按钮8~10px
- 需求只在 pdf：内置壁纸：8张程序生成SVG（1920x1080视觉基准，dataURL内联，零版权风险）
- 需求只在 pdf：上传壁纸：canvas压缩≤1920px、JPEG q0.82（存独立localStorage键，防5MB上限溢出）
- 需求只在 pdf：默认叠加：遮罩（0~85%可调）保证对比度；模糊0~50px

### LoD-Dawn__Fast-Vben-Admin

段落标题不一致，需求条目 98 / 135 一致（pdf 拆出 125 条）

- 标题只在 Markdown：Fast Vben Admin 产品需求文档 PRD
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 背景与结论
- 标题只在 Markdown：3. 产品定位
- 标题只在 Markdown：3.1 一句话愿景
- 标题只在 pdf：Fast Vben Admin产品需求文档PRD
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.背景与结论
- 标题只在 pdf：3.产品定位
- 标题只在 pdf：3.1一句话愿景
- 需求只在 Markdown：Fast Vben Admin 是面向 Python/Vue 技术栈团队的开箱即用中后台系统基座。它提供账号、组织、权限、菜单、字典、参数、日志、文件、通知、仪表盘和示例业务模块，使开发者可以直接在其上开发内部管理系统、SaaS 管理端、数据运营后台和项目交付后台。
- 需求只在 Markdown：缺口：初始化数据完整度；影响：默认角色、菜单、权限、字典、参数需要稳定可重复初始化
- 需求只在 Markdown：缺口：权限一致性；影响：菜单权限、按钮权限、接口权限需要同源，避免前后端不一致
- 需求只在 Markdown：缺口：通知闭环；影响：公告发布到用户消息、未读数、消息入口、已读操作需要明确验收
- 需求只在 Markdown：缺口：测试覆盖；影响：核心模块 API、权限、防越权、前端构建和关键 E2E 需要稳定通过
- 需求只在 Markdown：缺口：文档体系；影响：PRD、TRD、开发计划、部署、模块开发指南需要与实际实现一致
- 需求只在 Markdown：能力：代码生成；当前状态：已完成；建议版本：v1.2；说明：已支持从数据库表结构生成 FastAPI 路由、Schema、Vben 页面骨架
- 需求只在 Markdown：能力：对象存储；当前状态：已完成；建议版本：v1.2；说明：已支持 MinIO/S3 存储配置和私有文件授权 URL
- 需求只在 Markdown：能力：OAuth2/SSO；当前状态：部分完成；建议版本：v1.4；说明：已有授权码 + PKCE、刷新和撤销协议；企业 OIDC 已支持本地用户、角色和启用状态映射，真实第三方平台回调验收待补齐
- 需求只在 Markdown：邮箱 + 密码登录。
- 需求只在 pdf：Fast Vben Admin是面向Python/Vue技术栈团队的开箱即用中后台系统基座。它提供账号、组织、权限、菜单、字典、参数、日志、文件、通知、仪表盘和示例业务模块，使开发者可以直接在其上开发内部管理系统、SaaS管理端、数据运营后台和项目交付后台。
- 需求只在 pdf：邮箱+密码登录。
- 需求只在 pdf：重置密码token有过期时间。
- 需求只在 pdf：超级管理员可完成用户CRUD。
- 需求只在 pdf：普通用户直接请求无权限接口返回403。
- 需求只在 pdf：当前用户菜单接口/menus/me。
- 需求只在 pdf：当前用户权限码接口/permissions/me。
- 需求只在 pdf：字典类型code唯一。
- 需求只在 pdf：JSON类型参数需校验格式。
- 需求只在 pdf：日志导出作为v1.x增强。

### LordCasser__atlas

段落标题不一致，需求条目 22 / 118 一致（pdf 拆出 118 条）

- 标题只在 Markdown：Atlas 需求规格
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：2. 当前默认语言范围
- 标题只在 Markdown：3. 非目标
- 标题只在 Markdown：4. 功能需求
- 标题只在 pdf：Atlas需求规格
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：2.当前默认语言范围
- 标题只在 pdf：3.非目标
- 标题只在 pdf：4.功能需求
- 需求只在 Markdown：AI 辅助路径分析工具
- 需求只在 Markdown：确定性：基于 tree-sitter AST/query，不用 AI 猜测生成图谱。
- 需求只在 Markdown：MCP-first：Agent 消费是核心场景，不是 CLI 的附属功能。
- 需求只在 Markdown：从 project root 扫描当前 14 种语言文件。
- 需求只在 Markdown：git 项目优先使用 git ls-files，遵循 .gitignore。
- 需求只在 Markdown：支持 include/exclude glob 和 .atlasignore。
- 需求只在 Markdown：默认排除 .git、.atlas、node_modules、dist、build、out、target、pycache、.venv、venv、.gradle、.m2。
- 需求只在 Markdown：单文件失败、超大文件、grammar panic 不得中断整个索引。
- 需求只在 Markdown：合法 UTF-8 源码直接解析；非 UTF-8 源码仅在内存解码，优先覆盖中文 GBK/GB18030 与西欧 windows-1252（ISO-8859-1 类输入）。
- 需求只在 Markdown：Atlas 不因检测或转码改写原文件；文件身份始终基于原始磁盘字节，转码不应造成 永久 dirty 或 stale。
- 需求只在 pdf：AI辅助路径分析工具
- 需求只在 pdf：确定性：基于tree-sitter AST/query，不用AI猜测生成图谱。
- 需求只在 pdf：MCP-first：Agent消费是核心场景，不是CLI的附属功能。
- 需求只在 pdf：从project root扫描当前14种语言文件。
- 需求只在 pdf：git项目优先使用git ls-files，遵循.gitignore。
- 需求只在 pdf：支持include/exclude glob和.atlasignore。
- 需求只在 pdf：默认排除.git、.atlas、node_modules、dist、build、out、target、pycache、.venv、venv、.gradle、.m2。
- 需求只在 pdf：单文件失败、超大文件、grammar panic不得中断整个索引。
- 需求只在 pdf：合法UTF-8源码直接解析；非UTF-8源码仅在内存解码，优先覆盖中文GBK/GB18030与西欧windows-1252（ISO-8859-1类输入）。
- 需求只在 pdf：Atlas不因检测或转码改写原文件；文件身份始终基于原始磁盘字节，转码不应造成永久dirty或stale。

### LubyRuffy__ProxyCraft

段落标题不一致，需求条目 1 / 61 一致（pdf 拆出 45 条）

- 标题只在 Markdown：PRD: 命令行 HTTPS/HTTP2/SSE 代理工具 (代号: "ProxyCraft CLI")
- 标题只在 Markdown：1. 引言 (Introduction)
- 标题只在 Markdown：2. 目标 (Goals)
- 标题只在 Markdown：3. 目标用户 (Target Audience)
- 标题只在 Markdown：4. 功能需求 (Functional Requirements)
- 标题只在 pdf：PRD:命令行HTTPS/HTTP2/SSE代理工具(代号: "ProxyCraft CLI")
- 标题只在 pdf：1.引言(Introduction)
- 标题只在 pdf：2.目标(Goals)
- 标题只在 pdf：3.目标用户(Target Audience)
- 标题只在 pdf：4.功能需求(Functional Requirements)
- 需求只在 Markdown：ProxyCraft CLI 是一款轻量级、高性能的命令行代理工具，旨在为开发人员、安全测试人员和网络管理员提供便捷的流量观察、分析和调试能力。它专注于核心代理功能，支持最新的 Web 协议如 HTTPS, HTTP/2, 以及 Server-Sent Events (SSE)，并且完全通过命令行界面进行操作，无需图形用户界面。其设计灵感来源于 Burp Suite 的代理功能，但更侧重于命令行环境下的易用性和可集成性。
- 需求只在 Markdown：FR1.1: 工具能够作为 HTTP/HTTPS 代理服务器启动，监听在用户指定的 IP 地址和端口上。
- 需求只在 Markdown：FR1.1.1: 默认监听 127.0.0.1:8080，用户可通过命令行参数修改。
- 需求只在 Markdown：FR1.2: 支持 HTTP/1.1 协议的代理。
- 需求只在 Markdown：FR1.3: 能够将客户端请求转发到目标服务器，并将服务器响应返回给客户端。
- 需求只在 Markdown：FR1.4: 正确处理各种 HTTP 方法 (GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH 等)。
- 需求只在 Markdown：FR1.5: 正确处理常见的 HTTP 状态码。
- 需求只在 Markdown：FR2.1: 能够对 HTTPS 流量进行中间人解密。
- 需求只在 Markdown：FR2.2: 首次运行时自动生成自签名根 CA 证书。
- 需求只在 Markdown：FR2.2.1: 提供命令行选项导出根 CA 证书 (如 proxycraft-ca.pem)，方便用户导入到浏览器或操作系统信任存储中。
- 需求只在 pdf：ProxyCraft CLI是一款轻量级、高性能的命令行代理工具，旨在为开发人员、安全测试人员和网络管理员提供便捷的流量观察、分析和调试能力。它专注于核心代理功能，支持最新的Web协议如HTTPS, HTTP/2,以及Server-Sent Events (SSE)，并且完全通过命令行界面进行操作，无需图形用户界面。其设计灵感来源于Burp Suite的代理功能，但更侧重于命令行环境下的易用性和可集成性。
- 需求只在 pdf：FR1.1:工具能够作为HTTP/HTTPS代理服务器启动，监听在用户指定的IP地址和端口上。o FR1.1.1:默认监听127.0.0.1:8080，用户可通过命令行参数修改。
- 需求只在 pdf：FR1.2:支持HTTP/1.1协议的代理。
- 需求只在 pdf：FR1.3:能够将客户端请求转发到目标服务器，并将服务器响应返回给客户端。
- 需求只在 pdf：FR1.4:正确处理各种HTTP方法(GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH等)。
- 需求只在 pdf：FR1.5:正确处理常见的HTTP状态码。
- 需求只在 pdf：FR2.1:能够对HTTPS流量进行中间人解密。
- 需求只在 pdf：FR2.2:首次运行时自动生成自签名根CA证书。o FR2.2.1:提供命令行选项导出根CA证书(如proxycraft-ca.pem)，方便用户导入到浏览器或操作系统信任存储中。o FR2.2.2:如果CA证书已存在，则复用。
- 需求只在 pdf：FR2.3:为客户端请求的每个域名动态生成并使用由自签名根CA签发的服务器证书。
- 需求只在 pdf：FR2.5:用户可以通过命令行参数指定自定义的根CA证书和私钥。

### Mark7766__spring-ai-apps

段落标题不一致，需求条目 15 / 84 一致（pdf 拆出 57 条）

- 标题只在 Markdown：LearnAI Studio 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：LearnAI Studio产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品名称
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：课程开发者：AI 辅助快速创建课程，优化教学设计，扩大内容影响力。
- 需求只在 Markdown：Web 应用，计划扩展至 iOS/Android APP。
- 需求只在 Markdown：包含 AI 对话框、课程播放器、练习模块、开发者编辑器。
- 需求只在 Markdown：在线教育需求旺盛：2025 年全球在线教育市场预计超 5000 亿美元，AI 驱动的教育工具增长迅速。
- 需求只在 Markdown：传统课程局限：视频课程缺乏互动、个性化不足，用户完成率低（平均仅 15%）。
- 需求只在 Markdown：课程枯燥，难以坚持。
- 需求只在 Markdown：进度难跟踪，内容不匹配水平。
- 需求只在 Markdown：遇到问题无人解答，需自行搜索。
- 需求只在 Markdown：缺乏实践反馈，学习效果难评估。
- 需求只在 Markdown：课程开发耗时，需手动整理材料。
- 需求只在 pdf：课程开发者：AI辅助快速创建课程，优化教学设计，扩大内容影响力。
- 需求只在 pdf：Web应用，计划扩展至iOS/Android APP。
- 需求只在 pdf：包含AI对话框、课程播放器、练习模块、开发者编辑器。
- 需求只在 pdf：在线教育需求旺盛：2025年全球在线教育市场预计超5000亿美元，AI驱动的教育工具增长迅速。
- 需求只在 pdf：传统课程局限：视频课程缺乏互动、个性化不足，用户完成率低（平均仅15%）。
- 需求只在 pdf：学习者：o课程枯燥，难以坚持。o进度难跟踪，内容不匹配水平。o遇到问题无人解答，需自行搜索。o缺乏实践反馈，学习效果难评估。
- 需求只在 pdf：课程开发者：o课程开发耗时，需手动整理材料。o设计学习路径复杂，难以适配不同用户。o内容易过时，更新成本高。o难以评估课程效果，优化无依据。
- 需求只在 pdf：Eighteen平台共性：o数据隐私担忧，尤其企业用户。o用户体验割裂，跨设备同步差。o内容质量参差，审核机制不足。
- 需求只在 pdf：LearnAI Studio竞品优势劣势差异化Coursera课程丰富，品牌无AI互动，价AI辅导+课程结强格高合，个性化强Duolingo游戏化，粘性高仅限语言，功能多领域支持，深单一度定制ChatGPT通用问答，灵活无结构化课程，课程驱动，隐私隐私风险保障
- 需求只在 pdf：AI响应时间<1秒，课程加载<2秒。

### Mingyang0018__FastVideo3

段落标题不一致，需求条目 5 / 19 一致（pdf 拆出 15 条）

- 标题只在 Markdown：FastVideo3 产品需求文档（PRD）
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 设计目标（按优先级）
- 标题只在 pdf：FastVideo3产品需求文档（PRD）
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3设计目标（按优先级）
- 需求只在 Markdown：US-3（可替换性）：作为学生，我可以在配置文件中把"图生视频"的供应商从阿里云百炼切换为 SiliconFlow 或可灵，不改一行业务代码即可对比效果与成本。
- 需求只在 Markdown：US-6（人工把关）：作为导演（用户），我在每一步之间都能介入：改剧本稿、按 prompt 重写剧本、换定妆照、删掉坏首帧重画，然后再往下走；成片另有自动终审与一致性闸门给结论。
- 需求只在 Markdown：US-7（成本透明）：作为用户，我随时能看到当前任务已花费的 API 成本估算，并可设置预算上限自动熔断。
- 需求只在 Markdown：项：输入；内容：主题文本（必填）；风格、文化背景、目标时长、集数、画幅比例（默认竖屏 9:16，短剧形态）（选填）；也支持直接粘贴已有剧本（进入解析模式）
- 需求只在 Markdown：项：验收标准；内容：① 每句台词有对应音频且时长与镜头匹配（允许音频 ≤1.2 倍提速或补静帧策略）；② 默认模式口型同步主观可用；③ 双人同屏合成在纯 CPU 环境单镜头 ≤3 分钟完成
- 需求只在 Markdown：项：背景；内容：economy 档（flash-480P、540×960）用于教学零压力跑通；但要达到主流微短剧平台的观感（真人电影感、全片一致、有配乐包装），需要交付档
- 需求只在 Markdown：类别：成本；要求：单次 3 分钟短剧全 API 成本目标：无口型模式（audio_overlay）≤ ¥50；口型默认模式（S2V）≤ ¥150（估算见 TDD §7，以 pricing.yaml 实测校准为准）；支持预算上限熔断
- 需求只在 Markdown：类别：可移植；要求：Windows / Linux / macOS；Python 3.11（conda 环境）；无需 GPU（PyTorch 仅装 CPU 版，供 YOLOv8 本地推理，安装时须指定 CPU index 以免误拉 CUDA 大包）；可选 Docker（仅进阶数据库模式需要）
- 需求只在 Markdown：类别：安全；要求：API KEY 一律存于 .env（gitignore）；代码与日志中不得明文打印 KEY
- 需求只在 Markdown：全链路成功率（主题进 → 成片出）≥ 90%
- 需求只在 pdf：US-3（可替换性）：作为学生，我可以在配置文件中把"图生视频"的供应商从阿里云百炼切换为SiliconFlow或可灵，不改一行业务代码即可对比效果与成本。
- 需求只在 pdf：US-6（人工把关）：作为导演（用户），我在每一步之间都能介入：改剧本稿、按prompt重写剧本、换定妆照、删掉坏首帧重画，然后再往下走；成片另有自动终审与一致性闸门给结论。
- 需求只在 pdf：US-7（成本透明）：作为用户，我随时能看到当前任务已花费的API成本估算，并可设置预算上限自动熔断。
- 需求只在 pdf：项内容背景economy档（flash-480P、540×960）用于教学零压力跑通；但要达到主流微短剧平台的观感（真人电影感、全片一致、有配乐包装），需要交付档配置--quality high（或FV3_QUALITY=high）→
- 需求只在 pdf：类别要求性能3分钟短剧（约36个5秒镜头）全链路≤90分钟（默认并发4；实际受账号API异步任务并发配额制约，提额后可缩短）成本单次3分钟短剧全API成本目标：无口型模式（audio_overlay）≤¥50；口型默认模式（S2V）≤ ¥150（估算见TDD§7，以pricing.yaml实测校准为准）；支持预算上限熔断可靠性所有外部API调用：重试3次+指数退避；异步任务轮询超时保护；中断后再点一次只补缺口（产物与血缘都在盘上，零重复计费）可移植Windows / Linux /macOS；Python
- 需求只在 pdf：全链路成功率（主题进→成片出）≥90%
- 需求只在 pdf：单镜头一次通过率（无需重试）≥70%
- 需求只在 pdf：3分钟短剧成本≤¥150（口型默认模式）/≤¥50（音频直叠模式）
- 需求只在 pdf：新生按文档30分钟内跑通最小用例（Fake模式）
- 需求只在 pdf：学生能在简历中清晰描述：流水线状态机与幂等续跑、血缘驱动的产物作废、Provider抽象与多供应商适配、成本熔断与降级台账、VLM评审与一致性度量闸门——均为2026年AI应用工程师岗位高频技能点

### Neilouo__AI-FortuneTeller

段落标题不一致，需求条目 70 / 103 一致（pdf 拆出 84 条）

- 标题只在 Markdown：AI算命大师产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：AI算命大师产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2产品愿景
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：展示三种人格的介绍和特点
- 需求只在 Markdown：支持用户选择人格
- 需求只在 Markdown：选中后进入对应人格的对话模式
- 需求只在 Markdown：人格风格在对话中保持一致
- 需求只在 Markdown：支持公历日期输入
- 需求只在 Markdown：准确计算八字四柱
- 需求只在 Markdown：准确分析五行分布
- 需求只在 Markdown：生成性格特征描述
- 需求只在 Markdown：流畅的多轮对话
- 需求只在 Markdown：准确理解用户问题
- 需求只在 pdf：1.1人格选择系统
- 需求只在 pdf：☐展示三种人格的介绍和特点☐支持用户选择人格☐选中后进入对应人格的对话模式☐人格风格在对话中保持一致
- 需求只在 pdf：1.2八字计算系统
- 需求只在 pdf：☐支持公历日期输入☐准确计算八字四柱☐准确分析五行分布☐生成性格特征描述
- 需求只在 pdf：1.3智能对话系统
- 需求只在 pdf：1.4命理报告生成
- 需求只在 pdf：1.5心理报告生成
- 需求只在 pdf：2.1用户分析系统
- 需求只在 pdf：☐准确记录会话数据☐计算停留时长和改进率☐支持评分收集☐数据持久化存储
- 需求只在 pdf：2.2话题识别系统

### NewLifeX__AntJob

段落标题不一致，需求条目 1 / 69 一致（pdf 拆出 69 条）

- 标题只在 Markdown：AntJob 蚂蚁调度 — 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：AntJob蚂蚁调度—需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：SYS-1 调度器 Scheduler：核心调度引擎，管理 Handler 集合，从 DI 容器发现处理器，连接调度中心并启停调度。
- 需求只在 Markdown：SYS-2 处理器基类 Handler：作业处理器抽象基类，提供 Init→Start→Acquire→Process→Execute→OnFinish 完整生命周期，支持同步/异步双模。
- 需求只在 Markdown：SYS-3 任务上下文 JobContext：封装单次任务执行的全部状态（参数、结果、数据、异常、耗时、速度）。
- 需求只在 Markdown：SYS-4 调度模式 JobModes：三种模式——Data(数据窗口, 值=1)、Time(定时/Cron, 值=2)、Message(消息驱动, 值=3)。
- 需求只在 Markdown：SYS-5 任务状态 JobStatus：七态状态机——就绪→抽取中→处理中→完成/错误/取消/延迟重试。
- 需求只在 Markdown：SYS-6 作业与任务模型：IJob/JobModel/ITask/TaskModel，含 DataTime/End/Step/Offset/BatchSize/MaxTask 等调度参数。
- 需求只在 Markdown：SYS-7 作业提供者接口：IJobProvider 定义 Acquire/Produce/Report/Finish/GetJobs/SetJob 六个核心操作。
- 需求只在 Markdown：SYS-8 网络提供者：基于 NewLife.Remoting TCP RPC 连接调度中心，自动上报作业、申请任务、报告进度。
- 需求只在 Markdown：SYS-9 文件提供者：XML 文件持久化作业配置，适合离线/单机调试场景。
- 需求只在 Markdown：SYS-10 Http 提供者：HTTP 调度接入通道，与 NetworkJobProvider 功能等价；对接 Web 端 /AntJob/* 令牌与业务接口，适用于无 TCP 端口的环境。
- 需求只在 pdf：SYS-1调度器Scheduler：核心调度引擎，管理Handler集合，从DI容器发现处理器，连接调度中心并启停调度。
- 需求只在 pdf：SYS-2处理器基类Handler：作业处理器抽象基类，提供Init→Start→Acquire→Process→Execute→OnFinish完整生命周期，支持同步/异步双模。
- 需求只在 pdf：SYS-3任务上下文JobContext：封装单次任务执行的全部状态（参数、结果、数据、异常、耗时、速度）。
- 需求只在 pdf：SYS-4调度模式JobModes：三种模式——Data(数据窗口,值=1)、Time(定时/Cron,值=2)、Message(消息驱动,值=3)。
- 需求只在 pdf：SYS-5任务状态JobStatus：七态状态机——就绪→抽取中→处理中→完成/错误/取消/延迟重试。
- 需求只在 pdf：SYS-6作业与任务模型：IJob/JobModel/ITask/TaskModel，含DataTime/End/Step/Offset/BatchSize/MaxTask等调度参数。
- 需求只在 pdf：SYS-7作业提供者接口：IJobProvider定义Acquire/Produce/Report/Finish/GetJobs/SetJob六个核心操作。
- 需求只在 pdf：SYS-8网络提供者：基于NewLife.Remoting TCP RPC连接调度中心，自动上报作业、申请任务、报告进度。
- 需求只在 pdf：SYS-9文件提供者：XML文件持久化作业配置，适合离线/单机调试场景。
- 需求只在 pdf：SYS-10 Http提供者：HTTP调度接入通道，与NetworkJobProvider功能等价；对接Web端/AntJob/*令牌与业务接口，适用于无TCP端口的环境。

### NewLifeX__NewLife.AI

段落标题不一致，需求条目 1 / 136 一致（pdf 拆出 31 条）

- 标题只在 Markdown：NewLife.AI — 需求文档
- 标题只在 Markdown：1. 背景与愿景目标
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：1.3 工程分层
- 标题只在 pdf：NewLife.AI —需求文档
- 标题只在 pdf：1.背景与愿景目标
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：1.3工程分层
- 需求只在 Markdown：通过统一的 IChatClient 接口屏蔽 46 家服务商的协议差异，一行代码切换任意模型
- 需求只在 Markdown：提供完整的 Web 对话应用，开箱即用，支持多轮对话、流式输出、多模态交互
- 需求只在 Markdown：通过技能系统让非开发者也能用 Markdown "教会" AI 做特定事情
- 需求只在 Markdown：通过用户记忆进化让 AI 越用越懂用户
- 需求只在 Markdown：通过 API 网关让外部系统以标准协议接入 AI 能力
- 需求只在 Markdown：AI-1 服务商与协议适配：当前代码扫描包含 46 个模型服务商，通过 [AiClient] 特性注册；协议适配包含 OpenAI、Anthropic Messages、Google Gemini、DashScope、Ollama、AWS Bedrock 6 类。
- 需求只在 Markdown：AI-2 模型能力与接口：覆盖文本生成、流式输出、深度思考、视觉理解、图片生成/编辑、视频生成、语音识别/合成、文本向量等能力，通过统一接口和元数据标记为上层提供一致的调用体验。
- 需求只在 Markdown：AI-2a 统一模型接口：通过 IChatClient 统一同步与流式对话调用，上层无需直接关心各服务商协议差异。
- 需求只在 Markdown：AI-2b 模型能力元数据标记：通过模型能力标记描述 Thinking、Vision、Audio、Image、Video、Embedding、FunctionCalling 等能力，供前端和路由选择。
- 需求只在 Markdown：AI-2c 工具调用接口：ToolChatClient 提供函数调用/工具调用循环引擎（SDK 接口层实现），支持 Function Calling / Tool Use，自动执行工具调用循环。IToolProvider 定义工具提供者统一接口。具体工具实现和深入使用见 TOOL 模块。
- 需求只在 pdf：通过统一的IChatClient接口屏蔽46家服务商的协议差异，一行代码切换任意模型
- 需求只在 pdf：提供完整的Web对话应用，开箱即用，支持多轮对话、流式输出、多模态交互
- 需求只在 pdf：通过技能系统让非开发者也能用Markdown"教会"AI做特定事情
- 需求只在 pdf：通过用户记忆进化让AI越用越懂用户
- 需求只在 pdf：通过API网关让外部系统以标准协议接入AI能力
- 需求只在 pdf：AI-1服务商与协议适配：当前代码扫描包含46个模型服务商，通过[AiClient]特性注册；协议适配包含OpenAI、Anthropic Messages、Google Gemini、DashScope、Ollama、AWS Bedrock 6类。
- 需求只在 pdf：AI-2模型能力与接口：覆盖文本生成、流式输出、深度思考、视觉理解、图片生成/编辑、视频生成、语音识别/合成、文本向量等能力，通过统一接口和元数据标记为上层提供一致的调用体验。
- 需求只在 pdf：o AI-3a MCP客户端接口：NewLife.AI SDK层提供MCP客户端核心能力（无DB依赖），支持stdio和HTTP SSE传输。MCP客户端服务的具体管理和配置实现见TOOL-3。o AI-3b IChatFilter过滤器接口：IChatFilter/FilteredChatClient定义模型调用级横切过滤器接口，用于在对话前后插入自定义逻辑。具体Filter实现见TOOL-4。o AI-3c ChatClientBuilder：ChatClientBuilder构建器提供链式组合Filter与工具的入口，简化客户端装配。
- 需求只在 pdf：AI-4 SDK轻量对话服务与基础设施：2026-08起从魔方页面内嵌AI助手等场景下沉的SDK服务层，补齐ToolChatClient（积木）与MessageFlow（完整档）之间的轻量档，供生态零复制复用。
- 需求只在 pdf：o多轮对话、SSE流式输出、停止生成、重新生成、编辑消息继续对话。o后台继续生成：离开页面后生成任务继续，回来后恢复完整结果。o可恢复流/断线续传：SSE断线后按事件ID恢复未完成生成。o滑动窗口上下文：不限制对话总轮数，每次请求携带最近N轮历史（默认20），早期历史自然淡出；内置由工具循环Token估算守卫（TokenEstimator）兜底，需要摘要压缩时可在处理器链中按需扩展实现。

### NewLifeX__NewLife.Agent

段落标题不一致，需求条目 2 / 74 一致（pdf 拆出 75 条）

- 标题只在 Markdown：NewLife.Agent 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.Agent需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：一句话描述：继承 ServiceBase，你的程序就拥有了跨平台服务治理能力。
- 需求只在 Markdown：目标用户：需要长期运行后台服务的 .NET 开发者与运维人员。
- 需求只在 Markdown：核心场景：Windows 服务部署、Linux 守护进程、macOS LaunchAgent、ASP.NET Core 生产托管。
- 需求只在 Markdown：M1-2 ServiceModel / ServiceConfig：服务安装和查询的数据模型。
- 需求只在 Markdown：M1-3 SystemdSetting：Systemd .service 单元文件生成，支持 Type/Environment/Restart/KillMode/OOMScoreAdjust 等配置。
- 需求只在 Markdown：M1-4 Windows 平台支持类：Advapi32（SCM API P/Invoke）、Desktop（桌面进程启动）、NativeMethods（内存整理）、PowerStatus（电源状态）。
- 需求只在 Markdown：M2-1 Setting 配置模型：基于 Config<T> 基类，Agent.config 文件持久化。
- 需求只在 Markdown：M2-2 服务元数据配置：ServiceName/DisplayName/Description 独立配置。
- 需求只在 Markdown：M2-3 多实例部署：同一程序通过不同 ServiceName 形成多个独立实例。
- 需求只在 Markdown：M2-4 配置文件热加载：Config<T> 内置热加载机制，运行时修改配置即时生效。
- 需求只在 pdf：一句话描述：继承ServiceBase，你的程序就拥有了跨平台服务治理能力。
- 需求只在 pdf：目标用户：需要长期运行后台服务的.NET开发者与运维人员。
- 需求只在 pdf：核心场景：Windows服务部署、Linux守护进程、macOS LaunchAgent、ASP.NET Core生产托管。
- 需求只在 pdf：M1-2 ServiceModel/ServiceConfig：服务安装和查询的数据模型。
- 需求只在 pdf：M1-3 SystemdSetting：Systemd.service单元文件生成，支持Type/Environment/Restart/KillMode/OOMScoreAdjust等配置。
- 需求只在 pdf：M1-4 Windows平台支持类：Advapi32（SCM API P/Invoke）、Desktop（桌面进程启动）、NativeMethods（内存整理）、PowerStatus（电源状态）。
- 需求只在 pdf：M2-1 Setting配置模型：基于Config<T>基类，Agent.config文件持久化。
- 需求只在 pdf：M2-2服务元数据配置：ServiceName/DisplayName/Description独立配置。
- 需求只在 pdf：M2-3多实例部署：同一程序通过不同ServiceName形成多个独立实例。
- 需求只在 pdf：M2-4配置文件热加载：Config<T>内置热加载机制，运行时修改配置即时生效。

### NewLifeX__NewLife.BACnet

段落标题不一致，需求条目 29 / 100 一致（pdf 拆出 101 条）

- 标题只在 Markdown：NewLife.BACnet 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.BACnet需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：成为 .NET 生态中功能最完整、最易集成的 BACnet 协议库，让楼宇自动化工程师和 IoT 边缘开发者能够用最少的代码实现设备发现、数据采集、属性写入和事件处理，并无缝对接 NewLife IoT 物联网平台生态，成为楼控系统与 IoT 平台之间的可靠桥梁。
- 需求只在 Markdown：基础网络传输能力，支持不同物理/网络媒体的 BACnet 数据传输。
- 需求只在 Markdown：TRN-1 BACnet/IP (IPv4) UDP 传输：基于 UDP 的标准 BACnet/IP 通信，默认端口 47808（0xBAC0）
- 需求只在 Markdown：TRN-2 BACnet/IP (IPv6) UDP 传输：基于 UDP 的 IPv6 BACnet 通信
- 需求只在 Markdown：TRN-3 BBMD 广播管理：跨子网广播管理，支持 BBMD 对等体间转发
- 需求只在 Markdown：TRN-4 外部设备注册：外部设备（Foreign Device）向 BBMD 注册并接收广播
- 需求只在 Markdown：COD-1 ASN.1 BER 编解码：BACnet 专有的简化 TLV（Tag-Length-Value）格式编解码
- 需求只在 Markdown：COD-2 APDU 编解码：应用协议数据单元编解码，含确认/未确认/错误/分片等 PDU 类型
- 需求只在 Markdown：COD-3 NPDU 编解码：网络协议数据单元编解码，含源/目标地址、跳数管理
- 需求只在 Markdown：COD-4 BVLC (IPv4) 编解码：BACnet 虚拟链路控制层（IPv4）帧编解码
- 需求只在 pdf：成为.NET生态中功能最完整、最易集成的BACnet协议库，让楼宇自动化工程师和IoT边缘开发者能够用最少的代码实现设备发现、数据采集、属性写入和事件处理，并无缝对接NewLife IoT物联网平台生态，成为楼控系统与IoT平台之间的可靠桥梁。
- 需求只在 pdf：基础网络传输能力，支持不同物理/网络媒体的BACnet数据传输。
- 需求只在 pdf：TRN-1 BACnet/IP (IPv4) UDP传输：基于UDP的标准BACnet/IP通信，默认端口47808（0xBAC0）
- 需求只在 pdf：TRN-2 BACnet/IP (IPv6) UDP传输：基于UDP的IPv6 BACnet通信
- 需求只在 pdf：TRN-3 BBMD广播管理：跨子网广播管理，支持BBMD对等体间转发
- 需求只在 pdf：TRN-4外部设备注册：外部设备（Foreign Device）向BBMD注册并接收广播
- 需求只在 pdf：以下串口传输实现代码存在但已从编译中排除，需跨平台串口兼容性支持后重新启用：TRN-5 MS/TP (RS485)串口传输、TRN-6 PTP (RS232)串口传输、TRN-7通用串口传输基类、TRN-8 Ethernet 802.3直连传输、TRN-9 Windows管道传输
- 需求只在 pdf：COD-1 ASN.1 BER编解码：BACnet专有的简化TLV（Tag-Length-Value）格式编解码
- 需求只在 pdf：COD-2 APDU编解码：应用协议数据单元编解码，含确认/未确认/错误/分片等PDU类型
- 需求只在 pdf：COD-3 NPDU编解码：网络协议数据单元编解码，含源/目标地址、跳数管理

### NewLifeX__NewLife.Cube

段落标题不一致，需求条目 3 / 155 一致（pdf 拆出 155 条）

- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 Markdown：3. 功能需求
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 标题只在 pdf：3.功能需求
- 需求只在 Markdown：多前端支持：Vue 为官方前端与核心库载体；仓库内另提供 Angular / Svelte / NaiveUI / ArcoVue / Vuetify / TDesign / MUI / Shadcn 等参考实现，React 皮肤独立为 CubeAntd 仓库；MVC Razor（CubeNC）保持兼容
- 需求只在 Markdown：可扩展架构：通过 EntityController 继承、字段元数据、IModule 插件机制深度定制
- 需求只在 Markdown：超大数据支撑：基于 XCode ORM 的分表、读写分离、二级缓存，支撑单表 100 亿级数据
- 需求只在 Markdown：BASE-1 统一响应协议：所有 API 统一返回 ApiResponse<T> 结构，code=0 表示成功，列表接口使用 ApiListResponse<T> 携带分页信息。
- 需求只在 Markdown：BASE-2 权限注解：[EntityAuthorize(PermissionFlags.Detail)] 控制 Action 权限，[Menu(100, true, Icon = "fa-table")] 自动注册菜单。
- 需求只在 Markdown：BASE-3 模块化插件：通过 IModule 接口实现功能模块自动注册，NuGet 包引用后自动注册服务和路由。
- 需求只在 Markdown：BASE-4 跨域支持（CORS）：内置 CORS 支持，支持全允许和指定来源两种模式，支持 credentials 传递。
- 需求只在 Markdown：BASE-5 数据保护（DPAPI）：基于 DPAPI 的数据保护，密钥持久化到数据库。
- 需求只在 Markdown：BASE-6 数据保留策略：定时清理过期数据，支持按保留天数自动清理，支持按数据表配置不同策略。
- 需求只在 Markdown：BASE-7 应用插件管理：应用扩展插件的注册与查看管理。
- 需求只在 pdf：多前端支持：Vue为官方前端与核心库载体；仓库内另提供Angular / Svelte / NaiveUI / ArcoVue / Vuetify / TDesign / MUI / Shadcn等参考实现，React皮肤独立为CubeAntd仓库；MVC Razor（CubeNC）保持兼容
- 需求只在 pdf：可扩展架构：通过EntityController继承、字段元数据、IModule插件机制深度定制
- 需求只在 pdf：超大数据支撑：基于XCode ORM的分表、读写分离、二级缓存，支撑单表100亿级数据
- 需求只在 pdf：BASE-1统一响应协议：所有API统一返回ApiResponse<T>结构，code=0表示成功，列表接口使用ApiListResponse<T>携带分页信息。
- 需求只在 pdf：BASE-2权限注解：[EntityAuthorize(PermissionFlags.Detail)]控制Action权限，[Menu(100, true,Icon ="fa-table")]自动注册菜单。
- 需求只在 pdf：BASE-3模块化插件：通过IModule接口实现功能模块自动注册，NuGet包引用后自动注册服务和路由。
- 需求只在 pdf：BASE-4跨域支持（CORS）：内置CORS支持，支持全允许和指定来源两种模式，支持credentials传递。
- 需求只在 pdf：BASE-5数据保护（DPAPI）：基于DPAPI的数据保护，密钥持久化到数据库。
- 需求只在 pdf：BASE-6数据保留策略：定时清理过期数据，支持按保留天数自动清理，支持按数据表配置不同策略。
- 需求只在 pdf：BASE-7应用插件管理：应用扩展插件的注册与查看管理。

### NewLifeX__NewLife.IoT

段落标题不一致，需求条目 1 / 57 一致（pdf 拆出 56 条）

- 标题只在 Markdown：NewLife.IoT 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.IoT需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：SYS-1 统一异步驱动接口：IDriver 定义 OpenAsync/CloseAsync/ReadAsync/WriteAsync/ControlAsync 全异步 I/O 方法，CreateParameter/GetSpecification 元数据同步。
- 需求只在 Markdown：SYS-2 驱动抽象基类：DriverBase 提供 Diagnostics 开关、ServiceProvider 注入、RaiseDataReceived 推送触发、OnGetSpecification/OnCreateParameter 虚钩子；泛型版 DriverBase<TNode,TParameter> 固定节点和参数类型。
- 需求只在 Markdown：SYS-3 推送事件模型：DataReceived 事件直接定义在 IDriver 上，DriverDataEventArgs 携带 Node/Points/Result（含时间戳和质量码），轮询驱动无需触发。
- 需求只在 Markdown：SYS-4 结构化结果类型：IDriverResult 统一 IsSuccess/Code/Message；ReadResult 用 Points[]/Values[] 平行数组+Quality+Timestamp；WriteResult 为 readonly struct 零堆分配含 AffectedCount/EchoValue；ControlResult 含 OutputParameters 字典；均支持可选诊断帧。
- 需求只在 Markdown：SYS-5 数据质量码：DataQuality 枚举参考 OPC UA——Good/Uncertain/Bad/BadNotConnected/BadTimeout/BadChecksumError/BadProtocolError 三级七值。
- 需求只在 Markdown：SYS-6 结构化异常与错误码：IoTException 携带 IoTErrorCode；1000 段配置错误（InvalidParameter/DriverNotFound/NotSupported）应抛出；2000 段运行时错误（ConnectionFailed/Timeout/ChecksumError 等）走 Result.IsSuccess=false；3000 段设备状态（DeviceOffline/InvalidAddress）。
- 需求只在 Markdown：SYS-7 请求对象：WriteRequest 包装点位+值，支持 ()/(value)/(point,value) 三构造函数；ControlRequest 用 ServiceName+Parameters+Create() 工厂；均实现 IExtend 扩展元数据。
- 需求只在 Markdown：SYS-8 设备发现：IDiscoverableDriver.DiscoverAsync 扫描网络或总线上的子设备，返回 IEnumerable<IDeviceInfo>，适用于 Modbus/BACnet 等广播协议。
- 需求只在 Markdown：SYS-9 驱动工厂：DriverFactory.Register<T> 注册、Create(name,identifier) 创建实例（相同 identifier 共享单实例）、CreateParameter(name,parameter) 创建参数、ScanAll() 插件扫描；[DriverAttribute] 标注驱动名称。
- 需求只在 Markdown：SYS-10 传输层接口：ITransport 统一 Open/Close/Send/Receive/SendReceive（原子请求-响应），串口/TCP/UDP/HTTP 实现分别在 NewLife.IoTSerial 和 NewLife.IoTSocket 中。
- 需求只在 pdf：SYS-1统一异步驱动接口：IDriver定义OpenAsync/CloseAsync/ReadAsync/WriteAsync/ControlAsync全异步I/O方法，CreateParameter/GetSpecification元数据同步。
- 需求只在 pdf：SYS-2驱动抽象基类：DriverBase提供Diagnostics开关、ServiceProvider注入、RaiseDataReceived推送触发、OnGetSpecification/OnCreateParameter虚钩子；泛型版DriverBase<TNode,TParameter>固定节点和参数类型。
- 需求只在 pdf：SYS-3推送事件模型：DataReceived事件直接定义在IDriver上，DriverDataEventArgs携带Node/Points/Result（含时间戳和质量码），轮询驱动无需触发。
- 需求只在 pdf：SYS-4结构化结果类型：IDriverResult统一IsSuccess/Code/Message；ReadResult用Points[]/Values[]平行数组+Quality+Timestamp；WriteResult为readonly struct零堆分配含AffectedCount/EchoValue；ControlResult含OutputParameters字典；均支持可选诊断帧。
- 需求只在 pdf：SYS-5数据质量码：DataQuality枚举参考OPC UA—— Good/Uncertain/Bad/BadNotConnected/BadTimeout/BadChecksumError/ BadProtocolError三级七值。
- 需求只在 pdf：SYS-6结构化异常与错误码：IoTException携带IoTErrorCode；1000段配置错误（InvalidParameter/DriverNotFound/NotSupported）应抛出；2000段运行时错误（ConnectionFailed/Timeout/ChecksumError等）走Result.IsSuccess=false；3000段设备状态（DeviceOffline/InvalidAddress）。
- 需求只在 pdf：SYS-7请求对象：WriteRequest包装点位+值，支持()/(value)/(point,value)三构造函数；ControlRequest用ServiceName+Parameters+Create()工厂；均实现IExtend扩展元数据。
- 需求只在 pdf：SYS-8设备发现：IDiscoverableDriver.DiscoverAsync扫描网络或总线上的子设备，返回IEnumerable<IDeviceInfo>，适用于Modbus/BACnet等广播协议。
- 需求只在 pdf：SYS-9驱动工厂：DriverFactory.Register<T>注册、Create(name,identifier)创建实例（相同identifier共享单实例）、CreateParameter(name,parameter)创建参数、ScanAll()插件扫描；[DriverAttribute]标注驱动名称。
- 需求只在 pdf：SYS-10传输层接口：ITransport统一Open/Close/Send/Receive/SendReceive（原子请求-响应），串口/TCP/UDP/HTTP实现分别在NewLife.IoTSerial和NewLife.IoTSocket中。

### NewLifeX__NewLife.MQTT

段落标题不一致，需求条目 0 / 59 一致（pdf 拆出 59 条）

- 标题只在 Markdown：NewLife.MQTT 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.MQTT需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：PROT-1 MQTT 基础报文结构：4 位类型 + 4 位标志 + 1~4 字节变长剩余长度（最大 256MB），MqttCodec + PacketCodec 流式解析，UInt16 报文标识符线程安全分配。所有上层报文编解码的公共基础。
- 需求只在 Markdown：PROT-2 MQTT 3.1/3.1.1 报文编解码：14 种报文类型（CONNECT ~ DISCONNECT）完整序列化与反序列化，包括 MQTT 3.1 协议名（MQIsdp）识别。
- 需求只在 Markdown：PROT-3 MQTT 5.0 报文与属性系统：15 种报文类型（含 AUTH）+ 30 种属性标识符 + 7 种数据类型完整编解码，所有 ACK 报文 ReasonCode 扩展，服务端断开报文（DisconnectMessage）。
- 需求只在 Markdown：PROT-4 QoS 0/1/2 确认流程：三级服务质量完整确认流程（含 QoS 2 四步握手：PUBLISH→PUBREC→PUBREL→PUBCOMP）。
- 需求只在 Markdown：PROT-5 主题与通配符：/ 分层 + + 单层 + # 多层通配符匹配，$SYS 屏蔽通配符订阅，主题最大 65536 字节验证，共享订阅 $share/{group}/{topic} 格式解析。
- 需求只在 Markdown：传输层支持七种传输方式的统一接入，覆盖从标准 TCP 到弱网 UDP 的全场景。
- 需求只在 Markdown：TRAN-1 TCP / TLS / WebSocket / WSS：TCP 走 1883，协议泵由 MqttCodec 解析（内建 PROXY 头定界）；WebSocket 走独立端口（EnableWebSocket/WebSocketPort，端口为 0 时由系统分配，路径默认 /mqtt），由 HttpServer + MqttWebSocketHandler 桥接，子协议 mqtt。TLS 1.2+ 支持 pfx/pem 证书。
- 需求只在 Markdown：TRAN-2 MQTT over QUIC：基于 System.Net.Quic，ALPN mqtt，默认端口 14567，.NET 7+ 可用。
- 需求只在 Markdown：TRAN-3 MQTT over 可靠 UDP：自研可靠传输层（4 字节帧头 + 序列号 + Ack 确认 + 超时重发），全平台可用，无需操作系统 msquic 支持。
- 需求只在 Markdown：TRAN-4 ProxyProtocol v1/v2：服务端解析 HAProxy/nginx 代理协议 v1（文本）和 v2（二进制），透传真实客户端 IP。
- 需求只在 pdf：PROT-1 MQTT基础报文结构：4位类型+ 4位标志+ 1~4字节变长剩余长度（最大256MB），MqttCodec+PacketCodec流式解析，UInt16报文标识符线程安全分配。所有上层报文编解码的公共基础。
- 需求只在 pdf：PROT-2 MQTT 3.1/3.1.1报文编解码：14种报文类型（CONNECT~ DISCONNECT）完整序列化与反序列化，包括MQTT 3.1协议名（MQIsdp）识别。
- 需求只在 pdf：PROT-3 MQTT 5.0报文与属性系统：15种报文类型（含AUTH）+30种属性标识符+ 7种数据类型完整编解码，所有ACK报文ReasonCode扩展，服务端断开报文（DisconnectMessage）。
- 需求只在 pdf：PROT-4 QoS 0/1/2确认流程：三级服务质量完整确认流程（含QoS 2四步握手：PUBLISH→PUBREC→PUBREL→PUBCOMP）。
- 需求只在 pdf：PROT-5主题与通配符：/分层++单层+#多层通配符匹配，$SYS屏蔽通配符订阅，主题最大65536字节验证，共享订阅$share/{group}/{topic}格式解析。
- 需求只在 pdf：传输层支持七种传输方式的统一接入，覆盖从标准TCP到弱网UDP的全场景。
- 需求只在 pdf：TRAN-1 TCP / TLS / WebSocket / WSS：TCP走1883，协议泵由MqttCodec解析（内建PROXY头定界）；WebSocket走独立端口（EnableWebSocket/WebSocketPort，端口为0时由系统分配，路径默认/mqtt），由HttpServer+MqttWebSocketHandler桥接，子协议mqtt。TLS
- 需求只在 pdf：TRAN-2 MQTT over QUIC：基于System.Net.Quic，ALPN mqtt，默认端口14567，.NET 7+可用。
- 需求只在 pdf：TRAN-3 MQTT over可靠UDP：自研可靠传输层（4字节帧头+序列号+ Ack确认+超时重发），全平台可用，无需操作系统msquic支持。
- 需求只在 pdf：TRAN-4 ProxyProtocol v1/v2：服务端解析HAProxy/nginx代理协议v1（文本）和v2（二进制），透传真实客户端IP。

### NewLifeX__NewLife.Modbus

段落标题不一致，需求条目 0 / 13 一致（pdf 拆出 4 条）

- 标题只在 Markdown：NewLife.Modbus 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.Modbus需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：为 .NET 工业物联网生态提供一套协议最完整、功能码覆盖最全、传输变体最丰富的 Modbus 协议库，支持 IoTEdge 网关及各类工业应用开发，让 .NET 开发者能用最少的代码完成工业设备对接，同时具备充分的可扩展性和可观测性。
- 需求只在 Markdown：编码：CORE-12；功能：地址解析；一句话描述：支持 DO/0x/DI/1x/AI/3x/AO/4x 多格式 + 位域语法
- 需求只在 Markdown：编码：TRAN-1；功能：ModbusTCP（含 TLS）；一句话描述：标准 Modbus TCP/IP 实现，MBAP 头 + PDU，端口 502；设置 SslProtocol 后自动启用 TLS 安全传输，支持客户端证书验证
- 需求只在 Markdown：编码：FC-07；功能码：FC08；功能：诊断；一句话描述：子功能码诊断，支持 Echo Test
- 需求只在 Markdown：编码：FC-12；功能码：FC43；功能：读设备标识；一句话描述：读取从机设备标识码，支持指定起始 objectId，返回 ObjectId→字符串字典
- 需求只在 Markdown：编码：FC-13；功能码：FC07；功能：读异常状态；一句话描述：读取从机异常状态字节，Master + TCP/RTU/ASCII Slave 完整支持
- 需求只在 Markdown：编码：FC-14；功能码：FC11；功能：获取通信事件计数；一句话描述：获取从机通信事件计数器，Master + TCP/RTU/ASCII Slave 完整支持
- 需求只在 Markdown：编码：FC-15；功能码：FC12；功能：获取通信事件日志；一句话描述：获取从机通信事件日志列表，Master + TCP/RTU/ASCII Slave 完整支持
- 需求只在 Markdown：编码：FC-16；功能码：FC17；功能：报告服务器 ID；一句话描述：获取从机服务器标识和运行指示，Master + TCP/RTU/ASCII Slave 完整支持
- 需求只在 Markdown：编码：SLAVE-1；功能：TCP 从机服务；一句话描述：基于 NetServer 的高性能 TCP 从机，监听端口 502，支持多客户端并发连接
- 需求只在 pdf：为.NET工业物联网生态提供一套协议最完整、功能码覆盖最全、传输变体最丰富的Modbus协议库，支持IoTEdge网关及各类工业应用开发，让.NET开发者能用最少的代码完成工业设备对接，同时具备充分的可扩展性和可观测性。
- 需求只在 pdf：编码功能一句话描述TRAN-1 ModbusTCP（含标准Modbus TCP/IP TLS）实现，MBAP头+ PDU，端口502；设置SslProtocol后自动启用TLS安全传输，支持客户端证书验证TRAN-2 ModbusUDP Modbus over UDP无连接传输实现TRAN-3 ModbusRtuOverTCP RTU帧（含CRC）通过TCP传输TRAN-4 ModbusRtuOverUDP RTU帧（含CRC）通过UDP传输TRAN-5 ModbusIp网络基类TCP/UDP子类的公共抽象，统一管理Server地址和客户端生
- 需求只在 pdf：编码功能码功能一句话描述FC-13 FC07读异常状态读取从机异常状态字节，Master + TCP/RTU/ASCII Slave完整支持FC-14 FC11获取通信事件计获取从机通信事数件计数器，Master+ TCP/RTU/ASCII Slave完整支持FC-15 FC12获取通信事件日获取从机通信事志件日志列表，Master+ TCP/RTU/ASCII Slave完整支持FC-16 FC17报告服务器ID获取从机服务器标识和运行指示，Master+ TCP/RTU/ASCII Slave完整支持FC-17 FC20读文件记录读取从机文件记
- 需求只在 pdf：编码功能一句话描述SLAVE-1 TCP从机服务基于NetServer的高性能TCP从机，监听端口502，支持多客户端并发连接SLAVE-2会话处理OnReceive中解析19个功能码请求并路由响应，优先匹配自定义处理器SLAVE-3 List<RegisterUnit>寄存器数据存储保持寄存器/输入寄存器数据存储SLAVE-4线圈数据存储List<CoilUnit>线圈/离散输入数据存储SLAVE-5 RTU串口从机ModbusRtuSlave串口RTU从机实现SLAVE-6 ASCII串口从机ModbusAsciiSlave串口ASCII从机实现

### NewLifeX__NewLife.Remoting

段落标题不一致，需求条目 3 / 83 一致（pdf 拆出 82 条）

- 标题只在 Markdown：NewLife.Remoting 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.Remoting需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：包：NewLife.Remoting；定位：核心通信库；覆盖：RPC 客户端/服务端、协议编解码、连接管理、流式调用、客户端基类、指令下发管线、自动更新、NativeAOT 支持
- 需求只在 Markdown：使 .NET 开发者能在 net45 ~ net10.0 单一生态内完成全部远程通信需求——RPC（二进制高性能）、HTTP/REST、WebSocket 长连接、SRMP 远程消息协议，同时为 IoT 场景提供指令下发、设备管理和自动更新的一站式解决方案；net8.0+ 支持 NativeAOT 发布。
- 需求只在 Markdown：RPC-1 自定义协议帧：应用可通过自定义协议帧高效完成远程调用，支持粘拆包、双向消息、单向通知
- 需求只在 Markdown：RPC-2 可扩展编解码：支持 JSON 和二进制两种序列化方式，可按需替换编码器，兼顾调试便利性和传输效率
- 需求只在 Markdown：RPC-3 零拷贝内存管理：大吞吐场景下零拷贝传递数据，避免频繁内存分配和拷贝
- 需求只在 Markdown：RPC-4 控制器元数据识别：框架自动识别控制器方法的参数类型和返回类型，支持二进制参数和流式返回
- 需求只在 Markdown：RPC-5 控制器自动注册：控制器自动注册，开发者只需编写普通类即可暴露远程服务
- 需求只在 Markdown：RPC-6 请求路由与参数绑定：请求自动路由到控制器方法，框架自动完成参数绑定和生命周期管理
- 需求只在 Markdown：RPC-7 高可用连接管理：客户端连接支持单节点故障转移和连接池负载均衡，保障服务可用性
- 需求只在 Markdown：RPC-8 多协议客户端：客户端通过统一 API 连接远程服务，支持自动重连、故障转移和身份凭证注入
- 需求只在 pdf：包定位覆盖NewLife.Remoting核心通信库RPC客户端/服务端、协议编解码、连接管理、流式调用、客户端基类、指令下发管线、自动更新、NativeAOT支持NewLife.Remoting.Ext扩展库服务端控制器基类ensions（BaseController/ BaseDeviceController/ BaseOAuthController）、最小API宿主、设备管理服务、Token鉴权、命令响应总线
- 需求只在 pdf：使.NET开发者能在net45 ~ net10.0单一生态内完成全部远程通信需求——RPC（二进制高性能）、HTTP/REST、WebSocket长连接、SRMP远程消息协议，同时为IoT场景提供指令下发、设备管理和自动更新的一站式解决方案；net8.0+支持NativeAOT发布。
- 需求只在 pdf：RPC-1自定义协议帧：应用可通过自定义协议帧高效完成远程调用，支持粘拆包、双向消息、单向通知
- 需求只在 pdf：RPC-2可扩展编解码：支持JSON和二进制两种序列化方式，可按需替换编码器，兼顾调试便利性和传输效率
- 需求只在 pdf：RPC-3零拷贝内存管理：大吞吐场景下零拷贝传递数据，避免频繁内存分配和拷
- 需求只在 pdf：RPC-4控制器元数据识别：框架自动识别控制器方法的参数类型和返回类型，支持二进制参数和流式返回
- 需求只在 pdf：RPC-5控制器自动注册：控制器自动注册，开发者只需编写普通类即可暴露远程服务
- 需求只在 pdf：RPC-6请求路由与参数绑定：请求自动路由到控制器方法，框架自动完成参数绑定和生命周期管理
- 需求只在 pdf：RPC-7高可用连接管理：客户端连接支持单节点故障转移和连接池负载均衡，保障服务可用性
- 需求只在 pdf：RPC-8多协议客户端：客户端通过统一API连接远程服务，支持自动重连、故障转移和身份凭证注入

### NewLifeX__NewLife.RocketMQ

段落标题不一致，需求条目 0 / 68 一致（pdf 拆出 68 条）

- 标题只在 Markdown：NewLife.RocketMQ 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 痛点
- 标题只在 Markdown：1.3 愿景
- 标题只在 pdf：NewLife.RocketMQ需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2痛点
- 标题只在 pdf：1.3愿景
- 需求只在 Markdown：NewLife.RocketMQ 是企业级纯托管 .NET RocketMQ 客户端，专为 .NET 生态设计，覆盖 .NET Framework 4.5+ 到 .NET 10。给 .NET 开发者提供一个零外部依赖、双协议支持、多云适配的消息队列客户端。
- 需求只在 Markdown：协议覆盖不全：现有方案多数仅支持单一协议，无法同时兼容 Remoting（4.x Broker）和 gRPC（5.x Proxy）两种接入方式
- 需求只在 Markdown：外部依赖沉重：部分方案依赖 Google.Protobuf、Grpc.Net.Client 等第三方库，增加部署复杂度和包体积
- 需求只在 Markdown：框架兼容不足：大量企业仍运行在 .NET Framework 4.5+，但可用选项极为有限
- 需求只在 Markdown：云厂商适配分散：接入阿里云、华为云、腾讯云需要各自独立的 SDK，缺乏统一接口
- 需求只在 Markdown：PROTO-1 Remoting 协议通信：实现 RocketMQ 4.x/5.x Broker TCP 私有协议（二进制帧 + JSON/ROCKETMQ 序列化），支持连接池复用、Opaque 请求响应匹配、HMAC-SHA1 签名、SSL/TLS、VIP 通道，实现 60+ RequestCode 指令。
- 需求只在 Markdown：PROTO-2 gRPC Proxy 协议通信：实现 RocketMQ 5.x Proxy HTTP/2 + Protobuf 协议，手写 Protobuf 字段编解码（基于 NewLife.Core 的 SpanWriter/SpanReader，零外部依赖），支持 Unary + Server Streaming + Telemetry 长连接，实现 11 个核心 RPC 方法；明文端点强制 HTTP/2（h2c）、按调用声明 grpc-timeout，资源上报长连接保持 Proxy 侧客户端注册与订阅关系。
- 需求只在 Markdown：PROTO-3 NameServer 路由发现：Topic 路由查询与 30s 定时轮询刷新，多 Topic 路由管理，Broker 主从地址解析，支持 HTTP 方式获取 NameServer 地址（阿里云）。
- 需求只在 Markdown：PROTO-4 Broker 心跳与客户端注销：30s 定时心跳保活，客户端优雅注销。
- 需求只在 Markdown：PROTO-5 VIP 通道：BrokerPort - 2 优先级连接通道。
- 需求只在 pdf：NewLife.RocketMQ是企业级纯托管.NET RocketMQ客户端，专为.NET生态设计，覆盖.NET Framework 4.5+到.NET 10。给.NET开发者提供一个零外部依赖、双协议支持、多云适配的消息队列客户端。
- 需求只在 pdf：协议覆盖不全：现有方案多数仅支持单一协议，无法同时兼容Remoting（4.x Broker）和gRPC（5.x Proxy）两种接入方式
- 需求只在 pdf：外部依赖沉重：部分方案依赖Google.Protobuf、Grpc.Net.Client等第三方库，增加部署复杂度和包体积
- 需求只在 pdf：框架兼容不足：大量企业仍运行在.NET Framework 4.5+，但可用选项极为有限
- 需求只在 pdf：云厂商适配分散：接入阿里云、华为云、腾讯云需要各自独立的SDK，缺乏统一接口
- 需求只在 pdf：PROTO-1 Remoting协议通信：实现RocketMQ 4.x/5.x Broker TCP私有协议（二进制帧+ JSON/ROCKETMQ序列化），支持连接池复用、Opaque请求响应匹配、HMAC-SHA1签名、SSL/TLS、VIP通道，实现60+ RequestCode指令。
- 需求只在 pdf：PROTO-2 gRPC Proxy协议通信：实现RocketMQ 5.x Proxy HTTP/2 + Protobuf协议，手写Protobuf字段编解码（基于NewLife.Core的SpanWriter/SpanReader，零外部依赖），支持Unary + Server Streaming + Telemetry长连接，实现11个核心RPC方法；明文端点强制HTTP/2（h2c）、按调用声明grpc-timeout，资源上报长连接保持Proxy侧客户端注册与订阅关系。
- 需求只在 pdf：PROTO-3 NameServer路由发现：Topic路由查询与30s定时轮询刷新，多Topic路由管理，Broker主从地址解析，支持HTTP方式获取NameServer地址（阿里云）。
- 需求只在 pdf：PROTO-4 Broker心跳与客户端注销：30s定时心跳保活，客户端优雅注销。
- 需求只在 pdf：PROTO-5 VIP通道：BrokerPort- 2优先级连接通道。

### NewLifeX__NewLife.Siemens

段落标题不一致，需求条目 6 / 133 一致（pdf 拆出 72 条）

- 标题只在 Markdown：NewLife.Siemens 需求文档
- 标题只在 Markdown：1. 愿景与目标
- 标题只在 Markdown：1.0 项目愿景
- 标题只在 Markdown：1.1 背景与痛点
- 标题只在 Markdown：1.2 目标
- 标题只在 pdf：NewLife.Siemens需求文档
- 标题只在 pdf：1.愿景与目标
- 标题只在 pdf：1.0项目愿景
- 标题只在 pdf：1.1背景与痛点
- 标题只在 pdf：1.2目标
- 需求只在 Markdown：提供工业物联网领域最完整、最易用的西门子 PLC S7 协议 .NET 实现，作为 NewLife 开源生态的 IoT 标准驱动组件，让工控工程师能够用几行代码无缝接入任意型号的西门子 PLC，同时支持在 IoTEdge 工业网关中零代码配置化采集。
- 需求只在 Markdown：描述：建立、维护和销毁与 PLC 的 TCP 连接，处理断线自动重连
- 需求只在 Markdown：用户故事：作为工控工程师，我希望创建 S7Client 后调用 OpenAsync() 即可完成三层握手（TPKT → COTP → S7 Setup），以便无需关心底层协议细节
- 需求只在 Markdown：支持 TCP 连接建立（含 KeepAlive 设置）
- 需求只在 Markdown：完成 COTP ConnectionRequest / ConnectionConfirmed 握手
- 需求只在 Markdown：完成 S7 SetupMessage 协商 PDU 大小
- 需求只在 Markdown：断线后下次读写自动触发重连（GetStream 内部检测）
- 需求只在 Markdown：支持显式 Close() 释放连接
- 需求只在 Markdown：描述：以字节数组为基本单位，从任意 PLC 地址区域读取或写入数据
- 需求只在 Markdown：用户故事：作为工控工程师，我希望调用 ReadBytes(address, count) / WriteBytes(address, data) 即可完成数据交换，以便在需要时进行自定义数据解析
- 需求只在 pdf：提供工业物联网领域最完整、最易用的西门子PLC S7协议.NET实现，作为NewLife开源生态的IoT标准驱动组件，让工控工程师能够用几行代码无缝接入任意型号的西门子PLC，同时支持在IoTEdge工业网关中零代码配置化采集。
- 需求只在 pdf：描述：建立、维护和销毁与PLC的TCP连接，处理断线自动重连
- 需求只在 pdf：用户故事：作为工控工程师，我希望创建S7Client后调用OpenAsync()即可完成三层握手（TPKT→ COTP → S7 Setup），以便无需关心底层协议细节
- 需求只在 pdf：验收条件：☒支持TCP连接建立（含KeepAlive设置）☒完成COTP ConnectionRequest / ConnectionConfirmed握手☒完成S7 SetupMessage协商PDU大小☒断线后下次读写自动触发重连（GetStream内部检测）☒支持显式Close()释放连接
- 需求只在 pdf：描述：以字节数组为基本单位，从任意PLC地址区域读取或写入数据
- 需求只在 pdf：用户故事：作为工控工程师，我希望调用ReadBytes(address, count) / WriteBytes(address, data)即可完成数据交换，以便在需要时进行自定义数据解析
- 需求只在 pdf：验收条件：☒ReadBytes支持任意长度（超PDU限制时自动分多段）☒WriteBytes支持任意长度（超PDU限制时自动分多段）☒读写失败时抛出包含错误码的ApiException ☒支持所有地址区域：DB/ Input / Output / Memory / Timer / Counter
- 需求只在 pdf：用户故事：作为工控工程师，我希望使用"DB1.DBW0"、"M0.0"、"IW4"这样的西门子标准地址格式，以便与Step7/TIA Portal中的地址保持一致
- 需求只在 pdf：验收条件：☒支持DB（DBB/DBW/DBD/DBX/STRING）地址格式☒支持I/E（输入）地址（IB/IW/ID/I0.0等）☒支持Q/A（输出）地址（QB/QW/QD/Q0.0等）☒支持M（标志区）地址（MB/MW/MD/M0.0等）☒支持T（定时器）地址☒支持C（计数器）地址☒STRING地址格式：DB1.STRING0.60（第三段为最大长度）☒解析错误时抛出InvalidDataException
- 需求只在 pdf：描述：定义PLC侧数据类型与.NET侧类型的对应关系

### NewLifeX__Stardust

段落标题不一致，需求条目 2 / 30 一致（pdf 拆出 18 条）

- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 Markdown：2.1 模块总览
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 标题只在 pdf：2.1模块总览
- 需求只在 Markdown：一键接入分布式：几行代码完成分布式接入，应用零改造即可获得配置中心、注册中心、APM 能力
- 需求只在 Markdown：全平台覆盖：同一生态覆盖 .NET Framework 4.5 起至最新 .NET 10，Windows/Linux/macOS/Android/iOS/ARM/IoT 全平台
- 需求只在 Markdown：自带运维体系：StarAgent 守护进程 + 远程发布 + 指标&日志采集，极大降低分布式运维复杂度
- 需求只在 Markdown：编号：CFG；目标：配置中心；一句话描述：应用从中心读取配置，支持多环境热更新；所属工程：StarServer + SDK + StarWeb；架构文档：SVR-StarServer架构
- 需求只在 Markdown：编码：MLSDK-1；功能：JavaScript SDK（浏览器）；说明：UMD 单文件；登录、心跳性能、页面/路由/JS 错误/fetch/XHR 埋点；支持 secret 与 tokenProvider
- 需求只在 Markdown：编码：SVR-5；功能：分表服务；说明：支持按时间分表存储
- 需求只在 Markdown：编码：SVR-7；功能：Apollo 配置集成；说明：支持从 Apollo 配置中心同步
- 需求只在 Markdown：编码：NODE-16；功能：多供应商 DNS DDNS；说明：动态域名解析，支持阿里云/腾讯云(DNSPod)/优刻得(UDNS)/AWS Route53 四家供应商，服务端 DnsService 自动检测节点 IP 变化并触发 DNS 更新
- 需求只在 Markdown：编码：NODE-19；功能：域名供应商管理；说明：管理 DNS 供应商凭据配置（阿里云/AWS Route53 等），支持多供应商 DDNS
- 需求只在 Markdown：编码：NODE-24；功能：Go 原生 Agent；说明：无 .NET 运行时的轻量 Agent，支持登录/心跳/指标/事件/命令/服务安装；已通过 6 项一致性测试
- 需求只在 pdf：一键接入分布式：几行代码完成分布式接入，应用零改造即可获得配置中心、注册中心、APM能力
- 需求只在 pdf：全平台覆盖：同一生态覆盖.NET Framework 4.5起至最新.NET 10，Windows/Linux/macOS/Android/iOS/ARM/IoT全平台
- 需求只在 pdf：自带运维体系：StarAgent守护进程+远程发布+指标&日志采集，极大降低分布式运维复杂度
- 需求只在 pdf：编码功能说明MLSDK-1 JavaScript SDK（浏览UMD单文件；登录、器）心跳性能、页面/路由/J S错误/fetch/XHR埋点；支持secret与
- 需求只在 pdf：编码功能说明SVR-1健康检测接口提供服务健康状态检测端点SVR-2接口列表自动枚举所有注册的API接口SVR-3数据保留与清理自动清理过期数据SVR-4 .NET运行时同步自动同步官方.NET发布信息SVR-5分表服务支持按时间分表存储SVR-6上行链路服务处理客户端到服务端的上行数据通道SVR-7 Apollo配置集成支持从Apollo配置中心同步SVR-8远程命令执行安全StarAgent远程命令执编码功能说明行的安全策略、日志审计方案
- 需求只在 pdf：编码功能说明CFG-1配置拉取（GetAll）应用通过API拉取全部配置，支持版本号增量更新CFG-2配置设置（SetAll）应用上报所用配置键和缺失键，服务端更新CFG-3配置历史记录配置的变更历史，支持回滚追溯CFG-4配置数据管理在StarWeb上按应用编码功能说明/作用域管理配置项CFG-5应用规则（Scope）根据应用所在IP/机房自动匹配配置作用域CFG-7 HTTP配置提供者客户端通过HTTP从配置中心拉取配置CFG-8配置自动注册新应用首次拉取配置时自动创建应用记录
- 需求只在 pdf：编码功能说明APM-1埋点数据上报客户端按周期批量上报埋点统计数据APM-2压缩数据上报支持GZip压缩后的大批量数据上报APM-3追踪统计服务服务端核心统计引擎（约80%系统资源），处理埋点数据聚合编码功能说明APM-4应用每日统计按应用维度每日汇总统计指标APM-5埋点项统计按TraceItem维度统计各埋点的调用量、成功
- 需求只在 pdf：PUB-11附件管理部署包文件的上传、存储、分发PUB-12 Webhook支持部署事件触发的Webhook通知PUB-13产品版本管理管理产品级版本发布计
- 需求只在 pdf：GW-3网关集群管理管理网关实例集群GW-4网关节点管理管理各网关节点的运行状态GW-5网关证书管理管理网关SSL证书GW-6 StarGateway集成作为StarServer客户端统一接入GW-7 NAT代理转发通用TCP/UDP NAT代理，支持跨协议数据转发
- 需求只在 pdf：编码功能说明MCP-1 MCP HTTP端点POST/mcp端点，JSON-RPC 2.0协议，支持编码功能说明initialize/tools.l ist/tools.call

### NewLifeX__X

段落标题不一致，需求条目 0 / 136 一致（pdf 拆出 136 条）

- 标题只在 Markdown：NewLife.Core 需求文档
- 标题只在 Markdown：1. 背景与愿景
- 标题只在 Markdown：1.1 系统定位
- 标题只在 Markdown：1.2 愿景
- 标题只在 Markdown：2. 核心目标
- 标题只在 pdf：NewLife.Core需求文档
- 标题只在 pdf：1.背景与愿景
- 标题只在 pdf：1.1系统定位
- 标题只在 pdf：1.2愿景
- 标题只在 pdf：2.核心目标
- 需求只在 Markdown：NewLife.Core 是 NewLife 组件生态的基础核心库，为构建可扩展 .NET 应用程序提供高性能基础设施。支持 .NET Framework 4.5 至 .NET 10.0 全版本。
- 需求只在 Markdown：M1-1 类型转换：提供 ToInt()/ToBoolean()/ToDateTime() 等高效类型转换扩展方法。
- 需求只在 Markdown：M1-2 字符串扩展：字符串截取、编码、格式化、空值判断等工具方法。
- 需求只在 Markdown：M1-3 路径扩展：跨平台路径处理，智能处理多种路径格式。
- 需求只在 Markdown：M1-4 数据扩展：高效 IO 操作，流与字节数组转换。
- 需求只在 Markdown：M1-5 进程扩展：简化进程管理，获取进程信息。
- 需求只在 Markdown：M1-6 运行时信息：应用运行时信息获取，便于调试诊断。
- 需求只在 Markdown：M1-7 可销毁基类：标准资源释放模式，自动生命周期追踪。
- 需求只在 Markdown：M1-8 反射扩展：高性能反射工具，快速对象成员读写。
- 需求只在 Markdown：M1-9 拼音库：高效汉字转拼音，支持全拼和简拼。
- 需求只在 pdf：NewLife.Core是NewLife组件生态的基础核心库，为构建可扩展.NET应用程序提供高性能基础设施。支持.NET Framework 4.5至.NET 10.0全版本。
- 需求只在 pdf：M1-1类型转换：提供ToInt()/ToBoolean()/ToDateTime()等高效类型转换扩展方法。
- 需求只在 pdf：M1-2字符串扩展：字符串截取、编码、格式化、空值判断等工具方法。
- 需求只在 pdf：M1-3路径扩展：跨平台路径处理，智能处理多种路径格式。
- 需求只在 pdf：M1-4数据扩展：高效IO操作，流与字节数组转换。
- 需求只在 pdf：M1-5进程扩展：简化进程管理，获取进程信息。
- 需求只在 pdf：M1-6运行时信息：应用运行时信息获取，便于调试诊断。
- 需求只在 pdf：M1-7可销毁基类：标准资源释放模式，自动生命周期追踪。
- 需求只在 pdf：M1-8反射扩展：高性能反射工具，快速对象成员读写。
- 需求只在 pdf：M1-9拼音库：高效汉字转拼音，支持全拼和简拼。

### PGshen__thinking-map

段落标题不一致，需求条目 60 / 122 一致（pdf 拆出 97 条）

- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 Markdown：1.4 用户痛点
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定义
- 标题只在 pdf：1.2产品愿景
- 标题只在 pdf：1.3目标用户
- 标题只在 pdf：1.4用户痛点
- 需求只在 Markdown：ThinkingMap 是一款交互式AI问题解决可视化助手，将AI的思考和问题解决过程转化为可视化的图结构，允许用户在过程中随时干预、提问。
- 需求只在 Markdown：用户想要在思考过程中提供输入和调整方向，而不只是在开始和结束时
- 需求只在 Markdown：现有解决方案缺乏结构化的问题分解和可视化
- 需求只在 Markdown：透明化思考: 可视化AI的问题解决步骤和逻辑
- 需求只在 Markdown：用户控制: 在任何阶段干预和引导思考方向
- 需求只在 Markdown：结构化思维: 将复杂问题分解为可管理的步骤
- 需求只在 Markdown：探索性思考: 支持多种可能的解决路径和分支
- 需求只在 Markdown：提供明确的文本输入区域，支持多行输入
- 需求只在 Markdown：问题类型选择（研究型、创意型、分析型、规划型）
- 需求只在 Markdown：基于 ReactFlow 实现的可视化工作区，占用界面左侧 65% 宽度（默认）
- 需求只在 pdf：透明化思考:可视化AI的问题解决步骤和逻辑
- 需求只在 pdf：用户控制:在任何阶段干预和引导思考方向
- 需求只在 pdf：结构化思维:将复杂问题分解为可管理的步骤
- 需求只在 pdf：探索性思考:支持多种可能的解决路径和分支
- 需求只在 pdf：1.1问题输入界面
- 需求只在 pdf：1.2问题理解确认
- 需求只在 pdf：2.1可视化思考图展示
- 需求只在 pdf：基于ReactFlow实现的可视化工作区，占用界面左侧65%宽度（默认）
- 需求只在 pdf：节点信息展示：o节点类型标识（图标+文字）o问题概述（限制40字符，超出显示省略号）o目标概述（限制30字符，超出显示省略号）o结论概述（仅在已完成状态显示，限制50字符）
- 需求只在 pdf：节点状态标识：o待执行（灰色边框）o执行中（蓝色边框+动画效果）o已完成（绿色边框+完成图标）o错误状态（红色边框+警告图标）

### Peter-cuhk__robot-data-studio

段落标题不一致，需求条目 102 / 254 一致（pdf 拆出 249 条）

- 标题只在 Markdown：Robot Data Studio 产品需求文档（PRD）
- 标题只在 Markdown：1. 产品摘要
- 标题只在 Markdown：3. 产品原则
- 标题只在 Markdown：3.1 本地优先
- 标题只在 Markdown：3.2 原始数据只读
- 标题只在 pdf：Robot Data Studio产品需求文档（PRD）
- 标题只在 pdf：1.产品摘要
- 标题只在 pdf：3.产品原则
- 标题只在 pdf：3.1本地优先
- 标题只在 pdf：3.2原始数据只读
- 需求只在 Markdown：导入 LeRobot、ACT/robomimic 风格 HDF5 和 UMI/Zarr 数据集。
- 需求只在 Markdown：使用确定性规则和可插拔 VLM 检查数据质量。
- 需求只在 Markdown：通过非破坏式 Pipeline 进行裁剪、筛选、重采样、字段映射和坐标变换。
- 需求只在 Markdown：Rerun 等工具的多模态回放和空间可视化优秀，但不是完整的数据清洗平台。
- 需求只在 Markdown：LeRobot、robomimic、UMI 等项目拥有各自的数据读取、可视化或转换代码，但格式和抽象不同。
- 需求只在 Markdown：部分开源项目提供数据审查、成功率判断或质量评分，但缺少统一的 Schema、坐标语义和导出闭环。
- 需求只在 Markdown：实际 HDF5 文件通常只有容器格式相同，内部字段命名、shape、单位、时间戳和坐标约定并不统一。
- 需求只在 Markdown：Adapter SDK：格式 Reader/Writer 插件体系。
- 需求只在 Markdown：所有裁剪、过滤和转换保存为 Pipeline 配置。
- 需求只在 Markdown：总分必须能追溯到各维度和具体 Finding。
- 需求只在 pdf：导入LeRobot、ACT/robomimic风格HDF5和UMI/Zarr数据集。
- 需求只在 pdf：使用确定性规则和可插拔VLM检查数据质量。
- 需求只在 pdf：通过非破坏式Pipeline进行裁剪、筛选、重采样、字段映射和坐标变换。
- 需求只在 pdf：Rerun等工具的多模态回放和空间可视化优秀，但不是完整的数据清洗平台。
- 需求只在 pdf：LeRobot、robomimic、UMI等项目拥有各自的数据读取、可视化或转换代码，但格式和抽象不同。
- 需求只在 pdf：部分开源项目提供数据审查、成功率判断或质量评分，但缺少统一的Schema、坐标语义和导出闭环。
- 需求只在 pdf：实际HDF5文件通常只有容器格式相同，内部字段命名、shape、单位、时间戳和坐标约定并不统一。
- 需求只在 pdf：Adapter SDK：格式Reader/Writer插件体系。
- 需求只在 pdf：所有裁剪、过滤和转换保存为Pipeline配置。
- 需求只在 pdf：总分必须能追溯到各维度和具体Finding。

### Poghappy__IhuoniaoN8NFirecralwrules

段落标题不一致，需求条目 12 / 22 一致（pdf 拆出 77 条）

- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：2. 功能需求
- 标题只在 Markdown：2.1 核心功能（Must Have）
- 标题只在 Markdown：2.2 重要功能（Should Have）
- 标题只在 Markdown：2.3 可选功能（Could Have）
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：2.功能需求
- 标题只在 pdf：1.数据采集流程
- 标题只在 pdf：2.AI分析流程
- 标题只在 pdf：3.多租户数据隔离流程
- 需求只在 Markdown：愿景&非目标、MoSCoW 优先级
- 需求只在 Markdown：验收标准矩阵(故事↔验收用例 1:1)
- 需求只在 Markdown：不提供实时告警功能
- 需求只在 Markdown：用户故事：租户数据隔离；验收用例：同租户访问；测试场景：租户A访问租户A数据；预期结果：系统允许访问并返回数据
- 需求只在 Markdown：用户故事：团队协作；验收用例：共享任务；测试场景：用户创建共享任务；预期结果：团队成员可以看到共享任务
- 需求只在 Markdown：inputs: 用户故事、业务目标、技术约束
- 需求只在 Markdown：decisions: 功能优先级、技术方案、接口设计
- 需求只在 Markdown：artifacts: PRD文档、接口规范、数据模型
- 需求只在 Markdown：risks: 识别的风险和缓解措施
- 需求只在 Markdown：next_instruction: 基于PRD进行任务分解和项目规划
- 需求只在 pdf：愿景&非目标、MoSCoW优先级
- 需求只在 pdf：验收标准矩阵(故事↔验收用例1:1)
- 需求只在 pdf：1核心功能（Must Have）数据采集管理###功能描述提供完整的数据采集任务管理功能，支持多种数据源和采集方式。
- 需求只在 pdf：创建数据采集任务
- 需求只在 pdf：监控采集进度
- 需求只在 pdf：管理采集结果
- 需求只在 pdf：设置采集参数
- 需求只在 pdf：任务列表页面
- 需求只在 pdf：任务详情页面
- 需求只在 pdf：任务创建向导

### Q572071793__word-pinyin

段落标题不一致，需求条目 3 / 120 一致（pdf 拆出 35 条）

- 标题只在 Markdown：中文拼音转换工具需求规格说明书
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：2. 功能需求
- 标题只在 pdf：（无标题）
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目背景
- 标题只在 pdf：1.2项目目标
- 标题只在 pdf：2.功能需求
- 需求只在 Markdown：需求描述: 将输入的中文文本转换为对应的拼音
- 需求只在 Markdown：支持所有常用汉字的拼音转换
- 需求只在 Markdown：正确处理多音字，优先使用最常见的读音
- 需求只在 Markdown：支持带声调和不带声调的拼音输出
- 需求只在 Markdown：转换准确率需达到99%以上
- 需求只在 Markdown：输入1000个常用汉字，正确转换率≥99%
- 需求只在 Markdown：处理速度：1000字符≤2秒
- 需求只在 Markdown：需求描述: 将拼音显示在对应汉字的上方
- 需求只在 Markdown：每个汉字对应一个独立的显示框
- 需求只在 Markdown：拼音显示在汉字上方，字体大小适中
- 需求只在 pdf：1.1拼音转换功能
- 需求只在 pdf：需求描述:将输入的中文文本转换为对应的拼音
- 需求只在 pdf：验收标准: o输入1000个常用汉字，正确转换率≥99% o处理速度：1000字符≤2秒
- 需求只在 pdf：1.2拼音显示功能
- 需求只在 pdf：需求描述:将拼音显示在对应汉字的上方
- 需求只在 pdf：o支持符号的特殊位置调整（如"，。"放右下角，"·"放中间）
- 需求只在 pdf：验收标准: o拼音与汉字对齐准确，错位≤2像素
- 需求只在 pdf：1.3实时显示功能
- 需求只在 pdf：需求描述:用户输入时实时显示拼音转换结果
- 需求只在 pdf：详细要求: o输入延迟≤500ms开始转换

### Quirt-studio__Qurit-PPT

段落标题不一致，需求条目 102 / 386 一致（pdf 拆出 276 条）

- 标题只在 Markdown：Qurit PPT 产品需求文档 (PRD)
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：1.1 版本历史
- 标题只在 Markdown：1.2 文档目的
- 标题只在 Markdown：1.3 相关文档引用
- 标题只在 pdf：Qurit PPT产品需求文档(PRD)
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：1.1版本历史
- 标题只在 pdf：1.2文档目的
- 标题只在 pdf：1.3相关文档引用
- 需求只在 Markdown：用户故事地图 (User_Story_Map.md)
- 需求只在 Markdown：产品评估指标框架 (Metrics_Framework.md)
- 需求只在 Markdown：零误差合规: 自动遵循行业规范，实时拦截敏感内容
- 需求只在 Markdown：内容驱动设计: 基于内容特征自动生成专业设计
- 需求只在 Markdown：严谨动态细节: 物理约束的动画系统，服务内容而非装饰
- 需求只在 Markdown：完全自主设计: AI全程自主设计，无需用户选择模板
- 需求只在 Markdown：专业设计师: 25-40岁，设计相关专业背景
- 需求只在 Markdown：公司职员: 25-45岁，中高级管理层或专业岗位
- 需求只在 Markdown：学生: 18-28岁，研究生或高年级本科生
- 需求只在 Markdown：重视内容质量和专业性
- 需求只在 pdf：用户故事地图(User_Story_Map.md)
- 需求只在 pdf：产品评估指标框架(Metrics_Framework.md)
- 需求只在 pdf：零误差合规:自动遵循行业规范，实时拦截敏感内容
- 需求只在 pdf：内容驱动设计:基于内容特征自动生成专业设计
- 需求只在 pdf：严谨动态细节:物理约束的动画系统，服务内容而非装饰
- 需求只在 pdf：完全自主设计:AI全程自主设计，无需用户选择模板
- 需求只在 pdf：目标市场:中国专业PPT制作市场
- 需求只在 pdf：市场规模:约50亿人民币/年
- 需求只在 pdf：增长率:年增长15-20%
- 需求只在 pdf：3.1直接竞争对手详析

### RZfive__WorldBase

段落标题不一致，需求条目 6 / 59 一致（pdf 拆出 41 条）

- 标题只在 Markdown：多 Agent 群组对话：从「协调者传话」到「Agent 互相对话」
- 标题只在 Markdown：§ 01 现状评估：它现在到底是怎么跑的
- 标题只在 Markdown：discussion 模式的执行结构
- 标题只在 Markdown：§ 02 核心问题诊断：为什么「不能让多个 Agent 对话」
- 标题只在 Markdown：① 通信拓扑：纯 hub-and-spoke，无点对点
- 标题只在 pdf：多Agent群组对话：从「协调者传话」到「Agent互相对话」
- 标题只在 pdf：§ 01现状评估：它现在到底是怎么跑的
- 标题只在 pdf：discussion模式的执行结构
- 标题只在 pdf：§ 02核心问题诊断：为什么「不能让多个Agent对话」
- 标题只在 pdf：①通信拓扑：纯hub-and-spoke，无点对点
- 需求只在 Markdown：配置层：apps/electron/src/main/settings/agent-group-store.ts 持久化群组定义——协调者 agent、成员列表、maxRounds(1–5)、maxParallelWorkers(1–5)、sharedMemoryScopes、visibility。设置 UI 在 apps/electron/src/renderer/components/settings/AgentWorkspacePanel.vue。
- 需求只在 Markdown：选择：侧栏 openGroup → selectedGroupId → 作为第 10 个参数传给 chatStream → apps/electron/electron/main-process/ipc.ts 的 ai:chatStream 处理器 → buildGroupDeliberationSection()。
- 需求只在 Markdown：运行时：apps/electron/electron/main-process/ai/group-deliberation.ts（1232 行）的 runGroupDeliberation()。parseGroupRouting() 按 @提及 选模式：coordinator_only / targeted / discussion / coordinator_decides / mentioned_agent_decides。
- 需求只在 Markdown：子 agent 工具：spawn_subagents → apps/electron/src/main/ai-engine/agent/subagent-service.ts 的 SubagentService.runParallel()，各自独立 AgentCore、互不可见、阻塞到全部完成。
- 需求只在 Markdown：所有交互必须经 coordinator。Member A 无法直接对 Member B 说话，没有消息总线，没有 message_agent 工具。唯一的跨 agent 原语 spawn_subagents 是 fire-and-forget 的隔离并行——子 agent 互相看不见、阻塞到全部完成。
- 需求只在 Markdown：用户故事：作为任意成员，我执行任务时发现需要另一个 agent 的专长，应能直接向它发消息并等待回复，而不必回到用户或绕道 coordinator。
- 需求只在 Markdown：新增 message_agent 工具：参数 target_agent_id / message / timeout。
- 需求只在 Markdown：目标 agent 在自身上下文收到请求并产出回复；调用方拿到回复后继续。
- 需求只在 Markdown：支持超时与拒绝；复用 loop-detector.ts 防递归过深。
- 需求只在 Markdown：死锁检测：A 等 B、B 等 A 时主动报错放行。
- 需求只在 pdf：配置层：apps/electron/src/main/settings/agent-group-store.ts持久化群组定义——协调者agent、成员列表、maxRounds(1–5)、maxParallelWorkers(1–5)、sharedMemoryScopes、visibility。设置UI在
- 需求只在 pdf：选择：侧栏openGroup→selectedGroupId→作为第10个参数传给chatStream→apps/electron/electron/main-process/ipc.ts的ai:chatStream处理器→buildGroupDeliberationSection()。
- 需求只在 pdf：运行时：apps/electron/electron/main-process/ai/group- deliberation.ts（1232行）的runGroupDeliberation()。parseGroupRouting()按@提及选模式：coordinator_only/targeted/ discussion/coordinator_decides/mentioned_agent_decides。
- 需求只在 pdf：子agent工具：spawn_subagents→ apps/electron/src/main/ai-engine/agent/subagent-service.ts的SubagentService.runParallel()，各自独立AgentCore、互不可见、阻塞到全部完成。
- 需求只在 pdf：所有交互必须经coordinator。Member A无法直接对Member B说话，没有消息总线，没有message_agent工具。唯一的跨agent原语spawn_subagents是fire-and-forget的隔离并行——子agent互相看不见、阻塞到全部完成。
- 需求只在 pdf：用户故事：作为任意成员，我执行任务时发现需要另一个agent的专长，应能直接向它发消息并等待回复，而不必回到用户或绕道coordinator。
- 需求只在 pdf：验收标准：o新增message_agent工具：参数target_agent_id/message/ timeout。o目标agent在自身上下文收到请求并产出回复；调用方拿到回复后继续。o支持超时与拒绝；复用loop-detector.ts防递归过深。o死锁检测：A等B、B等A时主动报错放行。o UI复用agent_sidechat block呈现这次双向会话。
- 需求只在 pdf：技术要点：引入per-group-session的GroupMessageBus（in-memory）；目标agent用chatStream起一个sub-run；递归深度上限默认2层。
- 需求只在 pdf：验收标准：o激活已有的SharedBoard类型；新增read_board/update_board工具（字段级结构化写入）。o board状态作为system prompt section注入每个成员（diff注入，避免膨胀）。o并发写采用字段级合并+审计日志（谁、何时、改了哪格）。o UI：扩展group_progress或新增block呈现板子快照。
- 需求只在 pdf：技术要点：board存于GroupSession状态；仅注入「自上次读取后的diff」；保留全量审计log供转写回看。

### Rockomate__nextjs_blog

段落标题不一致，需求条目 17 / 39 一致（pdf 拆出 20 条）

- 标题只在 Markdown：奖学金管理系统需求文档
- 标题只在 Markdown：1. 引言
- 标题只在 Markdown：1.1 目的
- 标题只在 Markdown：1.2 背景
- 标题只在 Markdown：1.3 定义
- 标题只在 pdf：（无标题）
- 标题只在 pdf：1.引言
- 标题只在 pdf：1.1目的
- 标题只在 pdf：1.2背景
- 标题只在 pdf：1.3定义
- 需求只在 Markdown：本文档旨在详细描述奖学金管理系统的功能需求，以便开发团队能够设计和实现一个高效、可靠的奖学金管理平台。
- 需求只在 Markdown：学生信息管理：管理学生的个人信息和申请历史，预计管理的数据量为5000条学生记录。
- 需求只在 Markdown：奖学金信息管理：维护奖学金的各类信息，包括名称、金额、申请条件等，预计管理20种奖学金的信息。
- 需求只在 Markdown：申请提交与审批：支持学生在线提交奖学金申请，管理员进行审批，预计每年审批申请数量为3000件。
- 需求只在 Markdown：报表生成与数据分析：生成统计报表，分析申请和发放情况，预计每月生成报表10份。
- 需求只在 Markdown：学生端界面：用于提交申请、查看申请状态及历史记录，界面友好，易于操作。
- 需求只在 Markdown：管理员端界面：用于管理奖学金信息、审批申请和发放奖学金，具备数据统计和报表生成功能。
- 需求只在 Markdown：系统将采用B/S架构，通过Web浏览器访问，支持主流浏览器（Chrome, Firefox, Edge）。
- 需求只在 Markdown：系统应能够验证学生身份，确保信息的安全性。
- 需求只在 Markdown：名称：如"国家奖学金"
- 需求只在 pdf：学生信息管理：管理学生的个人信息和申请历史，预计管理的数据量为5000条学
- 需求只在 pdf：系统将采用B/S架构，通过Web浏览器访问，支持主流浏览器（Chrome,Firefox, Edge）。
- 需求只在 pdf：系统应提供奖学金申请和发放的统计报表，支持数据导出（如Excel格式），预计

### SXP-Simon__astrbot_plugin_qq_group_daily_analysis

段落标题不一致，需求条目 123 / 228 一致（pdf 拆出 227 条）

- 标题只在 Markdown：群聊记忆模块 PRD（初版）
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：1.1 关联文档
- 标题只在 Markdown：1.2 本文档目的
- 标题只在 Markdown：2. 项目背景
- 标题只在 pdf：群聊记忆模块PRD（初版）
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：1.1关联文档
- 标题只在 pdf：1.2本文档目的
- 标题只在 pdf：2.项目背景
- 需求只在 Markdown：文档类型：项目 PRD / 执行计划总纲
- 需求只在 Markdown：当前状态：立项完成，进入 Phase 1 设计冻结与落地准备阶段
- 需求只在 Markdown：Phase 1 技术提案：docs/group_memory_phase1_proposal.md
- 需求只在 Markdown：产品 / 方案负责人：确定目标边界、阶段优先级与质量标准
- 需求只在 Markdown：群管理员 / 高级用户：在灰度期间提供真实反馈
- 需求只在 Markdown：AstrBot 宿主生态：提供 KV、cron、UMO、persona、message history 等底层能力边界
- 需求只在 Markdown：完成收敛后的 Phase 1 提案，明确首期范围与技术路线
- 需求只在 Markdown：完成项目级 PRD，统一目标、里程碑、成功指标和执行策略
- 需求只在 Markdown：AstrBot 已提供插件级 KV、plugin_data、UMO、persona、cron 等核心能力
- 需求只在 Markdown：首期适合采用"群级作用域 + 轻量画像 + episode 记忆 + 最终总结增强"的方案
- 需求只在 pdf：文档类型：项目PRD /执行计划总纲
- 需求只在 pdf：当前状态：立项完成，进入Phase 1设计冻结与落地准备阶段
- 需求只在 pdf：Phase 1技术提案：docs/group_memory_phase1_proposal.md
- 需求只在 pdf：产品/方案负责人：确定目标边界、阶段优先级与质量标准
- 需求只在 pdf：群管理员/高级用户：在灰度期间提供真实反馈
- 需求只在 pdf：AstrBot宿主生态：提供KV、cron、UMO、persona、message history等底层能力
- 需求只在 pdf：完成收敛后的Phase 1提案，明确首期范围与技术路线
- 需求只在 pdf：完成项目级PRD，统一目标、里程碑、成功指标和执行策略
- 需求只在 pdf：AstrBot已提供插件级KV、plugin_data、UMO、persona、cron等核心能力
- 需求只在 pdf：首期适合采用"群级作用域+轻量画像+ episode记忆+最终总结增强"的方案

### SteveTom17__hotpulse

段落标题不一致，需求条目 34 / 62 一致（pdf 拆出 62 条）

- 标题只在 Markdown：1. 产品定义
- 标题只在 Markdown：1.1 当前实现状态（0.1.0）
- 标题只在 Markdown：2. 实现思路与范围
- 标题只在 Markdown：2.1 首版技术切分
- 标题只在 Markdown：2.1.1 技术栈决定
- 标题只在 pdf：1.产品定义
- 标题只在 pdf：1.1当前实现状态（0.1.0）
- 标题只在 pdf：2.实现思路与范围
- 标题只在 pdf：2.1首版技术切分
- 标题只在 pdf：2.1.1技术栈决定
- 需求只在 Markdown：数据连接器层：授权 HTTP API 连接器（凭据加密保存、指数退避、限流暂停、审计留痕）与客户 CSV 导入（显著标注"客户导入"）；24 小时窗口语义去重、跨源归并并保留全部原始链接（FR-02/FR-03）；Cron 每 30 分钟定时同步。
- 需求只在 Markdown：正式模型网关：DeepSeek（OpenAI 兼容）接入、结构化提示词、输出安全校验、[待确认] 占位符提取、额度扣减；未配置密钥时自动降级为显著标注的演示引擎（FR-05）。
- 需求只在 Markdown：内容包：生成、编辑、恢复历史版本、版本哈希；三确认人工审批（来源/事实/AI 标识）；合规导出包 manifest 含来源清单、事实清单、AI 标识与版本历史（FR-05/FR-07）。
- 需求只在 Markdown：计费试点：免费试用 30 天/30 额度，管理员人工开通专业版（¥399/月/工作区，150 额度/月），用量明细与已支付发票留痕；额度耗尽拒绝生成并提示升级。
- 需求只在 Markdown：法律与隐私：用户协议/隐私政策同意留痕（版本可追溯）、申诉/投诉/数据请求工单、账户数据删除（删除后审计留痕依法保留）。
- 需求只在 Markdown：当前所有演示热点、来源和品牌事实必须显著标注为模拟数据，不得直接对外发布；正式模型接入前必须先完成来源、内容安全、数据处理与标识评估（见 README 上线前清单）。
- 需求只在 Markdown：趋势处理层：定时任务拉取、统一字段、语义去重、计算 24 小时增速与跨源信号；保存原始来源链接和采集时间。
- 需求只在 Markdown：决策层：规则优先的风险分类 + LLM 辅助的行业相关性摘要；评分可解释、可人工覆盖。
- 需求只在 Markdown：审核与导出层：编辑器、必填事实确认、风险确认、AI 标识检查、导出包和不可篡改审计日志。
- 需求只在 Markdown：应用：TypeScript + React 19 + Vinext，兼顾产品界面、服务端接口和 Cloudflare Worker 运行环境。
- 需求只在 pdf：数据连接器层：授权HTTP API连接器（凭据加密保存、指数退避、限流暂停、审计留痕）与客户CSV导入（显著标注"客户导入"）；24小时窗口语义去重、跨源归并并保留全部原始链接（FR-02/FR-03）；Cron每30分钟定时同步。
- 需求只在 pdf：正式模型网关：DeepSeek（OpenAI兼容）接入、结构化提示词、输出安全校验、[待确认]占位符提取、额度扣减；未配置密钥时自动降级为显著标注的演示引擎（FR-05）。
- 需求只在 pdf：内容包：生成、编辑、恢复历史版本、版本哈希；三确认人工审批（来源/事实/AI标识）；合规导出包manifest含来源清单、事实清单、AI标识与版本历史（FR-05/FR-07）。
- 需求只在 pdf：计费试点：免费试用30天/30额度，管理员人工开通专业版（¥399/月/工作区，150额度/月），用量明细与已支付发票留痕；额度耗尽拒绝生成并提示升级。
- 需求只在 pdf：法律与隐私：用户协议/隐私政策同意留痕（版本可追溯）、申诉/投诉/数据请求工单、账户数据删除（删除后审计留痕依法保留）。尚未宣称完成：平台官方实时热搜接入、真实支付网关、自动发布、效果回收报表、企业级SSO与精细保留策略。
- 需求只在 pdf：当前所有演示热点、来源和品牌事实必须显著标注为模拟数据，不得直接对外发布；正式模型接入前必须先完成来源、内容安全、数据处理与标识评估（见README上线前清单）。
- 需求只在 pdf：趋势处理层：定时任务拉取、统一字段、语义去重、计算24小时增速与跨源信号；保存原始来源链接和采集时间。
- 需求只在 pdf：决策层：规则优先的风险分类+ LLM辅助的行业相关性摘要；评分可解释、可人工覆盖。
- 需求只在 pdf：审核与导出层：编辑器、必填事实确认、风险确认、AI标识检查、导出包和不可篡改审计日志。
- 需求只在 pdf：应用：TypeScript+ React 19 +Vinext，兼顾产品界面、服务端接口和Cloudflare Worker运行环境。

### StoneLL1__llm-wiki-desktop

段落标题不一致，需求条目 57 / 202 一致（pdf 拆出 174 条）

- 标题只在 Markdown：LLM Wiki Desktop — 产品需求文档（PRD）
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 产品概述
- 标题只在 Markdown：3. 背景与问题
- 标题只在 Markdown：3.1 用户现状
- 标题只在 pdf：LLM Wiki Desktop —产品需求文档（PRD）
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.产品概述
- 标题只在 pdf：3.背景与问题
- 标题只在 pdf：3.1用户现状
- 需求只在 Markdown：导入、来源库、本地与远程媒体、OCR、ASR、平台登录态和 AI 整理的已确认产品决策，以 ../docs/superpowers/specs/2026-07-24-import-source-media-flow-design.md 为唯一可信源。本文中的概览不得被解释为"确认导入后自动编译"。
- 需求只在 Markdown：无项目工作台、新建知识库、打开原生或兼容知识库、目录评估、信任 / 受限 / 只读、兼容启用、修复与进入 Import 的已确认产品决策，以 ../docs/superpowers/specs/2026-07-30-first-run-project-open-workbench-design.md 为唯一可信源。本文中的摘要不得被解释为允许把普通资料文件夹原地初始化成项目。
- 需求只在 Markdown：资料散落在 PDF、网页、公众号文章、PPT、Word、Excel、Markdown 和本地文件夹中。
- 需求只在 Markdown：RAG 工具能问答，但不擅长把知识沉淀成稳定、可编辑、可复用的页面。
- 需求只在 Markdown：AI Agent 能整理资料，但命令行门槛高，普通用户不容易获得稳定、可恢复、可视化的工作流。
- 需求只在 Markdown：用户需要一个本地桌面应用，把"资料导入、知识整理、图谱探索、问答溯源、HTML 输出、版本恢复"整合成一个可靠闭环。
- 需求只在 Markdown：以 Markdown 文件夹作为长期资产，避免锁定在单一应用。
- 需求只在 Markdown：用 Agent/LLM 自动完成重复整理工作，降低个人知识库维护成本。
- 需求只在 Markdown：先用已确认、可阅读的 Source 兑现首次价值，再用知识图谱提供后续的结构化惊喜。
- 需求只在 Markdown：用 Git 自动检查点保护用户资料和 AI 修改结果。
- 需求只在 pdf：资料散落在PDF、网页、公众号文章、PPT、Word、Excel、Markdown和本地文件夹中。
- 需求只在 pdf：RAG工具能问答，但不擅长把知识沉淀成稳定、可编辑、可复用的页面。
- 需求只在 pdf：AI Agent能整理资料，但命令行门槛高，普通用户不容易获得稳定、可恢复、可视化的工作流。
- 需求只在 pdf：用户需要一个本地桌面应用，把"资料导入、知识整理、图谱探索、问答溯源、HTML输出、版本恢复"整合成一个可靠闭环。
- 需求只在 pdf：以Markdown文件夹作为长期资产，避免锁定在单一应用。
- 需求只在 pdf：用Agent/LLM自动完成重复整理工作，降低个人知识库维护成本。
- 需求只在 pdf：先用已确认、可阅读的Source兑现首次价值，再用知识图谱提供后续的结构化惊喜。
- 需求只在 pdf：用Git自动检查点保护用户资料和AI修改结果。
- 需求只在 pdf：用Skill系统承接未来扩展，而不是把所有能力硬编码在应用中。
- 需求只在 pdf：文件透明：Wiki页面是普通Markdown，可被Obsidian、Git和外部编辑器访问。

### T-THA__AITravelPlanner

段落标题不一致，需求条目 69 / 200 一致（pdf 拆出 130 条）

- 标题只在 Markdown：AI 旅行规划师 - 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 核心价值
- 标题只在 pdf：AI旅行规划师-产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：1.3核心价值
- 需求只在 Markdown：通过 AI 大幅降低旅行规划的时间成本
- 需求只在 Markdown：用户可以成功注册账号
- 需求只在 Markdown：用户可以使用邮箱/手机号登录
- 需求只在 Markdown：密码加密存储
- 需求只在 Markdown：登录状态持久化（7天免登录）
- 需求只在 Markdown：支持密码找回流程
- 需求只在 Markdown：使用 Supabase Authentication 或 Firebase Auth
- 需求只在 Markdown：JWT Token 管理用户会话
- 需求只在 Markdown：密码使用 bcrypt 加密
- 需求只在 Markdown：用户可以修改个人信息
- 需求只在 pdf：通过AI大幅降低旅行规划的时间成本
- 需求只在 pdf：1.1注册/登录功能
- 需求只在 pdf：☐用户可以成功注册账号☐用户可以使用邮箱/手机号登录☐密码加密存储☐登录状态持久化（7天免登录）☐支持密码找回流程
- 需求只在 pdf：使用Supabase Authentication或Firebase Auth
- 需求只在 pdf：JWT Token管理用户会话
- 需求只在 pdf：密码使用bcrypt加密
- 需求只在 pdf：1.2用户信息管理
- 需求只在 pdf：☐用户可以修改个人信息☐偏好设置可保存并应用到后续规划☐修改操作有确认提示
- 需求只在 pdf：2.1语音输入功能
- 需求只在 pdf：☐用户可以点击按钮开始/结束录音☐语音实时转为文字显示☐识别准确率> 85% ☐支持噪音环境下的识别☐识别失败有友好提示

### TY-teo__ChargeWatching

段落标题不一致，需求条目 3 / 67 一致（pdf 拆出 33 条）

- 标题只在 Markdown：ChargeWatch — 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：2. 核心价值主张
- 标题只在 Markdown：3. 功能范围（MVP）
- 标题只在 Markdown：3.1 必做（P0）
- 标题只在 pdf：ChargeWatch —产品需求文档(PRD)
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：2.核心价值主张
- 标题只在 pdf：3.功能范围（MVP）
- 标题只在 pdf：3.1必做（P0）
- 需求只在 Markdown：目标用户：自己（chenran）— 关心 Mac 实际从充电器拉了多少瓦、电池是不是真的在充电、不同场景下的功耗模式
- 需求只在 Markdown：换新充电器/线材时验证 PD 协商是否到位（说好 100W，实际只拿到 60W？）
- 需求只在 Markdown：高负载工作时判断电是不是入不敷出（系统功耗 > 适配器输入 = 电池在帮忙供电）
- 需求只在 Markdown：长期回看「今天充了多少电、什么时段在充」
- 需求只在 Markdown：出差时排查酒店墙插充电速度
- 需求只在 Markdown：菜单栏实时显示
- 需求只在 Markdown：充电中：图标（SF Symbol bolt.fill）+ 数字瓦数，如 ⚡ 67W（图标是 SF Symbols，不是 emoji）
- 需求只在 Markdown：未充电但接电：图标（bolt.slash）+ AC
- 需求只在 Markdown：纯电池放电：图标（battery.50percent）+ 当前 SoC%
- 需求只在 Markdown：无电池（桌面 Mac）：图标（powerplug）+ 系统功耗
- 需求只在 pdf：目标用户：自己（chenran）—关心Mac实际从充电器拉了多少瓦、电池是不是真的在充电、不同场景下的功耗模式
- 需求只在 pdf：使用场景：o换新充电器/线材时验证PD协商是否到位（说好100W，实际只拿到60W？）o高负载工作时判断电是不是入不敷出（系统功耗>适配器输入=电池在帮忙供电）o长期回看「今天充了多少电、什么时段在充」o出差时排查酒店墙插充电速度
- 需求只在 pdf：菜单栏实时显示o充电中：图标（SF Symbol bolt.fill）+数字瓦数，如⚡67W（图标是SF Symbols，不是emoji）o未充电但接电：图标（bolt.slash）+AC o纯电池放电：图标（battery.50percent）+当前SoC% o无电池（桌面Mac）：图标（powerplug）+系统功耗
- 需求只在 pdf：下拉详情面板（点击菜单栏图标弹出）o当前状态横幅：充电中/ AC未充/放电中o关键数字（4项）：充入电池功率、适配器实际输入、系统总功耗、电池SoC o适配器信息：额定瓦数+协商电压电流（如100W PD, 20V/5A max）o充电曲线：最近1小时sparkline，hover显示具体数值o操作入口：「查看完整历史」「导出CSV」「设置」「退出」
- 需求只在 pdf：数据采集与持久化o 1Hz采样写入SQLite o自动降采样（24h/7d/30d三档）o跨进程重启不丢数据
- 需求只在 pdf：历史窗口o时间范围切换：今天/本周/本月/自定义o折线图：功率vs时间，可叠加SoC副坐标o统计卡片：累计充入(Wh)、平均充电功率、峰值功率、充电时长
- 需求只在 pdf：CSV导出：选定时间范围导出全量字段
- 需求只在 pdf：开机自启：通过SMAppService注册
- 需求只在 pdf：深色/浅色模式适配
- 需求只在 pdf：充电完成通知（可关）：电量到100%触发系统通知

### Thearetically-speaking__All-you-can-seal

段落标题不一致，需求条目 9 / 53 一致（pdf 拆出 48 条）

- 标题只在 Markdown：PRD — All You Can Seal Web（网页版热封 G-code 处理器）
- 标题只在 Markdown：1. 背景与目标
- 标题只在 Markdown：2. 用户与使用场景
- 标题只在 Markdown：3. 功能需求
- 标题只在 Markdown：FR-1 文件导入（拖拽 + 点击选择）
- 标题只在 pdf：PRD — All You Can Seal Web（网页版热封G-code处理器）
- 标题只在 pdf：1.背景与目标
- 标题只在 pdf：2.用户与使用场景
- 标题只在 pdf：3.功能需求
- 标题只在 pdf：FR-1文件导入（拖拽+点击选择）
- 需求只在 Markdown：支持拖拽（drag & drop）和点击文件选择两种方式；接受 .gcode.3mf 和裸 .gcode。
- 需求只在 Markdown：导入后立即在浏览器内解包（3mf 即 zip），文件不上传到任何服务器，页面上明确标注这一点（隐私是卖点）。
- 需求只在 Markdown：解析失败（非 zip、找不到 gcode、非 Bambu 结构）给出具体、可操作的错误提示（如"该文件缺少 CONFIG_BLOCK_END 标记，请确认使用 Bambu Studio 切片并选择 Bambu 打印机档位"）。
- 需求只在 Markdown：显示文件基本信息：文件名、机型（从 ;===== machine: 头解析）、盘数、每盘的层数与预计路径长度、切片时的喷嘴温度。
- 需求只在 Markdown：枚举 3mf 内所有 Metadata/plate_N.gcode（不再写死 plate_1）。
- 需求只在 Markdown：选择其中一盘或多盘进行改写（未选中的盘原样保留）；
- 需求只在 Markdown：导出时对每个被改写的盘同步更新其对应的 plate_N.gcode.md5。
- 需求只在 Markdown：每个参数带滑块 + 数字输入双控件，附一句"这个参数干什么用"的说明和调参方向提示（沿用 README 的 troubleshooting 经验，如"封不牢→温度 +5°C 或 Z 再压低"）。
- 需求只在 Markdown：超出允许范围直接阻止输入；接近危险边界（如 Z < −0.20）时显示黄色警告但允许继续。
- 需求只在 Markdown：参数记忆：用 localStorage 记住用户上次的参数（可选、可清除）。
- 需求只在 pdf：支持拖拽（drag&drop）和点击文件选择两种方式；接受.gcode.3mf和裸.gcode。
- 需求只在 pdf：导入后立即在浏览器内解包（3mf即zip），文件不上传到任何服务器，页面上明确标注这一点（隐私是卖点）。
- 需求只在 pdf：解析失败（非zip、找不到gcode、非Bambu结构）给出具体、可操作的错误提示（如"该文件缺少CONFIG_BLOCK_END标记，请确认使用Bambu Studio切片并选择Bambu打印机档位"）。
- 需求只在 pdf：显示文件基本信息：文件名、机型（从;=====machine:头解析）、盘数、每盘的层数与预计路径长度、切片时的喷嘴温度。
- 需求只在 pdf：枚举3mf内所有Metadata/plate_N.gcode（不再写死plate_1）。
- 需求只在 pdf：多盘文件：显示盘列表（含3mf自带的plate_N.png缩略图），用户可：o选择其中一盘或多盘进行改写（未选中的盘原样保留）；o或"全部改写"。
- 需求只在 pdf：导出时对每个被改写的盘同步更新其对应的plate_N.gcode.md5。
- 需求只在 pdf：允许范围（硬限参数默认值制）说明260°C喷嘴温度180–300°C（按热封温度机型上限进一步收紧）−0.15 mm−0.30 – +0.10 Z偏移负值=压入膜面mm 120%50–200%流量倍率注入M221 5 mm/s 1–30 mm/s移动速度主体所有独立G1 F行
- 需求只在 pdf：每个参数带滑块+数字输入双控件，附一句"这个参数干什么用"的说明和调参方向提示（沿用README的troubleshooting经验，如"封不牢→温度+5°C或Z再压低"）。
- 需求只在 pdf：超出允许范围直接阻止输入；接近危险边界（如Z <−0.20）时显示黄色警告但允许继续。

### WrBug__PolyHermes

段落标题不一致，需求条目 38 / 108 一致（pdf 拆出 106 条）

- 标题只在 Markdown：跟单回测功能产品需求文档 (PRD)
- 标题只在 Markdown：3.1 回测管理页面
- 标题只在 Markdown：3.1.1 页面布局
- 标题只在 Markdown：3.1.2 列表功能
- 标题只在 Markdown：3.1.3 列表操作
- 标题只在 pdf：跟单回测功能产品需求文档(PRD)
- 标题只在 pdf：3.1回测管理页面
- 标题只在 pdf：3.2新增回测任务
- 标题只在 pdf：3.3回测详情页面
- 标题只在 pdf：4.1回测执行规则
- 需求只在 Markdown：页面位置: 在跟单管理模块下新增"回测管理"菜单项
- 需求只在 Markdown：页面标题: "回测管理" / "Backtest Management"
- 需求只在 Markdown：Leader 筛选下拉框,支持按 Leader 过滤回测记录
- 需求只在 Markdown：状态筛选: 全部 / 运行中 / 已完成 / 已停止
- 需求只在 Markdown：按收益额排序 (升序/降序)
- 需求只在 Markdown：按收益率排序 (升序/降序)
- 需求只在 Markdown：按创建时间排序 (默认降序)
- 需求只在 Markdown：回测配置参数
- 需求只在 Markdown：详细交易记录
- 需求只在 Markdown：资金变化曲线图
- 需求只在 pdf：页面位置:在跟单管理模块下新增"回测管理"菜单项
- 需求只在 pdf：页面标题:"回测管理"/ "Backtest Management"
- 需求只在 pdf：Leader筛选下拉框,支持按Leader过滤回测记录
- 需求只在 pdf：状态筛选:全部/运行中/已完成/已停止
- 需求只在 pdf：按收益额排序(升序/降序)
- 需求只在 pdf：按收益率排序(升序/降序)
- 需求只在 pdf：按创建时间排序(默认降序)
- 需求只在 pdf：查看详情:点击后展开详细信息,包括: o回测配置参数o详细交易记录o资金变化曲线图o收益统计
- 需求只在 pdf：删除:删除回测记录(确认后不可恢复)
- 需求只在 pdf：回测名称(必填):用户自定义名称,方便识别

### Xiangyu-Lou__BlueDrop

段落标题不一致，需求条目 0 / 25 一致（pdf 拆出 15 条）

- 标题只在 Markdown：聚音 (BlueDrop) - 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：2. 目标用户与使用场景
- 标题只在 Markdown：3. 运行环境与前置条件
- 标题只在 Markdown：3.1 系统要求
- 标题只在 pdf：聚音(BlueDrop) -产品需求文档(PRD)
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：2.目标用户与使用场景
- 标题只在 pdf：3.运行环境与前置条件
- 标题只在 pdf：3.1系统要求
- 需求只在 Markdown：项目：蓝牙；要求：支持 Bluetooth 4.0+ 的蓝牙适配器（内置或外置均可）
- 需求只在 Markdown：项目：发送端；要求：iPhone (iOS 13+)，原生支持 A2DP
- 需求只在 Markdown：OS 版本校验 — 低于 Win10 Build 19041 → 提示升级系统
- 需求只在 Markdown：蓝牙适配器校验 — 未检测到蓝牙硬件 → 提示插入蓝牙适配器
- 需求只在 Markdown：虚拟声卡校验 — 未检测到 VB-Cable 设备 → 提示安装并提供下载链接
- 需求只在 Markdown：属性：编解码；描述：SBC（必须），AAC（可选，优先）
- 需求只在 Markdown：物理麦克风 — 列出所有音频输入设备，默认选择系统默认录音设备
- 需求只在 Markdown：本地监听耳机 — 列出所有音频输出设备，默认选择系统默认播放设备
- 需求只在 Markdown：虚拟麦克风输出 — 列出所有音频输入设备中的虚拟设备，自动高亮 CABLE Input
- 需求只在 Markdown：手机音频：水平音量推子 + 数值显示 + 静音按钮
- 需求只在 pdf：及以上，或Windows 11架构仅x64蓝牙支持Bluetooth 4.0+的蓝牙适配器（内置或外置均可）发送端iPhone (iOS 13+)，原生支持A2DP项目要求
- 需求只在 pdf：OS版本校验—低于Win10 Build 19041 →提示升级系统
- 需求只在 pdf：蓝牙适配器校验—未检测到蓝牙硬件→提示插入蓝牙适配器
- 需求只在 pdf：虚拟声卡校验—未检测到VB-Cable设备→提示安装并提供下载链接
- 需求只在 pdf：属性描述功能使PC作为A2DP Sink暴露给iPhone，接受配对并接收立体声媒体音频采样率44.1kHz /48kHz（自适应）声道立体声(Stereo)编解码SBC（必须），AAC（可选，优先）状态管理未连接→等待配对→已连接（显示设备名称）→断开参考实现AudioPlaybackConnector（Win10 2004+ A2DP Sink）
- 需求只在 pdf：物理麦克风—列出所有音频输入设备，默认选择系统默认录音设备
- 需求只在 pdf：本地监听耳机—列出所有音频输出设备，默认选择系统默认播放设备
- 需求只在 pdf：虚拟麦克风输出—列出所有音频输入设备中的虚拟设备，自动高亮CABLE Input
- 需求只在 pdf：手机音频：水平音量推子+数值显示+静音按钮
- 需求只在 pdf：麦克风：水平音量推子+数值显示+静音按钮

### Yotoha0303__KnowTrace-Workflow

段落标题不一致，需求条目 41 / 136 一致（pdf 拆出 135 条）

- 标题只在 Markdown：1. 术语
- 标题只在 Markdown：2. 内容类型
- 标题只在 Markdown：3. 用户故事
- 标题只在 Markdown：US-01 快速保存
- 标题只在 Markdown：US-02 手动分类
- 标题只在 pdf：1.术语
- 标题只在 pdf：2.内容类型
- 标题只在 pdf：3.用户故事
- 标题只在 pdf：US-01快速保存
- 标题只在 pdf：US-02手动分类
- 需求只在 Markdown：标题、Content Type 和 Category 都可以为空。
- 需求只在 Markdown：AI 调用不出现在保存事务中。
- 需求只在 Markdown：一条 Capture 最多一个 Content Type。
- 需求只在 Markdown：一条 Capture 可以关联零个或多个 Category。
- 需求只在 Markdown：重复关联同一 Category 保持幂等。
- 需求只在 Markdown：已归档 Category 不能新增关联，但原有关系保留。
- 需求只在 Markdown：修改分类不创建正文 Revision，但需要更新时间。
- 需求只在 Markdown：Category 名称必填并进行规范化后唯一判断。
- 需求只在 Markdown：没有关联任何 Capture 的 Category 可以在二次确认后永久删除；有关联记录时必须拒绝，记录是否归档不影响该限制。
- 需求只在 Markdown：MVP 不做无限层级目录；Category 为扁平结构。
- 需求只在 pdf：标题、Content Type和Category都可以为空。
- 需求只在 pdf：AI调用不出现在保存事务中。
- 需求只在 pdf：一条Capture最多一个Content Type。
- 需求只在 pdf：一条Capture可以关联零个或多个Category。
- 需求只在 pdf：重复关联同一Category保持幂等。
- 需求只在 pdf：已归档Category不能新增关联，但原有关系保留。
- 需求只在 pdf：修改分类不创建正文Revision，但需要更新时间。
- 需求只在 pdf：Category名称必填并进行规范化后唯一判断。
- 需求只在 pdf：没有关联任何Capture的Category可以在二次确认后永久删除；有关联记录时必须拒绝，记录是否归档不影响该限制。
- 需求只在 pdf：MVP不做无限层级目录；Category为扁平结构。

### ZJM189__Daily_News

段落标题不一致，需求条目 127 / 183 一致（pdf 拆出 183 条）

- 标题只在 Markdown：AI 热点信息每日汇总系统 PRD
- 标题只在 Markdown：2026-09-14 增量：首页日期筛选
- 标题只在 Markdown：2026-09-08 增量：自然语言信息库聊天助手
- 标题只在 Markdown：2026-09-09 增量：公开今日简报
- 标题只在 Markdown：2026-09-06 增量：我的收藏
- 标题只在 pdf：AI热点信息每日汇总系统PRD
- 标题只在 pdf：2026-09-14增量：首页日期筛选
- 标题只在 pdf：2026-09-08增量：自然语言信息库聊天助手
- 标题只在 pdf：2026-09-09增量：公开今日简报
- 标题只在 pdf：2026-09-06增量：我的收藏
- 需求只在 Markdown：公开首页的简报日期升级为可交互的日历筛选控件。用户默认查看北京时间当天已发布的 AI 简报，选择过去日期后，首页加载该日期已发布的简报；未来日期不可选择。所选日期没有已发布简报时展示明确空状态。日期文本需要比原有日期标签更醒目。/history 页面仍保持登录保护。
- 需求只在 Markdown：网页端新增全局悬浮聊天入口，用户可用自然语言描述要查的内容，系统先通过 LibraryChatIntentClassifier 判断是否属于信息库查询，范围外问题返回固定拒答；范围内问题通过管理员配置的默认启用 LLM Provider + DeepAgents 理解意图，并调用 search_library_database 只读工具查询已采集入库内容。首期定位为"LLM 驱动的站内信息库聊天查询"，支持 SSE 流式状态、回答文本、结果卡片和用户级聊天历史落库；不触发外部实时检索、不新增普通用户采集权限、不做通用聊天机器人。详见 自然语言信息库检索需求。
- 需求只在 Markdown：产品首期不做推送渠道，不开放公开注册，不允许普通用户添加外部 URL 信息源。普通用户通过"我的关注"配置个性化规则，影响自己的看板排序和默认筛选。
- 需求只在 Markdown：帮助用户快速了解当天 AI 热点。
- 需求只在 Markdown：把分散来源统一到一个可检索 Web 看板。
- 需求只在 Markdown：通过管理员后台保障来源、任务、用户和 LLM 配置可维护。
- 需求只在 Markdown：查看今日 AI 简报。
- 需求只在 Markdown：添加外部 URL 信息源。
- 需求只在 Markdown：侧边栏按 shadcn/ui Sidebar 风格组织为 Header、分组导航和 Footer。
- 需求只在 Markdown：主内容区统一使用 PageHeader 承载页面标题、说明和页面级操作。
- 需求只在 pdf：公开首页的简报日期升级为可交互的日历筛选控件。用户默认查看北京时间当天已发布的AI简报，选择过去日期后，首页加载该日期已发布的简报；未来日期不可选择。所选日期没有已发布简报时展示明确空状态。日期文本需要比原有日期标签更醒目。/history页面仍保持登录保护。
- 需求只在 pdf：网页端新增全局悬浮聊天入口，用户可用自然语言描述要查的内容，系统先通过LibraryChatIntentClassifier判断是否属于信息库查询，范围外问题返回固定拒答；范围内问题通过管理员配置的默认启用LLM Provider + DeepAgents理解意图，并调用search_library_database只读工具查询已采集入库内容。首期定位为"LLM驱动的站内信息库聊天查询"，支持SSE流式状态、回答文本、结果卡片和用户级聊天历史落库；不触发外部实时检索、不新增普通用户采集权限、不做通用聊天机器人。详见自然语言信息库检索需求。
- 需求只在 pdf：产品首期不做推送渠道，不开放公开注册，不允许普通用户添加外部URL信息源。普通用户通过"我的关注"配置个性化规则，影响自己的看板排序和默认筛选。
- 需求只在 pdf：帮助用户快速了解当天AI热点。
- 需求只在 pdf：把分散来源统一到一个可检索Web看板。
- 需求只在 pdf：通过管理员后台保障来源、任务、用户和LLM配置可维护。
- 需求只在 pdf：查看今日AI简报。
- 需求只在 pdf：添加外部URL信息源。
- 需求只在 pdf：侧边栏按shadcn/ui Sidebar风格组织为Header、分组导航和Footer。
- 需求只在 pdf：主内容区统一使用PageHeader承载页面标题、说明和页面级操作。

### ZedeX__agentforge

段落标题不一致，需求条目 79 / 181 一致（pdf 拆出 152 条）

- 标题只在 Markdown：Agent 智能体平台系统 需求说明书
- 标题只在 Markdown：1. 基础资源层
- 标题只在 Markdown：2. 核心引擎层
- 标题只在 Markdown：3. 能力服务层
- 标题只在 Markdown：4. 接入交互层
- 标题只在 pdf：Agent智能体平台系统需求说明书
- 标题只在 pdf：（五）Agent运行时引擎
- 需求只在 Markdown：管控与执行分离：平台层负责调度、管控、校验，Agent 运行时仅负责单任务执行
- 需求只在 Markdown：算力资源池：容器化弹性算力，支持 Serverless 模式 Agent 实例按需拉起销毁，实现资源隔离与按量计费
- 需求只在 Markdown：模型服务网关：统一接入国内外主流大模型与私有化开源模型，标准化调用协议；具备智能路由、计量统计、密钥配额管理、Prompt 缓存能力
- 需求只在 Markdown：任务编排与调度引擎：任务状态机管理、DAG 解析与分发、依赖关系校验、异常处理、多 Agent 协同模式调度
- 需求只在 Markdown：智能规划引擎：任务复杂度识别、子任务拆解、DAG 生成、动态重规划、规划策略沉淀优化
- 需求只在 Markdown：Agent 运行时引擎：Agent 实例生命周期管理、上下文注入、ReAct/Reflexion 推理循环驱动、Token 水位管控、执行状态同步
- 需求只在 Markdown：Agent 仓库：Agent 全生命周期管理、能力标签体系、效果动态评分、低代码配置台
- 需求只在 Markdown：质量评估服务：自动质量校验、效果评测、Badcase 归集、效果数据回流优化
- 需求只在 Markdown：前端交互控制台：运营后台、Agent 配置工作台、调试沙箱、终端对话界面
- 需求只在 Markdown：意图理解与任务形式化：语义解析与实体抽取、按复杂度路由分发、生成结构化 Task Schema
- 需求只在 pdf：管控与执行分离：平台层负责调度、管控、校验，Agent运行时仅负责单任务执行
- 需求只在 pdf：算力资源池：容器化弹性算力，支持Serverless模式Agent实例按需拉起销毁，实现资源隔离与按量计费
- 需求只在 pdf：模型服务网关：统一接入国内外主流大模型与私有化开源模型，标准化调用协议；具备智能路由、计量统计、密钥配额管理、Prompt缓存能力
- 需求只在 pdf：任务编排与调度引擎：任务状态机管理、DAG解析与分发、依赖关系校验、异常处理、多Agent协同模式调度
- 需求只在 pdf：智能规划引擎：任务复杂度识别、子任务拆解、DAG生成、动态重规划、规划策略沉淀优化
- 需求只在 pdf：Agent运行时引擎：Agent实例生命周期管理、上下文注入、ReAct/Reflexion推理循环驱动、Token水位管控、执行状态同步
- 需求只在 pdf：Agent仓库：Agent全生命周期管理、能力标签体系、效果动态评分、低代码配置台
- 需求只在 pdf：质量评估服务：自动质量校验、效果评测、Badcase归集、效果数据回流优化
- 需求只在 pdf：前端交互控制台：运营后台、Agent配置工作台、调试沙箱、终端对话界面
- 需求只在 pdf：意图理解与任务形式化：语义解析与实体抽取、按复杂度路由分发、生成结构化Task Schema

### ZhengWG__quant_free

段落标题不一致，需求条目 62 / 119 一致（pdf 拆出 118 条）

- 标题只在 Markdown：产品设计文档 (PRD)
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：产品设计文档(PRD)
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目名称
- 标题只在 pdf：1.2项目定位
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：功能：VSCode插件，支持查看股票、基金、期货实时数据
- 需求只在 Markdown：特点：实时涨跌显示、走势图、基金排行榜、持仓信息
- 需求只在 Markdown：参考价值：UI设计、数据展示方式、VSCode插件开发模式
- 需求只在 Markdown：功能：策略运行、日志保存、K线图显示
- 需求只在 Markdown：特点：量化交易策略开发环境
- 需求只在 Markdown：参考价值：策略执行框架、K线图可视化
- 需求只在 Markdown：功能：基于深度强化学习的自动化股票交易框架
- 需求只在 Markdown：特点：策略生成、回测、实盘交易
- 需求只在 Markdown：参考价值：AI策略生成技术、交易执行框架
- 需求只在 Markdown：✅ 自选股管理（添加/删除/分组）
- 需求只在 pdf：1.1实时行情监控模块
- 需求只在 pdf：✅自选股管理（添加/删除/分组）
- 需求只在 pdf：✅实时价格刷新（可配置刷新频率）
- 需求只在 pdf：✅涨跌幅颜色标识（红涨绿跌）
- 需求只在 pdf：✅快速查看详情（点击查看K线图）
- 需求只在 pdf：✅价格提醒设置（涨跌到目标价提醒）
- 需求只在 pdf：✅市场指数显示（上证、深证、创业板等）
- 需求只在 pdf：1.2 AI策略推荐模块
- 需求只在 pdf：✅策略生成（基于当前市场数据）
- 需求只在 pdf：✅策略解释（AI说明推荐理由）

### ZooHero500__imgsplit

段落标题不一致，需求条目 0 / 47 一致（pdf 拆出 47 条）

- 标题只在 Markdown：需求 1: 图片上传
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：需求 2: 分割线编辑
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：需求 3: 图片分割与下载
- 标题只在 pdf：需求1:图片上传
- 标题只在 pdf：需求2:分割线编辑
- 标题只在 pdf：需求3:图片分割与下载
- 标题只在 pdf：需求4:落地页
- 标题只在 pdf：需求5:操作台
- 需求只在 Markdown：Objective: 作为用户，我希望能够快速上传图片到画布，以便开始分割操作
- 需求只在 Markdown：When 用户将图片文件拖拽到上传区域, the 分割系统 shall 读取图片并在画布中居中展示
- 需求只在 Markdown：When 用户点击上传区域, the 分割系统 shall 打开文件选择器，仅允许选择图片格式文件（PNG、JPG、JPEG、WebP）
- 需求只在 Markdown：When 用户选择或拖入图片后, the 分割系统 shall 在画布上按等比缩放展示图片，并自动适配画布可视区域
- 需求只在 Markdown：If 用户上传的文件不是支持的图片格式, the 分割系统 shall 显示格式不支持的错误提示
- 需求只在 Markdown：If 用户上传的图片文件大小超过 20MB, the 分割系统 shall 显示文件过大的错误提示，并建议压缩后重试
- 需求只在 Markdown：Objective: 作为用户，我希望能够在画布上自由添加和拖拽分割线，以便精确控制分割位置
- 需求只在 Markdown：When 用户点击添加横向分割线按钮, the 分割系统 shall 在画布中央添加一条水平分割线
- 需求只在 Markdown：When 用户点击添加纵向分割线按钮, the 分割系统 shall 在画布中央添加一条垂直分割线
- 需求只在 Markdown：When 用户拖拽分割线, the 分割系统 shall 实时更新分割线位置，并显示对应的像素坐标
- 需求只在 pdf：Objective:作为用户，我希望能够快速上传图片到画布，以便开始分割操作
- 需求只在 pdf：When用户将图片文件拖拽到上传区域,the分割系统shall读取图片并在画布中居中展示
- 需求只在 pdf：When用户点击上传区域,the分割系统shall打开文件选择器，仅允许选择图片格式文件（PNG、JPG、JPEG、WebP）
- 需求只在 pdf：When用户选择或拖入图片后,the分割系统shall在画布上按等比缩放展示图片，并自动适配画布可视区域
- 需求只在 pdf：If用户上传的文件不是支持的图片格式,the分割系统shall显示格式不支持的错误提示
- 需求只在 pdf：If用户上传的图片文件大小超过20MB, the分割系统shall显示文件过大的错误提示，并建议压缩后重试
- 需求只在 pdf：Objective:作为用户，我希望能够在画布上自由添加和拖拽分割线，以便精确控制分割位置
- 需求只在 pdf：When用户点击添加横向分割线按钮,the分割系统shall在画布中央添加一条水平分割线
- 需求只在 pdf：When用户点击添加纵向分割线按钮,the分割系统shall在画布中央添加一条垂直分割线
- 需求只在 pdf：When用户拖拽分割线,the分割系统shall实时更新分割线位置，并显示对应的像素坐标

### aAAaqwq__KGKB

段落标题不一致，需求条目 13 / 40 一致（pdf 拆出 36 条）

- 标题只在 Markdown：Knowledge Graph KB — 产品需求文档 (PRD)
- 标题只在 Markdown：1. 项目愿景与定位
- 标题只在 Markdown：1.1 一句话定位
- 标题只在 Markdown：1.2 项目愿景
- 标题只在 Markdown：1.3 核心价值主张
- 标题只在 pdf：Knowledge Graph KB —产品需求文档(PRD)
- 标题只在 pdf：1.项目愿景与定位
- 标题只在 pdf：1.1一句话定位
- 标题只在 pdf：1.2项目愿景
- 标题只在 pdf：1.3核心价值主张
- 需求只在 Markdown：维度：CLI支持；Notion/Obsidian：❌；QMD：✅；GitNexus：❌；MiroFish：❌；KGKB (本项目)：✅
- 需求只在 Markdown：支持文本、URL、Markdown三种输入格式
- 需求只在 Markdown：支持标签分类
- 需求只在 Markdown：支持元数据（来源、时间、作者）
- 需求只在 Markdown：使用D3.js或Cytoscape.js渲染图谱
- 需求只在 Markdown：支持节点拖拽和缩放
- 需求只在 Markdown：点击节点显示详情
- 需求只在 Markdown：支持按标签筛选显示
- 需求只在 Markdown：支持手动创建关联
- 需求只在 Markdown：支持定义关联类型（相关、因果、包含等）
- 需求只在 pdf：CLI支持AI Agent❌ ⚠️❌❌✅ OpenClaw集成
- 需求只在 pdf：☐支持文本、URL、Markdown三种输入格式☐支持标签分类☐支持元数据（来源、时间、作者）☐存储到本地SQLite F2:向量化引擎
- 需求只在 pdf：☐支持OpenAI embedding API ☐支持Ollama本地embedding ☐支持自定义API endpoint ☐向量存储到FAISS/ChromaDB F3:图谱可视化（WebUI）
- 需求只在 pdf：☐使用D3.js或Cytoscape.js渲染图谱☐支持节点拖拽和缩放☐点击节点显示详情☐支持按标签筛选显示F4:基础关联kgkb link<node1_id><node2_id>--relation"相关"
- 需求只在 pdf：☐支持手动创建关联☐支持定义关联类型（相关、因果、包含等）☐关联在图谱中可视化显示
- 需求只在 pdf：推荐关联关系F7:OpenClaw集成
- 需求只在 pdf：作为OpenClaw Skill集成F8:基础预测
- 需求只在 pdf：-向量索引（FAISS管理，元数据存储）
- 需求只在 pdf：排除功能原因计划版本v1.1自动关联技术复杂度高v1.2 AI预测需要更多数据v1.1 OpenClaw集成依赖API稳定v2.0多用户协作架构改动大v2.0插件系统优先级低
- 需求只在 pdf：Given我有一条知识要存入

### anzx01__cusops

段落标题不一致，需求条目 130 / 196 一致（pdf 拆出 191 条）

- 标题只在 Markdown：AI接待员 PRD
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 产品定位
- 标题只在 Markdown：3. 目标用户
- 标题只在 Markdown：3.1 首个 ICP
- 标题只在 pdf：AI接待员PRD
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.产品定位
- 标题只在 pdf：3.目标用户
- 标题只在 pdf：3.1首个ICP
- 需求只在 Markdown：文档目标：定义 MVP 的产品边界、核心流程、功能需求、指标和验收标准
- 需求只在 Markdown：长期愿景可以是"中小服务商的 AI 员工平台"，但 MVP 阶段只聚焦"接待、筛选、预约、转人工"。
- 需求只在 Markdown：客户咨询不能及时回复
- 需求只在 Markdown：晚上、周末、忙碌时段容易漏单
- 需求只在 Markdown：重复问题占用人工
- 需求只在 Markdown：客户信息收集不完整，后续跟进低效
- 需求只在 Markdown：预约、改约、提醒依赖人工
- 需求只在 Markdown：用数据展示 AI 带来的预约量和节省时间
- 需求只在 Markdown：不让 MVP 用户搭流程
- 需求只在 Markdown：AI 必须有明确边界和人工兜底
- 需求只在 pdf：文档目标：定义MVP的产品边界、核心流程、功能需求、指标和验收标准
- 需求只在 pdf：长期愿景可以是"中小服务商的AI员工平台"，但MVP阶段只聚焦"接待、筛选、预约、转人工"。
- 需求只在 pdf：主要痛点：o客户咨询不能及时回复o晚上、周末、忙碌时段容易漏单o重复问题占用人工o客户信息收集不完整，后续跟进低效o预约、改约、提醒依赖人工
- 需求只在 pdf：用数据展示AI带来的预约量和节省时间
- 需求只在 pdf：不让MVP用户搭流程
- 需求只在 pdf：AI必须有明确边界和人工兜底
- 需求只在 pdf：一个真实高价值渠道接入，建议根据市场选择：o海外市场：SMS或WhatsApp o中国市场：微信/企微或短信
- 需求只在 pdf：Google Calendar或Outlook Calendar写入
- 需求只在 pdf：基础数据面板和ROI展示
- 需求只在 pdf：语音AI全自动接电话

### appstore-discounts__appstore-discounts

段落标题不一致，需求条目 42 / 186 一致（pdf 拆出 171 条）

- 标题只在 Markdown：App Store Discounts器 - 前端展示页面 需求文档 (PRD)
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 访问地址
- 标题只在 Markdown：1.3 技术选型
- 标题只在 pdf：App Store Discounts器-前端展示页面需求文档(PRD)
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2访问地址
- 标题只在 pdf：1.3技术选型
- 需求只在 Markdown：类别：构建工具；选型：Vite；说明：快速构建，原生 ESM 支持
- 需求只在 Markdown：类别：样式方案；选型：Tailwind CSS；说明：快速开发，响应式支持优秀，tree-shaking 体积小
- 需求只在 Markdown：类别：部署；选型：Cloudflare Pages；说明：支持自定义域名，自动 CI/CD
- 需求只在 Markdown：按日期分组：相同日期（按浏览器本地时区计算）的折扣应用归为一组，每组显示日期标题
- 需求只在 Markdown：日期格式根据当前语言本地化（中文：2026年5月23日 / 英文：May 23, 2026）
- 需求只在 Markdown：折扣数据来源：基于 src/data/storage/{region}.json 重新计算折扣信息，而非 rss.json（因为 rss.json 仅保留最近 3 天的折扣记录，数据范围有限）
- 需求只在 Markdown：去重规则：同一应用（trackId 相同）且折扣信息完全一致时才进行去重，保留最新的一条记录
- 需求只在 Markdown：信息项：通知禁用标识；数据来源：notificationDisabled（构建时从 apps.json 标注）；展示方式：应用名称旁显示图标（�+禁止符号），鼠标悬浮提示"推送已禁用"（仅当 allowNotification: false 时显示）
- 需求只在 Markdown：在 apps.json 中，若应用配置项包含 allowNotification: false，则认为该应用已禁用推送
- 需求只在 Markdown：在构建时（generateWebData.ts）根据 apps.json 将 notificationDisabled: true 写入每条折扣记录
- 需求只在 pdf：1.1数据展示规则
- 需求只在 pdf：按日期分组：相同日期（按浏览器本地时区计算）的折扣应用归为一组，每组显示日期标题o日期格式根据当前语言本地化（中文：2026年5月23日/英文：May 23, 2026）
- 需求只在 pdf：折扣数据来源：基于src/data/storage/{region}.json重新计算折扣信息，而非rss.json（因为rss.json仅保留最近3天的折扣记录，数据范围有限）
- 需求只在 pdf：去重规则：同一应用（trackId相同）且折扣信息完全一致时才进行去重，保留最新的一条记录
- 需求只在 pdf：1.2应用卡片信息
- 需求只在 pdf：通知禁用标识应用名称旁显示图标ed（构建时从（�+禁止符号），鼠apps.json标注）标悬浮提示"推送已禁用"（仅当
- 需求只在 pdf：在apps.json中，若应用配置项包含allowNotification:false，则认为该应用已禁用推送
- 需求只在 pdf：在构建时（generateWebData.ts）根据apps.json将notificationDisabled: true写入每条折扣记录
- 需求只在 pdf：前端独立提供/api/disabled-apps端点供详情页查询（返回{ ids: number[]}格式）
- 需求只在 pdf：1.3应用信息缓存策略

### arana-db__kiwi

段落标题不一致，需求条目 5 / 77 一致（pdf 拆出 76 条）

- 标题只在 Markdown：Kiwi 产品需求文档（PRD）
- 标题只在 Markdown：1. 产品目标 / 北极星
- 标题只在 Markdown：2. 用户画像与场景（反推）
- 标题只在 Markdown：3. Requirement 产品视图
- 标题只在 Markdown：稳定性、Oracle provenance 与工作连续性
- 标题只在 pdf：Kiwi产品需求文档（PRD）
- 标题只在 pdf：1.产品目标/北极星
- 标题只在 pdf：2.用户画像与场景（反推）
- 标题只在 pdf：3. Requirement产品视图
- 标题只在 pdf：稳定性、Oracle provenance与工作连续性
- 需求只在 Markdown：稳定性和工作连续性：进入 M7 前的硬门禁、Oracle provenance 信任根和可恢复工作状态。
- 需求只在 Markdown：兼容、存储、Raft、可观测性和性能：当前 Cache OFF 主线 M1–M6 的实现与验证合同。
- 需求只在 Markdown：Hot Tier 和组合发行：长期 M7–M9 合同，当前保持 Frozen。
- 需求只在 Markdown：REQ-STABILITY-001：启动热层生产实现前须门禁明确通过，且用户须明确批准一个单独的 implementation task。
- 需求只在 Markdown：REQ-STABILITY-002：门禁至少覆盖 Redis 8.8.1 differential、RocksDB close/reopen、Raft commit/apply/durability、Snapshot、成员变更、进程级故障注入、资源边界、可观测性。
- 需求只在 Markdown：REQ-STABILITY-003：门禁证据须绑定 branch/HEAD/平台/工具链/命令/结果/未覆盖风险；仅单测不算稳定。
- 需求只在 Markdown：REQ-STABILITY-004：门禁未过期间只允许设计热层合同，禁止新增 Redis-derived 生产依赖/loader/数据路径/默认配置。
- 需求只在 Markdown：REQ-STABILITY-005：任何解除冻结决定须追加到 DECISIONS.md 并同步 SDD.md，不得由 PR 隐式解除。
- 需求只在 Markdown：REQ-STABILITY-006：门禁通过只允许提交新规划与授权请求；即使用户同意 M7 转为 Ready，fork/loader/发行/热层实现仍只能在单独获批的 implementation task 中执行。
- 需求只在 Markdown：REQ-COMPAT-008：Oracle provenance 须 primary build 与 verifier 独立重建 binary SHA-256 完全一致，正式证据只来自独立重建产物。
- 需求只在 pdf：稳定性和工作连续性：进入M7前的硬门禁、Oracle provenance信任根和可恢复工作状态。
- 需求只在 pdf：兼容、存储、Raft、可观测性和性能：当前Cache OFF主线M1–M6的实现与验证合同。
- 需求只在 pdf：Hot Tier和组合发行：长期M7–M9合同，当前保持Frozen。
- 需求只在 pdf：REQ-STABILITY-001：启动热层生产实现前须门禁明确通过，且用户须明确批准一个单独的implementation task。
- 需求只在 pdf：REQ-STABILITY-002：门禁至少覆盖Redis 8.8.1 differential、RocksDB close/reopen、Raft commit/apply/durability、Snapshot、成员变更、进程级故障注入、资源边界、可观测性。
- 需求只在 pdf：REQ-STABILITY-003：门禁证据须绑定branch/HEAD/平台/工具链/命令/结果/未覆盖风险；仅单测不算稳定。
- 需求只在 pdf：REQ-STABILITY-004：门禁未过期间只允许设计热层合同，禁止新增Redis- derived生产依赖/loader/数据路径/默认配置。
- 需求只在 pdf：REQ-STABILITY-005：任何解除冻结决定须追加到DECISIONS.md并同步SDD.md，不得由PR隐式解除。
- 需求只在 pdf：REQ-STABILITY-006：门禁通过只允许提交新规划与授权请求；即使用户同意M7转为Ready，fork/loader/发行/热层实现仍只能在单独获批的implementation task中执行。
- 需求只在 pdf：REQ-COMPAT-008：Oracle provenance须primary build与verifier独立重建binary SHA-256完全一致，正式证据只来自独立重建产物。

### arch-team__devpace

段落标题不一致，需求条目 0 / 166 一致（pdf 拆出 19 条）

- 标题只在 Markdown：devpace 需求
- 标题只在 Markdown：F5：AI 主导管理
- 标题只在 Markdown：S28：DORA 度量查看
- 标题只在 Markdown：S30：CI/CD 自动感知
- 标题只在 Markdown：F7：Linear AI 借鉴增强
- 标题只在 pdf：devpace需求
- 标题只在 pdf：F5：AI主导管理
- 标题只在 pdf：S28：DORA度量查看
- 标题只在 pdf：S30：CI/CD自动感知
- 标题只在 pdf：F7：Linear AI借鉴增强
- 需求只在 Markdown：维度：回答的问题；说明：有哪些用户场景？每个场景需要什么功能？非功能约束是什么（性能、兼容性等）？
- 需求只在 Markdown：维度：主要读者；说明：实现者——需要知道"做哪些功能、做到什么程度"
- 需求只在 Markdown：/pace-init 通过对话收集项目信息
- 需求只在 Markdown：自动生成 .devpace/ 目录和所有必需文件
- 需求只在 Markdown：生成的价值功能树结构合理
- 需求只在 Markdown：角色：开发者 场景：新开一个 Claude Code 会话，继续昨天的工作 期望：Claude 自动知道做到哪了，直接继续，不需要我重新解释
- 需求只在 Markdown：Claude 会话开始自动读取 state.md
- 需求只在 Markdown：用 1 句自然语言报告当前状态
- 需求只在 Markdown：用户说"继续"就能从上次断点恢复
- 需求只在 Markdown：/pace-status detail 展开到产品功能级别
- 需求只在 pdf：维度说明回答的问题有哪些用户场景？每个场景需要什么功能？非功能约束是什么（性能、兼容性等）？上游输入vision.md（业务目标拆解为场景）、design.md（设计方案拆解为功能点）下游消费roadmap.md（需求条目排入实施阶段）更新时机新增用户场景、功能需求变更、发现遗漏的非功能需求时类别项目管理——功能验收规格，不进入产品运行时主要读者实现者——需要知道"做哪些功能、做到什么程度"
- 需求只在 pdf：角色：开发者场景：新开一个Claude Code会话，继续昨天的工作期望：Claude自动知道做到哪了，直接继续，不需要我重新解释
- 需求只在 pdf：角色：开发者场景：做到一半，发现需要加一个新功能期望：告诉Claude新需求，它自动分析影响、调整计划
- 需求只在 pdf：角色：开发者场景：某个功能需要提前做期望：调整优先级后迭代计划自动重排
- 需求只在 pdf：☒识别已完成工作中需要返工的部分☒质量检查重置为未检查（需要重新验证）☒CR事件记录变更原因
- 需求只在 pdf：角色：开发者场景：当前迭代接近尾声或已结束，需要关闭当前迭代并规划下一个迭代的范围期望：Claude引导完成迭代关闭和新迭代的PF选择，生成迭代文件
- 需求只在 pdf：角色：开发者/运维场景：上线后发现生产问题，需要追溯问题来源并创建修复CR期望：自动追溯到引入变更的CR和PF，创建defect/hotfix CR驱动修复闭环
- 需求只在 pdf：角色：开发者（兼多角色）场景：同一个人在不同阶段需要以不同角色视角查看项目信息期望：Claude自动推断当前角色，或通过命令显式切换，输出内容随角色变化
- 需求只在 pdf：☒project.md支持自主级别:字段配置（辅助/标准/自主）☒辅助模式下Gate失败时询问而非自动修复☒标准模式保持当前所有行为不变（默认）☒自主模式下简化审批条件放宽（≤5文件）☒Gate 3在任何自主级别下都是人类阻塞门禁
- 需求只在 pdf：角色：开发者/PM场景：用户不确定当前最该做什么，需要跨域（CR/迭代/Release/度量）的全局导航建议期望：一条命令获得基于多维信号的优先级推荐，附带推理依据和操作指引

### armylau__tetris_game

段落标题不一致，需求条目 34 / 99 一致（pdf 拆出 85 条）

- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目目标
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：2. 功能需求
- 标题只在 Markdown：2.1 核心游戏功能
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目目标
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：2.功能需求
- 标题只在 pdf：2.1核心游戏功能
- 需求只在 Markdown：描述: 实现7种经典俄罗斯方块形状
- 需求只在 Markdown：O型方块（正方形）
- 需求只在 Markdown：验收标准: 所有7种方块能正确显示和旋转
- 需求只在 Markdown：描述: 实现方块的移动和旋转控制
- 需求只在 Markdown：左右移动：方向键左右
- 需求只在 Markdown：快速下落：方向键下
- 需求只在 Markdown：旋转：空格键或上方向键
- 需求只在 Markdown：硬降落：上方向键（快速到底）
- 需求只在 Markdown：验收标准: 方块能响应所有控制指令
- 需求只在 Markdown：描述: 实现10x20的游戏板
- 需求只在 pdf：描述:实现7种经典俄罗斯方块形状
- 需求只在 pdf：详细要求: o I型方块（长条）o O型方块（正方形）o T型方块o S型方块o Z型方块o J型方块o L型方块
- 需求只在 pdf：验收标准:所有7种方块能正确显示和旋转
- 需求只在 pdf：描述:实现方块的移动和旋转控制
- 需求只在 pdf：详细要求: o左右移动：方向键左右o快速下落：方向键下o旋转：空格键或上方向键o硬降落：上方向键（快速到底）
- 需求只在 pdf：验收标准:方块能响应所有控制指令
- 需求只在 pdf：描述:实现10x20的游戏板
- 需求只在 pdf：详细要求: o 10列20行的游戏区域o边界检测o方块堆叠逻辑
- 需求只在 pdf：验收标准:方块能正确堆叠，不会超出边界
- 需求只在 pdf：描述:实现完整的行消除机制

### bdim404__Qwen3-TTS-WebUI

段落标题不一致，需求条目 150 / 224 一致（pdf 拆出 189 条）

- 标题只在 Markdown：Qwen3-TTS 多人对话功能需求文档
- 标题只在 Markdown：1. 功能概述
- 标题只在 Markdown：2. 核心需求
- 标题只在 Markdown：2.1 音色复用机制
- 标题只在 Markdown：3. 数据模型设计
- 标题只在 pdf：Qwen3-TTS多人对话功能需求文档
- 标题只在 pdf：1.功能概述
- 标题只在 pdf：2.核心需求
- 标题只在 pdf：2.1音色复用机制
- 标题只在 pdf：3.数据模型设计
- 需求只在 Markdown：用户可将 Qwen3-TTS 创建的音色进行持久存储
- 需求只在 Markdown：音色类型：CustomVoice / VoiceDesign / VoiceClone
- 需求只在 Markdown：绑定音色（引用音色库ID 或 使用预定义音色）
- 需求只在 Markdown：颜色标记（用于在对话中区分）
- 需求只在 Markdown：是否自动合并
- 需求只在 Markdown：间隔策略：intelligent（智能间隔）
- 需求只在 Markdown：合并后的音频路径
- 需求只在 Markdown：JSON格式（完整数据）
- 需求只在 Markdown：CSV格式（角色、文本、指令）
- 需求只在 Markdown：SRT字幕格式（时间轴 + 文本）
- 需求只在 pdf：用户可将Qwen3-TTS创建的音色进行持久存储
- 需求只在 pdf：音色类型：CustomVoice/ VoiceDesign / VoiceClone
- 需求只在 pdf：音色数据：o CustomVoice:speaker名称o VoiceDesign:instruct指令o VoiceClone:缓存的x_vector引用
- 需求只在 pdf：绑定音色（引用音色库ID或使用预定义音色）
- 需求只在 pdf：个性化显示：o头像/图标o颜色标记（用于在对话中区分）
- 需求只在 pdf：默认TTS参数：o language o max_new_tokens o temperature o top_k o top_p o repetition_penalty
- 需求只在 pdf：对话状态：o draft（草稿）o generating（生成中）o completed（已完成）o failed（失败）o partial（部分成功）
- 需求只在 pdf：生成模式：o sequential（顺序生成）o batch（批量生成）
- 需求只在 pdf：音频合并配置：o是否自动合并o间隔策略：intelligent（智能间隔）o合并后的音频路径
- 需求只在 pdf：导出对话：o JSON格式（完整数据）o CSV格式（角色、文本、指令）o SRT字幕格式（时间轴+文本）o音频文件（分段或合并）

### bugkiwi__elons-job

段落标题不一致，需求条目 13 / 58 一致（pdf 拆出 47 条）

- 标题只在 Markdown：1. 产品定义
- 标题只在 Markdown：1.1 一句话描述
- 标题只在 Markdown：1.2 核心原则
- 标题只在 Markdown：1.3 MVP 不做
- 标题只在 Markdown：2. 用户场景
- 标题只在 pdf：1.产品定义
- 标题只在 pdf：1.1一句话描述
- 标题只在 pdf：1.2核心原则
- 标题只在 pdf：1.3 MVP不做
- 标题只在 pdf：2.用户场景
- 需求只在 Markdown：用户使用自己的 TypeSafe API Key，默认提供少量过滤规则，也可以自行新增、修改和关闭规则。
- 需求只在 Markdown：只处理 X 评论区
- 需求只在 Markdown：不修改 X 原始数据，只改变本地显示
- 需求只在 Markdown：TypeSafe API Key 由用户自己提供
- 需求只在 Markdown：API 异常时 Fail Open：不隐藏评论
- 需求只在 Markdown：MVP 只分析文本，不分析图片和视频
- 需求只在 Markdown：X 首页推荐流过滤
- 需求只在 Markdown：图片 / 视频色情识别
- 需求只在 Markdown：插件开发者代付 TypeSafe API 成本
- 需求只在 Markdown：提供 测试连接
- 需求只在 pdf：用户使用自己的TypeSafe API Key，默认提供少量过滤规则，也可以自行新增、修改和关闭规则。
- 需求只在 pdf：只处理X评论区
- 需求只在 pdf：不修改X原始数据，只改变本地显示
- 需求只在 pdf：TypeSafe API Key由用户自己提供
- 需求只在 pdf：API异常时Fail Open：不隐藏评论
- 需求只在 pdf：MVP只分析文本，不分析图片和视频
- 需求只在 pdf：X首页推荐流过滤
- 需求只在 pdf：图片/视频色情识别
- 需求只在 pdf：插件开发者代付TypeSafe API成本
- 需求只在 pdf：提供测试连接

### caesarloo__obsidian-svn

段落标题不一致，需求条目 57 / 91 一致（pdf 拆出 80 条）

- 标题只在 Markdown：Vault SVN 版本管理插件 - 需求文档 (v1.1)
- 标题只在 Markdown：1. 背景与目标
- 标题只在 Markdown：2. 范围
- 标题只在 Markdown：包含范围 (MVP)
- 标题只在 Markdown：不包含范围 (本期)
- 标题只在 pdf：Vault SVN版本管理插件-需求文档(v1.1)
- 标题只在 pdf：1.背景与目标
- 标题只在 pdf：2.范围
- 标题只在 pdf：包含范围(MVP)
- 标题只在 pdf：不包含范围(本期)
- 需求只在 Markdown：配置 SVN 认证凭据（用户名、密码）。
- 需求只在 Markdown：支持可选的安全凭据存储（使用 Obsidian 提供的安全存储机制）。
- 需求只在 Markdown：工作副本默认使用当前 Obsidian 库根目录。
- 需求只在 Markdown："暂存"仅作为提交选择，不对应 SVN 命令。
- 需求只在 Markdown："还原"对应还原（svn revert）。
- 需求只在 Markdown：文件夹支持折叠/展开（折叠为 "-"，展开为 "+"）。
- 需求只在 Markdown：采用内联对比为主，侧边对比为辅的展示方式
- 需求只在 Markdown：支持与最新版本的差异对比
- 需求只在 Markdown：对于大文件，采用异步加载和分页显示
- 需求只在 Markdown：使用通知提示更新完成
- 需求只在 pdf：配置SVN认证凭据（用户名、密码）。
- 需求只在 pdf：支持可选的安全凭据存储（使用Obsidian提供的安全存储机制）。
- 需求只在 pdf：工作副本默认使用当前Obsidian库根目录。
- 需求只在 pdf：文件/文件夹右侧提供"暂存/还原"图标动作：o"暂存"仅作为提交选择，不对应SVN命令。o"还原"对应还原（svn revert）。
- 需求只在 pdf：文件夹支持折叠/展开（折叠为"-"，展开为"+"）。
- 需求只在 pdf：点击文件可以查看文件差异（svn diff）：o采用内联对比为主，侧边对比为辅的展示方式o支持与最新版本的差异对比o对于大文件，采用异步加载和分页显示
- 需求只在 pdf：更新后显示本次更新的文件列表：o使用通知提示更新完成o在面板中展示详细的更新文件列表o支持点击文件查看详细信息o添加更新统计信息（文件数量、大小等）
- 需求只在 pdf：支持一键生成提交备注摘要（由Copilot生成）。
- 需求只在 pdf：Copilot生成摘要仅填充提交日志文本框，不自动触发提交。
- 需求只在 pdf：Copilot生成摘要失败时仅提示，不阻断手动提交。

### calderbuild__MD_Audit

段落标题不一致，需求条目 12 / 100 一致（pdf 拆出 99 条）

- 标题只在 Markdown：产品需求文档 (PRD)
- 标题只在 Markdown：Markdown SEO 诊断 Agent
- 标题只在 Markdown：1. 项目背景与目标
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标
- 标题只在 pdf：产品需求文档(PRD)
- 标题只在 pdf：Markdown SEO诊断Agent
- 标题只在 pdf：1.项目背景与目标
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2目标
- 需求只在 Markdown：原生Markdown支持: 无需转换，直接分析.md文件
- 需求只在 Markdown：双引擎分析: 规则引擎（快速、准确）+ AI引擎（深度、智能）
- 需求只在 Markdown：可执行建议: 提供具体的代码示例和修改建议，而非泛泛而谈
- 需求只在 Markdown：配置化规则: 支持自定义SEO规则阈值，适应不同场景
- 需求只在 Markdown：Markdown报告: 输出人类可读的Markdown格式报告，便于分享和存档
- 需求只在 Markdown：技术博主: 使用Markdown撰写技术文章，需要优化SEO以提升文章曝光
- 需求只在 Markdown：文档工程师: 维护产品文档站（如GitBook、VuePress），需确保文档SEO友好
- 需求只在 Markdown：内容运营: 管理静态博客（如Hugo、Jekyll），需批量检查内容质量
- 需求只在 Markdown：用户使用CLI命令分析Markdown文件：python main.py analyze article.md --keyword "Python SEO"
- 需求只在 Markdown：总分和分项得分
- 需求只在 pdf：原生Markdown支持:无需转换，直接分析.md文件
- 需求只在 pdf：双引擎分析:规则引擎（快速、准确）+AI引擎（深度、智能）
- 需求只在 pdf：可执行建议:提供具体的代码示例和修改建议，而非泛泛而谈
- 需求只在 pdf：配置化规则:支持自定义SEO规则阈值，适应不同场景
- 需求只在 pdf：Markdown报告:输出人类可读的Markdown格式报告，便于分享和存档
- 需求只在 pdf：技术博主:使用Markdown撰写技术文章，需要优化SEO以提升文章曝光
- 需求只在 pdf：文档工程师:维护产品文档站（如GitBook、VuePress），需确保文档SEO友好
- 需求只在 pdf：内容运营:管理静态博客（如Hugo、Jekyll），需批量检查内容质量
- 需求只在 pdf：用户使用CLI命令分析Markdown文件：python main.py analyze
- 需求只在 pdf：输出Markdown格式的诊断报告，包含：o总分和分项得分o严重问题列表（Critical Issues）o优化建议（Suggestions）o AI生成的具体改进方案

### cholf5__skynet

段落标题不一致，需求条目 93 / 166 一致（pdf 拆出 156 条）

- 标题只在 Markdown：PRD — Skynet (C#) — 极简 Skynet 风格 Actor 框架（面向游戏后端，C# 实现）
- 标题只在 Markdown：1. 总体目标与非目标
- 标题只在 Markdown：1.1 目标
- 标题只在 Markdown：1.2 非目标
- 标题只在 Markdown：2. 设计原则与约束
- 标题只在 pdf：PRD —Skynet (C#)—极简Skynet风格Actor框架（面向游戏后端，C#实现）
- 标题只在 pdf：1.总体目标与非目标
- 标题只在 pdf：1.1目标
- 标题只在 pdf：1.2非目标
- 标题只在 pdf：2.设计原则与约束
- 需求只在 Markdown：透明调用语义：对用户，send/call 与 Skynet 语义一致（本地/远程对用户透明），但框架内部可 short-circuit 用于优化。
- 需求只在 Markdown：类型优先：首选 Interface + SourceGenerator 方案，自动生成 proxy/stub 与序列化代码，保证 IDE/编译器保护。
- 需求只在 Markdown：兼容 Skynet 用法：提供 handle（数字）与 name（字符串）双向映射接口，并支持 uniqueservice 与简单 multicast/room 功能。
- 需求只在 Markdown：登录认证服务（LoginActor）：客户端发起 login 请求→ Gate 转发到 LoginActor → LoginActor 调用 DB Actor 验证 → 返回结果。
- 需求只在 Markdown：房间/房间管理（RoomActor + Multicast）：多个玩家加入同一 RoomActor，广播消息到该房间成员。
- 需求只在 Markdown：网关/会话管理（GateServer + SessionActor）：TCP/WebSocket 连接接入，绑定到 SessionActor，服务器 Actor 向该 SessionActor 发反向消息。
- 需求只在 Markdown：全服唯一服务（DataCenter 或 UniqueService）：某些全局资源由 uniqueservice 承担（单例）。
- 需求只在 Markdown：Actor 基类 Actor：封装 Channel mailbox，提供 Tell(Func<Task>) / Ask<T>(Func<Task<T>>)。
- 需求只在 Markdown：ActorSystem / ActorHost：启动时加载/注册 Actor，实现本地 registry（handle ↔ name 映射）。
- 需求只在 Markdown：生命周期 API：CreateService(name?)、GetByHandle(handle)、GetByName(name)、Kill(handle)、ListServices()。
- 需求只在 pdf：透明调用语义：对用户，send/call与Skynet语义一致（本地/远程对用户透明），但框架内部可short-circuit用于优化。
- 需求只在 pdf：类型优先：首选Interface + SourceGenerator方案，自动生成proxy/stub与序列化代码，保证IDE/编译器保护。
- 需求只在 pdf：兼容Skynet用法：提供handle（数字）与name（字符串）双向映射接口，并支持uniqueservice与简单multicast/room功能。
- 需求只在 pdf：登录认证服务（LoginActor）：客户端发起login请求→Gate转发到LoginActor → LoginActor调用DB Actor验证→返回结果。
- 需求只在 pdf：房间/房间管理（RoomActor+Multicast）：多个玩家加入同一RoomActor，广播消息到该房间成员。
- 需求只在 pdf：网关/会话管理（GateServer+SessionActor）：TCP/WebSocket连接接入，绑定到SessionActor，服务器Actor向该SessionActor发反向消息。
- 需求只在 pdf：全服唯一服务（DataCenter或UniqueService）：某些全局资源由uniqueservice承担（单例）。
- 需求只在 pdf：Actor基类Actor：封装Channel mailbox，提供Tell(Func<Task>)/ Ask<T>(Func<Task<T>>)。
- 需求只在 pdf：ActorSystem /ActorHost：启动时加载/注册Actor，实现本地registry（handle↔ name映射）。
- 需求只在 pdf：生命周期API：CreateService(name?)、GetByHandle(handle)、GetByName(name)、Kill(handle)、ListServices()。

### cnjack__jcode

段落标题不一致，需求条目 22 / 111 一致（pdf 拆出 109 条）

- 标题只在 Markdown：JCode Artifacts PRD（Web / Desktop）
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：2. 问题定义
- 标题只在 Markdown：3. 产品定义
- 标题只在 Markdown：4. 目标
- 标题只在 pdf：JCode Artifacts PRD（Web/Desktop）
- 标题只在 pdf：1.背景
- 标题只在 pdf：2.问题定义
- 标题只在 pdf：3.产品定义
- 标题只在 pdf：4.目标
- 需求只在 Markdown：UI 原型与评审：internal-doc/artifacts-ui/index.html、internal-doc/artifacts-ui/design-notes.md
- 需求只在 Markdown：Agent 知道哪个文件是最终结果，界面不知道。
- 需求只在 Markdown：Files 面板展示整个工作区，用户难以区分"源文件"和"交付物"。
- 需求只在 Markdown：Web 与 Desktop 有可视化承载能力，但 CLI/TUI 和 ACP 没有统一的 Artifact UI 契约，强行暴露工具只会造成不可完成的工具调用。
- 需求只在 Markdown：文件内容在会话 JSONL 中的副本；
- 需求只在 Markdown：CLI/ACP 协议中的通用输出类型。
- 需求只在 Markdown：Agent 生成并验证 reports/analysis.html。
- 需求只在 Markdown：当前 Web/Desktop 会话自动打开 Artifacts 面板并展示报告。
- 需求只在 Markdown：Agent 最终回复中同时给出可点击的 Artifact 卡片或链接。
- 需求只在 Markdown：用户稍后打开历史会话，Artifacts 标签显示数量。点击后可以看到该会话曾交付的报告、图表和说明文档；文件缺失时保留元数据并显示 missing 状态，下载、分享和原生打开动作禁用，同时提供"重新检测"。恢复文件后用户可重新检测并继续预览。
- 需求只在 pdf：UI原型与评审：internal-doc/artifacts-ui/index.html、internal-doc/artifacts-ui/
- 需求只在 pdf：Agent知道哪个文件是最终结果，界面不知道。
- 需求只在 pdf：Files面板展示整个工作区，用户难以区分"源文件"和"交付物"。
- 需求只在 pdf：Web与Desktop有可视化承载能力，但CLI/TUI和ACP没有统一的Artifact UI契约，强行暴露工具只会造成不可完成的工具调用。
- 需求只在 pdf：文件内容在会话JSONL中的副本；
- 需求只在 pdf：CLI/ACP协议中的通用输出类型。
- 需求只在 pdf：Agent生成并验证reports/analysis.html。
- 需求只在 pdf：当前Web/Desktop会话自动打开Artifacts面板并展示报告。
- 需求只在 pdf：Agent最终回复中同时给出可点击的Artifact卡片或链接。
- 需求只在 pdf：用户稍后打开历史会话，Artifacts标签显示数量。点击后可以看到该会话曾交付的报告、图表和说明文档；文件缺失时保留元数据并显示missing状态，下载、分享和原生打开动作禁用，同时提供"重新检测"。恢复文件后用户可重新检测并继续预览。

### cuixbo__OnePanel

段落标题不一致，需求条目 117 / 162 一致（pdf 拆出 165 条）

- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 产品概述
- 标题只在 Markdown：3. 产品目标
- 标题只在 Markdown：4. 目标用户
- 标题只在 Markdown：5. 核心设计原则
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.产品概述
- 标题只在 pdf：3.产品目标
- 标题只在 pdf：4.目标用户
- 标题只在 pdf：5.核心设计原则
- 需求只在 Markdown：纯文本编辑，不支持 Markdown、富文本、附件。
- 需求只在 Markdown：默认快捷键为 Command + Control + P。
- 需求只在 Markdown：窗口支持"悬浮 / 固定"两种状态。
- 需求只在 Markdown：面板焦点状态下按 ESC 隐藏。
- 需求只在 Markdown：支持跨 Mission Control 桌面唤起。
- 需求只在 Markdown：高频文本记录用户：需要频繁记录和取用命令、文案、备忘的 macOS 用户。
- 需求只在 Markdown：作为一名用户，我希望按 ESC 就能快速隐藏面板，这样我可以在需要专注当前应用时立刻收起它。
- 需求只在 Markdown：形态：macOS 状态栏图标。
- 需求只在 Markdown：作用：应用常驻入口，用于显示或隐藏 OnePanel 主面板。
- 需求只在 Markdown：交互重点：支持键盘输入、文本选择、复制、粘贴、拖动、缩放、ESC 隐藏。
- 需求只在 pdf：纯文本编辑，不支持Markdown、富文本、附件。
- 需求只在 pdf：默认快捷键为Command+Control+P。
- 需求只在 pdf：窗口支持"悬浮/固定"两种状态。
- 需求只在 pdf：面板焦点状态下按ESC隐藏。
- 需求只在 pdf：支持跨Mission Control桌面唤起。
- 需求只在 pdf：高频文本记录用户：需要频繁记录和取用命令、文案、备忘的macOS用户。
- 需求只在 pdf：作为一名用户，我希望按ESC就能快速隐藏面板，这样我可以在需要专注当前应用时立刻收起它。
- 需求只在 pdf：形态：macOS状态栏图标。
- 需求只在 pdf：作用：应用常驻入口，用于显示或隐藏OnePanel主面板。
- 需求只在 pdf：交互重点：支持键盘输入、文本选择、复制、粘贴、拖动、缩放、ESC隐藏。

### dasi0227__QA-Agent

段落标题不一致，需求条目 116 / 169 一致（pdf 拆出 213 条）

- 标题只在 Markdown：QA_Agent 产品需求文档
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 产品概述
- 标题只在 Markdown：2.1 项目名称
- 标题只在 Markdown：2.2 产品定位
- 标题只在 pdf：QA_Agent产品需求文档
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.产品概述
- 标题只在 pdf：2.1项目名称
- 标题只在 pdf：2.2产品定位
- 需求只在 Markdown：文档名称：QA_Agent 产品需求文档
- 需求只在 Markdown：面向对象：产品、设计、前端开发、后端开发、Agent 工程实现
- 需求只在 Markdown：文档目标：明确 QA_Agent 当前阶段的产品定位、核心资产、技术方向、功能模块和版本演进规律，为后续分阶段研发提供统一依据
- 需求只在 Markdown：如何在资产底座稳定之后，再逐步接入真正可用的 Agent 能力，而不是一开始就让系统承担过大的智能链路复杂度。
- 需求只在 Markdown：当前阶段正式支持的资料输入格式以 Markdown 为主。
- 需求只在 Markdown：后续再接入 Agent 能力
- 需求只在 Markdown：资产之间的关系清晰稳定，能够支撑后续真实 Agent 接入。
- 需求只在 Markdown：前端不依赖真实 Agent 也能完整跑通核心资产工作流。
- 需求只在 Markdown：RAG 能提供稳定、可复用、可验证的资料证据召回能力。
- 需求只在 Markdown：生成 Agent 能把资料转为结构化问答集，而不是泛化文本。
- 需求只在 pdf：文档名称：QA_Agent产品需求文档
- 需求只在 pdf：面向对象：产品、设计、前端开发、后端开发、Agent工程实现
- 需求只在 pdf：文档目标：明确QA_Agent当前阶段的产品定位、核心资产、技术方向、功能模块和版本演进规律，为后续分阶段研发提供统一依据
- 需求只在 pdf：如何在资产底座稳定之后，再逐步接入真正可用的Agent能力，而不是一开始就让系统承担过大的智能链路复杂度。
- 需求只在 pdf：当前阶段正式支持的资料输入格式以Markdown为主。
- 需求只在 pdf：后续再接入Agent能力
- 需求只在 pdf：资产之间的关系清晰稳定，能够支撑后续真实Agent接入。
- 需求只在 pdf：前端不依赖真实Agent也能完整跑通核心资产工作流。阶段二及以后成功标准
- 需求只在 pdf：RAG能提供稳定、可复用、可验证的资料证据召回能力。
- 需求只在 pdf：生成Agent能把资料转为结构化问答集，而不是泛化文本。

### davidhoo__MarkdownReader

段落标题不一致，需求条目 77 / 163 一致（pdf 拆出 136 条）

- 标题只在 Markdown：MarkdownReader 多窗口需求文档
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：2. 产品目标
- 标题只在 Markdown：3. 非目标
- 标题只在 Markdown：4. 术语
- 标题只在 pdf：MarkdownReader多窗口需求文档
- 标题只在 pdf：1.背景
- 标题只在 pdf：2.产品目标
- 标题只在 pdf：3.非目标
- 标题只在 pdf：4.术语
- 需求只在 Markdown：该会话使用的 undo/redo 历史。
- 需求只在 Markdown：能够作为窗口打开目标的本地 Markdown 文件、纯文本文件或目录。
- 需求只在 Markdown：当前 key window。菜单快捷键和文档级命令必须路由到该窗口；隐藏窗口、非 key window 和系统 Panel 不得响应。
- 需求只在 Markdown：尚未打开文件或目录、未创建待保存 Untitled 文档的主窗口。空白窗口显示 Welcome 页面，可以被下一次打开操作复用。
- 需求只在 Markdown：内容、脏状态、Untitled 状态和保存面板状态；
- 需求只在 Markdown：PDF 导出目标和进行中状态；
- 需求只在 Markdown：File > New Window：创建一个新的空白窗口。
- 需求只在 Markdown：File > New File：在当前活动窗口创建 Untitled 文档，保持现有新建文件语义。
- 需求只在 Markdown：Cmd+N：保留现有"新建文件"行为；
- 需求只在 Markdown：Cmd+Shift+N：新建空白窗口。
- 需求只在 pdf：该会话使用的undo/redo历史。
- 需求只在 pdf：能够作为窗口打开目标的本地Markdown文件、纯文本文件或目录。
- 需求只在 pdf：当前key window。菜单快捷键和文档级命令必须路由到该窗口；隐藏窗口、非key window和系统Panel不得响应。
- 需求只在 pdf：尚未打开文件或目录、未创建待保存Untitled文档的主窗口。空白窗口显示Welcome页面，可以被下一次打开操作复用。
- 需求只在 pdf：内容、脏状态、Untitled状态和保存面板状态；
- 需求只在 pdf：PDF导出目标和进行中状态；
- 需求只在 pdf：File>New Window：创建一个新的空白窗口。
- 需求只在 pdf：File>New File：在当前活动窗口创建Untitled文档，保持现有新建文件语义。
- 需求只在 pdf：快捷键建议：o Cmd+N：保留现有"新建文件"行为；o Cmd+Shift+N：新建空白窗口。
- 需求只在 pdf：应用收到的系统open URL/file事件；

### davidhoo__buddy

段落标题不一致，需求条目 34 / 348 一致（pdf 拆出 318 条）

- 标题只在 Markdown：Buddy 需求文档
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：1.1 目标用户
- 标题只在 Markdown：1.2 核心问题
- 标题只在 Markdown：1.3 产品目标
- 标题只在 pdf：Buddy需求文档
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：1.1目标用户
- 标题只在 pdf：1.2核心问题
- 标题只在 pdf：1.3产品目标
- 需求只在 Markdown：多 Actor 协作难以持续管理：人手动在不同 CLI 之间复制上下文、切换 reviewer、判断是否继续，成本高且容易漏状态。
- 需求只在 Markdown：长任务缺乏可恢复性：CLI 会话、倒计时、轮次、失败原因、输出文件分散，应用重启后难以准确接回。
- 需求只在 Markdown：人工校准窗口不稳定：没有明确的 30 秒决策窗口，用户容易错过"继续 / 修改 / 暂停 / 结束"的节点。
- 需求只在 Markdown：本地工程上下文缺少统一视图：任务状态、对话、文件、diff、终端分散在多个工具里，无法围绕同一 task scope 查看。
- 需求只在 Markdown：Claude + Codex 两个 Actor（不含 OpenCode、Kimi）
- 需求只在 Markdown：三栏 UI 骨架（Sidebar + Chat + 右侧面板），右侧面板仅"运行状态"标签页可用，其余标签页按钮置灰
- 需求只在 Markdown：运行状态标签页采用 Codex App 风格的内嵌漂浮卡：进度 / 输出 / 来源三段式信息层级
- 需求只在 Markdown：任务 CRUD、Runner 状态机、倒计时、打断、双确认结束
- 需求只在 Markdown：buddy-python 数据目录读写兼容
- 需求只在 Markdown：DMG 打包（不含签名公证）
- 需求只在 pdf：多Actor协作难以持续管理：人手动在不同CLI之间复制上下文、切换reviewer、判断是否继续，成本高且容易漏状态。
- 需求只在 pdf：长任务缺乏可恢复性：CLI会话、倒计时、轮次、失败原因、输出文件分散，应用重启后难以准确接回。
- 需求只在 pdf：人工校准窗口不稳定：没有明确的30秒决策窗口，用户容易错过"继续/修改/暂停/结束"的节点。
- 需求只在 pdf：本地工程上下文缺少统一视图：任务状态、对话、文件、diff、终端分散在多个工具里，无法围绕同一task scope查看。
- 需求只在 pdf：Claude + Codex两个Actor（不含OpenCode、Kimi）
- 需求只在 pdf：三栏UI骨架（Sidebar+ Chat +右侧面板），右侧面板仅"运行状态"标签页可用，其余标签页按钮置灰
- 需求只在 pdf：运行状态标签页采用Codex App风格的内嵌漂浮卡：进度/输出/来源三段式信息层级
- 需求只在 pdf：任务CRUD、Runner状态机、倒计时、打断、双确认结束
- 需求只在 pdf：buddy-python数据目录读写兼容
- 需求只在 pdf：DMG打包（不含签名公证）

### davidhoo__jsonpath

段落标题不一致，需求条目 11 / 93 一致（pdf 拆出 55 条）

- 标题只在 Markdown：产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2产品愿景
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：合规性： 实现 RFC 9535 标准定义的全部 JSONPath 语法和语义
- 需求只在 Markdown：正确性： 查询结果与标准一致，边界行为可预测
- 需求只在 Markdown：兼容性： 遵循 Go 语义版本规范，破坏性变更仅在主版本发布
- 需求只在 Markdown：实用性： 保留 keys()、min()、max() 等实用扩展函数
- 需求只在 Markdown：功能：CLI 工具 jp；状态：✅；说明：支持文件/stdin 输入、彩色输出
- 需求只在 Markdown：使用 utf8.RuneCountInString() 替代 len()
- 需求只在 Markdown：仅影响字符串参数，数组/对象的 length 行为不变
- 需求只在 Markdown：length("café") 返回 4（含重音字符）
- 需求只在 Markdown：length([]) 返回 0（数组行为不变）
- 需求只在 Markdown：现有测试全部通过
- 需求只在 pdf：合规性：实现RFC 9535标准定义的全部JSONPath语法和语义
- 需求只在 pdf：正确性：查询结果与标准一致，边界行为可预测
- 需求只在 pdf：兼容性：遵循Go语义版本规范，破坏性变更仅在主版本发布
- 需求只在 pdf：实用性：保留keys()、min()、max()等实用扩展函数
- 需求只在 pdf：CLI工具jp支持文件/stdin输入、彩色输出
- 需求只在 pdf：使用utf8.RuneCountInString()替代len()
- 需求只在 pdf：仅影响字符串参数，数组/对象的length行为不变
- 需求只在 pdf：☐&&优先级高于|| ☐括号可以覆盖默认优先级☐!对复合表达式的求值正确（De Morgan定律）☐RFC 9535测试套件中相关用例通过
- 需求只在 pdf：对字符串应用数组索引→空结果
- 需求只在 pdf：对数字应用字段名选择器→空结果

### dotnet9__Vex

段落标题不一致，需求条目 1 / 6 一致（pdf 拆出 2 条）

- 标题只在 Markdown：Vex 需求文档
- 标题只在 Markdown：1. 产品定位与范围
- 标题只在 Markdown：2. 用户场景
- 标题只在 Markdown：3. 功能需求
- 标题只在 Markdown：Markdown 和表格专项
- 标题只在 pdf：Vex需求文档
- 标题只在 pdf：1.产品定位与范围
- 标题只在 pdf：2.用户场景
- 标题只在 pdf：3.功能需求
- 标题只在 pdf：Markdown和表格专项
- 需求只在 Markdown：编号：FR-01；需求：新建、打开、保存、另存、改名、删除及最近记录；关键验收条件：支持 .md、.markdown、.mdown、.txt；保留实际路径与编码；取消不显示成功；删除明确目标并确认
- 需求只在 Markdown：编号：FR-04；需求：格式工具、查找替换与剪贴板；关键验收条件：常用标题、列表、任务、引用、代码、表格、链接、图片和行内格式；查找支持大小写、整词、正则、计数及循环提示；HTML 粘贴转 Markdown
- 需求只在 Markdown：编号：FR-07；需求：Markdown 渲染与图片；关键验收条件：支持任务、表格、脚注、公式、化学表达、Mermaid 等引擎能力；七项语法可设置；附件使用相对路径时保留目录关系，同名不同内容不覆盖
- 需求只在 Markdown：编号：FR-08；需求：自动保存、恢复草稿与外部冲突保护；关键验收条件：自动保存默认关闭，只写已有文件且磁盘仍为保存基线；草稿可全文预览，恢复为独立未保存文档；失败持续提示并支持重试
- 需求只在 Markdown：代码、长链接、宽表格、复杂公式和图表不能覆盖其他正文或按钮。PDF 正文可选取，图片嵌入及离线读取需要逐格式检查；不能从浏览器预览推导所有导出格式等价。
- 需求只在 pdf：代码、长链接、宽表格、复杂公式和图表不能覆盖其他正文或按钮。PDF正文可选取，图片嵌入及离线读取需要逐格式检查；不能从浏览器预览推导所有导出格式等价。

### dtsola__xiaoyaoprivatebill

段落标题不一致，需求条目 45 / 114 一致（pdf 拆出 66 条）

- 标题只在 Markdown：PRD：小遥账单助手 MVP版本
- 标题只在 Markdown：1. 产品定位（一句话）
- 标题只在 Markdown：2. 用户故事（核心场景）
- 标题只在 Markdown：3. 功能清单（MVP范围）
- 标题只在 Markdown：核心数据功能
- 标题只在 pdf：PRD：小遥账单助手MVP版本
- 标题只在 pdf：1.产品定位（一句话）
- 标题只在 pdf：2.用户故事（核心场景）
- 标题只在 pdf：3.功能清单（MVP范围）
- 标题只在 pdf：4.核心流程图
- 需求只在 Markdown：账单解析与导入：支持上传支付宝(CSV)和微信(XLSX/CSV)账单文件
- 需求只在 Markdown：多文件合并：支持同时上传多个账单文件并合并分析
- 需求只在 Markdown：数据自动识别：自动识别账单来源（支付宝/微信）
- 需求只在 Markdown：数据标准化：将不同平台的账单格式统一处理
- 需求只在 Markdown：会话管理：基于会话的数据处理，30分钟超时自动清理
- 需求只在 Markdown：年度分析：年度消费趋势、收支比例、分类占比
- 需求只在 Markdown：月度分析：月度消费明细、环比变化、趋势图
- 需求只在 Markdown：分类分析：按消费类别的统计、趋势、占比分析
- 需求只在 Markdown：时间分析：每日热力图、时段分布、工作日/周末对比
- 需求只在 Markdown：消费洞察：消费画像、商家分析、习惯识别
- 需求只在 pdf：演示模式☐演示数据生成：内置示例账单数据☐演示模式切换：支持进入/退出演示模式☐演示标识：清晰显示当前为演示模式隐私保护☐本地数据处理：所有分析在服务器端完成，不永久存储☐会话自动清理：会话结束后自动删除所有上传文件☐隐私声明：明确告知用户数据处理方式
- 需求只在 pdf：个性化定制☐自定义分类：用户可创建和编辑消费分类☐分类规则：设置自动分类规则☐预算管理：设置分类预算和提醒高级功能☐AI理财建议：基于消费数据的个性化建议☐目标追踪：储蓄目标进度追踪☐账单对比：不同时期消费对比☐账单合并导入：支持拖拽批量导入平台扩展☐云闪付支持：支持银联云闪付账单☐京东支付支持：支持京东支付账单☐美团支付支持：支持美团支付账单
- 需求只在 pdf：首屏加载：<3秒（不含演示数据）
- 需求只在 pdf：账单解析：<5秒（1000条记录）
- 需求只在 pdf：图表渲染：<1秒（100个数据点）
- 需求只在 pdf：文件上传：支持最大16MB文件
- 需求只在 pdf：分辨率：支持320px - 4K显示器
- 需求只在 pdf：文件编码：支持UTF-8、GBK（支付宝CSV）
- 需求只在 pdf：数据传输：HTTPS加密传输
- 需求只在 pdf：POST/api/upload-上传账单文件

### dtsola__xiaoyaosearch-dingding-export-md

段落标题不一致，需求条目 19 / 65 一致（pdf 拆出 47 条）

- 标题只在 Markdown：PRD：小遥搜索钉钉导出工具 MVP版本
- 标题只在 Markdown：1. 产品定位（一句话）
- 标题只在 Markdown：1.1 产品目标
- 标题只在 Markdown：2. 适用人群
- 标题只在 Markdown：3. 使用场景
- 标题只在 pdf：PRD：小遥搜索钉钉导出工具MVP版本
- 标题只在 pdf：1.产品定位（一句话）
- 标题只在 pdf：1.1产品目标
- 标题只在 pdf：2.适用人群
- 标题只在 pdf：3.使用场景
- 需求只在 Markdown：👨‍💻 知识管理爱好者 - 希望将云端文档备份到本地，防止数据丢失
- 需求只在 Markdown：💼 自由职业者 - 需要将钉钉内容迁移到 Obsidian、Logseq 等本地笔记工具
- 需求只在 Markdown：🏢 创业团队 IT 运维 - 负责企业知识库的定期备份和合规归档
- 需求只在 Markdown：📝 技术文档维护者 - 需要将 API 文档导出到本地进行版本控制
- 需求只在 Markdown：🎓 学生用户 - 在 Windows/macOS 等不同平台上都需要使用
- 需求只在 Markdown：✅ 支持单个文档导出
- 需求只在 Markdown：✅ 支持批量文档导出
- 需求只在 Markdown：✅ 支持文件夹递归导出
- 需求只在 Markdown：✅ 支持完整知识库导出
- 需求只在 Markdown：✅ 多格式转换（.docx/.md/.pdf/.xlsx/.jpg）
- 需求只在 pdf：👨‍💻知识管理爱好者-希望将云端文档备份到本地，防止数据丢失
- 需求只在 pdf：💼自由职业者-需要将钉钉内容迁移到Obsidian、Logseq等本地笔记工具
- 需求只在 pdf：🏢创业团队IT运维-负责企业知识库的定期备份和合规归档
- 需求只在 pdf：📝技术文档维护者-需要将API文档导出到本地进行版本控制
- 需求只在 pdf：🎓学生用户-在Windows/macOS等不同平台上都需要使用
- 需求只在 pdf：✅支持单个文档导出
- 需求只在 pdf：✅支持批量文档导出
- 需求只在 pdf：✅支持文件夹递归导出
- 需求只在 pdf：✅支持完整知识库导出
- 需求只在 pdf：✅多格式转换（.docx/.md/.pdf/.xlsx/.jpg）

### dtsola__xiaoyaosearch-feishu-export-md

段落标题不一致，需求条目 12 / 99 一致（pdf 拆出 37 条）

- 标题只在 Markdown：PRD：小遥搜索飞书导出工具 MVP版本
- 标题只在 Markdown：1. 产品定位（一句话）
- 标题只在 Markdown：2. 用户故事（核心场景）
- 标题只在 Markdown：3. 功能清单（MVP范围）
- 标题只在 Markdown：3.1 配置管理模块
- 标题只在 pdf：PRD：小遥搜索飞书导出工具MVP版本
- 标题只在 pdf：1.产品定位（一句话）
- 标题只在 pdf：2.用户故事（核心场景）
- 标题只在 pdf：3.功能清单（MVP范围）
- 标题只在 pdf：4.核心流程图
- 需求只在 Markdown：交互式引导用户输入飞书App ID和App Secret
- 需求只在 Markdown：生成配置文件 ~/.feishu-export/config.json
- 需求只在 Markdown：验证配置有效性（测试API连接）
- 需求只在 Markdown：配置查看 (feishu-export config get)
- 需求只在 Markdown：显示当前配置信息（脱敏处理）
- 需求只在 Markdown：配置更新 (feishu-export config set)
- 需求只在 Markdown：更新单个配置项
- 需求只在 Markdown：支持重置配置
- 需求只在 Markdown：支持存储多个飞书应用配置
- 需求只在 Markdown：通过 --profile 参数切换
- 需求只在 pdf：1配置管理模块☐配置初始化(feishu-export init) o交互式引导用户输入飞书App ID和App Secret o生成配置文件~/.feishu-export/config.json o验证配置有效性（测试API连接）☐配置查看(feishu-export config get) o显示当前配置信息（脱敏处理）☐配置更新(feishu-export config set) o更新单个配置项o支持重置配置☐多租户支持o支持存储多个飞书应用配置o通过--profile参数切换
- 需求只在 pdf：3知识库导出模块☐完整知识库导出(feishu-export wiki<wiki_id>) o导出整个知识库的目录结构o保留知识库的层级关系o生成索引文件README.md o支持图片/附件下载选项☐单节点导出(feishu-export wiki-node<node_id>) o导出知识库中的单个节点o支持指定导出深度
- 需求只在 pdf：4认证与授权☐飞书开放平台认证o支持App ID + App Secret认证方式o自动获取和管理tenant_access_token o Token自动刷新机制☐权限验证o导出前验证用户对文档的访问权限o友好的权限错误提示
- 需求只在 pdf：5资源处理（可选）☐图片下载（默认启用，可通过--no-images禁用）o自动识别并下载文档中的图片o支持PNG、JPG、JPEG、GIF等格式o处理图片重名冲突（追加序号）o未下载时保留原始URL引用☐附件处理（默认启用，可通过--no-attachments禁用）o下载附件到本地assets/目录o下载时在Markdown中更新为本地链接o未下载时保留附件原始链接
- 需求只在 pdf：6增量导出☐变更检测o记录每次导出的文档元数据（~/.feishu-export/meta.json）o通过文档的updated_at字段判断是否需要更新☐增量导出模式(--incremental) o仅导出有变更的文档o跳过未修改的文档以节省API调用
- 需求只在 pdf：7并发控制☐并发请求配置o支持设置并发数（默认3，最大10）o避免触发API限流☐速率限制o实现令牌桶算法o自动适配飞书API限流策略
- 需求只在 pdf：8进度显示☐命令行进度条o显示当前导出进度（已处理/总数）o显示当前处理速度（文档/秒）o预估剩余时间☐详细日志(--verbose) o显示每个文档的导出状态o显示API请求详情
- 需求只在 pdf：9错误处理☐重试机制o网络错误自动重试（最多3次）o指数退避策略☐断点续传o记录导出进度到中间文件o支持从中断处继续导出
- 需求只在 pdf：☐导出模板定制-支持自定义Markdown导出格式☐多格式支持-支持导出为HTML、PDF格式☐全文搜索-在本地导出的文档中进行全文搜索☐自动更新-CLI工具自动检测新版本
- 需求只在 pdf：-output-o string./output输出目录路径

### entropy-cloud__nop-entropy

段落标题不一致，需求条目 7 / 24 一致（pdf 拆出 29 条）

- 标题只在 Markdown：核心需求
- 标题只在 Markdown：1. 业务目标与范围
- 标题只在 Markdown：2. 用户角色与场景
- 标题只在 Markdown：3. 核心功能需求
- 标题只在 Markdown：4. 非功能性需求
- 需求只在 Markdown：软件功能：AI辅助智能代码生成系统，用户输入需求即可自动生成各种DSL模型文件，用户可以进行局部调整，最后点击生成即可生成一个完整应用 技术背景：单体应用，Java Web应用，面向一般技术人员。
- 需求只在 Markdown：通过模型列表管理第三方模型服务, 具有modelId, provider, modelName, baseUrl, apiKey等属性。
- 需求只在 Markdown：需求编号：FR1.1；需求描述：支持输入方式：自然语言/结构化表单/关键词标签；来源：3.1；类型：功能；优先级：高；验收标准：-
- 需求只在 Markdown：需求编号：FR1.2；需求描述：支持Markdown/Excel文件导入；来源：3.1-Q4；类型：功能；优先级：中；验收标准：-
- 需求只在 Markdown：需求编号：FR1.4；需求描述：支持多AI模型并行生成同一提示词，版本评分（百分制）；来源：3.1-Q5；类型：功能；优先级：中；验收标准：-
- 需求只在 Markdown：需求编号：FR2.1；需求描述：支持生成语言：SQL/Java/JavaScript/XML/YAML/Markdown/自定义DSL；来源：3.2；类型：功能；优先级：高；验收标准：-
- 需求只在 Markdown：需求编号：FR2.4；需求描述：支持分部分生成并自动检查/修正DSL；来源：3.2；类型：功能；优先级：高；验收标准：-
- 需求只在 Markdown：需求编号：NFR3.2；具体指标：支持DSL导出离线编辑（低优先级）；问题/决策：Q17：离线功能优先级低
- 需求只在 Markdown：类别：AI模型扩展；需求编号：IE2；需求描述：支持GPT/Claude/本地模型（REST调用）；问题/决策：Q23：通过后端模型链接调用
- 需求只在 Markdown：类别：降级方案；需求编号：IE4；需求描述：AI失败时支持手动录入/修改DSL（生成新版本）；问题/决策：Q25：任何AI生成内容均可手工编辑
- 需求只在 pdf：软件功能：AI辅助智能代码生成系统，用户输入需求即可自动生成各种DSL模型文件，用户可以进行局部调整，最后点击生成即可生成一个完整应用技术背景：单体应用，Java Web应用，面向一般技术人员。
- 需求只在 pdf：通过模型列表管理第三方模型服务,具有modelId,provider, modelName, baseUrl, apiKey等属性。
- 需求只在 pdf：业务目标与范围
- 需求只在 pdf：AI生成DSL→可视化编辑→应用生成→结果导出/下载SR2--不包含：1.范围边范围版本协作界/用户权限管理、应用部署/移动端支持、团队协作功能
- 需求只在 pdf：用户角色与场景
- 需求只在 pdf：技术工程师快速生成原型应实时预览生成结技术背景需掌握用，通过调整果SQL和JavaScript DSL模型完善数据分析师创建报表模板自然语言需求示无需角色权限，DSL例库底层框架统一处理权限问题需求分析工程师细化原始需求，AI生成结果支持需团队共享功能设计业务用例和重新生成或改进测试用例
- 需求只在 pdf：核心功能需求
- 需求只在 pdf：1智能需求输入
- 需求只在 pdf：FR1.1 3.1-支持输入功能高方式：自然语言/结构化表单/关键词标签
- 需求只在 pdf：FR1.2 3.1-Q4-支持功能中Markdown /Excel文件导入FR1.3 3.1-Q5-多轮需求功能高澄清机制：AI生成初步版本后提供改进按钮FR1.4 3.1-Q5-支持多AI功能中模型并行生成同一提示词，版本评分（百分制）

### fanfan-de__anybox

段落标题不一致，需求条目 49 / 109 一致（pdf 拆出 108 条）

- 标题只在 Markdown：Anybox 计划模块产品需求（PRD）
- 标题只在 Markdown：1. 产品结论
- 标题只在 Markdown：2. 产品目标
- 标题只在 Markdown：3. 非目标
- 标题只在 Markdown：4. 核心用户场景
- 标题只在 pdf：Anybox计划模块产品需求（PRD）
- 标题只在 pdf：1.产品结论
- 标题只在 pdf：2.产品目标
- 标题只在 pdf：3.非目标
- 标题只在 pdf：4.核心用户场景
- 需求只在 Markdown：等待用户确认的 Agent 建议。
- 需求只在 Markdown：将明确、重复的执行要求转为 Automation。
- 需求只在 Markdown：待确认：Agent 计划建议与需要用户决定的变更。
- 需求只在 Markdown：项目：真实 Project 下的任务集合。
- 需求只在 Markdown：Agent 建议、委托与执行记录。
- 需求只在 Markdown：Automation 关联与活动记录。
- 需求只在 Markdown：延续 Anybox 成熟、安静、克制的桌面生产力风格。
- 需求只在 Markdown：使用 Activity Rail、侧栏、主工作区、右侧检查器的既有工作台结构。
- 需求只在 Markdown：默认采用紧凑行、工具栏和面板，不把页面设计成营销式 Dashboard 或多层卡片集合。
- 需求只在 Markdown：所有图标按钮使用真实 button、可见焦点态和 tooltip；图标统一使用现有 Lucide 体系。
- 需求只在 pdf：等待用户确认的Agent建议。
- 需求只在 pdf：将明确、重复的执行要求转为Automation。
- 需求只在 pdf：待确认：Agent计划建议与需要用户决定的变更。
- 需求只在 pdf：项目：真实Project下的任务集合。
- 需求只在 pdf：Agent建议、委托与执行记录。
- 需求只在 pdf：Automation关联与活动记录。
- 需求只在 pdf：延续Anybox成熟、安静、克制的桌面生产力风格。
- 需求只在 pdf：使用Activity Rail、侧栏、主工作区、右侧检查器的既有工作台结构。
- 需求只在 pdf：默认采用紧凑行、工具栏和面板，不把页面设计成营销式Dashboard或多层卡片集合。
- 需求只在 pdf：所有图标按钮使用真实button、可见焦点态和tooltip；图标统一使用现有Lucide体系。

### flycalm__md-reader-miniprogram

段落标题不一致，需求条目 67 / 158 一致（pdf 拆出 124 条）

- 标题只在 Markdown：MD 阅读器小程序 PRD
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：2. 背景与问题
- 标题只在 Markdown：3. 产品目标
- 标题只在 Markdown：3.1 MVP 目标
- 标题只在 pdf：MD阅读器小程序PRD
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：2.背景与问题
- 标题只在 pdf：3.产品目标
- 标题只在 pdf：3.1 MVP目标
- 需求只在 Markdown：小程序需在 app.json 的 supportedMaterials 中声明 text/markdown。
- 需求只在 Markdown：从聊天素材打开时，启动场景值为 1173，文件信息由 forwardMaterials 提供。
- 需求只在 Markdown："自动打开"或"设为微信默认 Markdown 应用"不属于小程序可控制能力。
- 需求只在 Markdown：体验版和正式版的 supportedMaterials 配置相互独立，需要分别验证。
- 需求只在 Markdown：小程序声明支持 text/markdown，打开文案暂定为"用 MD 阅读器阅读"。
- 需求只在 Markdown：小程序启动或重新唤起时检查场景值和 forwardMaterials。
- 需求只在 Markdown：接收到多个素材时，仅处理第一个合法 Markdown 文件，并提示其余文件暂未打开。
- 需求只在 Markdown：体验版可通过场景值 1173 完成模拟调试。
- 需求只在 Markdown：iOS 和 Android 微信中均能从聊天文件进入正确阅读页。
- 需求只在 Markdown：选择非 .md 文件时拒绝读取，并说明当前仅支持 Markdown。
- 需求只在 pdf：小程序需在app.json的supportedMaterials中声明text/markdown。
- 需求只在 pdf：从聊天素材打开时，启动场景值为1173，文件信息由forwardMaterials提供。
- 需求只在 pdf："自动打开"或"设为微信默认Markdown应用"不属于小程序可控制能力。
- 需求只在 pdf：体验版和正式版的supportedMaterials配置相互独立，需要分别验证。
- 需求只在 pdf：小程序声明支持text/markdown，打开文案暂定为"用MD阅读器阅读"。
- 需求只在 pdf：小程序启动或重新唤起时检查场景值和forwardMaterials。
- 需求只在 pdf：接收到多个素材时，仅处理第一个合法Markdown文件，并提示其余文件暂未打开。
- 需求只在 pdf：体验版可通过场景值1173完成模拟调试。
- 需求只在 pdf：iOS和Android微信中均能从聊天文件进入正确阅读页。
- 需求只在 pdf：选择非.md文件时拒绝读取，并说明当前仅支持Markdown。

### gitxuzhefeng__timelines

段落标题不一致，需求条目 25 / 127 一致（pdf 拆出 149 条）

- 标题只在 Markdown：一期迭代：核心闭环与单机可用 (MVP)
- 标题只在 Markdown：二期迭代：多模态 AI 深度赋能与智能洞察 (V1.0)
- 标题只在 Markdown：三期迭代：全平台协同与探索商业化团队版 (V2.0)
- 标题只在 Markdown：1. 创建 Tauri 项目
- 标题只在 Markdown：2. 进入目录
- 标题只在 pdf：今天记录：09:00 VSCode - main.ts 09:30 Chrome - GitHub Pull Request 10:00 Zoom - Team Standup 10:30 Slack - #general ...
- 标题只在 pdf：一期迭代：核心闭环与单机可用(MVP)
- 标题只在 pdf：二期迭代：多模态AI深度赋能与智能洞察(V1.0)
- 标题只在 pdf：三期迭代：全平台协同与探索商业化团队版(V2.0)
- 标题只在 pdf：1.创建Tauri项目
- 需求只在 Markdown：无感记录 - 后台自动追踪，无需手动操作
- 需求只在 Markdown：AI 分类 - 自动识别活动类型（编程/开会/文档/摸鱼）
- 需求只在 Markdown：每日洞察 - 每天知道自己时间都去哪了
- 需求只在 Markdown：飞书集成 - 每日报告直接推送到飞书
- 需求只在 Markdown：数据采集（客户端） 功能 描述 优先级 窗口追踪 记录活跃窗口/应用名称 P0 时间分块 自动识别连续工作段 P0 键盘/鼠标活动 检测是否在活跃使用电脑 P1 关键截屏 检测任务切换时轻量截屏（可关闭） P2 隐私过滤 自动跳过密码/银行等敏感页面 P1
- 需求只在 Markdown：AI 分析 功能 描述 优先级 活动分类 AI 自动归类：Coding/开会/写文档/刷网页/摸鱼 P0 时间占比统计 每个类别占用时间及百分比 P0 模式识别 识别高效时段、周期模式 P1 异常检测 检测异常长时间消耗 P1 意图猜测 对不确定的活动请用户确认 P1
- 需求只在 Markdown：每日报告 功能 描述 优先级 飞书推送 每天固定时间推送报告到飞书 P0 时间线视图 可视化一天的时间分布 P0 生产力评分 基于活动类型计算分数 P1 对比分析 与昨天/上周对比 P2 用户补充 用户可修正 AI 分类 P1
- 需求只在 Markdown：设置中心 功能 描述 优先级 追踪开关 随时开启/暂停追踪 P0 截屏开关 可关闭截屏功能 P1 敏感应用 用户指定不追踪的应用 P1 推送时间 设置每日报告推送时间 P1 数据存储 本地/云端选择 P2
- 需求只在 Markdown：窗口追踪：使用 platform crate 获取活跃窗口
- 需求只在 Markdown：数据存储：本地 SQLite + 加密
- 需求只在 pdf：无感记录-后台自动追踪，无需手动操作
- 需求只在 pdf：AI分类-自动识别活动类型（编程/开会/文档/摸鱼）
- 需求只在 pdf：每日洞察-每天知道自己时间都去哪了
- 需求只在 pdf：飞书集成-每日报告直接推送到飞书
- 需求只在 pdf：数据采集（客户端）功能描述优先级窗口追踪记录活跃窗口/应用名称P0时间分块自动识别连续工作段P0键盘/鼠标活动检测是否在活跃使用电脑P1关键截屏检测任务切换时轻量截屏（可关闭）P2隐私过滤自动跳过密码/银行等敏感页面P1
- 需求只在 pdf：AI分析功能描述优先级活动分类AI自动归类：Coding/开会/写文档/刷网页/摸鱼P0时间占比统计每个类别占用时间及百分比P0模式识别识别高效时段、周期模式P1异常检测检测异常长时间消耗P1意图猜测对不确定的活动请用户确认P1
- 需求只在 pdf：每日报告功能描述优先级飞书推送每天固定时间推送报告到飞书P0时间线视图可视化一天的时间分布P0生产力评分基于活动类型计算分数P1对比分析与昨天/上周对比P2用户补充用户可修正AI分类P1
- 需求只在 pdf：设置中心功能描述优先级追踪开关随时开启/暂停追踪P0截屏开关可关闭截屏功能P1敏感应用用户指定不追踪的应用P1推送时间设置每日报告推送时间P1数据存储本地/云端选择P2
- 需求只在 pdf：窗口追踪：使用platform crate获取活跃窗口
- 需求只在 pdf：数据存储：本地SQLite +加密

### grapeot__opencode_android_client

段落标题不一致，需求条目 5 / 112 一致（pdf 拆出 105 条）

- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：1.1 它不是什么
- 标题只在 Markdown：1.2 核心交互范式
- 标题只在 Markdown：Steer 范式
- 标题只在 Markdown：Markdown 作为交互窗口
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：1.1它不是什么
- 标题只在 pdf：1.2核心交互范式
- 标题只在 pdf：1.3与iOS Client的关系
- 标题只在 pdf：1.4核心能力总览
- 需求只在 Markdown：OpenCode Android Client 是 OpenCode AI 编程助手的原生 Android 客户端，让开发者可以在手机/平板上远程监控 AI 工作进度、发送指令、审查代码变更。
- 需求只在 Markdown：OpenCode Android Client 是一个面向 OpenCode 服务端的原生 Android 远程控制应用。它不是一个独立的 AI 编程工具，而是运行在 Mac/Server 上的 OpenCode 实例的移动端延伸——让用户可以在沙发上、通勤中或任何远离电脑的场景下，发送指令、监控 AI 工作进度、浏览 Markdown 报告、切换模型。
- 需求只在 Markdown：Surface——AI 通过 Markdown 窗口向人类展示它正在做的决策、读到的代码、跑过的命令、分析和结论。文本是自然语言 Markdown，可以嵌入截图（如部署结果、图表、UI diff），而不是纯代码。这是 AI 与人之间的主要信息通道。
- 需求只在 Markdown：Review——人类阅读 Markdown，审查看法对不对、方向偏不偏。大多数内容是文档、分析、调研，天然适合 Markdown 呈现；偶尔需要看代码 diff 确认细节。人类在这个环节是在做判断，不是在写代码。
- 需求只在 Markdown：Steer——发现方向偏了，通过语音快速下达纠偏指令（"停，不要用继承，换成组合模式"），或者切换模型/Agent 重新开始。指令以自然语言下达，不需要打字。
- 需求只在 Markdown：这个循环在两端都是异步的：AI 在电脑上跑，人类在手机上审。两边的节奏不需要同步——这是移动端相对于桌面端的独特优势。但也因此引入了一个真实痛点：当 AI 停下来等人类决定时（如 question tool），人类目前收不到任何通知，双方都在空转。这个问题的解决方案不在 UX 设计层面，而在 Android 工程层面——需要前台服务（Foreground Service）配合通知（Notification）或持续通知来主动触达用户。
- 需求只在 Markdown：不强调代码语法高亮，强调 Markdown 渲染质量（标题层级、列表、链接、代码块、图片嵌入）。用户要审的是 AI 的思考过程和产出物，不是代码的美学。
- 需求只在 Markdown：完善的图片嵌入支持：AI 可以截取部署结果的截图、生成图表、拍摄 UI 对比图，嵌入 Markdown 报告中。App 有专门的 Skill 体系教 AI 如何使用这些能力。
- 需求只在 Markdown：内容形态不限于编程：AI 产出的可以是代码 diff，也可以是调研文章、分析报告、系统设计文档。Markdown 天然兼容所有这些形态。
- 需求只在 Markdown：文件浏览的核心不是"在手机上写代码"，而是快速确认 AI 的改动。用户绝大部分情况下通过 Chat 窗口中的 tool/patch 卡片直接跳转到文件预览——Files Tab 是一个兜底入口，不是主工作流。当用户在 Chat 里看到 edit_file 卡片，点一下卡片上的文件路径就进入预览，不需要切到 Files Tab 去翻目录树。
- 需求只在 pdf：OpenCode Android Client是OpenCode AI编程助手的原生Android客户端，让开发者可以在手机/平板上远程监控AI工作进度、发送指令、审查代码变更。
- 需求只在 pdf：OpenCode Android Client是一个面向OpenCode服务端的原生Android远程控制应用。它不是一个独立的AI编程工具，而是运行在Mac/Server上的OpenCode实例的移动端延伸——让用户可以在沙发上、通勤中或任何远离电脑的场景下，发送指令、监控AI工作进度、浏览Markdown报告、切换模型。
- 需求只在 pdf：Surface——AI通过Markdown窗口向人类展示它正在做的决策、读到的代码、跑过的命令、分析和结论。文本是自然语言Markdown，可以嵌入截图（如部署结果、图表、UI diff），而不是纯代码。这是AI与人之间的主要信息通道。
- 需求只在 pdf：Review——人类阅读Markdown，审查看法对不对、方向偏不偏。大多数内容是文档、分析、调研，天然适合Markdown呈现；偶尔需要看代码diff确认细节。人类在这个环节是在做判断，不是在写代码。
- 需求只在 pdf：Steer——发现方向偏了，通过语音快速下达纠偏指令（"停，不要用继承，换成组合模式"），或者切换模型/Agent重新开始。指令以自然语言下达，不需要打字。
- 需求只在 pdf：这个循环在两端都是异步的：AI在电脑上跑，人类在手机上审。两边的节奏不需要同步——这是移动端相对于桌面端的独特优势。但也因此引入了一个真实痛点：当AI停下来等人类决定时（如question tool），人类目前收不到任何通知，双方都在空转。这个问题的解决方案不在UX设计层面，而在Android工程层面——需要前台服务（Foreground Service）配合通知（Notification）或持续通知来主动触达用户。
- 需求只在 pdf：不强调代码语法高亮，强调Markdown渲染质量（标题层级、列表、链接、代码块、图片嵌入）。用户要审的是AI的思考过程和产出物，不是代码的美学。
- 需求只在 pdf：完善的图片嵌入支持：AI可以截取部署结果的截图、生成图表、拍摄UI对比图，嵌入Markdown报告中。App有专门的Skill体系教AI如何使用这些能力。
- 需求只在 pdf：内容形态不限于编程：AI产出的可以是代码diff，也可以是调研文章、分析报告、系统设计文档。Markdown天然兼容所有这些形态。文件卡片预览（非代码编辑器）
- 需求只在 pdf：文件浏览的核心不是"在手机上写代码"，而是快速确认AI的改动。用户绝大部分情况下通过Chat窗口中的tool/patch卡片直接跳转到文件预览——Files Tab是一个兜底入口，不是主工作流。当用户在Chat里看到edit_file卡片，点一下卡片上的文件路径就进入预览，不需要切到Files Tab去翻目录树。

### guobin211__local-db

段落标题不一致，需求条目 103 / 147 一致（pdf 拆出 142 条）

- 标题只在 Markdown：local-db 客户端需求说明
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心特性
- 标题只在 Markdown：1.3 技术架构
- 标题只在 Markdown：2.1 数据库下载安装
- 标题只在 pdf：local-db客户端需求说明
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2核心特性
- 标题只在 pdf：1.3技术架构
- 标题只在 pdf：2.1数据库下载安装
- 需求只在 Markdown：local-db 是一个跨平台的数据库管理工具，旨在简化本地开发环境中多种数据库的安装、配置和管理流程。通过提供统一的图形化界面，让开发者能够快速搭建和管理本地数据库环境。
- 需求只在 Markdown：前端技术栈：React + TypeScript + TailwindCSS + Zustand
- 需求只在 Markdown：数据持久化：Tauri Store 插件
- 需求只在 Markdown：限制：每种数据库类型最多只能安装 1 个实例
- 需求只在 Markdown：数据库图标和名称
- 需求只在 Markdown：运行状态（运行中/已停止）
- 需求只在 Markdown：快捷操作按钮（启动/停止/重启/删除）
- 需求只在 Markdown：已安装的数据库类型显示为禁用状态（每种数据库最多 1 个实例）
- 需求只在 Markdown：用户名密码（如适用）
- 需求只在 Markdown：名称、版本、类型
- 需求只在 pdf：local-db是一个跨平台的数据库管理工具，旨在简化本地开发环境中多种数据库的安装、配置和管理流程。通过提供统一的图形化界面，让开发者能够快速搭建和管理本地数据库环境。
- 需求只在 pdf：前端技术栈：React+ TypeScript + TailwindCSS + Zustand
- 需求只在 pdf：数据持久化：Tauri Store插件
- 需求只在 pdf：限制：每种数据库类型最多只能安装1个实例
- 需求只在 pdf：2.1数据库列表页面
- 需求只在 pdf：每个数据库卡片显示：o数据库图标和名称o版本号o运行状态（运行中/已停止）o端口号o快捷操作按钮（启动/停止/重启/删除）
- 需求只在 pdf：2.2数据库安装页面
- 需求只在 pdf：已安装的数据库类型显示为禁用状态（每种数据库最多1个实例）
- 需求只在 pdf：配置安装参数：o安装路径o数据目录o日志目录o默认端口o用户名密码（如适用）
- 需求只在 pdf：2.3数据库详情页面

### gwwen05__CodeCompass

段落标题不一致，需求条目 34 / 106 一致（pdf 拆出 105 条）

- 标题只在 Markdown：1. 产品概述 / Product Overview
- 标题只在 Markdown：2. 用户画像 / User Personas
- 标题只在 Markdown：P1: 小王 — Java 初学者
- 标题只在 Markdown：P2: 老李 — Java 后端开发
- 标题只在 Markdown：P3: 小陈 — 企业新人
- 标题只在 pdf：1.产品概述/ Product Overview
- 标题只在 pdf：2.用户画像/ User Personas
- 标题只在 pdf：P1:小王—Java初学者
- 标题只在 pdf：P2:老李—Java后端开发
- 标题只在 pdf：P3:小陈—企业新人
- 需求只在 Markdown：调用链不透明：IDE 只能看单步跳转，难以理解完整的调用链路
- 需求只在 Markdown：CodeCompass 通过 AI Agent 自动分析代码库，将代码转化为可查询的知识图谱，让开发者可以像对话一样理解代码。
- 需求只在 Markdown：年龄: 22，应届毕业生
- 需求只在 Markdown：技能: 基础 Java，Spring Boot 基础，无生产级项目经验
- 需求只在 Markdown：痛点: 第一次面对真实项目代码，不知道从哪开始
- 需求只在 Markdown：目标: 理解项目结构，从真实代码中学习
- 需求只在 Markdown：使用频率: 每天使用，作为学习工具
- 需求只在 Markdown：年龄: 30，5 年以上经验
- 需求只在 Markdown：技能: 精通 Java，Spring 生态，微服务
- 需求只在 Markdown：痛点: 加入新团队/新项目，需要快速理解大型代码库
- 需求只在 pdf：调用链不透明：IDE只能看单步跳转，难以理解完整的调用链路
- 需求只在 pdf：CodeCompass通过AI Agent自动分析代码库，将代码转化为可查询的知识图谱，让开发者可以像对话一样理解代码。
- 需求只在 pdf：年龄:22，应届毕业生
- 需求只在 pdf：技能:基础Java，Spring Boot基础，无生产级项目经验
- 需求只在 pdf：痛点:第一次面对真实项目代码，不知道从哪开始
- 需求只在 pdf：目标:理解项目结构，从真实代码中学习
- 需求只在 pdf：使用频率:每天使用，作为学习工具
- 需求只在 pdf：年龄:30，5年以上经验
- 需求只在 pdf：技能:精通Java，Spring生态，微服务
- 需求只在 pdf：痛点:加入新团队/新项目，需要快速理解大型代码库

### hackmagic__opennavicat

段落标题不一致，需求条目 18 / 122 一致（pdf 拆出 34 条）

- 标题只在 Markdown：OpenNavicat 补足需求文档（对标 DBX）
- 标题只在 Markdown：0. 文档说明
- 标题只在 Markdown：0.0 对标基线与修订记录
- 标题只在 Markdown：0.1 目标
- 标题只在 Markdown：0.2 非目标
- 标题只在 pdf：OpenNavicat补足需求文档（对标DBX）
- 标题只在 pdf：0.文档说明
- 标题只在 pdf：0.0对标基线与修订记录
- 标题只在 pdf：0.1目标
- 标题只在 pdf：0.2非目标
- 需求只在 Markdown：向后兼容：除非明确说明，不得破坏现有 CLI/GUI 行为。
- 需求只在 Markdown：现有 CLI、GUI 主流程仍可用。
- 需求只在 Markdown：核心模块之间不出现反向依赖 —— docs/module_dependency_matrix.md（scripts/build_dependency_matrix.py 自动生成），261 条顶层导入边、0 违规（2026-10-06，含 ClickHouse / Oracle 驱动与 Phase 6 流水线）（2026-09-30，含 ClickHouse / Oracle 驱动）。
- 需求只在 Markdown：至少 1 个连接器迁移到新分层 —— 全部 9 个 connector 现居 open_navicat/drivers/，dal/base_connector.py 与 dal/*_connector.py 保留兼容 shim。
- 需求只在 Markdown：已落地的新模块有模块说明 —— open_navicat/drivers/README.md（职责表、接入新引擎的两步流程、package 必填 / super().init() / 单线程 executor 桥接等约定与坑）。types / sql / formats / platform 尚未成模块，待各自 Phase 落地时补。
- 需求只在 Markdown：至少 1 个 CLI 命令、1 个 GUI 调用路径迁移到新分层 —— CLI：conn engines|add|test|open 全走注册表 + dsn.py；GUI：connection_dialog.py 的引擎下拉框 / 端口默认值 / 测试错误展示改走 drivers.registry 与 drivers.dsn。
- 需求只在 Markdown：新增模块的单元测试覆盖率不低于项目当前基线（基线：289 passed / 16 skipped，装 pytest-asyncio 前是 243/62；当前 556 passed）。
- 需求只在 Markdown：连接失败、超时、SQL 错误、AI 错误均使用统一错误对象（open_navicat/errors.py）；插件错误 ONV-PLG-001 已定义，待 Phase 8 接入。
- 需求只在 Markdown：CLI 展示结构化错误（conn add --test / conn test）；GUI 连接对话框"测试连接"失败时展示 NavicatError.render()（错误码 + 脱敏说明）。
- 需求只在 Markdown：错误码保持稳定，不复用、不改义（ONV-<域>-<序号>，见 ERROR_CATALOG 常量表）。
- 需求只在 pdf：向后兼容：除非明确说明，不得破坏现有CLI/GUI行为。
- 需求只在 pdf：实现要点（踩坑记录）：查询与取消触发器要用asyncio.wait(FIRST_COMPLETED)显式竞速。不要用"嵌套ensure_future+直接await协程"——外层Task.cancel()会卡在内层任务后面，取消永远传不下去，run_until_complete死等。后台查询也必须走同一个CancelToken。
- 需求只在 pdf：☐提供MCP Server原型。☐至少包含以下工具：o list connections o list databases o describe table o execute query o open session o execute redis command ☐支持只读/安全写/高风险写三种策略。☐写操作支持确认或dry-run。☐AI结果包含可追踪的上下文来源。☐AI调用链路与本地CLI / GUI解耦，可独立测试。
- 需求只在 pdf：插件ID /版本/权限
- 需求只在 pdf：UI容器（如后续支持）
- 需求只在 pdf：☐支持插件发现与加载。☐支持插件卸载与禁用。☐支持插件权限声明。☐支持签名校验。☐支持至少1个外部插件示例。☐支持插件依赖冲突检测。☐定义插件包格式与manifest schema（参考DBX manifest v1，但不必照抄）。☐支持插件日志与错误上报。
- 需求只在 pdf：☐凭据加密存储。☐支持密钥迁移。☐支持敏感字段脱敏。☐支持审计日志记录关键操作。☐支持失败操作的恢复策略。☐支持安全提示和确认。☐支持离线或受控环境部署时的安全降级说明。
- 需求只在 pdf：让OpenNavicat支持更多运行形态。
- 需求只在 pdf：☐支持CLI standalone。☐支持GUI standalone。☐支持Docker / Web形态。☐支持MCP形态。☐支持自动更新。☐支持签名校验和完整性检查。☐支持常见包管理渠道接入（brew/ scoop / winget /flatpak）。☐CLI独立包不依赖Qt，体积< 30 MB。☐给出GUI体积削减方案与实测数据（Nuitka/ Qt模块裁剪）。
- 需求只在 pdf：统一错误模型✅open_navicat/errors.py

### hexianWeb__Third-Person-MC

段落标题不一致，需求条目 2 / 40 一致（pdf 拆出 23 条）

- 标题只在 Markdown：PRD —— Third-Person-MC 体素世界引擎（v3.0）
- 标题只在 Markdown：1. 产品概述与目标
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心体验流程
- 标题只在 Markdown：1.3 在线预览
- 标题只在 pdf：PRD —— Third-Person-MC体素世界引擎（v3.0）
- 标题只在 pdf：1.产品概述与目标
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2核心体验流程
- 标题只在 pdf：1.3在线预览
- 需求只在 Markdown：属性：数据持久化；规格：支持 Chunk 数据缓存
- 需求只在 Markdown：Chunk 动态加载/卸载正常工作
- 需求只在 Markdown：相同 Seed 生成一致的地形
- 需求只在 Markdown：多生态平滑过渡
- 需求只在 Markdown：地形振幅与 FBM 参数可调节
- 需求只在 Markdown：Chunk 随机事件系统实现
- 需求只在 Markdown：操作：普通攻击；按键：Z；说明：支持连击 Combo
- 需求只在 Markdown：功能：越肩切换；规格：支持左/右肩视角平滑过渡
- 需求只在 Markdown：角色移动流畅，动画衔接自然
- 需求只在 Markdown：相机跟随不穿透地形
- 需求只在 pdf：1.1 Chunk管理属性规格Chunk尺寸16 × 16 × 64方块动态加载基于玩家位置动态加载/卸载Chunk渲染距离可调节，默认8 Chunks数据持久化支持Chunk数据缓存
- 需求只在 pdf：1.2地形生成属性规格Perlin Noise + FBM噪声算法种子系统相同Seed生成相同世界地形振幅可调节高度变化幅度地面细节FBM控制表面侵蚀细节
- 需求只在 pdf：1.3生态系统（Biome）生态类型特征平原广阔草地，稀疏树木森林橡树为主，密集植被白桦林白桦树群落樱花林粉色樱花树沙漠沙地，仙人掌冻洋冰雪地形
- 需求只在 pdf：1.4 Chunk随机事件（新功能）
- 需求只在 pdf：1.5验收标准☒Chunk动态加载/卸载正常工作☒相同Seed生成一致的地形☒多生态平滑过渡☒地形振幅与FBM参数可调节☐Chunk随机事件系统实现
- 需求只在 pdf：2.1运动系统操作按键说明
- 需求只在 pdf：普通攻击支持连击Combo
- 需求只在 pdf：2.2相机系统功能规格相机类型第三人称跟随避障系统自动检测地形，防止穿模视角旋转鼠标控制，360°自由旋转越肩切换支持左/右肩视角平滑过渡
- 需求只在 pdf：2.3验收标准☒角色移动流畅，动画衔接自然☒相机跟随不穿透地形☒攻击Combo连击正常☒越肩切换动画平滑
- 需求只在 pdf：3.1游戏内HUD组件位置功能血量条屏幕下方显示玩家当前血量饥饿条屏幕下方显示饥饿值经验条屏幕下方显示经验进度快捷栏屏幕下方物品快捷栏（装饰性）坐标显示左上角显示玩家世界坐标指南针右上角方向指示信息面板右上角FPS、时间、天数等按键提示左下角实时按键反馈组件位置功能聊天框左下角聊天/命令输入准星屏幕中央瞄准指示小地图右下角周围地形预览

### iflytek__skillhub

段落标题不一致，需求条目 62 / 119 一致（pdf 拆出 115 条）

- 标题只在 Markdown：技能详情与审核页文件浏览侧边栏 - 产品需求文档 (PRD)
- 标题只在 Markdown：技能详情页
- 标题只在 Markdown：审核详情页
- 标题只在 Markdown：桌面端
- 标题只在 Markdown：移动端
- 标题只在 pdf：技能详情与审核页文件浏览侧边栏-产品需求文档(PRD)
- 标题只在 pdf：Phase 1:共享模型与交互方案落地
- 标题只在 pdf：Phase 2:技能详情页集成
- 标题只在 pdf：Phase 3:审核页能力补齐
- 标题只在 pdf：Phase 4:回归与体验完善
- 需求只在 Markdown：平铺文件列表无法反映目录层级，用户难以理解 skill 包结构。
- 需求只在 Markdown：审核人员在审核页中无法点开任意文件验证实现内容，只能依赖 README 或下载压缩包离线查看。
- 需求只在 Markdown：现有三个 Tab 的主体内容已经承担不同职责，若继续把文件浏览塞入当前"文件"Tab，会使"概览"与"版本"场景下的跨文件查看成本偏高。
- 需求只在 Markdown：用统一的侧边文件浏览体验取代当前平铺文件列表，降低理解 skill 包结构的成本。
- 需求只在 Markdown：保持现有三个 Tab 的主语义不变，同时让用户在任意 Tab 下都能快速查看文件内容。
- 需求只在 Markdown：将现有平铺 files 列表重构为目录树，支持文件夹展开 / 合并。
- 需求只在 Markdown：支持 Markdown 文档渲染、常见文本文件源码预览，以及大文件 / 不支持文件类型的不可预览提示。
- 需求只在 Markdown：对 JSON / YAML / TS / JS 等文本文件提供更完整的语法高亮能力。
- 需求只在 Markdown：用户进入技能详情页，默认看到"概览 / 文件 / 版本"三个 Tab。
- 需求只在 Markdown：无论当前停留在哪个 Tab，页面都显示文件浏览侧边栏。
- 需求只在 pdf：平铺文件列表无法反映目录层级，用户难以理解skill包结构。
- 需求只在 pdf：审核人员在审核页中无法点开任意文件验证实现内容，只能依赖README或下载压缩包离线查看。
- 需求只在 pdf：现有三个Tab的主体内容已经承担不同职责，若继续把文件浏览塞入当前"文件"Tab，会使"概览"与"版本"场景下的跨文件查看成本偏高。
- 需求只在 pdf：用统一的侧边文件浏览体验取代当前平铺文件列表，降低理解skill包结构的成本。
- 需求只在 pdf：保持现有三个Tab的主语义不变，同时让用户在任意Tab下都能快速查看文件内容。
- 需求只在 pdf：将现有平铺files列表重构为目录树，支持文件夹展开/合并。
- 需求只在 pdf：支持Markdown文档渲染、常见文本文件源码预览，以及大文件/不支持文件类型的不可预览提示。
- 需求只在 pdf：对JSON / YAML / TS / JS等文本文件提供更完整的语法高亮能力。
- 需求只在 pdf：用户进入技能详情页，默认看到"概览/文件/版本"三个Tab。
- 需求只在 pdf：无论当前停留在哪个Tab，页面都显示文件浏览侧边栏。

### jaylinwang__zen

段落标题不一致，需求条目 40 / 72 一致（pdf 拆出 72 条）

- 标题只在 Markdown：禅 产品需求文档
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：2. 已确认需求与建议默认值
- 标题只在 Markdown：3. 目标与范围
- 标题只在 Markdown：4. 用户流程
- 标题只在 pdf：禅产品需求文档
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：2.已确认需求与建议默认值
- 标题只在 pdf：3.目标与范围
- 标题只在 pdf：4.用户流程
- 需求只在 Markdown：「禅」是一款面向个人自用、覆盖 Mac 与 iPhone 的独立应用，专注于轻量计时与本地时间记录。用户可以不填写任务直接开始专注，在结束后补记这段时间做了什么。记录保存为独立目录中的可读文件，方便日后由用户或 AI 检索、整理和回顾。
- 需求只在 Markdown：当前只考虑 Mac 与 iPhone，暂不考虑 Apple Watch。开始与主动放弃的操作必须方便；两端具体交付顺序待确认。
- 需求只在 Markdown：采用本地文件存储，Mac 与 iPhone 之间的文件同步由用户自行寻找方案并管理；App 不提供内置云同步或云后端。
- 需求只在 Markdown：文件应方便用户和 AI 后续维护与回顾。
- 需求只在 Markdown：应用名称为「禅」，使用 zen 作为项目名称和项目目录名。
- 需求只在 Markdown：支持专注声音定制，木鱼使用真实器物敲击录音，保留自然音色与余音。默认每 2 秒一声，支持音量和敲击间隔调整；声音内置，离线可用。陪伴声音单选：静音、木鱼、松风、细雨。有声选项在专注期间循环播放，提供统一音量和试听，不做混音。磬声仅用于结束提醒，不属于陪伴声音，也不在开始时播放。结束统一敲磬提醒，提醒音量独立于背景声（默认 65%），在每轮开始时固定。
- 需求只在 Markdown：Mac 端采用原生菜单栏应用，支持全局快捷键；两端的建议分工见第 3 节。
- 需求只在 Markdown：专注默认 25 分钟，休息默认 5 分钟；休息与下一轮均手动开始。
- 需求只在 Markdown：建议每次专注一个 Markdown 文件，以稳定会话 ID 命名，界面按日展示；减少两端新增记录时改写同一文件的机会。
- 需求只在 Markdown：Mac 与 iPhone 采用相同的可读文件格式。用户自行选择外部工具同步文件，或自行复制文件。
- 需求只在 pdf：「禅」是一款面向个人自用、覆盖Mac与iPhone的独立应用，专注于轻量计时与本地时间记录。用户可以不填写任务直接开始专注，在结束后补记这段时间做了什么。记录保存为独立目录中的可读文件，方便日后由用户或AI检索、整理和回顾。
- 需求只在 pdf：当前只考虑Mac与iPhone，暂不考虑Apple Watch。开始与主动放弃的操作必须方便；两端具体交付顺序待确认。
- 需求只在 pdf：采用本地文件存储，Mac与iPhone之间的文件同步由用户自行寻找方案并管理；App不提供内置云同步或云后端。
- 需求只在 pdf：文件应方便用户和AI后续维护与回顾。
- 需求只在 pdf：应用名称为「禅」，使用zen作为项目名称和项目目录名。
- 需求只在 pdf：支持专注声音定制，木鱼使用真实器物敲击录音，保留自然音色与余音。默认每2秒一声，支持音量和敲击间隔调整；声音内置，离线可用。陪伴声音单选：静音、木鱼、松风、细雨。有声选项在专注期间循环播放，提供统一音量和试听，不做混音。磬声仅用于结束提醒，不属于陪伴声音，也不在开始时播放。结束统一敲磬提醒，提醒音量独立于背景声（默认65%），在每轮开始时固定。
- 需求只在 pdf：Mac端采用原生菜单栏应用，支持全局快捷键；两端的建议分工见第3节。
- 需求只在 pdf：专注默认25分钟，休息默认5分钟；休息与下一轮均手动开始。
- 需求只在 pdf：建议每次专注一个Markdown文件，以稳定会话ID命名，界面按日展示；减少两端新增记录时改写同一文件的机会。
- 需求只在 pdf：Mac与iPhone采用相同的可读文件格式。用户自行选择外部工具同步文件，或自行复制文件。

### jerryjiao__dsh-wewrite

段落标题不一致，需求条目 1 / 95 一致（pdf 拆出 89 条）

- 标题只在 Markdown：dsh-wewrite 产品需求文档（PRD）
- 标题只在 Markdown：1. 问题陈述
- 标题只在 Markdown：2. 目标用户与场景
- 标题只在 Markdown：2.1 主要画像：技术型公众号号主（核心，占预期 80%+）
- 标题只在 Markdown：2.2 次要画像：重度内容创业者（v0.1 服务其单账号场景）
- 标题只在 pdf：dsh-wewrite产品需求文档（PRD）
- 标题只在 pdf：1.问题陈述
- 标题只在 pdf：2.目标用户与场景
- 标题只在 pdf：2.1主要画像：技术型公众号号主（核心，占预期80%+）
- 标题只在 pdf：2.2次要画像：重度内容创业者（v0.1服务其单账号场景）
- 需求只在 Markdown：排版工具只有排版：doocs/md 这类编辑器解决「Markdown→微信图文」，但选题、写作、配图、推送全靠人肉串联，最终还要手动复制粘贴进公众号后台。
- 需求只在 Markdown：AI 写作工具是黑盒 SaaS：135编辑器、壹伴、讯飞绘文等闭源工具按年订阅，模型不是用户自己的，风格不可控，数据经过第三方。
- 需求只在 Markdown：开源管线工具上手门槛高：md2wechat-skill（Go CLI）等项目的用户反馈集中在三件事——微信 IP 白名单/凭据配置踩坑、CLI 环境折腾、出稿慢（知乎实测者原话大意：「用那点时间我手动排版 10 篇都够了」，来源见 §3）。
- 需求只在 Markdown：没有定时化：以上方案几乎都没有「RRULE 定时跑管线 → 自动进草稿箱」的能力，内容创作者每天仍要手动触发。
- 需求只在 Markdown：身份：开发者 / AI 从业者 / 独立博主，25-40 岁，运营科技、AI、开发向公众号（周更 2-7 篇）。
- 需求只在 Markdown：环境：本机已装 DSH（~/.dsh/ 已存在，已配模型插件与 API key），会用命令行但不享受折腾配置。
- 需求只在 Markdown：技术水平：高。能读懂报错、会配环境变量；但期待「装完即用」，不接受为了发一篇文章研究半天 IP 白名单。
- 需求只在 Markdown：DSH 生态空白确认：AdamPlatin123/awesome-dsh-plugins（仓库）的研究目录收录约 60 个插件（dsh-weixin-bot / dsh-wecom-bot 为 IM 桥接，dsh-feishu-bot 为飞书 bot 等），没有任何一个微信公众号写作/发布管线插件。PLUGINS.md 登记清单目前仅 4 条且支持 PR 收录（约定 @dsh-external/* scope + repo 打 dsh-plugin topic）。→ dsh-wewrite 是 DSH 生态内该品类第一个，先发窗口明确。
- 需求只在 Markdown：DSH 原生，一条命令装进已有生产力工具：竞品要么是独立部署的重平台（AIWriteX），要么是裸 CLI（md2wechat-skill），要么是 SaaS（135/壹伴/讯飞）。我们装进用户每天已经在用的本地 harness，模型、会话、UI tab 全部复用，零额外部署。
- 需求只在 Markdown：管线源自真实生产使用：不是 prompt demo，是 Jerry 实际运营纪律的产物（质量门禁 --strict、编号配图一致性门禁都在管线里）。
- 需求只在 pdf：排版工具只有排版：doocs/md这类编辑器解决「Markdown→微信图文」，但选题、写作、配图、推送全靠人肉串联，最终还要手动复制粘贴进公众号后台。
- 需求只在 pdf：AI写作工具是黑盒SaaS：135编辑器、壹伴、讯飞绘文等闭源工具按年订阅，模型不是用户自己的，风格不可控，数据经过第三方。
- 需求只在 pdf：开源管线工具上手门槛高：md2wechat-skill（Go CLI）等项目的用户反馈集中在三件事——微信IP白名单/凭据配置踩坑、CLI环境折腾、出稿慢（知乎实测者原话大意：「用那点时间我手动排版10篇都够了」，来源见§3）。
- 需求只在 pdf：没有定时化：以上方案几乎都没有「RRULE定时跑管线→自动进草稿箱」的能力，内容创作者每天仍要手动触发。
- 需求只在 pdf：身份：开发者/ AI从业者/独立博主，25-40岁，运营科技、AI、开发向公众号（周更2-7篇）。
- 需求只在 pdf：环境：本机已装DSH（~/.dsh/已存在，已配模型插件与API key），会用命令行但不享受折腾配置。
- 需求只在 pdf：技术水平：高。能读懂报错、会配环境变量；但期待「装完即用」，不接受为了发一篇文章研究半天IP白名单。
- 需求只在 pdf：DSH生态空白确认：AdamPlatin123/awesome-dsh-plugins（仓库）的研究目录收录约60个插件（dsh-weixin-bot/ dsh-wecom-bot为IM桥接，dsh-feishu-bot为飞书bot等），没有任何一个微信公众号写作/发布管线插件。PLUGINS.md登记清单目前仅4条且支持PR收录（约定@dsh-external/*scope + repo打dsh-plugin topic）。→dsh- wewrite是DSH生态内该品类第一个，先发窗口明确。
- 需求只在 pdf：DSH原生，一条命令装进已有生产力工具：竞品要么是独立部署的重平台（AIWriteX），要么是裸CLI（md2wechat-skill），要么是SaaS（135/壹伴/讯飞）。我们装进用户每天已经在用的本地harness，模型、会话、UI tab全部复用，零额外部署。
- 需求只在 pdf：管线源自真实生产使用：不是prompt demo，是Jerry实际运营纪律的产物（质量门禁--strict、编号配图一致性门禁都在管线里）。

### jnMetaCode__agency-orchestrator

段落标题不一致，需求条目 6 / 42 一致（pdf 拆出 42 条）

- 标题只在 Markdown：Agency Orchestrator — 产品需求文档
- 标题只在 Markdown：为什么不直接用 CrewAI / LangGraph？
- 标题只在 Markdown：P0 — MVP（v0.1）
- 标题只在 Markdown：F1: Workflow YAML 定义
- 标题只在 Markdown：F2: DAG 执行引擎
- 标题只在 pdf：Agency Orchestrator —产品需求文档
- 标题只在 pdf：为什么不直接用CrewAI /LangGraph？
- 标题只在 pdf：P0 —MVP（v0.1）
- 标题只在 pdf：LLM配置
- 标题只在 pdf：P1 —增强（v0.2）
- 需求只在 Markdown：核心差异：别人是「给你一个框架，角色你自己写」，我们是「角色已经写好 211 个，你只需要编排」。
- 需求只在 Markdown：YAML 驱动 —— 编排逻辑写在配置文件里，不写代码
- 需求只在 Markdown：角色复用 —— 直接引用 agency-agents 的角色定义，不重新发明
- 需求只在 Markdown：LLM 无关 —— 支持 Claude / OpenAI / Ollama 等任意后端（但 MVP 先做 1 个）
- 需求只在 Markdown：最少依赖 —— 不依赖 LangChain / CrewAI 等框架，但允许用成熟的小工具库（js-yaml、官方 SDK）
- 需求只在 Markdown：渐进式 —— 最简单的串行流 5 分钟上手，复杂流程按需加
- 需求只在 Markdown：role 字段引用 agency-agents 的目录路径，自动读取 .md 文件作为 system prompt
- 需求只在 Markdown：depends_on 定义依赖关系，引擎自动计算执行顺序和并行机会
- 需求只在 Markdown：output 命名该步骤的输出，供后续步骤用 {{变量名}} 引用
- 需求只在 Markdown：{{input变量}} 引用工作流输入
- 需求只在 pdf：核心差异：别人是「给你一个框架，角色你自己写」，我们是「角色已经写好211个，你只需要编排」。
- 需求只在 pdf：YAML驱动——编排逻辑写在配置文件里，不写代码
- 需求只在 pdf：角色复用——直接引用agency-agents的角色定义，不重新发明
- 需求只在 pdf：LLM无关——支持Claude / OpenAI / Ollama等任意后端（但MVP先做1个）
- 需求只在 pdf：最少依赖——不依赖LangChain / CrewAI等框架，但允许用成熟的小工具库（js-yaml、官方SDK）
- 需求只在 pdf：渐进式——最简单的串行流5分钟上手，复杂流程按需加
- 需求只在 pdf：role字段引用agency-agents的目录路径，自动读取.md文件作为system prompt
- 需求只在 pdf：depends_on定义依赖关系，引擎自动计算执行顺序和并行机会
- 需求只在 pdf：output命名该步骤的输出，供后续步骤用{{变量名}}引用
- 需求只在 pdf：{{input变量}}引用工作流输入F2: DAG执行引擎

### jnMetaCode__openshorts

段落标题不一致，需求条目 3 / 57 一致（pdf 拆出 35 条）

- 标题只在 Markdown：OpenShorts · 开片 — 需求文档（PRD v2）
- 标题只在 Markdown：1. 定位
- 标题只在 Markdown：2. 目标用户与场景
- 标题只在 Markdown：2.1 用户故事（M1 验收用）
- 标题只在 Markdown：2.2 竞品对照
- 标题只在 pdf：OpenShorts ·开片—需求文档（PRD v2）
- 标题只在 pdf：1.定位
- 标题只在 pdf：2.目标用户与场景
- 标题只在 pdf：2.1用户故事（M1验收用）
- 标题只在 pdf：2.2竞品对照
- 需求只在 Markdown：面向中文创作者先行（界面、模板、TTS 音色、发布规格全部按国内平台），英文随后。
- 需求只在 Markdown：不是模型，不是剪辑器，不是 SaaS；是把"脚本 → 画面 → 配音 → 字幕 → 合成 → 发布"串成一条可控、可复现、成本透明的流水线。
- 需求只在 Markdown：与 MoneyPrinterTurbo（119k★）的关系：它证明了"话题 → 素材库拼片 → TTS"这条零成本路线有海量需求；我们把这条路线做进来当默认免费路径，再加上它没有的：真·AI 出片（本地 / 云端）、验收员看图把关、花费预览、一条命令或双击安装。
- 需求只在 Markdown：作为自媒体新手，我输入"为什么猫爱钻纸箱"，10 分钟内拿到一条带字幕配音的竖版视频，中间只做了两次选择（模板、来源），全程 0 元。
- 需求只在 Markdown：作为账号运营，我把同一脚本换 3 个音色批量出 3 版，文件名和封面自动区分。（M3）
- 需求只在 Markdown：作为开发者，我在 CI 里用 openshorts render project.json 出片，不打开界面。（M1）
- 需求只在 Markdown：输入：话题 / 文案 / 一篇文章链接（v2 后）。
- 需求只在 Markdown：流程：AI 写口播脚本（分段、每段一个画面意图）→ 每段配画面 → TTS 配音 → 逐字/逐句字幕 → BGM → 合成 9:16 1080P → 导出 + 发布规格（封面、标题、话题标签）。
- 需求只在 Markdown：画面来源默认 素材库（Pexels / Pixabay 免费片段，按每段关键词匹配），可切 AI 配图（文生图，成本低）或 AI 出片。
- 需求只在 Markdown："免费"的准确含义：0 元，但不是零配置——素材库要一把免费的 Pexels/Pixabay API key（注册即得，界面一键引导），脚本要一个文本模型（用户自己的 key，或本地 Ollama），配音用 Edge TTS（免费但依赖微软非官方端点，可能变动；离线备选见 docs/tts.md）。产品不内置任何共享 key。
- 需求只在 pdf：面向中文创作者先行（界面、模板、TTS音色、发布规格全部按国内平台），英文随后。
- 需求只在 pdf：不是模型，不是剪辑器，不是SaaS；是把"脚本→画面→配音→字幕→合成→发布"串成一条可控、可复现、成本透明的流水线。
- 需求只在 pdf：与MoneyPrinterTurbo（119k★）的关系：它证明了"话题→素材库拼片→ TTS"这条零成本路线有海量需求；我们把这条路线做进来当默认免费路径，再加上它没有的：真·AI出片（本地/云端）、验收员看图把关、花费预览、一条命令或双击安装。
- 需求只在 pdf：作为自媒体新手，我输入"为什么猫爱钻纸箱"，10分钟内拿到一条带字幕配音的竖版视频，中间只做了两次选择（模板、来源），全程0元。
- 需求只在 pdf：作为账号运营，我把同一脚本换3个音色批量出3版，文件名和封面自动区分。（M3）
- 需求只在 pdf：作为开发者，我在CI里用openshorts render project.json出片，不打开界面。（M1）
- 需求只在 pdf：输入：话题/文案/一篇文章链接（v2后）。
- 需求只在 pdf：流程：AI写口播脚本（分段、每段一个画面意图）→每段配画面→TTS配音→逐字/逐句字幕→BGM →合成9:16 1080P →导出+发布规格（封面、标题、话题标签）。
- 需求只在 pdf：画面来源默认素材库（Pexels/ Pixabay免费片段，按每段关键词匹配），可切AI配图（文生图，成本低）或AI出片。
- 需求只在 pdf："免费"的准确含义：0元，但不是零配置——素材库要一把免费的Pexels/Pixabay API key（注册即得，界面一键引导），脚本要一个文本模型（用户自己的key，或本地Ollama），配音用Edge TTS（免费但依赖微软非官方端点，可能变动；离线备选见docs/tts.md）。产品不内置任何共享key。

### junerver__ComposeHooks

段落标题不一致，需求条目 0 / 45 一致（pdf 拆出 35 条）

- 标题只在 Markdown：需求：为 hooks2 发布 wasmJs（及 js）变体
- 标题只在 Markdown：1.1 谁在依赖这个
- 标题只在 Markdown：1.2 当前的问题
- 标题只在 Markdown：1.3 期望收益
- 标题只在 Markdown：2.1 核心需求（P0）
- 标题只在 pdf：需求：为hooks2发布wasmJs（及js）变体
- 标题只在 pdf：1.1谁在依赖这个
- 标题只在 pdf：1.2当前的问题
- 标题只在 pdf：1.3期望收益
- 标题只在 pdf：2.1核心需求（P0）
- 需求只在 Markdown：useState / useGetState / useLatestState（状态）
- 需求只在 Markdown：useContext / createContext（上下文）
- 需求只在 Markdown：Palette 计划建设在线文档站点，目标是在浏览器中提供组件的真实可交互预览（可点击、可调参的 Compose 组件）。这需要为 Palette 的 palette 模块启用 wasmJs target，用 Compose Multiplatform 编译到 WebAssembly 运行在浏览器里。
- 需求只在 Markdown：ID：R2；需求：核心状态 hooks 全部可用；说明：下表"必须在 wasmJs 可用"的 hooks 不能因平台限制降级或编译失败。
- 需求只在 Markdown：ID：R3；需求：发布 js 变体（可选）；说明：wasmJs 是主目标；js 变体作为兼容补充（部分场景需要纯 JS target）。如成本高可暂缓。
- 需求只在 Markdown：Hook：useRedux / createStore / ReduxProvider；风险点：大量使用 KClass<*> 做状态/动作类型注册（CreateStore.kt:24-25）。；建议处理：KClass 在 wasmJs 支持有限；可能需改用字符串键或 KClass 简化用法。
- 需求只在 Markdown：现状：commonMain 直接 import kotlin.reflect.KClass 等，且 kotlin.reflect 在 commonMain 是可用的（stdlib 提供）。
- 需求只在 Markdown：wasmJs 情况：kotlin-reflect 对 wasmJs 的支持是有限的——KClass 基本可用，但 KFunction/反射调用（call()/members）在 wasmJs 下不可用或行为不同。
- 需求只在 Markdown：审计每一处 KClass/KFunction 的实际用途：是仅做类型标记/Map 键，还是真的调用反射方法？
- 需求只在 Markdown：若仅做键：KClass 作为 Map 键在 wasmJs 可用，无需改动。
- 需求只在 pdf：useState/useGetState/useLatestState（状态）
- 需求只在 pdf：Palette计划建设在线文档站点，目标是在浏览器中提供组件的真实可交互预览（可点击、可调参的Compose组件）。这需要为Palette的palette模块启用wasmJs target，用Compose Multiplatform编译到WebAssembly运行在浏览器里。
- 需求只在 pdf：}target，随库发布。这是Compose Multiplatform官方推荐的Web目标（wasm而非js）。R2核心状态hooks全部下表"必须在wasmJs可用可用"的hooks不能因平台限制降级或编译失败。
- 需求只在 pdf：ID需求说明R3发布js变体（可选）wasmJs是主目标；js变体作为兼容补充（部分场景需要纯JS target）。如成本高可暂缓。R4带副作用/平台能力的见§4"平台能力风险hooks提供wasmJs适点"。配或明确的降级策略
- 需求只在 pdf：11）。但实际网络调on降级。用是注入式（serviceFunction由调用方传入），不绑Hook风险点建议处理定HTTP客户端。
- 需求只在 pdf：>Unit，no-op。不阻塞Types.kt:106），通R1/R2。过createContext注入实际存储实现，不在commonMain绑定具体存储。usePageVisibility/可能依赖平台事件提供wasmJs useNetwork等浏览器（browser）的actual
- 需求只在 pdf：现状：commonMain直接import kotlin.reflect.KClass等，且kotlin.reflect在commonMain是可用的（stdlib提供）。
- 需求只在 pdf：wasmJs情况：kotlin-reflect对wasmJs的支持是有限的——KClass基本可用，但KFunction/反射调用（call()/members）在wasmJs下不可用或行为不同。
- 需求只在 pdf：审计每一处KClass/KFunction的实际用途：是仅做类型标记/Map键，还是真的调用反射方法？
- 需求只在 pdf：若仅做键：KClass作为Map键在wasmJs可用，无需改动。

### konghanghang__openlist-strm

段落标题不一致，需求条目 41 / 161 一致（pdf 拆出 146 条）

- 标题只在 Markdown：OpenList-STRM 项目需求文档 (PRD)
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目简介
- 标题只在 Markdown：1.2 核心价值
- 标题只在 Markdown：1.3 技术栈
- 标题只在 pdf：OpenList-STRM项目需求文档(PRD)
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目简介
- 标题只在 pdf：1.2核心价值
- 标题只在 pdf：1.3技术栈
- 需求只在 Markdown：免挂载：无需挂载网盘，通过 STRM 文件直接播放
- 需求只在 Markdown：节省空间：本地只存储小体积的 STRM 文件
- 需求只在 Markdown：灵活调度：每个配置独立定时任务，可视化 Cron 编辑器
- 需求只在 Markdown：高性能：Go 语言实现，每配置独立并发控制
- 需求只在 Markdown：MediaWarp 集成：支持 302 重定向代理，优化播放体验
- 需求只在 Markdown：Web UI 管理：无需编辑配置文件，所有配置通过 Web UI 管理
- 需求只在 Markdown：部署：单二进制文件（前端嵌入）/ Docker
- 需求只在 Markdown：功能描述：与 Alist API 集成，获取文件列表和生成直链
- 需求只在 Markdown：支持多个 Alist 实例配置
- 需求只在 Markdown：支持 Alist 签名功能（安全增强）
- 需求只在 pdf：免挂载：无需挂载网盘，通过STRM文件直接播放
- 需求只在 pdf：节省空间：本地只存储小体积的STRM文件
- 需求只在 pdf：灵活调度：每个配置独立定时任务，可视化Cron编辑器
- 需求只在 pdf：高性能：Go语言实现，每配置独立并发控制
- 需求只在 pdf：MediaWarp集成：支持302重定向代理，优化播放体验
- 需求只在 pdf：Web UI管理：无需编辑配置文件，所有配置通过Web UI管理
- 需求只在 pdf：部署：单二进制文件（前端嵌入）/Docker
- 需求只在 pdf：功能描述：与Alist API集成，获取文件列表和生成直链
- 需求只在 pdf：详细需求：o支持Alist v3 API o支持多个Alist实例配置o支持Alist签名功能（安全增强）o支持自定义请求头和认证o错误处理和重试机制
- 需求只在 pdf：功能描述：根据Alist文件列表生成对应的STRM文件

### kunhuang12345__wuthering-waves-automation

段落标题不一致，需求条目 53 / 303 一致（pdf 拆出 289 条）

- 标题只在 Markdown：《鸣潮》游戏自动化系统需求文档
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 技术栈
- 标题只在 pdf：（无标题）
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目背景
- 标题只在 pdf：1.2项目目标
- 标题只在 pdf：1.3技术栈
- 需求只在 Markdown：核心框架: LangChain + AutoGPT架构
- 需求只在 Markdown：决策模型: 强化学习算法
- 需求只在 Markdown：数据存储: SQLite + Redis缓存
- 需求只在 Markdown：委托任务自动接取和完成
- 需求只在 Markdown：每日签到奖励领取
- 需求只在 Markdown：日常副本挑战
- 需求只在 Markdown：材料收集任务
- 需求只在 Markdown：声骸系统日常维护
- 需求只在 Markdown：任务识别功能: 系统需要能够自动识别游戏界面中的任务相关元素，包括任务列表、任务状态、任务奖励等信息。识别方式包括界面元素匹配、文本识别和图标识别等多种方式，确保在不同游戏界面下都能准确识别任务信息。
- 需求只在 Markdown：任务优先级计算: 系统需要根据任务的奖励价值、完成难度、时间限制、体力消耗等多个维度来智能计算任务优先级。优先级算法需要考虑任务的基础奖励、额外奖励、完成时间、体力消耗比例等因素，并能够根据玩家的当前状态动态调整优先级。
- 需求只在 pdf：核心框架: LangChain +AutoGPT架构
- 需求只在 pdf：AI模型: o OCR识别:PaddleOCR/Tesseract o图像分类:YOLOv8/ResNet o决策模型:强化学习算法
- 需求只在 pdf：数据存储: SQLite +Redis缓存
- 需求只在 pdf：1.1日常任务自动化
- 需求只在 pdf：任务识别功能:系统需要能够自动识别游戏界面中的任务相关元素，包括任务列表、
- 需求只在 pdf：任务优先级计算:系统需要根据任务的奖励价值、完成难度、时间限制、体力消耗
- 需求只在 pdf：任务执行流程:系统需要能够自动执行完整的任务流程，包括任务接取、任务执行、
- 需求只在 pdf：任务状态监控:系统需要实时监控任务的执行状态，包括任务进度、完成情况、异
- 需求只在 pdf：奖励管理:系统需要自动处理任务完成后的奖励领取和整理工作，包括经验值、材
- 需求只在 pdf：1.2资源收集自动化

### kyre-99__MacDynamicIslandPet

段落标题不一致，需求条目 76 / 183 一致（pdf 拆出 156 条）

- 标题只在 Markdown：MacDynamicIslandPet 拟人化与记忆上下文升级 PRD
- 标题只在 Markdown：1. 项目背景
- 标题只在 Markdown：2. 产品目标
- 标题只在 Markdown：2.1 总目标
- 标题只在 Markdown：2.2 用户感知目标
- 标题只在 pdf：MacDynamicIslandPet拟人化与记忆上下文升级PRD
- 标题只在 pdf：1.项目背景
- 标题只在 pdf：2.产品目标
- 标题只在 pdf：2.1总目标
- 标题只在 pdf：2.2用户感知目标
- 需求只在 Markdown：召回的 1~3 条高相关记忆
- 需求只在 Markdown：1 条未完成念头或挂念事项
- 需求只在 Markdown：MacDynamicIslandPet/PetInternalStateManager.swift
- 需求只在 Markdown：memory/pet-internal-state.json
- 需求只在 Markdown：MacDynamicIslandPet/MemoryCardManager.swift
- 需求只在 Markdown：MacDynamicIslandPet/RelationshipMemoryManager.swift
- 需求只在 Markdown：MacDynamicIslandPet/WorkingMemoryManager.swift
- 需求只在 Markdown：ConversationManager.buildSystemPrompt()
- 需求只在 Markdown：本次生成使用了哪些上下文
- 需求只在 Markdown：召回了哪些记忆
- 需求只在 pdf：召回的1~3条高相关记忆
- 需求只在 pdf：1条未完成念头或挂念事项
- 需求只在 pdf：补充关键日志：o本次生成使用了哪些上下文o召回了哪些记忆o当前内部状态是什么
- 需求只在 pdf：手动触发3次对话
- 需求只在 pdf：手动触发3次自言自语
- 需求只在 pdf：在ConversationManager中补充了对话上下文日志，记录用户输入、system prompt规模、历史轮数，以及性格/关系/情绪/知识等上下文片段
- 需求只在 pdf：在CommentGenerator中补充了自言自语与气泡请求日志，记录触发场景、人格提示、关系提示、主人状态、知识量和最终来源
- 需求只在 pdf：在SelfTalkManager中补充了触发原因、映射trigger scene、当前app、停留时长、冷却状态等观测日志
- 需求只在 pdf：这一步为后续每轮prompt裁剪和连续性调优提供了可观测基础
- 需求只在 pdf：在以下事件中更新内部状态：o用户主动对话o长时间未互动o被忽略o触发自言自语o收到积极回应

### lhxone__TeacherDesk

段落标题不一致，需求条目 23 / 86 一致（pdf 拆出 82 条）

- 标题只在 Markdown：教师工作台（TeacherDesk）产品需求文档 PRD
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：教师工作台（TeacherDesk）产品需求文档PRD
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：课堂现场可用：抽签、点名、座位图必须在手机上单手 3 秒内触达。
- 需求只在 Markdown：离线容忍：PWA 缓存静态资源与最近访问的班级/学生数据，弱网可读。
- 需求只在 Markdown：前后端分离：后端只提供 JSON API，前端独立部署。
- 需求只在 Markdown：密码规则：8–64 位，至少包含字母与数字。
- 需求只在 Markdown：邮箱唯一；密码使用 bcrypt（cost=12）哈希存储。
- 需求只在 Markdown：注册成功后自动登录，返回 access token + refresh token。
- 需求只在 Markdown：连续 5 次失败锁定 15 分钟（按邮箱 + IP 计数）。
- 需求只在 Markdown：支持"记住我"（refresh token 有效期 30 天，否则 7 天）。
- 需求只在 Markdown：Access Token：JWT，HS256，有效期 2 小时，放在 Authorization: Bearer <token>。
- 需求只在 Markdown：Refresh Token：随机 opaque 字符串，哈希后存库，一次性使用（rotation），有效期 7/30 天。
- 需求只在 pdf：课堂现场可用：抽签、点名、座位图必须在手机上单手3秒内触达。
- 需求只在 pdf：离线容忍：PWA缓存静态资源与最近访问的班级/学生数据，弱网可读。
- 需求只在 pdf：前后端分离：后端只提供JSON API，前端独立部署。
- 需求只在 pdf：密码规则：8–64位，至少包含字母与数字。
- 需求只在 pdf：邮箱唯一；密码使用bcrypt（cost=12）哈希存储。
- 需求只在 pdf：注册成功后自动登录，返回access token + refresh token。
- 需求只在 pdf：连续5次失败锁定15分钟（按邮箱+ IP计数）。
- 需求只在 pdf：支持"记住我"（refresh token有效期30天，否则7天）。
- 需求只在 pdf：Access Token：JWT，HS256，有效期2小时，放在Authorization:Bearer <token>。
- 需求只在 pdf：Refresh Token：随机opaque字符串，哈希后存库，一次性使用（rotation），有效期7/30天。

### liamyueng__xu-ai-news-rag

段落标题不一致，需求条目 28 / 119 一致（pdf 拆出 111 条）

- 标题只在 Markdown：产品需求文档 (PRD)
- 标题只在 Markdown：1. 引言
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 产品愿景
- 标题只在 pdf：产品需求文档(PRD)
- 标题只在 pdf：1.引言
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：1.3产品愿景
- 需求只在 Markdown：功能描述: 定时从investing.com等财经网站抓取新闻
- 需求只在 Markdown：每小时自动抓取一次
- 需求只在 Markdown：支持去重功能
- 需求只在 Markdown：功能描述: 提供用户注册、登录、权限管理
- 需求只在 Markdown：密码加密存储
- 需求只在 Markdown：功能描述: 增删改查知识库内容
- 需求只在 Markdown：支持分页查询
- 需求只在 Markdown：支持筛选和排序
- 需求只在 Markdown：支持批量操作
- 需求只在 Markdown：功能描述: 基于向量相似度的智能搜索
- 需求只在 pdf：1.1新闻自动抓取
- 需求只在 pdf：功能描述:定时从investing.com等财经网站抓取新闻
- 需求只在 pdf：验收标准: o每小时自动抓取一次o抓取成功率> 90% o支持去重功能
- 需求只在 pdf：1.2用户认证系统
- 需求只在 pdf：功能描述:提供用户注册、登录、权限管理
- 需求只在 pdf：验收标准: o支持JWT token认证o密码加密存储o会话管理
- 需求只在 pdf：功能描述:增删改查知识库内容
- 需求只在 pdf：验收标准: o支持分页查询o支持筛选和排序o支持批量操作o支持Excel导入
- 需求只在 pdf：功能描述:基于向量相似度的智能搜索
- 需求只在 pdf：验收标准: o搜索响应时间<2秒o结果按相关度排序o支持联网搜索兜底

### liangyimingcom__BRClient

段落标题不一致，需求条目 130 / 236 一致（pdf 拆出 181 条）

- 标题只在 Markdown：BRClient 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述与定位
- 标题只在 Markdown：1.1 产品定义
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 产品愿景
- 标题只在 pdf：BRClient产品需求文档(PRD)
- 标题只在 pdf：1.产品概述与定位
- 标题只在 pdf：1.1产品定义
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3产品愿景
- 需求只在 Markdown：编制日期: 2025年12月
- 需求只在 Markdown：编制人: 产品团队
- 需求只在 Markdown：目标用户: 企业技术团队、AI开发者、内容创作者
- 需求只在 Markdown：差异化: 专注、简洁、开源、跨平台
- 需求只在 Markdown：简单至上: 降低使用门槛，开箱即用
- 需求只在 Markdown：性能优先: 快速响应，流畅体验
- 需求只在 Markdown：安全可靠: 数据本地存储，隐私保护
- 需求只在 Markdown：开放生态: 开源协议，插件扩展
- 需求只在 Markdown：P0: 核心功能，必须实现
- 需求只在 Markdown：P1: 重要功能，尽快实现
- 需求只在 pdf：编制日期:2025年12月
- 需求只在 pdf：编制人:产品团队
- 需求只在 pdf：目标用户:企业技术团队、AI开发者、内容创作者
- 需求只在 pdf：差异化:专注、简洁、开源、跨平台
- 需求只在 pdf：简单至上:降低使用门槛，开箱即用
- 需求只在 pdf：性能优先:快速响应，流畅体验
- 需求只在 pdf：安全可靠:数据本地存储，隐私保护
- 需求只在 pdf：开放生态:开源协议，插件扩展
- 需求只在 pdf：P0:核心功能，必须实现
- 需求只在 pdf：P1:重要功能，尽快实现

### lintsinghua__oops

段落标题不一致，需求条目 3 / 82 一致（pdf 拆出 64 条）

- 标题只在 Markdown：oops — 产品需求说明（PRD）
- 标题只在 Markdown：1. 背景与证据（2026-10-14 核实）
- 标题只在 Markdown：1.1 官方需求长期悬而未决
- 标题只在 Markdown：1.2 竞品（2026-10-14 快照）
- 标题只在 Markdown：2. 产品定位
- 标题只在 pdf：oops —产品需求说明（PRD）
- 标题只在 pdf：1.背景与证据（2026-10-14核实）
- 标题只在 pdf：1.1官方需求长期悬而未决
- 标题只在 pdf：1.2竞品（2026-10-14快照）
- 标题只在 pdf：2.产品定位
- 需求只在 Markdown：oops 是一个给任意编程 Agent（Claude Code、Codex、Gemini CLI、Cursor CLI，以及任何终端 Agent）用的整轮撤销工具。
- 需求只在 Markdown：Agent 每开始一轮，oops 就给工作区拍一张增量快照。不管这一轮是用 Edit 工具、sed -i、python - <<EOF、rm -rf 还是 git clean -fdx 改的文件，也不管文件有没有进 git，都能用 oops undo 一键撤回。
- 需求只在 Markdown：不依赖 Agent 自己的检查点，不碰用户的 git 仓库。默认只在本机运行，不联网。
- 需求只在 Markdown：用户只需要记住一个词：oops。出事时直接敲 oops，进入交互式时间线（Bubble Tea TUI）：选中一轮 → 预览 diff → 回车撤销。oops undo 是无交互的快捷方式；在 Agent 会话里也可以用 /oops。
- 需求只在 Markdown：MVP（v0.1）：oops init 30 秒内一次接好本机所有 Agent（可一键撤销接入）；自动按轮快照；交互式时间线；undo / rewind / redo / restore / list / show / diff；会话内 /oops；通用包装器 oops run；支持 macOS、Linux、Windows。完整的用户旅程见 DESIGN.md §1。
- 需求只在 Markdown：项目：RonitSachdev/ccundo；★：1,401；最近推送：2025-07-27；范围与不足：只支持 Claude Code；只解析 Edit 类工具调用，不覆盖 bash；简介自称"claude now natively supports this feature"，事实上已停更
- 需求只在 Markdown：结论：需求硬、长期未满足；现有方案要么绑死单个 Agent，要么只是雏形。oops 的机会在于"跨 Agent、文件系统级、对已有改动安全"的成熟实现，并且必须在官方补齐之前抢到心智。
- 需求只在 Markdown：主：oops undo — Ctrl+Z for coding agents.
- 需求只在 Markdown：中文：Agent 闯祸，一键撤回。
- 需求只在 Markdown：备选："Undo anything your agent did. Even rm -rf."
- 需求只在 pdf：oops是一个给任意编程Agent（Claude Code、Codex、Gemini CLI、Cursor CLI，以及任何终端Agent）用的整轮撤销工具。
- 需求只在 pdf：Agent每开始一轮，oops就给工作区拍一张增量快照。不管这一轮是用Edit工具、sed-i、python-<<EOF、rm-rf还是git clean-fdx改的文件，也不管文件有没有进git，都能用oops undo一键撤回。
- 需求只在 pdf：不依赖Agent自己的检查点，不碰用户的git仓库。默认只在本机运行，不联网。
- 需求只在 pdf：用户只需要记住一个词：oops。出事时直接敲oops，进入交互式时间线（Bubble Tea TUI）：选中一轮→预览diff →回车撤销。oops undo是无交互的快捷方式；在Agent会话里也可以用/oops。
- 需求只在 pdf：MVP（v0.1）：oops init 30秒内一次接好本机所有Agent（可一键撤销接入）；自动按轮快照；交互式时间线；undo/rewind/redo/restore /list/ show/diff；会话内/oops；通用包装器oops run；支持macOS、Linux、Windows。完整的用户旅程见DESIGN.md §1。
- 需求只在 pdf：结论：需求硬、长期未满足；现有方案要么绑死单个Agent，要么只是雏形。oops的机会在于"跨Agent、文件系统级、对已有改动安全"的成熟实现，并且必须在官方补齐之前抢到心智。
- 需求只在 pdf：主：oops undo— Ctrl+Z for coding agents.
- 需求只在 pdf：中文：Agent闯祸，一键撤回。
- 需求只在 pdf：备选："Undo anything your agent did. Even rm-rf."
- 需求只在 pdf：先保命，再好用：oops自己绝不能丢用户数据。每次撤销前都先拍一张安全快照，撤销本身也能撤销。

### lonnnnnng__fluxdown

段落标题不一致，需求条目 25 / 56 一致（pdf 拆出 52 条）

- 标题只在 Markdown：桌面端 CLI
- 标题只在 Markdown：桌面端 GUI
- 标题只在 Markdown：移动端 App
- 标题只在 pdf：桌面端CLI
- 标题只在 pdf：桌面端GUI
- 标题只在 pdf：移动端App
- 需求只在 Markdown：普通下载用户：通过 GUI 或 App 添加链接，查看进度，暂停或继续任务。
- 需求只在 Markdown：命令行用户：使用 fluxdown CLI 检测协议、检查后端、立即下载或管理本地队列。
- 需求只在 Markdown：发布维护者：使用本地脚本和 GitHub Actions 构建多端产物，准备 GitHub Release。
- 需求只在 Markdown：技术集成方：基于 Rust core 的任务模型或 CLI JSON 输出集成到自动化系统。
- 需求只在 Markdown：download：立即执行单个下载并输出 JSON 摘要。
- 需求只在 Markdown：download 和 add 支持可选 --sha256；配置后下载完成必须校验最终文件，直连下载校验失败返回错误，队列任务校验失败进入 failed。
- 需求只在 Markdown：download、add、start、run 支持 --hls-variant-index（从 0 开始）和 --hls-keep-ts；前两者保存 HLS 任务配置，后两者可在本次执行中指定 variant 或启用 TS 输出。
- 需求只在 Markdown：通过 --store 覆盖默认队列文件路径。
- 需求只在 Markdown：可选输入 SHA-256；配置后下载完成必须校验最终文件，校验失败进入 failed。
- 需求只在 Markdown：本地 JSON 队列持久化。
- 需求只在 pdf：普通下载用户：通过GUI或App添加链接，查看进度，暂停或继续任务。
- 需求只在 pdf：命令行用户：使用fluxdown CLI检测协议、检查后端、立即下载或管理本地队列。
- 需求只在 pdf：发布维护者：使用本地脚本和GitHub Actions构建多端产物，准备GitHub Release。
- 需求只在 pdf：技术集成方：基于Rust core的任务模型或CLI JSON输出集成到自动化系统。
- 需求只在 pdf：download：立即执行单个下载并输出JSON摘要。
- 需求只在 pdf：download和add支持可选--sha256；配置后下载完成必须校验最终文件，直连下载校验失败返回错误，队列任务校验失败进入failed。
- 需求只在 pdf：download、add、start、run支持--hls-variant-index（从0开始）和-- hls-keep-ts；前两者保存HLS任务配置，后两者可在本次执行中指定variant或启用TS输出。
- 需求只在 pdf：通过--store覆盖默认队列文件路径。
- 需求只在 pdf：可选输入SHA-256；配置后下载完成必须校验最终文件，校验失败进入failed。
- 需求只在 pdf：本地JSON队列持久化。

### maczh__mgin

段落标题不一致，需求条目 7 / 94 一致（pdf 拆出 91 条）

- 标题只在 Markdown：mgin v2 架构重构 · 增量 PRD
- 标题只在 Markdown：0. 一句话定位
- 标题只在 Markdown：1. 现状盘点（v2-arch 分支实测）
- 标题只在 Markdown：1.1 已就绪能力（a285b65 已完成，不重复列入待办）
- 标题只在 Markdown：1.2 分类盘点表
- 标题只在 pdf：mgin v2架构重构·增量PRD
- 标题只在 pdf：0.一句话定位
- 标题只在 pdf：1.现状盘点（v2-arch分支实测）
- 标题只在 pdf：1.1已就绪能力（a285b65已完成，不重复列入待办）
- 标题只在 pdf：1.2分类盘点表
- 需求只在 Markdown：文档版本：v1.0（增量，基于既有 mgin 框架，非从零设计）
- 需求只在 Markdown：分支基线：v2-arch（从 jh 拉出，已含提交 a285b65 补齐三大生产缺口）
- 需求只在 Markdown：作者：产品经理 许清楚（Xu）
- 需求只在 Markdown：配套文档：docs/mgin-architecture-options.md（6 套架构方案与三大空白区实测，本 PRD 的起点）
- 需求只在 Markdown：做什么：脚手架 cmd/scaffold.go 生成的 router/controller/service/dao/model 五层统一收纳到 internal/ 下；在框架内明确 pkg/（对外可导入，如 client、registry、errcode、i18n、health、models）与 internal/（框架内部实现，如 db、mgin、config 内部细节）的边界，并写明各包归属。
- 需求只在 Markdown：mgin new 生成的工程含 internal/router|controller|service|dao|model；旧式顶层平铺工程 go build 仍通过（框架不强依赖 internal/）；
- 需求只在 Markdown：提供一份 pkg/ vs internal/ 包归属表，纳入 README；
- 需求只在 Markdown：go vet ./... 针对脚手架与框架相关包干净。
- 需求只在 Markdown：理由：当前脚手架把五层平铺在顶层（实测 scaffold.go 写 write("router/router.go", ...)），无 internal 边界，随业务增长包耦合失控，域间易越界直连（见 mgin-architecture-options.md §3.6）。
- 需求只在 Markdown：mgin.go 中不再出现逐组件的 if Contains(Used,...) 初始化/关闭链；
- 需求只在 pdf：文档版本：v1.0（增量，基于既有mgin框架，非从零设计）
- 需求只在 pdf：分支基线：v2-arch（从jh拉出，已含提交a285b65补齐三大生产缺口）
- 需求只在 pdf：作者：产品经理许清楚（Xu）
- 需求只在 pdf：配套文档：docs/mgin-architecture-options.md（6套架构方案与三大空白区实测，本PRD的起点）
- 需求只在 pdf：做什么：脚手架cmd/scaffold.go生成的router/controller/service/dao/model五层统一收纳到internal/下；在框架内明确pkg/（对外可导入，如client、registry、errcode、i18n、health、models）与internal/（框架内部实现，如db、mgin、config内部细节）的边界，并写明各包归属。
- 需求只在 pdf：mgin new生成的工程含internal/router|controller|service|dao| model；旧式顶层平铺工程go build仍通过（框架不强依赖internal/）；
- 需求只在 pdf：提供一份pkg/vs internal/包归属表，纳入README；
- 需求只在 pdf：go vet./...针对脚手架与框架相关包干净。
- 需求只在 pdf：理由：当前脚手架把五层平铺在顶层（实测scaffold.go写write("router/router.go",...)），无internal边界，随业务增长包耦合失控，域间易越界直连（见mgin-architecture-options.md§3.6）。
- 需求只在 pdf：mgin.go中不再出现逐组件的if Contains(Used,...)初始化/关闭链；

### mapleLeafOfficial__Skillhub

段落标题不一致，需求条目 62 / 119 一致（pdf 拆出 116 条）

- 标题只在 Markdown：技能详情与审核页文件浏览侧边栏 - 产品需求文档 (PRD)
- 标题只在 Markdown：技能详情页
- 标题只在 Markdown：审核详情页
- 标题只在 Markdown：桌面端
- 标题只在 Markdown：移动端
- 标题只在 pdf：技能详情与审核页文件浏览侧边栏-产品需求文档(PRD)
- 标题只在 pdf：Phase 1:共享模型与交互方案落地
- 标题只在 pdf：Phase 2:技能详情页集成
- 标题只在 pdf：Phase 3:审核页能力补齐
- 标题只在 pdf：Phase 4:回归与体验完善
- 需求只在 Markdown：平铺文件列表无法反映目录层级，用户难以理解 skill 包结构。
- 需求只在 Markdown：审核人员在审核页中无法点开任意文件验证实现内容，只能依赖 README 或下载压缩包离线查看。
- 需求只在 Markdown：现有三个 Tab 的主体内容已经承担不同职责，若继续把文件浏览塞入当前"文件"Tab，会使"概览"与"版本"场景下的跨文件查看成本偏高。
- 需求只在 Markdown：用统一的侧边文件浏览体验取代当前平铺文件列表，降低理解 skill 包结构的成本。
- 需求只在 Markdown：保持现有三个 Tab 的主语义不变，同时让用户在任意 Tab 下都能快速查看文件内容。
- 需求只在 Markdown：将现有平铺 files 列表重构为目录树，支持文件夹展开 / 合并。
- 需求只在 Markdown：支持 Markdown 文档渲染、常见文本文件源码预览，以及大文件 / 不支持文件类型的不可预览提示。
- 需求只在 Markdown：对 JSON / YAML / TS / JS 等文本文件提供更完整的语法高亮能力。
- 需求只在 Markdown：用户进入技能详情页，默认看到"概览 / 文件 / 版本"三个 Tab。
- 需求只在 Markdown：无论当前停留在哪个 Tab，页面都显示文件浏览侧边栏。
- 需求只在 pdf：平铺文件列表无法反映目录层级，用户难以理解skill包结构。
- 需求只在 pdf：审核人员在审核页中无法点开任意文件验证实现内容，只能依赖README或下载压缩包离线查看。
- 需求只在 pdf：现有三个Tab的主体内容已经承担不同职责，若继续把文件浏览塞入当前"文件"Tab，会使"概览"与"版本"场景下的跨文件查看成本偏高。
- 需求只在 pdf：用统一的侧边文件浏览体验取代当前平铺文件列表，降低理解skill包结构的成本。
- 需求只在 pdf：保持现有三个Tab的主语义不变，同时让用户在任意Tab下都能快速查看文件内容。
- 需求只在 pdf：将现有平铺files列表重构为目录树，支持文件夹展开/合并。
- 需求只在 pdf：支持Markdown文档渲染、常见文本文件源码预览，以及大文件/不支持文件类型的不可预览提示。
- 需求只在 pdf：对JSON / YAML / TS / JS等文本文件提供更完整的语法高亮能力。
- 需求只在 pdf：用户进入技能详情页，默认看到"概览/文件/版本"三个Tab。
- 需求只在 pdf：无论当前停留在哪个Tab，页面都显示文件浏览侧边栏。

### molix-shu__find-seafood

段落标题不一致，需求条目 53 / 84 一致（pdf 拆出 74 条）

- 标题只在 Markdown：识鲜地图 PRD v0.1
- 标题只在 Markdown：1. 产品定位
- 标题只在 Markdown：2. MVP 目标
- 标题只在 Markdown：3. MVP 范围
- 标题只在 Markdown：3.1 包含
- 标题只在 pdf：识鲜地图PRD v0.1
- 标题只在 pdf：1.产品定位
- 标题只在 pdf：2. MVP目标
- 标题只在 pdf：3. MVP范围
- 标题只在 pdf：3.1包含
- 需求只在 Markdown：置信度高于等于 80% 时展示主结果。
- 需求只在 Markdown：置信度 50%-79% 时展示候选结果，不直接下定论。
- 需求只在 Markdown：置信度低于 50% 或识别失败时，引导用户重新拍摄或使用搜索。
- 需求只在 Markdown：首版星星数使用 1-5 星。
- 需求只在 Markdown：用户提交后进入审核机制；MVP 可先使用"先发布、后举报/抽审"的轻审核模式。
- 需求只在 Markdown：编号：REC-001；需求：用户可拍照上传海鲜图片；优先级：P0；验收标准：支持调用相机拍照并上传
- 需求只在 Markdown：编号：REC-002；需求：用户可从相册选择图片；优先级：P0；验收标准：支持选择本地图片并上传
- 需求只在 Markdown：编号：SEARCH-001；需求：支持标准名搜索；优先级：P0；验收标准：搜索"皮皮虾"可命中详情页
- 需求只在 Markdown：编号：SEARCH-002；需求：支持别名搜索；优先级：P0；验收标准：搜索"虾爬子"可命中皮皮虾
- 需求只在 Markdown：编号：SEARCH-003；需求：支持模糊匹配；优先级：P1；验收标准：输入部分关键词可展示相关结果
- 需求只在 pdf：置信度高于等于80%时展示主结果。
- 需求只在 pdf：置信度50%-79%时展示候选结果，不直接下定论。
- 需求只在 pdf：置信度低于50%或识别失败时，引导用户重新拍摄或使用搜索。
- 需求只在 pdf：首版星星数使用1-5星。
- 需求只在 pdf：用户提交后进入审核机制；MVP可先使用"先发布、后举报/抽审"的轻审核模式。
- 需求只在 pdf：编号需求优先级验收标准REC-001 P0用户可拍照上传支持调用相机拍海鲜图片照并上传REC-002 P0用户可从相册选支持选择本地图择图片片并上传REC-003 P0系统返回识别结返回海鲜名称、果置信度、候选结果编号需求优先级验收标准REC-004 P0低置信度时展示置信度低于80%候选项时不直接给唯一结论REC-005 P0识别失败时提供展示重新拍摄和兜底路径文字搜索入口REC-006 P2保存识别记录成功识别后进入用户历史记录
- 需求只在 pdf：编号需求优先级验收标准SEARCH-001 P0支持标准名搜索搜索"皮皮虾"可命中详情页SEARCH-002 P0支持别名搜索搜索"虾爬子"可命中皮皮虾SEARCH-003 P1支持模糊匹配输入部分关键词可展示相关结果SEARCH-004 P2无结果时可反馈用户可提交未收新增录关键词
- 需求只在 pdf：编号需求优先级验收标准MAP-001 P0展示地图点位用户可看到附近餐馆点位MAP-002 P0支持按海鲜筛选从详情页进入时默认筛选当前海鲜MAP-003 P0展示餐馆推荐卡点击点位展示餐片馆、星星数、标签、评价MAP-004 P1支持切换筛选海用户可在地图页鲜切换海鲜品类MAP-005 P0支持定位授权未授权时提示授权用途，并提供手动城市兜底MAP-006 P2支持地图导航点击导航可跳转系统地图或小程序地图能力
- 需求只在 pdf：编号需求优先级验收标准CMS-001 P0管理员可维护海可新增、编辑、鲜资料下架海鲜条目CMS-002 P0管理员可维护安高风险提示支持全提醒独立编辑CMS-003 P1管理员可审核用可通过、拒绝、户图片隐藏图片CMS-004 P1管理员可审核用可通过、拒绝、户评论隐藏评论CMS-005 P2管理员可处理餐可合并重复餐馆馆纠错和修正位置
- 需求只在 pdf：图片存储：阿里云OSS

### mufflegyro__dsh-bottom-info-bar

段落标题不一致，需求条目 4 / 50 一致（pdf 拆出 40 条）

- 标题只在 Markdown：PRD：底部信息栏 v1.6（多服务商适配 + 分账修复）
- 标题只在 Markdown：FR-1 花费按服务商账户隔离（Bug 修复）
- 标题只在 Markdown：FR-2 余额严格跟随当前服务商（Bug 修复）
- 标题只在 Markdown：FR-3 智谱适配器（GLM Coding Plan 订阅额度，零设置）
- 标题只在 Markdown：FR-4 Kimi 适配器（API 余额，零设置）
- 标题只在 pdf：PRD：底部信息栏v1.6（多服务商适配+分账修复）
- 标题只在 pdf：FR-1花费按服务商账户隔离（Bug修复）
- 标题只在 pdf：FR-2余额严格跟随当前服务商（Bug修复）
- 标题只在 pdf：FR-3智谱适配器（GLM Coding Plan订阅额度，零设置）
- 标题只在 pdf：FR-4 Kimi适配器（API余额，零设置）
- 需求只在 Markdown：Given 用户在一个会话里先后使用 OpenCode 与 DeepSeek，账本含两家的记录；When 当前服务商为 DeepSeek；Then "本对话/今日/本月/全部"均只含 provider 归属 DeepSeek 账户的记录，OpenCode 记录不出现
- 需求只在 Markdown：Given 某服务商在当前记账中无任何记录；When 信息栏渲染；Then 对应金额显示 0 而不是显示其他服务商的合计
- 需求只在 Markdown：描述：余额账户映射只认当前活动服务商；对未适配/未知服务商，不再回退显示 DeepSeek 余额。
- 需求只在 Markdown：Given 当前服务商为 opencode-go（订阅制）；When 信息栏渲染；Then 不显示任何余额（含不显示 DeepSeek 余额）
- 需求只在 Markdown：Given 当前服务商为未适配平台（如 minimax）；When 信息栏渲染；Then 显示"未适配"引导而非 DeepSeek 余额
- 需求只在 Markdown：Given 当前服务商为 deepseek；Then 照常显示 DeepSeek 真实余额（行为不变）
- 需求只在 Markdown：描述：自动识别服务商 zai（国际）/ zai-coding-cn（国内 BigModel），读取 DSH 凭据 ZAI_API_KEY / ZAI_CODING_CN_API_KEY，查询 GLM Coding Plan 套餐等级与已用/剩余百分比、重置时刻；按订阅窗口制显示（剩余百分比 + 重置倒计时）。
- 需求只在 Markdown：接口：GET {host}/api/monitor/usage/quota/limit；国内 host=open.bigmodel.cn（Authorization 头直接放 API Key，无 Bearer），国际 host=api.z.ai（Bearer 前缀）。
- 需求只在 Markdown：Given 用户配置 ZAI_API_KEY（或 ZAI_CODING_CN_API_KEY）；When 当前服务商为 zai（或 zai-coding-cn）；Then 信息栏显示套餐等级（lite/standard/pro/max）与已用/剩余百分比，且无需任何插件设置
- 需求只在 Markdown：Given 接口返回 TOKENS_LIMIT（unit=3 等窗口）与 TIME_LIMIT；Then 正确映射为窗口显示，未知窗口类型跳过不报错
- 需求只在 pdf：验收标准（Given-When-Then）：o Given用户在一个会话里先后使用OpenCode与DeepSeek，账本含两家的记录；When当前服务商为DeepSeek；Then"本对话/今日/本月/全部"均只含provider归属DeepSeek账户的记录，OpenCode记录不出现o Given某服务商在当前记账中无任何记录；When信息栏渲染；Then对应金额显示0而不是显示其他服务商的合计
- 需求只在 pdf：描述：余额账户映射只认当前活动服务商；对未适配/未知服务商，不再回退显示DeepSeek余额。
- 需求只在 pdf：验收标准：o Given当前服务商为opencode-go（订阅制）；When信息栏渲染；Then不显示任何余额（含不显示DeepSeek余额）o Given当前服务商为未适配平台（如minimax）；When信息栏渲染；Then显示"未适配"引导而非DeepSeek余额o Given当前服务商为deepseek；Then照常显示DeepSeek真实余额（行为不变）
- 需求只在 pdf：描述：自动识别服务商zai（国际）/zai-coding-cn（国内BigModel），读取DSH凭据ZAI_API_KEY /ZAI_CODING_CN_API_KEY，查询GLM Coding Plan套餐等级与已用/剩余百分比、重置时刻；按订阅窗口制显示（剩余百分比+重置倒计时）。
- 需求只在 pdf：接口：GET{host}/api/monitor/usage/quota/limit；国内host=open.bigmodel.cn（Authorization头直接放API Key，无Bearer），国际host=api.z.ai（Bearer前缀）。
- 需求只在 pdf：验收标准：o Given用户配置ZAI_API_KEY（或ZAI_CODING_CN_API_KEY）；When当前服务商为zai（或zai-coding-cn）；Then信息栏显示套餐等级（lite/standard/pro/max）与已用/剩余百分比，且无需任何插件设置o Given接口返回TOKENS_LIMIT（unit=3等窗口）与TIME_LIMIT；Then正确映射为窗口显示，未知窗口类型跳过不报错o Given接口401/超时/格式异常；Then显示"刷新失败/降级"，保留上次快照，不崩溃o Given无凭据；Then显示"未配置密钥"引导
- 需求只在 pdf：描述：自动识别服务商moonshotai / moonshotai-cn /kimi-coding，读取凭据MOONSHOT_API_KEY /KIMI_API_KEY，查询余额。
- 需求只在 pdf：接口：GET https://api.moonshot.cn/v1/users/me/balance（Bearer），解析balance_infos（total/granted/topped_up，CNY）。
- 需求只在 pdf：验收标准：o Given配置MOONSHOT_API_KEY；When当前服务商为moonshotai；Then显示真实余额（¥），60s自动刷新o Given接口失败/无凭据；Then降级提示，不崩溃、不串显示其他服务商余额
- 需求只在 pdf：描述：自动识别服务商openrouter，读取凭据OPENROUTER_API_KEY，查询剩余credits（USD）。

### qtgf520__kai-qt

段落标题不一致，需求条目 13 / 114 一致（pdf 拆出 84 条）

- 标题只在 Markdown：Kai2 9000 功能需求规格说明（AI 可直接解析执行）
- 标题只在 Markdown：1. 更改提供商名称
- 标题只在 Markdown：2. 增加思考强度按钮
- 标题只在 Markdown：3. 设置里增加流式输出开关
- 标题只在 Markdown：4. 提示词字数上限增加
- 标题只在 pdf：Kai2 9000功能需求规格说明（AI可直接解析执行）
- 标题只在 pdf：1.更改提供商名称
- 标题只在 pdf：2.增加思考强度按钮
- 标题只在 pdf：3.设置里增加流式输出开关
- 标题只在 pdf：4.提示词字数上限增加
- 需求只在 Markdown：目标：支持自定义 Provider（模型服务商）的显示名称。
- 需求只在 Markdown：位置：Settings > Provider / 模型提供商 列表；Provider 配置数据结构。
- 需求只在 Markdown：每个 Provider 配置项增加 displayName 字段，缺省时 fallback 到默认名。
- 需求只在 Markdown：UI 上名称可编辑（输入框），保存后全局生效（对话列表、模型选择下拉框、消息来源标签）。
- 需求只在 Markdown：修改名称后，所有显示 Provider 的地方同步更新，无需重启。
- 需求只在 Markdown：内置 Provider 默认名作为 placeholder，自定义名持久化到配置。
- 需求只在 Markdown：目标：控制推理类模型（如 DeepSeek-R1、o1、Gemini Thinking）的思考深度/推理预算。
- 需求只在 Markdown：位置：聊天输入栏旁 / 模型选择面板；[CONFIG_KEY] = reasoningEffort。
- 需求只在 Markdown：提供 3~5 档可选：低 / 中 / 高 / 最高（映射为 minimal / low / medium / high / xhigh，按 provider 支持的枚举适配）。
- 需求只在 Markdown：仅在当前选中模型支持 reasoning 时显示该按钮。
- 需求只在 pdf：目标：支持自定义Provider（模型服务商）的显示名称。
- 需求只在 pdf：位置：Settings> Provider/模型提供商列表；Provider配置数据结构。
- 需求只在 pdf：行为：o每个Provider配置项增加displayName字段，缺省时fallback到默认名。o UI上名称可编辑（输入框），保存后全局生效（对话列表、模型选择下拉框、消息来源标签）。
- 需求只在 pdf：验收标准：o修改名称后，所有显示Provider的地方同步更新，无需重启。o内置Provider默认名作为placeholder，自定义名持久化到配置。
- 需求只在 pdf：目标：控制推理类模型（如DeepSeek-R1、o1、Gemini Thinking）的思考深度/推理预算。
- 需求只在 pdf：位置：聊天输入栏旁/模型选择面板；[CONFIG_KEY]=reasoningEffort。
- 需求只在 pdf：行为：o提供3~5档可选：低/中/高/最高（映射为minimal/low/ medium/high/xhigh，按provider支持的枚举适配）。o仅在当前选中模型支持reasoning时显示该按钮。o值写入请求体（如reasoning_effort/thinking参数），透传至对应API。
- 需求只在 pdf：验收标准：o切换档位后，下一次请求携带对应参数。o对不支持thinking的模型自动隐藏，且不传参。
- 需求只在 pdf：位置：Settings>聊天；[CONFIG_KEY]=streamingEnabled，默认true。
- 需求只在 pdf：行为：o开关关闭时，调用API使用非流式模式（stream=false），结果整体渲染。o开关实时生效，无需重启会话。

### raceychan__lihil

段落标题不一致，需求条目 3 / 76 一致（pdf 拆出 74 条）

- 标题只在 Markdown：Socket Channel 实时协议能力 PRD
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：2. 目标
- 标题只在 Markdown：3. 非目标
- 标题只在 Markdown：4. 现状
- 标题只在 pdf：Socket Channel实时协议能力PRD
- 标题只在 pdf：1.背景
- 标题只在 pdf：2.目标
- 标题只在 pdf：3.非目标
- 标题只在 pdf：4.现状
- 需求只在 Markdown：MessageEnvelope 包含 topic、event、payload。
- 需求只在 Markdown：Topic("room:{room_id}") 能把 topic pattern 编译为带命名参数的正则。
- 需求只在 Markdown：ChannelBase 提供 on_join()、on_message(env)、on_leave()。
- 需求只在 Markdown：ChannelBase.publish() 和 emit() 能通过 bus 向当前 resolved topic fanout。
- 需求只在 Markdown：SocketSession.handle_message() 处理 join、leave 和普通事件。
- 需求只在 Markdown：SocketHub.channel() 注册 channel 类型，并按 topic pattern 匹配创建 channel。
- 需求只在 Markdown：SocketBus 默认实现为进程内 InMemorySocketBus。
- 需求只在 Markdown：Envelope 没有 ref、join_ref、event_id、seq 等字段。
- 需求只在 Markdown：join 成功不会返回标准 ack，duplicate join 也不会给客户端明确反馈。
- 需求只在 Markdown：文档提到的 on_<event> 自动分发尚未在代码中实现。
- 需求只在 pdf：MessageEnvelope包含topic、event、payload。
- 需求只在 pdf：Topic("room:{room_id}")能把topic pattern编译为带命名参数的正则。
- 需求只在 pdf：ChannelBase提供on_join()、on_message(env)、on_leave()。
- 需求只在 pdf：ChannelBase.publish()和emit()能通过bus向当前resolved topic fanout。
- 需求只在 pdf：SocketSession.handle_message()处理join、leave和普通事件。
- 需求只在 pdf：SocketHub.channel()注册channel类型，并按topic pattern匹配创建channel。
- 需求只在 pdf：SocketBus默认实现为进程内InMemorySocketBus。
- 需求只在 pdf：Envelope没有ref、join_ref、event_id、seq等字段。
- 需求只在 pdf：join成功不会返回标准ack，duplicate join也不会给客户端明确反馈。
- 需求只在 pdf：文档提到的on_<event>自动分发尚未在代码中实现。

### rzx007__nanobot-ts

段落标题不一致，需求条目 16 / 97 一致（pdf 拆出 67 条）

- 标题只在 Markdown：Nanobot TypeScript 版本 - 产品需求文档 (PRD)
- 标题只在 Markdown：1. 概述
- 标题只在 Markdown：1.1 产品目标
- 标题只在 Markdown：1.2 产品愿景
- 标题只在 Markdown：1.3 技术选型
- 标题只在 pdf：Nanobot TypeScript版本-产品需求文档(PRD)
- 标题只在 pdf：1.概述
- 标题只在 pdf：1.1产品目标
- 标题只在 pdf：1.2产品愿景
- 标题只在 pdf：1.3技术选型
- 需求只在 Markdown：类别：LLM SDK；选择：@ai-sdk (Vercel AI SDK)；理由：统一的提供商接口，支持 OpenAI、Anthropic、OpenRouter 等
- 需求只在 Markdown：需求：在多个聊天应用(WhatsApp, Feishu, Email)上有一个智能助手
- 需求只在 Markdown：需求：快速集成 AI 代理到现有应用
- 需求只在 Markdown：场景：添加新的聊天渠道、自定义工具、修改 Agent 行为
- 需求只在 Markdown：关键功能：插件系统、工具 API、事件钩子
- 需求只在 Markdown：需求：研究 AI 代理架构，修改核心逻辑
- 需求只在 Markdown：✅ 配置文件生成自动化
- 需求只在 Markdown：✅ 首次使用有引导提示
- 需求只在 Markdown：✅ 消息路由延迟 < 50ms
- 需求只在 Markdown：✅ 支持媒体文件处理
- 需求只在 pdf：需求：在多个聊天应用(WhatsApp,Feishu,Email)上有一个智能助手
- 需求只在 pdf：需求：快速集成AI代理到现有应用
- 需求只在 pdf：场景：添加新的聊天渠道、自定义工具、修改Agent行为
- 需求只在 pdf：关键功能：插件系统、工具API、事件钩子
- 需求只在 pdf：需求：研究AI代理架构，修改核心逻辑
- 需求只在 pdf：✅配置文件生成自动化
- 需求只在 pdf：✅首次使用有引导提示
- 需求只在 pdf：✅消息路由延迟< 50ms
- 需求只在 pdf：✅支持媒体文件处理
- 需求只在 pdf：✅文件读写工具

### sameencai__KarvisForYou

段落标题不一致，需求条目 46 / 130 一致（pdf 拆出 151 条）

- 标题只在 Markdown：KarvisForAll 需求文档
- 标题只在 Markdown：1.1 背景
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 与 Karvis-opensource 的关系
- 标题只在 Markdown：1.4 核心原则
- 标题只在 pdf：KarvisForAll需求文档
- 标题只在 pdf：1.1背景
- 标题只在 pdf：1.2项目定位
- 标题只在 pdf：1.3与Karvis-opensource的关系
- 标题只在 pdf：1.4核心原则
- 需求只在 Markdown：数据隔离：用户 A 绝不能看到用户 B 的任何数据
- 需求只在 Markdown：成本可控：管理员能监控和控制总体 LLM 开销
- 需求只在 Markdown：通过环境变量配置 LLM API Key、企微应用参数
- 需求只在 Markdown：通过 Web 管理页面查看：用户列表、各用户消息量、LLM token 用量
- 需求只在 Markdown：在企微中直接给 Karvis 发消息（文字/语音/图片/视频/链接）
- 需求只在 Markdown：通过对话设置个人偏好（昵称、AI 人格风格等）
- 需求只在 Markdown：通过 Web 页面查看自己的数据（只读）
- 需求只在 Markdown：系统检测到 user_id 不在用户注册表中
- 需求只在 Markdown：新用户发送任意消息后，5 秒内收到欢迎引导 + 消息处理结果
- 需求只在 Markdown：不影响其他用户的正常使用
- 需求只在 pdf：数据隔离：用户A绝不能看到用户B的任何数据
- 需求只在 pdf：成本可控：管理员能监控和控制总体LLM开销
- 需求只在 pdf：通过环境变量配置LLM API Key、企微应用参数
- 需求只在 pdf：通过Web管理页面查看：用户列表、各用户消息量、LLM token用量
- 需求只在 pdf：在企微中直接给Karvis发消息（文字/语音/图片/视频/链接）
- 需求只在 pdf：通过对话设置个人偏好（昵称、AI人格风格等）
- 需求只在 pdf：通过Web页面查看自己的数据（只读）
- 需求只在 pdf：系统检测到user_id不在用户注册表中
- 需求只在 pdf：新用户发送任意消息后，5秒内收到欢迎引导+消息处理结果
- 需求只在 pdf：不影响其他用户的正常使用F2：用户注册表

### sarahwangy__knowho

段落标题不一致，需求条目 0 / 66 一致（pdf 拆出 32 条）

- 标题只在 Markdown：1. 产品愿景
- 标题只在 Markdown：2. 用户画像
- 标题只在 Markdown：3. 功能范围与优先级
- 标题只在 Markdown：4. Ticket 拆解
- 标题只在 Markdown：P0 — 核心层（先做，撑起产品价值）
- 标题只在 pdf：1.产品愿景
- 标题只在 pdf：2.用户画像
- 标题只在 pdf：3.功能范围与优先级
- 标题只在 pdf：4. Ticket拆解
- 标题只在 pdf：P0 —核心层（先做，撑起产品价值）
- 需求只在 Markdown：描述： 设计并实现最简录入表单，字段：姓名（必填）、认识场合、一句话印象、标签（可多选）。表单需在移动端一屏内完成，不滚动。
- 需求只在 Markdown：从打开到提交 ≤ 30秒（实测）
- 需求只在 Markdown：移动端（375px）一屏内可完成
- 需求只在 Markdown：姓名为唯一必填项，其余可跳过
- 需求只在 Markdown：提交后跳转到该人的档案页
- 需求只在 Markdown：估时： 3天（含设计稿 + 前端实现）
- 需求只在 Markdown：描述： POST /api/contacts 接口，接收联系人基础信息，写入数据库，返回新建记录 ID。
- 需求只在 Markdown：接口返回 201，包含 contact_id
- 需求只在 Markdown：姓名为空时返回 400 + 错误信息
- 需求只在 Markdown：数据落库，可通过 GET /api/contacts/:id 查询
- 需求只在 pdf：描述：设计并实现最简录入表单，字段：姓名（必填）、认识场合、一句话印象、标签（可多选）。表单需在移动端一屏内完成，不滚动。
- 需求只在 pdf：验收标准：☐从打开到提交≤30秒（实测）☐移动端（375px）一屏内可完成☐姓名为唯一必填项，其余可跳过☐提交后跳转到该人的档案页
- 需求只在 pdf：估时：3天（含设计稿+前端实现）
- 需求只在 pdf：描述：POST/api/contacts接口，接收联系人基础信息，写入数据库，返回新建记录ID。
- 需求只在 pdf：验收标准：☐接口返回201，包含contact_id ☐姓名为空时返回400 +错误信息☐数据落库，可通过GET/api/contacts/:id查询
- 需求只在 pdf：描述：提供预设标签（读书会、健身群、邻居、工作、社群、家人、其他），支持用户新建自定义标签。标签存为独立实体，联系人与标签多对多关联。
- 需求只在 pdf：验收标准：☐预设标签在新建表单中可直接点选☐可新建自定义标签并即时使用☐标签列表页可按标签筛选联系人
- 需求只在 pdf：描述：展示单个联系人完整信息：头像/姓名、标签、认识场合、重要日期、互动时间线（倒序）、备注。顶部固定"见面前提示卡"入口（P1阶段实现内容，P0先留位置）。
- 需求只在 pdf：验收标准：☐所有字段正确展示☐时间线按时间倒序排列☐支持编辑入口（跳转编辑页）☐移动端布局正常
- 需求只在 pdf：描述：实现GET/api/contacts/:id、PATCH/api/contacts/:id、DELETE /api/contacts/:id。

### shangbian__Enterprise-Brain-Platform

段落标题一致，需求条目 16 / 23 一致（pdf 拆出 50 条）

- 需求只在 Markdown：5.2.2 数据接入与知识构建 5.2.2.1需求描述 用户根据诊断建议，需要将核心业务系统（如ERP）的数据接入平台，并上传企业积累的非结构化知识文档（如工艺文件、质量标准），为后续分析和应用构建数据和知识基础。 5.2.2.2业务流程
- 需求只在 Markdown：平台需提供常见企业系统（ERP, MES等）的连接器，并支持通用接口（API, DB）和文件上传。
- 需求只在 Markdown：知识库需支持多种常见文档格式的解析（OCR, NLP）。
- 需求只在 Markdown：查询和渲染性能需优化，以支持大数据量下的快速响应。
- 需求只在 Markdown：5.5 后台功能需求 5.5.1 知识管理平台 5.5.1.1需求描述 提供对企业结构化和非结构化知识进行全生命周期管理的功能，包括知识的采集、处理、存储、组织和应用支持。 5.5.1.2业务流程 管理员或知识贡献者通过平台上传文档、管理FAQ、配置知识源、进行内容标注、设置敏感词等。系统自动对文档进行切分、索引。知识库内容供前台问答、AI模型训练等使用。 5.5.1.3页面原型
- 需求只在 Markdown：支持多种格式文档（Word, PDF, Excel, 图片等）的导入和解析（含OCR）。
- 需求只在 Markdown：支持多种调度策略（定时、周期、事件触发、依赖关系）。
- 需求只在 pdf：1.3页面原型5 5.1.4业务规则（核心原则）5 5.2用户旅程6 5.2.1初始配置与诊断6
- 需求只在 pdf：2.2数据接入与知识构建7 5.2.3自主分析与可视化8 5.2.4 Agent助手搭建与应用9
- 需求只在 pdf：2.5持续监控与优化10 5.3前端功能需求11 5.3.1 PC端（浏览器）11 5.3.2移动端（supMobile/企业微信/飞书/钉钉）12 5.4 AI工具中心功能需求13 5.4.1需求描述13
- 需求只在 pdf：4.2业务流程13 5.4.3页面原型（主要工具）13 5.4.4业务规则13 5.5后台功能需求14
- 需求只在 pdf：5.1知识管理平台14 5.5.2模型管理平台15 5.5.3数据管理平台16 5.5.4用户中心21
- 需求只在 pdf：5.5任务调度21 5.5.6 AI能力开放平台22 5.6大脑能力中心22 5.6.1基础能力22 5.6.2数据能力23 5.6.3辅助决策能力23 5.6.4行业赋能能力23 5.7大模型、Agent及知识库管理24 5.7.1需求描述24 5.7.2业务流程24 5.7.3页面原型24 5.7.4业务规则24
- 需求只在 pdf：1 2025年目标与战略5.1.1需求描述为应对2025年市场挑战，企业大脑平台确立以"标准化"为核心突破方向，结合技术架构轻量化、大模型深度赋能、弹性商业模式创新，并通过分阶段实施保障战略落地，构建差异化竞争力。5.1.2业务流程（战略实施步骤）
- 需求只在 pdf：2用户旅程5.2.1初始配置与诊断5.2.1.1需求描述用户（如制造运营经理李明）首次登录平台，希望快速了解可用功能，并通过诊断工具了解自身信息化水平，获得个性化的企业大脑建设起点和路径建议，快速体验初步价值（如知识问答）。5.2.1.2业务流程
- 需求只在 pdf：2.2数据接入与知识构建5.2.2.1需求描述用户根据诊断建议，需要将核心业务系统（如ERP）的数据接入平台，并上传企业积累的非结构化知识文档（如工艺文件、质量标准），为后续分析和应用构建数据和知识基础。5.2.2.2业务流程
- 需求只在 pdf：平台需提供常见企业系统（ERP,MES等）的连接器，并支持通用接口（API,DB）和文件上传。

### shikanon__cookies

段落标题不一致，需求条目 39 / 94 一致（pdf 拆出 92 条）

- 标题只在 Markdown：广告需求收集及策略分析 PRD
- 标题只在 Markdown：1. 产品定义
- 标题只在 Markdown：2. 产品目标
- 标题只在 Markdown：Project 关联
- 标题只在 Markdown：3. 用户与核心场景
- 标题只在 pdf：广告需求收集及策略分析PRD
- 标题只在 pdf：1.产品定义
- 标题只在 pdf：2.产品目标
- 标题只在 pdf：Project关联
- 标题只在 pdf：3.用户与核心场景
- 需求只在 Markdown：本模块是 cookies 的默认入口。用户不需要先理解广告术语或填写长表单，只需像与广告策略顾问沟通一样描述目标。Codex 负责理解上下文、规划下一步并调用合适的广告 Skills；Skills 负责需求采集、品牌知识、受众洞察、策略规划、合规检查和产物生成。
- 需求只在 Markdown：Project 是四系统共同的全局上下文，由共享基座拥有；本系统不再创建另一类"项目"。
- 需求只在 Markdown：StrategyWorkspace、Conversation、Brief、ResearchArtifact、Strategy、StrategyExperiment 和 StrategyReview 必须携带非空 project_id。
- 需求只在 Markdown：一个 Project 默认创建一个主策略工作区；按市场、产品或阶段拆分时可创建多个，但工作区只属于一个 Project。
- 需求只在 Markdown：策略批准后只允许默认交接到同一 Project 的创意或投放对象；跨 Project 复用使用复制/引用动作并保存来源 Project 与版本。
- 需求只在 Markdown：导航权限按 strategy.* 动作计算，不复用其他系统业务角色。
- 需求只在 Markdown：全局 Provider、知识库和用户管理通过 /admin/* 打开，不复制到本系统设置。
- 需求只在 Markdown：Skill：brand-context；触发场景：需要品牌事实或规范；核心输入：品牌 ID、任务范围；主要输出：定位、语气、必说信息、禁用项
- 需求只在 Markdown：Skill：audience-insight；触发场景：需要拆解目标人群；核心输入：产品、目标、历史数据；主要输出：人群分层、痛点、触发场景、假设
- 需求只在 Markdown：Skill：asset-experience；触发场景：需要引用历史素材经验；核心输入：品牌、渠道、广告类型；主要输出：可复用经验、失败模式、适用条件
- 需求只在 pdf：本模块是cookies的默认入口。用户不需要先理解广告术语或填写长表单，只需像与广告策略顾问沟通一样描述目标。Codex负责理解上下文、规划下一步并调用合适的广告Skills；Skills负责需求采集、品牌知识、受众洞察、策略规划、合规检查和产物生成。
- 需求只在 pdf：Project是四系统共同的全局上下文，由共享基座拥有；本系统不再创建另一类"项目"。
- 需求只在 pdf：StrategyWorkspace、Conversation、Brief、ResearchArtifact、Strategy、StrategyExperiment和StrategyReview必须携带非空project_id。
- 需求只在 pdf：一个Project默认创建一个主策略工作区；按市场、产品或阶段拆分时可创建多个，但工作区只属于一个Project。
- 需求只在 pdf：策略批准后只允许默认交接到同一Project的创意或投放对象；跨Project复用使用复制/引用动作并保存来源Project与版本。
- 需求只在 pdf：导航权限按strategy.*动作计算，不复用其他系统业务角色。
- 需求只在 pdf：全局Provider、知识库和用户管理通过/admin/*打开，不复制到本系统设置。
- 需求只在 pdf：需要品牌事实或品牌ID、任务定位、语气、必规范说信息、禁用项
- 需求只在 pdf：需要拆解目标人产品、目标、历人群分层、痛
- 需求只在 pdf：需要引用历史素品牌、渠道、广可复用经验、失

### skywind3000__toys

段落标题不一致，需求条目 3 / 76 一致（pdf 拆出 65 条）

- 标题只在 Markdown：请求（仿 PHP 超全局变量命名）
- 标题只在 Markdown：说明
- 标题只在 Markdown：站点本地模块 import
- 标题只在 pdf：请求（仿PHP超全局变量命名）
- 标题只在 pdf：站点本地模块import
- 需求只在 Markdown：使用 Mako + Flask 做一个类似 PHP 的系统。使用 MakoServer 以后，用户新建动态页面或者纯 HTTP/JSON 接口，只需要在文档根目录内新增 .mako 文件即可，不用改到 Flask。
- 需求只在 Markdown：.mako 模板本质是执行任意 Python 代码，等同本机运行脚本，使用者须知悉。
- 需求只在 Markdown：基于 Mako / Flask，提供一套类似 .php 的网页服务；
- 需求只在 Markdown：用户请求 http://localhost:5000/web/demo.mako 的话，就会解析出相对路径，到文档根目录下寻找对应 .mako 文件并渲染返回；
- 需求只在 Markdown：启动后指定一个文档根目录，就能为下面的所有 .mako 脚本提供页面服务，用户写新的动态页面，新增 .mako 文件就行，不必改 Flask 端任何一行代码；
- 需求只在 Markdown：防止 .mako 源码以静态文件形式泄露：扩展名判断大小写不敏感，且基于规范化后的真实路径判断（防范 Windows 下 demo.MAKO、尾部点 demo.mako.、NTFS 数据流 demo.mako::$DATA 等写法绕过扩展名检查、走静态分支吐出模板源码；尾部点剥除仅 Windows 主动特判——Linux 下此类字面文件名不存在、自然 404 fail-closed，有意跨平台分裂）；
- 需求只在 Markdown：服务自身与配置的防回吐：makoserver.py 自身与 makoserver.ini（.py / .ini 均不在静态白名单，天然 404）、实际加载命中的配置文件、已配置的日志文件（后两者路径启动时记录，请求解析全程对最终目标文件比对——初始路径先行、PATH_INFO 回溯与 index 兜底解析出的目标终点收口，命中即 404）——比对覆盖静态分支（回吐 secret 与访客日志）与模板分支（日志 / 配置若起名 *.mako 会被当模板编译执行），回溯与兜底旁路同堵；
- 需求只在 Markdown：如果请求映射到目录（含 /）：URL 末尾无 / 时先 301 重定向补斜杠（对齐 Apache DirectorySlash，防页内相对链接错链），再依次尝试追加 index.mako、index.html、index.htm；
- 需求只在 Markdown：支持 PHP 的 PATH_INFO 尾挂机制：请求 xxx.mako/尾挂路径（如 /index.mako/hello）时渲染 xxx.mako，尾挂部分（/hello）经 _SERVER['PATH_INFO'] 传入，脚本可据此实现漂亮 URL 路由（无需 query string）；静态文件不带尾挂（style.css/hello → 404）；尾挂中的 ../ 已被路径规范化先行钳制，不构成穿透；
- 需求只在 Markdown：Flask 端提供 bridge 函数/对象供 .mako 脚本使用，详见下文「Bridge API」一节；
- 需求只在 pdf：使用Mako + Flask做一个类似PHP的系统。使用MakoServer以后，用户新建动态页面或者纯HTTP/JSON接口，只需要在文档根目录内新增.mako文件即可，不用改到Flask。
- 需求只在 pdf：.mako模板本质是执行任意Python代码，等同本机运行脚本，使用者须知悉。
- 需求只在 pdf：基于Mako /Flask，提供一套类似.php的网页服务；
- 需求只在 pdf：用户请求http://localhost:5000/web/demo.mako的话，就会解析出相对路径，到文档根目录下寻找对应.mako文件并渲染返回；
- 需求只在 pdf：启动后指定一个文档根目录，就能为下面的所有.mako脚本提供页面服务，用户写新的动态页面，新增.mako文件就行，不必改Flask端任何一行代码；
- 需求只在 pdf：防止.mako源码以静态文件形式泄露：扩展名判断大小写不敏感，且基于规范化后的真实路径判断（防范Windows下demo.MAKO、尾部点demo.mako.、NTFS数据流demo.mako::$DATA等写法绕过扩展名检查、走静态分支吐出模板源码；尾部点剥除仅Windows主动特判——Linux下此类字面文件名不存在、自然404 fail-closed，有意跨平台分裂）；
- 需求只在 pdf：服务自身与配置的防回吐：makoserver.py自身与makoserver.ini（.py/ .ini均不在静态白名单，天然404）、实际加载命中的配置文件、已配置的日志文件（后两者路径启动时记录，请求解析全程对最终目标文件比对——初始路径先行、PATH_INFO回溯与index兜底解析出的目标终点收口，命中即404）——比对覆盖静态分支（回吐secret与访客日志）与模板分支（日志/配置若起名*.mako会被当模板编译执行），回溯与兜底旁路同堵；
- 需求只在 pdf：如果请求映射到目录（含/）：URL末尾无/时先301重定向补斜杠（对齐Apache DirectorySlash，防页内相对链接错链），再依次尝试追加index.mako、index.html、index.htm；
- 需求只在 pdf：支持PHP的PATH_INFO尾挂机制：请求xxx.mako/尾挂路径（如/index.mako/hello）时渲染xxx.mako，尾挂部分（/hello）经_SERVER['PATH_INFO']传入，脚本可据此实现漂亮URL路由（无需query string）；静态文件不带尾挂（style.css/hello→404）；尾挂中的../已被路径规范化先行钳制，不构成穿透；
- 需求只在 pdf：Flask端提供bridge函数/对象供.mako脚本使用，详见下文「Bridge API」一节；

### staklab__jianji

段落标题不一致，需求条目 266 / 321 一致（pdf 拆出 321 条）

- 标题只在 Markdown：简记文档中心 PRD
- 标题只在 Markdown：1. 文档信息
- 标题只在 Markdown：2. 背景与目标
- 标题只在 Markdown：3. 产品定位
- 标题只在 Markdown：4. 当前项目现状
- 标题只在 pdf：简记文档中心PRD
- 标题只在 pdf：1.文档信息
- 标题只在 pdf：2.背景与目标
- 标题只在 pdf：3.产品定位
- 标题只在 pdf：4.当前项目现状
- 需求只在 Markdown：样式方案：Tailwind CSS v4，已定义液态玻璃风格的色彩和字体 token。
- 需求只在 Markdown：UI 模块：Dashboard、DocView、ProjectView、Sidebar、Header。
- 需求只在 Markdown：依赖中已有 express、dotenv、tsx，但当前未发现服务端入口。
- 需求只在 Markdown：数据表：当前为任务表格静态 UI，并提供表格、看板、甘特图切换按钮外观。
- 需求只在 Markdown：URL 路由与深层链接。
- 需求只在 Markdown：后端 API、数据库和文件存储。
- 需求只在 Markdown：Excel 式表格、公式、筛选、排序、视图。
- 需求只在 Markdown：支持 Markdown 快捷输入。
- 需求只在 Markdown：支持文档导出为 Markdown、HTML、PDF。
- 需求只在 Markdown：支持从 Markdown 导入文档。
- 需求只在 pdf：样式方案：Tailwind CSS v4，已定义液态玻璃风格的色彩和字体token。
- 需求只在 pdf：UI模块：Dashboard、DocView、ProjectView、Sidebar、Header。
- 需求只在 pdf：依赖中已有express、dotenv、tsx，但当前未发现服务端入口。
- 需求只在 pdf：数据表：当前为任务表格静态UI，并提供表格、看板、甘特图切换按钮外观。
- 需求只在 pdf：URL路由与深层链接。
- 需求只在 pdf：后端API、数据库和文件存储。
- 需求只在 pdf：Excel式表格、公式、筛选、排序、视图。
- 需求只在 pdf：支持Markdown快捷输入。
- 需求只在 pdf：支持文档导出为Markdown、HTML、PDF。
- 需求只在 pdf：支持从Markdown导入文档。

### superman1006__MeetMind

段落标题不一致，需求条目 7 / 67 一致（pdf 拆出 58 条）

- 标题只在 Markdown：MeetMind 产品需求文档（PRD）
- 标题只在 Markdown：0. 阅读指南：编号与符号约定
- 标题只在 Markdown：1. 文档说明
- 标题只在 Markdown：1.1 文档目的
- 标题只在 Markdown：1.2 读者对象
- 标题只在 pdf：MeetMind产品需求文档（PRD）
- 标题只在 pdf：0.阅读指南：编号与符号约定
- 标题只在 pdf：1.文档说明
- 标题只在 pdf：1.1文档目的
- 标题只在 pdf：1.2读者对象
- 需求只在 Markdown：符号：P0 / P1 / P2；英文 / 全称：Priority；中文含义：优先级；用来做什么：标记一条需求有多重要、多紧急。数字越小越重要：P0 = 必须做（不做产品就不能上线），P1 = 重要，P2 = 锦上添花、可延后。（本文目前只用到 P0~P2；有些团队还会用 P3 表示"想到了但暂不做"）；例子：「用户登录」是 P0；「会话分组」是 P2
- 需求只在 Markdown：符号：G1 / G2 / G3 ...；英文 / 全称：Goal；中文含义：业务目标；用来做什么：给"我们想达成什么"编号，方便后面引用。G = Goal。见第 3 章；例子：G1 = 支持多用户安全使用
- 需求只在 Markdown：符号：OQ；英文 / 全称：Open Question；中文含义：待澄清问题；用来做什么：还没拍板、需要进一步确认的点；例子：见 11.4
- 需求只在 Markdown：指导排期：给出里程碑与路线图（Section 9），作为研发拆 Story、估时、验收的依据。
- 需求只在 Markdown：优先级：P0；含义：核心路径 / 多用户上线的前置必备能力，缺失则产品不可对外；排期预期：必须在对应里程碑交付
- 需求只在 Markdown：优先级：P2；含义：增强型 / 锦上添花能力；排期预期：资源允许时交付，可延后
- 需求只在 Markdown：没有工具治理：Agent 可调用文件读取、进程查看等工具，但无权限策略、无风险分级、无沙箱、无人工审批，存在安全隐患。
- 需求只在 Markdown：容错薄弱：进行中的讨论一旦中断（关闭会话/进程退出）即丢失，无 checkpoint / 恢复 / 重发能力。
- 需求只在 Markdown：编排单一：只有"架构师 + 各 Agent 自主选下一个"一种路由模式，缺少面向不同需求类型的固定工作流。
- 需求只在 Markdown：运维不友好：模型 URL / Key / 名称 / 温度等只能改 .env 重启，无法在前端配置。
- 需求只在 pdf：指导排期：给出里程碑与路线图（Section 9），作为研发拆Story、估时、验收的依据。
- 需求只在 pdf：优先级含义排期预期P0核心路径/多用户上线必须在对应里程碑交付的前置必备能力，缺失则产品不可对外P1显著提升体验或可运维尽量在对应里程碑交付性的重要能力P2增强型/锦上添花能力资源允许时交付，可延后
- 需求只在 pdf：没有工具治理：Agent可调用文件读取、进程查看等工具，但无权限策略、无风险分级、无沙箱、无人工审批，存在安全隐患。
- 需求只在 pdf：容错薄弱：进行中的讨论一旦中断（关闭会话/进程退出）即丢失，无checkpoint /恢复/重发能力。
- 需求只在 pdf：编排单一：只有"架构师+各Agent自主选下一个"一种路由模式，缺少面向不同需求类型的固定工作流。
- 需求只在 pdf：运维不友好：模型URL / Key /名称/温度等只能改.env重启，无法在前端配置。
- 需求只在 pdf：能力有缺口：会话标题需手动改、无todolist、RAG无query改写、不支持文件作为消息输入、无上下文用量与压缩策略。
- 需求只在 pdf：对用户：把"开一次跨职能需求评审会"压缩成一次对话，几分钟内得到结构化结论+分工待办。
- 需求只在 pdf：对团队：每个Agent绑定本职知识库与工具，输出贴合角色、可直接落地。
- 需求只在 pdf：对平台：可扩展的工具/工作流/知识库体系，使其能从需求评审扩展到更多协作场景。

### terryso__ccpet

段落标题不一致，需求条目 12 / 44 一致（pdf 拆出 48 条）

- 标题只在 Markdown：状态栏宠物 产品需求文档 (PRD)
- 标题只在 Markdown：版本: 0.1
- 标题只在 Markdown：1. 目标与背景 (Goals and Background Context)
- 标题只在 Markdown：目标 (Goals)
- 标题只在 Markdown：背景 (Background Context)
- 标题只在 pdf：状态栏宠物产品需求文档(PRD)
- 标题只在 pdf：版本:0.1
- 标题只在 pdf：1.目标与背景(Goals and Background Context)
- 标题只在 pdf：2.需求(Requirements)
- 标题只在 pdf：3.用户界面设计目标(User Interface Design Goals)
- 需求只在 Markdown：FR1: 系统必须在 Claude Code 状态栏中持续显示一个由 ASCII 字符组成的宠物。
- 需求只在 Markdown：FR2: 宠物旁边必须显示一个可视化的能量条，用以表示其当前状态。
- 需求只在 Markdown：FR3: 当用户在编辑器中产生编码活动（消耗Token）时，宠物的能量条必须增加。
- 需求只在 Markdown：FR4: 当用户在设定的一段时间内没有编码活动时，宠物的能量条必须减少。
- 需求只在 Markdown：FR5: 宠物的 ASCII 表情必须根据能量条的数值自动变化，以反映其不同状态（如开心、饥饿、生病、死亡）。
- 需求只在 Markdown：FR6: 用户必须能通过一个特定的命令来"领养"一只新宠物，以重置死亡后的状态。
- 需求只在 Markdown：NFR1: 扩展程序必须是高性能且轻量级的，其对 IDE 的 CPU 和内存占用必须降到最低，不能对用户的编码体验产生可感知的性能影响。
- 需求只在 Markdown：NFR2: 所有的状态更新都必须是环境式(ambient)和非干扰性的，不能使用弹窗或系统通知。
- 需求只在 Markdown：NFR3: 扩展程序的所有数据和逻辑必须完全在用户本地运行和存储，不得向任何外部服务器发送任何与用户代码或使用习惯相关的数据，以保障隐私。
- 需求只在 Markdown：NFR4: 扩展程序必须能在所有支持 Claude Code 的操作系统上（Windows, macOS, Linux）稳定运行。
- 需求只在 pdf：FR1:系统必须在Claude Code状态栏中持续显示一个由ASCII字符组成的宠物。
- 需求只在 pdf：FR2:宠物旁边必须显示一个可视化的能量条，用以表示其当前状态。
- 需求只在 pdf：FR3:当用户在编辑器中产生编码活动（消耗Token）时，宠物的能量条必须增加。
- 需求只在 pdf：FR4:当用户在设定的一段时间内没有编码活动时，宠物的能量条必须减少。
- 需求只在 pdf：FR5:宠物的ASCII表情必须根据能量条的数值自动变化，以反映其不同状态（如开心、饥饿、生病、死亡）。
- 需求只在 pdf：FR6:用户必须能通过一个特定的命令来"领养"一只新宠物，以重置死亡后的状态。非功能性需求(Non-Functional Requirements)
- 需求只在 pdf：NFR1:扩展程序必须是高性能且轻量级的，其对IDE的CPU和内存占用必须降到最低，不能对用户的编码体验产生可感知的性能影响。
- 需求只在 pdf：NFR2:所有的状态更新都必须是环境式(ambient)和非干扰性的，不能使用弹窗或系统通知。
- 需求只在 pdf：NFR3:扩展程序的所有数据和逻辑必须完全在用户本地运行和存储，不得向任何外部服务器发送任何与用户代码或使用习惯相关的数据，以保障隐私。
- 需求只在 pdf：NFR4:扩展程序必须能在所有支持Claude Code的操作系统上（Windows,macOS, Linux）稳定运行。

### terryso__mcp-pinterest

段落标题不一致，需求条目 3 / 96 一致（pdf 拆出 49 条）

- 标题只在 Markdown：1. 引言
- 标题只在 Markdown：1.1 项目目标
- 标题只在 Markdown：1.2 范围
- 标题只在 Markdown：1.3 目标受众
- 标题只在 Markdown：2. 当前特性 (MVP - Minimum Viable Product)
- 标题只在 pdf：1.引言
- 标题只在 pdf：1.1项目目标
- 标题只在 pdf：1.2范围
- 标题只在 pdf：1.3目标受众
- 标题只在 pdf：2.当前特性(MVP - Minimum Viable Product)
- 需求只在 Markdown：本项目旨在开发一个遵循模型上下文协议 (Model Context Protocol, MCP) 的服务器。该服务器的核心功能是提供与 Pinterest 平台交互的能力，允许 MCP 客户端（如 IDE、AI 助手等）通过标准化的接口搜索 Pinterest 图片，获取图片信息，并将图片下载到指定位置。目的是为了方便将 Pinterest 的内容集成到各种支持 MCP 的工具和应用中。
- 需求只在 Markdown：实现基于 MCP 的服务器。
- 需求只在 Markdown：提供 pinterest_search Tool，根据关键词搜索图片。
- 需求只在 Markdown：提供 pinterest_get_image_info Tool，根据图片 ID 获取详细信息。
- 需求只在 Markdown：提供 pinterest_search_and_download Tool，根据关键词搜索并下载图片。
- 需求只在 Markdown：图片下载到固定的服务器端目录 (../downloads)。
- 需求只在 Markdown：文件名使用固定格式 (pinterest_{imageId}.{fileExtension})。
- 需求只在 Markdown：服务器应能处理并发请求（具体并发数待定）。
- 需求只在 Markdown：提供明确的错误信息给客户端。
- 需求只在 Markdown：(未来) 可配置性：下载目录和文件名模板可通过环境变量配置。
- 需求只在 pdf：本项目旨在开发一个遵循模型上下文协议(Model Context Protocol, MCP)的服务器。该服务器的核心功能是提供与Pinterest平台交互的能力，允许MCP客户端（如IDE、AI助手等）通过标准化的接口搜索Pinterest图片，获取图片信息，并将图片下载到指定位置。目的是为了方便将Pinterest的内容集成到各种支持MCP的工具和应用中。
- 需求只在 pdf：Functional requirements: o实现基于MCP的服务器。o提供pinterest_search Tool，根据关键词搜索图片。o提供pinterest_get_image_info Tool，根据图片ID获取详细信息。o提供pinterest_search_and_download Tool，根据关键词搜索并下载图片。o图片下载到固定的服务器端目录(../downloads)。o文件名使用固定格式(pinterest_{imageId}.{fileExtension})。
- 需求只在 pdf：Non-functional requirements: o服务器应能处理并发请求（具体并发数待定）。o提供明确的错误信息给客户端。o (未来)可配置性：下载目录和文件名模板可通过环境变量配置。
- 需求只在 pdf：User experience requirements:(主要针对客户端开发者) API接口清晰，易于使用。
- 需求只在 pdf：Integration requirements:遵循MCP协议规范。
- 需求只在 pdf：Compliance requirements:(待定，例如：是否需要遵守Pinterest API使用条款)}
- 需求只在 pdf：Story US-Future-001: Configurable Download Directory Status: 'Draft' Requirements: o通过MCP_PINTEREST_DOWNLOAD_DIR环境变量配置下载根目录。o未设置则使用默认../downloads。o启动时验证路径有效性和写入权限。o客户端无法指定路径。
- 需求只在 pdf：o通过MCP_PINTEREST_FILENAME_TEMPLATE环境变量配置全局文件名模板。o未设置则使用默认pinterest_{imageId}.{fileExtension}。o支持{imageId},{fileExtension},{timestamp},{index}变量。o验证模板有效性，清理非法字符，无效则回退默认模板。o客户端无法指定模板。
- 需求只在 pdf：内部文档: o架构文档:详细描述了系统组件、数据流和部署。
- 需求只在 pdf：核心库: o Model Context Protocol SDK:@modelcontextprotocol/sdk o Pinterest Scraper:@myno_21/pinterest-scraper

### terryso__tv-recommender-mcp-server

段落标题不一致，需求条目 3 / 88 一致（pdf 拆出 42 条）

- 标题只在 Markdown：1. Title: PRD for 美剧推荐 MCP 服务器
- 标题只在 Markdown：Status: 定稿 (v0.2)
- 标题只在 Markdown：Epic-1: 核心推荐工具 MVP
- 标题只在 Markdown：Epic-2: 增强与扩展 (Future Enhancement)
- 标题只在 Markdown：Epic-3: 个性化与集成 (Future Enhancement)
- 标题只在 pdf：1. Title: PRD for美剧推荐MCP服务器
- 标题只在 pdf：Status:定稿(v0.2)
- 标题只在 pdf：Epic-1:核心推荐工具MVP
- 标题只在 pdf：Epic-2:增强与扩展(Future Enhancement)
- 标题只在 pdf：Epic-3:个性化与集成(Future Enhancement)
- 需求只在 Markdown：本项目旨在开发一个 Model Context Protocol (MCP) 服务器，用于提供美剧推荐服务。该服务器将集成到支持 MCP 的大型语言模型 (LLM) 客户端（如 Claude Desktop）中，通过调用外部影视数据库 API（如 TMDb 或 TVmaze）来扩展 LLM 的能力，使用户能够通过自然语言交互获取实时、个性化和可解释的美剧推荐。
- 需求只在 Markdown：实现 MCP Server 基础框架 (TypeScript)。
- 需求只在 Markdown：实现与外部影视 API (TMDb 或 TVmaze) 的集成。
- 需求只在 Markdown：实现三个核心推荐工具的 MCP 接口。
- 需求只在 Markdown：实现工具内部调用 API、处理数据和格式化响应的逻辑。
- 需求只在 Markdown：实现基本的错误处理和日志记录。
- 需求只在 Markdown：性能: API 调用及处理的 P95 响应时间 < 2 秒。
- 需求只在 Markdown：可靠性: 工具调用成功率 > 95%。
- 需求只在 Markdown：安全性: API Key 安全存储和使用。
- 需求只在 Markdown：可维护性: 代码结构清晰，遵循 TypeScript 最佳实践。
- 需求只在 pdf：本项目旨在开发一个Model Context Protocol (MCP)服务器，用于提供美剧推荐服务。该服务器将集成到支持MCP的大型语言模型(LLM)客户端（如Claude Desktop）中，通过调用外部影视数据库API（如TMDb或TVmaze）来扩展LLM的能力，使用户能够通过自然语言交互获取实时、个性化和可解释的美剧推荐。
- 需求只在 pdf：功能性需求: o实现MCP Server基础框架(TypeScript)。o实现与外部影视API (TMDb或TVmaze)的集成。o实现三个核心推荐工具的MCP接口。o实现工具内部调用API、处理数据和格式化响应的逻辑。o实现基本的错误处理和日志记录。
- 需求只在 pdf：非功能性需求: o性能:API调用及处理的P95响应时间< 2秒。o可靠性:工具调用成功率> 95%。o安全性:API Key安全存储和使用。o可维护性:代码结构清晰，遵循TypeScript最佳实践。
- 需求只在 pdf：用户体验需求: o工具返回的推荐结果应清晰、相关且易于LLM理解和呈现。o错误信息应转化为用户友好的提示(❓Q6.2)。
- 需求只在 pdf：集成需求: o服务器需能被标准MCP客户端发现和调用。
- 需求只在 pdf：合规需求: o遵守所选外部API的服务条款和使用限制。
- 需求只在 pdf：Story 2.1: Keyword/Theme Based Discovery (story-2-1-keyword- discovery.md) Status: Draft Requirements:按关键词或主题发现影视剧。
- 需求只在 pdf：Story 2.2: Early Actor Works Discovery (story-2-2-early-works.md) Status: Draft Requirements:查看演员早期作品并按时间排序。
- 需求只在 pdf：Story 2.3: Detailed Episode Information and Interaction (story-2-3-episode- details.md) Status: Draft Requirements:查看单集详情（客串、评分、剧照）并支持单集评分。
- 需求只在 pdf：Story 2.4: Provider/Network/Company Content Aggregation (story-2-4- provider-aggregation.md) Status: Draft Requirements:按平台/网络/公司聚合浏览内容。

### tyrchen__index-tts-rs

段落标题不一致，需求条目 1 / 40 一致（pdf 拆出 32 条）

- 标题只在 Markdown：IndexTTS-2.5 Rust 高性能语音合成系统产品需求文档 (indextts-rust-prd)
- 标题只在 Markdown：1. 产品愿景与定位
- 标题只在 Markdown：1.1 双核产品形态
- 标题只在 Markdown：2. 目标用户与核心使用场景 (Personas & Use Cases)
- 标题只在 Markdown：3. 功能需求说明 (Functional Requirements)
- 标题只在 pdf：IndexTTS-2.5 Rust高性能语音合成系统产品需求文档(indextts-rust-prd)
- 标题只在 pdf：1.产品愿景与定位
- 标题只在 pdf：1.1双核产品形态
- 标题只在 pdf：2.目标用户与核心使用场景(Personas & Use Cases)
- 标题只在 pdf：3.功能需求说明(Functional Requirements)
- 需求只在 Markdown：内存与启动过重：原版 Python 方案常驻内存高达 4.8 GB，每次 CLI 启动需加载庞大的 Python 解释器与 transformers/librosa 依赖，冷启动耗时数秒。
- 需求只在 Markdown：难以被其他应用内嵌集成：Python 依赖复杂的虚拟环境（uv/conda），难以作为轻量级、类型安全的原生库（Crate）直接编译进桌面端应用、游戏引擎或高性能后端服务。
- 需求只在 Markdown：对 AI Agent 不友好：缺乏面向 Agent 的毫秒级常驻响应（Daemon）、结构化 JSON/JSONL 遥测输出、标准输入流式朗读（Streaming Stdin）以及原生 MCP (Model Context Protocol) 协议支持。
- 需求只在 Markdown：形态一：可嵌入式 Rust 核心库（Crate: index-tts-rs-core） 供第三方 Rust 开发者通过 cargo add 集成，提供编译期类型安全、零 unwrap、支持异步流式（Stream<Item = Result<AudioChunk>>）与 Actor 并发调度的原生 API。
- 需求只在 Markdown：形态二：面向 AI Agent 与开发者的全能命令行与服务套件（App: itts CLI & Server） 提供单二进制 CLI，内置 音色快照管理（.itts_voice）、自动驻留后台守护进程（Auto-Warm Daemon）、MCP Server (stdio) 以及 OpenAI 兼容 HTTP/WebSocket 语音接口。
- 需求只在 Markdown：FR-1.1 零样本音色提取：支持输入任意 3s ~ 15s 的常见音频文件（WAV / MP3 / FLAC / M4A，任意采样率与声道），自动完成重采样、特征提取并生成 SpeakerContext。
- 需求只在 Markdown：将提取出的 SpeakerContext（包含 conds、prompt_condition、ref_mel、style 四个张量）及元数据（源音频哈希、采样率、时长、创建时间、音色别名）保存为单文件 <name>.itts_voice（体积约 1.5 MB）。
- 需求只在 Markdown：当传入预编译的 .itts_voice 音色名或文件路径时，引擎完全跳过加载 w2v-bert-2.0（2.2GB）、EmoVec（622MB）和 CampPlus（27MB），仅加载 1.68 GB 合成主干权重即可直接合成。
- 需求只在 Markdown：支持默认「说话人音频兼作情感参考（emo_alpha = 1.0）」，同时支持可选传入第二段独立的情感参考音频（--emo-ref）与情感强度系数（--emo-alpha 0.0..=2.0），在提取阶段合成定制化的 conds = spk_cond + emo_alpha * emovec。
- 需求只在 Markdown：FR-2.1 多语种与混合语种支持：支持中文（zh）、英文（en）、日文（ja）、粤语（yue）及中英混合（zh/en）合成。
- 需求只在 pdf：内存与启动过重：原版Python方案常驻内存高达4.8 GB，每次CLI启动需加载庞大的Python解释器与transformers/librosa依赖，冷启动耗时数秒。
- 需求只在 pdf：难以被其他应用内嵌集成：Python依赖复杂的虚拟环境（uv/conda），难以作为轻量级、类型安全的原生库（Crate）直接编译进桌面端应用、游戏引擎或高性能后端服务。
- 需求只在 pdf：对AI Agent不友好：缺乏面向Agent的毫秒级常驻响应（Daemon）、结构化JSON/JSONL遥测输出、标准输入流式朗读（Streaming Stdin）以及原生MCP (Model Context Protocol)协议支持。
- 需求只在 pdf：形态一：可嵌入式Rust核心库（Crate:index-tts-rs-core）供第三方Rust开发者通过cargo add集成，提供编译期类型安全、零unwrap、支持异步流式（Stream<Item=Result<AudioChunk>>）与Actor并发调度的原生API。
- 需求只在 pdf：形态二：面向AI Agent与开发者的全能命令行与服务套件（App:itts CLI & Server）提供单二进制CLI，内置音色快照管理（.itts_voice）、自动驻留后台守护进程（Auto-Warm Daemon）、MCP Server (stdio)以及OpenAI兼容HTTP/WebSocket语音接口。
- 需求只在 pdf：FR-1.1零样本音色提取：支持输入任意3s~15s的常见音频文件（WAV/ MP3 / FLAC /M4A，任意采样率与声道），自动完成重采样、特征提取并生成SpeakerContext。
- 需求只在 pdf：FR-1.2轻量级.itts_voice音色快照持久化：o将提取出的SpeakerContext（包含conds、prompt_condition、ref_mel、style四个张量）及元数据（源音频哈希、采样率、时长、创建时间、音色别名）保存为单文件<name>.itts_voice（体积约1.5 MB）。
- 需求只在 pdf：FR-1.3纯合成免编码器加载（Encoder-Free Synthesis）：o当传入预编译的.itts_voice音色名或文件路径时，引擎完全跳过加载w2v-bert-2.0（2.2GB）、EmoVec（622MB）和CampPlus（27MB），仅加载1.68 GB合成主干权重即可直接合成。
- 需求只在 pdf：FR-1.4独立情感参考与混合控制（Emotion Blending）：o支持默认「说话人音频兼作情感参考（emo_alpha=1.0）」，同时支持可选传入第二段独立的情感参考音频（--emo-ref）与情感强度系数（-- emo-alpha 0.0..=2.0），在提取阶段合成定制化的conds=spk_cond + emo_alpha*emovec。
- 需求只在 pdf：FR-2.1多语种与混合语种支持：支持中文（zh）、英文（en）、日文（ja）、粤语（yue）及中英混合（zh/en）合成。

### tyxben__AI_novel

段落标题不一致，需求条目 10 / 168 一致（pdf 拆出 102 条）

- 标题只在 Markdown：PPT HTML-First 渲染方案需求文档
- 标题只在 Markdown：1. 项目背景
- 标题只在 Markdown：1.1 现状
- 标题只在 Markdown：1.2 问题
- 标题只在 Markdown：1.3 新策略
- 标题只在 pdf：PPT HTML-First渲染方案需求文档
- 标题只在 pdf：1.项目背景
- 标题只在 pdf：1.1现状
- 标题只在 pdf：1.2问题
- 标题只在 pdf：1.3新策略
- 需求只在 Markdown：9 阶段流水线：文档分析 → 内容提取 → 内容增强 → 演示计划 → 大纲生成 → 内容创作 → 设计编排 → 配图生成 → PPT 渲染
- 需求只在 Markdown：40+ Pydantic 数据模型（SlideSpec / SlideContent / SlideDesign / ColorScheme / FontSpec / DecorationSpec 等）
- 需求只在 Markdown：5 个视觉主题（modern / business / creative / tech / education）
- 需求只在 Markdown：12 种布局类型（title_hero / section_divider / text_left_image_right / data_highlight / timeline / comparison 等）
- 需求只在 Markdown：任务队列集成（_run_ppt_outline / _run_ppt_continue）
- 需求只在 Markdown：Web UI 有 PPT Tab（但按钮禁用中）
- 需求只在 Markdown：布局调整困难，需要手动计算每个元素的 left / top / width / height
- 需求只在 Markdown：调试成本高：每次调整都需要重新生成完整 .pptx 文件
- 需求只在 Markdown：装饰元素（渐变 / 形状 / 分割线）实现复杂
- 需求只在 Markdown：AI 生成 HTML 幻灯片（基于现有的 SlideSpec 数据）
- 需求只在 pdf：9阶段流水线：文档分析→内容提取→内容增强→演示计划→大纲生成→内容创作→设计编排→配图生成→PPT渲染
- 需求只在 pdf：40+ Pydantic数据模型（SlideSpec/ SlideContent / SlideDesign / ColorScheme / FontSpec / DecorationSpec等）
- 需求只在 pdf：5个视觉主题（modern/ business / creative / tech /education）
- 需求只在 pdf：12种布局类型（title_hero/ section_divider / text_left_image_right / data_highlight / timeline / comparison等）
- 需求只在 pdf：任务队列集成（_run_ppt_outline/_run_ppt_continue）
- 需求只在 pdf：Web UI有PPT Tab（但按钮禁用中）
- 需求只在 pdf：布局调整困难，需要手动计算每个元素的left / top / width / height
- 需求只在 pdf：调试成本高：每次调整都需要重新生成完整.pptx文件
- 需求只在 pdf：装饰元素（渐变/形状/分割线）实现复杂
- 需求只在 pdf：AI生成HTML幻灯片（基于现有的SlideSpec数据）

### weiwei929__wireguard_plus

段落标题不一致，需求条目 68 / 102 一致（pdf 拆出 94 条）

- 标题只在 Markdown：WireGuard Plus - 产品需求文档 (PRD)
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 项目目标
- 标题只在 Markdown：1.3 项目愿景
- 标题只在 pdf：WireGuard Plus -产品需求文档(PRD)
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目背景
- 标题只在 pdf：1.2项目目标
- 标题只在 pdf：1.3项目愿景
- 需求只在 Markdown：每种伪装模式能够正常转换WireGuard流量
- 需求只在 Markdown：伪装后的流量能够绕过基本的DPI检测
- 需求只在 Markdown：支持动态切换伪装模式
- 需求只在 Markdown：性能损失控制在30%以内
- 需求只在 Markdown：界面响应式设计，支持桌面和移动端
- 需求只在 Markdown：操作流程直观，新用户5分钟内能创建隧道
- 需求只在 Markdown：配置文件生成正确，客户端能正常连接
- 需求只在 Markdown：实时数据更新延迟不超过5秒
- 需求只在 Markdown：密钥生成符合WireGuard安全标准
- 需求只在 Markdown：IP地址分配无冲突
- 需求只在 pdf：1.1流量伪装引擎
- 需求只在 pdf：☐每种伪装模式能够正常转换WireGuard流量☐伪装后的流量能够绕过基本的DPI检测☐支持动态切换伪装模式☐性能损失控制在30%以内
- 需求只在 pdf：☐界面响应式设计，支持桌面和移动端☐操作流程直观，新用户5分钟内能创建隧道☐配置文件生成正确，客户端能正常连接☐实时数据更新延迟不超过5秒
- 需求只在 pdf：1.3配置管理系统
- 需求只在 pdf：☐密钥生成符合WireGuard安全标准☐IP地址分配无冲突☐配置验证能发现常见错误☐支持批量配置操作
- 需求只在 pdf：Web界面响应时间<2秒
- 需求只在 pdf：流量转换延迟增加< 50ms
- 需求只在 pdf：作为一个需要绕过网络限制的用户我希望能够简单地部署一个伪装的WireGuard服务以便于在受限网络环境下正常使用VPN服务
- 需求只在 pdf：作为一个系统管理员我希望能够批量管理多个用户的VPN配置以便于为组织提供统一的VPN服务
- 需求只在 pdf：作为一个网络工具开发者我希望能够扩展新的伪装模块以便于适应不断变化的网络环境

### wgcairui__airplay-receiver

段落标题不一致，需求条目 45 / 209 一致（pdf 拆出 132 条）

- 标题只在 Markdown：AirPlay接收端APP - 产品需求文档(PRD)
- 标题只在 Markdown：📖 产品概述
- 标题只在 Markdown：🎯 产品目标
- 标题只在 Markdown：👥 用户画像与使用场景
- 标题只在 Markdown：1. 移动办公族 - 张工程师
- 标题只在 pdf：AirPlay接收端APP-产品需求文档(PRD)
- 标题只在 pdf：📖产品概述
- 标题只在 pdf：🎯产品目标
- 标题只在 pdf：👥用户画像与使用场景
- 标题只在 pdf：🔧功能需求详述
- 需求只在 Markdown：应用启动时间 < 3秒
- 需求只在 Markdown：电池续航影响 < 15%/小时
- 需求只在 Markdown：背景: 软件工程师，经常需要多屏调试代码
- 需求只在 Markdown：需求: 将MacBook代码扩展到平板，提高开发效率
- 需求只在 Markdown：痛点: 外接显示器不便携，咖啡厅无法使用双屏
- 需求只在 Markdown：背景: UI/UX设计师，使用Mac进行设计工作
- 需求只在 Markdown：需求: 平板作为第二屏显示参考素材或预览效果
- 需求只在 Markdown：痛点: 需要大屏预览设计稿，iPad连接复杂
- 需求只在 Markdown：背景: 经常出差开会，需要展示PPT和数据
- 需求只在 Markdown：需求: 用平板作为便携展示屏，会议室投屏
- 需求只在 pdf：应用启动时间<3秒
- 需求只在 pdf：电池续航影响<15%/小时
- 需求只在 pdf：AirPlay服务发现与连接
- 需求只在 pdf：☐Mac能在AirPlay列表中发现OPPO Pad ☐连接成功率>95%（同一网络环境下）☐支持自动连接，无需额外验证步骤☐支持记住已配对设备，后续快速连接
- 需求只在 pdf：视频流接收与渲染
- 需求只在 pdf：验收标准: ☐支持1080p、4K分辨率切换☐延迟控制在50ms以内☐支持60fps、144fps帧率显示☐音画同步误差<40ms ☐长时间播放无卡顿和花屏
- 需求只在 pdf：双屏模式支持
- 需求只在 pdf：功能描述:支持镜像和扩展两种显示模式
- 需求只在 pdf：☐镜像模式画面比例正确无变形☐扩展模式支持独立窗口拖拽☐横竖屏切换响应时间<2秒☐支持Mac系统偏好设置中的显示器排列
- 需求只在 pdf：触控交互支持

### wordflowlab__novel-writer-openspec

段落标题不一致，需求条目 10 / 68 一致（pdf 拆出 258 条）

- 标题只在 Markdown：Novel-Writer-OpenSpec 产品需求文档（PRD）
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 核心价值主张
- 标题只在 Markdown：1. 清晰的上下文管理
- 标题只在 Markdown：2. 严格的规格格式
- 标题只在 pdf：Novel-Writer-OpenSpec产品需求文档（PRD）
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2核心价值主张
- 标题只在 pdf：1.3目标用户
- 标题只在 pdf：1.4核心问题与解决方案
- 需求只在 Markdown：借鉴理念：specs/（真相）+ changes/（提案）的双轨制结构
- 需求只在 Markdown：独立工具：使用 novelspec 命令，独立命名空间，避免与 OpenSpec 冲突
- 需求只在 Markdown：novelspec/specs/ 存储已确定的设定（角色、世界观、大纲）
- 需求只在 Markdown：novelspec/changes/ 管理待创作的章节和设定变更
- 需求只在 Markdown：AI 明确知道"当前真相"和"工作任务"
- 需求只在 Markdown：使用 Requirements + Scenarios 格式，让规格可验证
- 需求只在 Markdown：SHALL/MUST 关键词明确约束强度
- 需求只在 Markdown：ADDED/MODIFIED/REMOVED 清晰管理设定演进
- 需求只在 Markdown：novelspec validate 自动检查一致性
- 需求只在 Markdown：project.md 承载了创作原则和风格指南，相当于 novel-writer 的 constitution
- 需求只在 pdf：借鉴理念：specs/（真相）+changes/（提案）的双轨制结构
- 需求只在 pdf：独立工具：使用novelspec命令，独立命名空间，避免与OpenSpec冲突
- 需求只在 pdf：清晰的上下文管理
- 需求只在 pdf：novelspec/specs/存储已确定的设定（角色、世界观、大纲）
- 需求只在 pdf：novelspec/changes/管理待创作的章节和设定变更
- 需求只在 pdf：AI明确知道"当前真相"和"工作任务"
- 需求只在 pdf：严格的规格格式
- 需求只在 pdf：使用Requirements + Scenarios格式，让规格可验证
- 需求只在 pdf：SHALL/MUST关键词明确约束强度
- 需求只在 pdf：ADDED/MODIFIED/REMOVED清晰管理设定演进

### wordflowlab__novel-writer

段落标题不一致，需求条目 51 / 115 一致（pdf 拆出 112 条）

- 标题只在 Markdown：Novel Writer 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品名称
- 标题只在 Markdown：1.2 产品定位
- 标题只在 Markdown：1.3 目标用户
- 标题只在 pdf：Novel Writer产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品名称
- 标题只在 pdf：1.2产品定位
- 标题只在 pdf：1.3目标用户
- 需求只在 Markdown：参考 Spec-Kit 方法论的 AI 智能小说创作平台，采用规格驱动创作(Spec-Driven Writing)的理念，通过结构化的工作流程（风格设定→故事大纲→章节规划→任务分解→内容创作）来组织小说项目的创建和管理。专注于为中文内容创作者提供智能化的小说写作辅助能力，支持多种文体风格、角色管理、世界观构建等功能。
- 需求只在 Markdown：降低创作门槛：通过 AI 辅助简化创作流程，帮助新手快速上手
- 需求只在 Markdown：保证内容质量：AI 智能建议，保持风格一致性和逻辑连贯性
- 需求只在 Markdown：版本管理便捷：Git 集成，轻松管理创作版本
- 需求只在 Markdown：分阶段执行：遵循 style → story → outline → chapters → write 的渐进式流程
- 需求只在 Markdown：AI 增强：每个阶段都有 AI 智能辅助，提升创作质量
- 需求只在 Markdown：伏笔管理：伏笔设置和回收计划
- 需求只在 Markdown：优先级管理：P0-P3 的任务优先级
- 需求只在 Markdown：情节连贯：确保与前后章节的逻辑连接
- 需求只在 Markdown：生成 AI 助手配置文件
- 需求只在 pdf：参考Spec-Kit方法论的AI智能小说创作平台，采用规格驱动创作(Spec-Driven Writing)的理念，通过结构化的工作流程（风格设定→故事大纲→章节规划→任务分解→内容创作）来组织小说项目的创建和管理。专注于为中文内容创作者提供智能化的小说写作辅助能力，支持多种文体风格、角色管理、世界观构建等功能。
- 需求只在 pdf：降低创作门槛：通过AI辅助简化创作流程，帮助新手快速上手
- 需求只在 pdf：保证内容质量：AI智能建议，保持风格一致性和逻辑连贯性
- 需求只在 pdf：版本管理便捷：Git集成，轻松管理创作版本
- 需求只在 pdf：分阶段执行：遵循style → story → outline → chapters → write的渐进式流程
- 需求只在 pdf：AI增强：每个阶段都有AI智能辅助，提升创作质量
- 需求只在 pdf：style_type:文体风格（网文/文学/轻小说）
- 需求只在 pdf：principles:创作原则列表
- 需求只在 pdf：生成.specify/memory/writing-constitution.md
- 需求只在 pdf：包含完整的风格规范文档

### wth461694678__text-block-timer

段落标题不一致，需求条目 10 / 75 一致（pdf 拆出 69 条）

- 标题只在 Markdown：📋 PRD: Core Timer
- 标题只在 Markdown：1.1 需求来源
- 标题只在 Markdown：1.2 核心痛点
- 标题只在 Markdown：1.3 目标
- 标题只在 Markdown：4.1 计时器数据结构
- 标题只在 pdf：📋PRD: Core Timer
- 标题只在 pdf：1.1需求来源
- 标题只在 pdf：1.2核心痛点
- 标题只在 pdf：1.3目标
- 标题只在 pdf：4.1计时器数据结构
- 需求只在 Markdown：Obsidian 用户在日常笔记中记录任务、会议、学习等活动，需要一种轻量级、零侵入的方式来追踪各项活动的耗时。现有的计时工具要么是独立应用（需要在 Obsidian 外操作），要么使用独立数据库（数据与笔记割裂）。用户希望计时数据直接嵌入笔记文本，随笔记一同迁移、版本控制。
- 需求只在 Markdown：ID：US-07；角色：日常用户；故事：我希望计时器的外观可以自定义；验收标准：设置面板中可修改运行/暂停图标、颜色、显示风格（徽章/纯文本）、时间格式
- 需求只在 Markdown：ID：US-09；角色：多语言用户；故事：我希望插件界面显示我的语言；验收标准：插件自动跟随 Obsidian 语言设置，支持中/英/繁中/日/韩
- 需求只在 Markdown：光标所在行有 timer-r → 暂停
- 需求只在 Markdown：光标所在行有 timer-p → 继续
- 需求只在 Markdown：光标所在行无计时器 → 创建新计时器
- 需求只在 Markdown："调整耗时"仅对已暂停计时器生效，运行中时禁用并显示 tooltip
- 需求只在 Markdown：监听 CM6 EditorView.updateListener 中的文档变更
- 需求只在 Markdown：检测 Checkbox 状态字符变化（如   → /）
- 需求只在 Markdown：根据 runningCheckboxState（如 /）和 pausedCheckboxState（如 -xX）配置决定触发动作
- 需求只在 pdf：Obsidian用户在日常笔记中记录任务、会议、学习等活动，需要一种轻量级、零侵入的方式来追踪各项活动的耗时。现有的计时工具要么是独立应用（需要在Obsidian外操作），要么使用独立数据库（数据与笔记割裂）。用户希望计时数据直接嵌入笔记文本，随笔记一同迁移、版本控制。
- 需求只在 pdf：光标所在行有timer-r→暂停
- 需求只在 pdf：光标所在行有timer-p→继续
- 需求只在 pdf：光标所在行无计时器→创建新计时器
- 需求只在 pdf：3.2右键编辑器菜单
- 需求只在 pdf："调整耗时"仅对已暂停计时器生效，运行中时禁用并显示tooltip
- 需求只在 pdf：监听CM6 EditorView.updateListener中的文档变更
- 需求只在 pdf：检测Checkbox状态字符变化（如→/）
- 需求只在 pdf：根据runningCheckboxState（如/）和pausedCheckboxState（如-xX）配置决定触发动作
- 需求只在 pdf：预览模式下通过pointerdown DOM事件监听Checkbox点击，轮询文件变更

### wukun2005-gif__patentExaminator

段落标题不一致，需求条目 23 / 128 一致（pdf 拆出 130 条）

- 标题只在 Markdown：专利复审 AI 助手 — 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：B-008 产品方向基线
- 标题只在 Markdown：v0.1.0 功能矩阵
- 标题只在 Markdown：2. 背景与动机
- 标题只在 pdf：专利复审AI助手—产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：B-008产品方向基线
- 标题只在 pdf：v0.1.0功能矩阵
- 标题只在 pdf：2.背景与动机
- 需求只在 Markdown：文档阅读与摘要：AI 可以快速提取申请文件的技术方案要素、权利要求结构、声称的技术效果。
- 需求只在 Markdown：AI 交互式解读：审查员上传完整申请文件后，AI 以对话方式帮助其快速理解专利——用通俗语言解释技术方案、梳理发明要点、指出关键创新之处。审查员可随时追问（"这个技术方案的核心创新在哪里？""这段描述是否清楚？"），AI 在对话上下文中持续解答。这是审查员"舒了好大一口气"的核心体验——不是结构化拆解，而是理解。
- 需求只在 Markdown：特征拆解：AI 可以按三步法框架输出结构化的 claim chart，并标注说明书出处。
- 需求只在 Markdown：文献对照：AI 可以将权利要求技术特征与用户上传的对比文件逐项比对，标注公开状态和引用出处，并识别区别特征候选。
- 需求只在 Markdown：时间轴自动校验：AI 可以自动核查每篇对比文件的公开日与申请日/优先权日的先后关系，过滤不可用文件。
- 需求只在 Markdown：OCR 解析：对扫描版 PDF 申请文件先做 OCR 再解析，避免审查员手动转换格式。
- 需求只在 Markdown：不替代发文系统、OA 格式、法条引用、正式三步法论证，APP 产出是审查员起草 OA 的素材。
- 需求只在 Markdown：Step 6 — 查看和微调 她发现特征 B 的说明书出处标注为"待确认"（黄色标注），直接在表格里点击编辑，手动补充正确段落号。右侧 AI 对话框里她追问："特征 B 和特征 C 是否可以合并为一个技术特征？"，AI 给出分析，她决定保持拆解不变。
- 需求只在 Markdown：上传单个文件（.pdf / .docx / .txt / .html）；单文件上限 200 页 / 100 MB
- 需求只在 Markdown：选择本地文件夹（仅 Chrome/Edge 支持 File System Access API；Firefox/Safari 用户使用多文件上传 <input type="file" multiple> 替代）
- 需求只在 pdf：文档阅读与摘要：AI可以快速提取申请文件的技术方案要素、权利要求结构、声称的技术效果。
- 需求只在 pdf：AI交互式解读：审查员上传完整申请文件后，AI以对话方式帮助其快速理解专利——用通俗语言解释技术方案、梳理发明要点、指出关键创新之处。审查员可随时追问（"这个技术方案的核心创新在哪里？""这段描述是否清楚？"），AI在对话上下文中持续解答。这是审查员"舒了好大一口气"的核心体验——不是结构化拆解，而是理解。
- 需求只在 pdf：特征拆解：AI可以按三步法框架输出结构化的claim chart，并标注说明书出处。
- 需求只在 pdf：文献对照：AI可以将权利要求技术特征与用户上传的对比文件逐项比对，标注公开状态和引用出处，并识别区别特征候选。
- 需求只在 pdf：时间轴自动校验：AI可以自动核查每篇对比文件的公开日与申请日/优先权日的先后关系，过滤不可用文件。
- 需求只在 pdf：OCR解析：对扫描版PDF申请文件先做OCR再解析，避免审查员手动转换格式。
- 需求只在 pdf：不替代发文系统、OA格式、法条引用、正式三步法论证，APP产出是审查员起草OA的素材。
- 需求只在 pdf：Step 6 —查看和微调她发现特征B的说明书出处标注为"待确认"（黄色标注），直接在表格里点击编辑，手动补充正确段落号。右侧AI对话框里她追问："特征B和特征C是否可以合并为一个技术特征？"，AI给出分析，她决定保持拆解不变。
- 需求只在 pdf：上传单个文件（.pdf/ .docx / .txt /.html）；单文件上限200页/ 100 MB
- 需求只在 pdf：选择本地文件夹（仅Chrome/Edge支持File System Access API；Firefox/Safari用户使用多文件上传<input type="file"multiple>替代）

### xgwangdl__wikiknowledge

段落标题不一致，需求条目 43 / 95 一致（pdf 拆出 95 条）

- 标题只在 Markdown：AI 知识库问答系统需求文档
- 标题只在 Markdown：1. 项目定位
- 标题只在 Markdown：2. 范围
- 标题只在 Markdown：2.1 本期做
- 标题只在 Markdown：2.2 本期不做
- 标题只在 pdf：AI知识库问答系统需求文档
- 标题只在 pdf：1.项目定位
- 标题只在 pdf：2.范围
- 标题只在 pdf：2.1本期做
- 标题只在 pdf：2.2本期不做
- 需求只在 Markdown：面向企业/团队场景的"AI 知识库问答系统"：管理员上传文档建立知识库，用户以自然语言提问，系统通过 RAG 检索知识库内容，结合大模型生成带引用来源的回答，并支持会话记忆、反馈评估、安全控制与可观测性。
- 需求只在 Markdown：微服务拆分，保持单体 + 模块化
- 需求只在 Markdown：语音对话、视频、移动 App
- 需求只在 Markdown：用户名 + 密码注册登录，密码使用 BCrypt 存储
- 需求只在 Markdown：登录成功返回 Access Token + Refresh Token
- 需求只在 Markdown：Access Token 有效期短（如 30 分钟），Refresh Token 可轮换
- 需求只在 Markdown：未登录访问业务接口返回 401
- 需求只在 Markdown：刷新令牌可获取新 Access Token，旧 Refresh Token 失效
- 需求只在 Markdown：单文件限制 20MB，单次上传最多 10 个文件
- 需求只在 Markdown：上传后进入异步流水线：解析 -> 清洗 -> 切片 -> 向量化 -> 入库
- 需求只在 pdf：面向企业/团队场景的"AI知识库问答系统"：管理员上传文档建立知识库，用户以自然语言提问，系统通过RAG检索知识库内容，结合大模型生成带引用来源的回答，并支持会话记忆、反馈评估、安全控制与可观测性。
- 需求只在 pdf：微服务拆分，保持单体+模块化
- 需求只在 pdf：语音对话、视频、移动App
- 需求只在 pdf：用户名+密码注册登录，密码使用BCrypt存储
- 需求只在 pdf：登录成功返回Access Token + Refresh Token
- 需求只在 pdf：Access Token有效期短（如30分钟），Refresh Token可轮换
- 需求只在 pdf：未登录访问业务接口返回401
- 需求只在 pdf：刷新令牌可获取新Access Token，旧Refresh Token失效
- 需求只在 pdf：单文件限制20MB，单次上传最多10个文件
- 需求只在 pdf：上传后进入异步流水线：解析->清洗->切片->向量化->入库

### xi-lie5__Story-Platform

段落标题不一致，需求条目 113 / 164 一致（pdf 拆出 119 条）

- 标题只在 Markdown：StoryForge 前端功能需求文档
- 标题只在 Markdown：1. 项目概述
- 标题只在 Markdown：1.1 项目名称
- 标题只在 Markdown：1.2 项目定位
- 标题只在 Markdown：1.3 核心价值
- 标题只在 pdf：StoryForge前端功能需求文档
- 标题只在 pdf：1.项目概述
- 标题只在 pdf：1.1项目名称
- 标题只在 pdf：1.2项目定位
- 标题只在 pdf：1.3核心价值
- 需求只在 Markdown：StoryForge是一个基于AI技术的交互式故事创作与阅读平台，允许用户创建、编辑、发布和阅读具有多分支结局的互动故事。
- 需求只在 Markdown：多分支叙事：支持创建具有多个选择分支和结局的互动故事
- 需求只在 Markdown：社区分享：用户可以发布作品供其他用户阅读和体验
- 需求只在 Markdown：可视化编辑：提供直观的故事节点图谱编辑工具
- 需求只在 Markdown：浏览和阅读已发布的故事
- 需求只在 Markdown：注册账号并登录
- 需求只在 Markdown：创建和管理自己的故事作品
- 需求只在 Markdown：查看个人统计信息
- 需求只在 Markdown：审核用户提交的故事
- 需求只在 Markdown：管理系统用户
- 需求只在 pdf：StoryForge是一个基于AI技术的交互式故事创作与阅读平台，允许用户创建、编辑、发
- 需求只在 pdf：支持第三方注册（微信、QQ、微博）-预留接口
- 需求只在 pdf：支持第三方登录（微信、QQ、微博）-预留接口
- 需求只在 pdf：5.1故事创建工具
- 需求只在 pdf：8.1管理员控制台
- 需求只在 pdf：页面加载时间<3秒

### xiaodong-l__amazon-1688-selector

段落标题不一致，需求条目 4 / 88 一致（pdf 拆出 18 条）

- 标题只在 Markdown：📊 v2.2 版本需求设计文档
- 标题只在 Markdown：🎯 版本概述
- 标题只在 Markdown：📋 功能需求
- 标题只在 Markdown：FR-001: 数据库集成
- 标题只在 Markdown：需求描述
- 标题只在 pdf：📊v2.2版本需求设计文档
- 标题只在 pdf：🎯版本概述
- 标题只在 pdf：📋功能需求
- 标题只在 pdf：FR-001:数据库集成
- 标题只在 pdf：FR-002:商品数据表设计
- 需求只在 Markdown：数据持久化 - 从 CSV 文件升级为数据库存储
- 需求只在 Markdown：历史追踪 - 记录商品数据变化历史
- 需求只在 Markdown：趋势对比 - 支持周/月/季度数据对比分析
- 需求只在 Markdown：查询优化 - 支持复杂查询和数据导出
- 需求只在 Markdown：将数据存储从 CSV 文件升级为关系型数据库，支持高效查询和数据管理。
- 需求只在 Markdown：支持 SQLite (默认，零配置)
- 需求只在 Markdown：支持 PostgreSQL (生产环境)
- 需求只在 Markdown：通过配置切换数据库类型
- 需求只在 Markdown：数据库连接池管理
- 需求只在 Markdown：定义数据模型类
- 需求只在 pdf：数据持久化-从CSV文件升级为数据库存储
- 需求只在 pdf：历史追踪-记录商品数据变化历史
- 需求只在 pdf：趋势对比-支持周/月/季度数据对比分析
- 需求只在 pdf：查询优化-支持复杂查询和数据导出
- 需求只在 pdf：将数据存储从CSV文件升级为关系型数据库，支持高效查询和数据管理。功能点
- 需求只在 pdf：☐支持SQLite (默认，零配置) ☐支持PostgreSQL (生产环境) ☐通过配置切换数据库类型☐数据库连接池管理
- 需求只在 pdf：☐使用SQLAlchemy作为ORM ☐定义数据模型类☐支持异步操作(asyncpg) ☐数据库迁移工具(Alembic)
- 需求只在 pdf：-分区表(按月分区，优化大数据量查询)
- 需求只在 pdf：验收标准☐每次采集自动记录历史数据☐历史数据可按时段查询☐支持30天以上历史数据☐分区表正常工作(PostgreSQL)
- 需求只在 pdf：☐支持Cron表达式配置☐默认每天采集一次☐支持自定义采集频率☐采集任务队列管理

### xiaojilele-glitch__WhyBuddy

段落标题不一致，需求条目 11 / 88 一致（pdf 拆出 88 条）

- 标题只在 Markdown：审计链 / 不可篡改日志 需求文档
- 标题只在 Markdown：US-1: 定义审计事件类型和关键操作
- 标题只在 Markdown：验收标准
- 标题只在 Markdown：US-2: 采集和记录审计事件
- 标题只在 Markdown：验收标准
- 标题只在 pdf：审计链/不可篡改日志需求文档
- 标题只在 pdf：US-1:定义审计事件类型和关键操作
- 标题只在 pdf：US-2:采集和记录审计事件
- 标题只在 pdf：US-3: Append-Only Log存储和防篡改
- 标题只在 pdf：US-4:时间戳验证和可信时间源
- 需求只在 Markdown：作为系统，我需要明确定义哪些操作必须记录到审计链，包括决策、权限变更、数据访问、Agent 执行等，这样确保审计链覆盖所有关键事件。
- 需求只在 Markdown：AC-1.1: 系统定义 AuditEventType 枚举，包括 DECISION_MADE、PERMISSION_GRANTED、PERMISSION_REVOKED、DATA_ACCESSED、AGENT_EXECUTED、AGENT_FAILED、CONFIG_CHANGED、USER_LOGIN、USER_LOGOUT、ESCALATION_REQUESTED、ESCALATION_APPROVED
- 需求只在 Markdown：AC-1.2: 每个事件类型包含 severity（INFO、WARNING、CRITICAL）、category（security、compliance、operational）、description
- 需求只在 Markdown：AC-1.3: 关键操作（DECISION_MADE、PERMISSION_GRANTED、DATA_ACCESSED）标记为 severity=CRITICAL，必须记录
- 需求只在 Markdown：AC-1.4: 系统支持扩展事件类型，新增事件类型需要管理员审批
- 需求只在 Markdown：AC-1.5: 事件类型定义存储到数据库，支持版本控制
- 需求只在 Markdown：AC-2.1: AuditEvent 包含 eventId、eventType、timestamp、actor（userId/agentId）、action、resource、result、context、metadata
- 需求只在 Markdown：AC-2.2: 系统在以下关键点自动采集事件：决策生成、权限变更、数据查询、Agent 执行、配置变更
- 需求只在 Markdown：AC-2.3: 事件采集包含完整的上下文信息：sessionId、requestId、sourceIp、userAgent、organizationId
- 需求只在 Markdown：AC-2.4: 事件采集不阻塞主业务流程（异步写入或缓冲）
- 需求只在 pdf：作为系统，我需要明确定义哪些操作必须记录到审计链，包括决策、权限变更、数据访问、Agent执行等，这样确保审计链覆盖所有关键事件。
- 需求只在 pdf：AC-1.1:系统定义AuditEventType枚举，包括DECISION_MADE、PERMISSION_GRANTED、PERMISSION_REVOKED、DATA_ACCESSED、AGENT_EXECUTED、AGENT_FAILED、CONFIG_CHANGED、USER_LOGIN、USER_LOGOUT、ESCALATION_REQUESTED、ESCALATION_APPROVED
- 需求只在 pdf：AC-1.2:每个事件类型包含severity（INFO、WARNING、CRITICAL）、category（security、compliance、operational）、description
- 需求只在 pdf：AC-1.3:关键操作（DECISION_MADE、PERMISSION_GRANTED、DATA_ACCESSED）标记为severity=CRITICAL，必须记录
- 需求只在 pdf：AC-1.4:系统支持扩展事件类型，新增事件类型需要管理员审批
- 需求只在 pdf：AC-1.5:事件类型定义存储到数据库，支持版本控制
- 需求只在 pdf：AC-2.1:AuditEvent包含eventId、eventType、timestamp、actor（userId/agentId）、action、resource、result、context、metadata
- 需求只在 pdf：AC-2.2:系统在以下关键点自动采集事件：决策生成、权限变更、数据查询、Agent执行、配置变更
- 需求只在 pdf：AC-2.3:事件采集包含完整的上下文信息：sessionId、requestId、sourceIp、userAgent、organizationId
- 需求只在 pdf：AC-2.4:事件采集不阻塞主业务流程（异步写入或缓冲）

### yangyunice__WorkMesh

段落标题不一致，需求条目 92 / 363 一致（pdf 拆出 312 条）

- 标题只在 Markdown：Personal Portal 移动端产品需求文档 (PRD)
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 产品目标
- 标题只在 Markdown：2.1 产品目标
- 标题只在 pdf：Personal Portal移动端产品需求文档(PRD)
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：1.3产品目标
- 标题只在 pdf：2.1产品目标
- 需求只在 Markdown：🎯 场景导向: 针对个人用户碎片化、高频次的使用习惯设计
- 需求只在 Markdown：🔄 生态融合: 就业、订单、布道三大业务闭环
- 需求只在 Markdown：📱 多端适配: 移动端网页、H5、PWA、可封装为 iOS/Android 原生应用
- 需求只在 Markdown：🔗 体系共用: 与 PC 端、企业端、管理端共用账号、数据库、订单和审核体系
- 需求只在 Markdown：核心业务闭环: 实现就业、订单、布道三条核心链路的移动端完整支持
- 需求只在 Markdown：高频操作优化: 首页快捷入口、状态切换、消息通知等高频功能易用性达标
- 需求只在 Markdown：多端数据同步: 与 PC 端、企业端、管理端数据实时同步，状态一致
- 需求只在 Markdown：用户体验优化: AI 推荐、智能匹配、个性化首页等提升用户体验的功能
- 需求只在 Markdown：离线能力: PWA 离线缓存、关键数据本地存储
- 需求只在 Markdown：性能优化: 首屏加载 < 2s，操作响应 < 500ms
- 需求只在 pdf：🎯场景导向:针对个人用户碎片化、高频次的使用习惯设计
- 需求只在 pdf：🔄生态融合:就业、订单、布道三大业务闭环
- 需求只在 pdf：📱多端适配:移动端网页、H5、PWA、可封装为iOS/Android原生应用
- 需求只在 pdf：🔗体系共用:与PC端、企业端、管理端共用账号、数据库、订单和审核体系
- 需求只在 pdf：触控操作优先，按钮尺寸≥44x44px
- 需求只在 pdf：核心操作流程≤3步
- 需求只在 pdf：消息通知及时触达原则4:生态融合(Ecosystem Integration)
- 需求只在 pdf：统一消息中心，不遗漏任何重要信息原则5:性能优先(Performance First)
- 需求只在 pdf：首屏加载<2s（4G网络）
- 需求只在 pdf：列表滚动流畅，帧率≥50fps

### yaomindong1996__forge-admin

段落标题不一致，需求条目 88 / 173 一致（pdf 拆出 135 条）

- 标题只在 Markdown：编码规则设定 功能需求文档
- 标题只在 Markdown：1. 概述
- 标题只在 Markdown：1.1 文档目的
- 标题只在 Markdown：1.2 功能背景
- 标题只在 Markdown：1.3 功能目标
- 标题只在 pdf：编码规则设定功能需求文档
- 标题只在 pdf：1.概述
- 标题只在 pdf：1.1文档目的
- 标题只在 pdf：1.2功能背景
- 标题只在 pdf：1.3功能目标
- 需求只在 Markdown：规则编码（rule_code）在同一租户下唯一，格式为大写字母+数字+下划线，建议格式 模块_实体_ID（如 CARRIER_ID、PO_ORDER_NO）
- 需求只在 Markdown：前置码即分组：将某段标记为"前置码"（is_prefix=Y），即表示该段值作为 SEQ 流水号的分组依据；例如把 SYS_VAR(orgCode) 段标记为前置码，则不同 orgCode 各自独立计数
- 需求只在 Markdown：段类型切换时，相关配置项自动联动（如非 SEQ 段的重置相关字段置灰）
- 需求只在 Markdown：SEQ 类型行高亮显示以便识别
- 需求只在 Markdown：DATE 段支持年(y/yy/yyyy)、月(M/MM)、日(d/dd)、时(H/HH)、分(m/mm)、秒(s/ss)格式符
- 需求只在 Markdown：DECIMAL 十进制：0-9（最常用，如 0001、9999）
- 需求只在 Markdown：ALPHA_UPPER 大写字母：默认 A-Z 全集26个字符；可选去除易混淆字符后为 A-H、J-N、P-Y 共23个字符
- 需求只在 Markdown：ALPHA_LOWER 小写字母：默认 a-z 全集26个字符；可选去除易混淆字符后为 a-h、j-n、p-y 共23个字符
- 需求只在 Markdown：ALPHANUMERIC 字母数字：默认 0-9A-Z 全集36个字符；可选去除易混淆字符后为 0-9 + A-H + J-N + P-Y 共33个字符（容量最大）
- 需求只在 Markdown：去除易混淆字符（可选开关，仅字母进制生效）：SEQ 段配置 excludeAmbiguous（Y/N），开启后字母进制去除 I、O、Z（及小写 i、o、z），因与数字 1、0、2 相似易混淆；默认关闭（使用完整字符集）
- 需求只在 pdf：规则编码（rule_code）在同一租户下唯一，格式为大写字母+数字+下划线，建议格式模块_实体_ID（如CARRIER_ID、PO_ORDER_NO）
- 需求只在 pdf：前置码即分组：将某段标记为"前置码"（is_prefix=Y），即表示该段值作为SEQ流水号的分组依据；例如把SYS_VAR(orgCode)段标记为前置码，则不同orgCode各自独立计数
- 需求只在 pdf：段类型切换时，相关配置项自动联动（如非SEQ段的重置相关字段置灰）
- 需求只在 pdf：SEQ类型行高亮显示以便识别
- 需求只在 pdf：DATE段支持年(y/yy/yyyy)、月(M/MM)、日(d/dd)、时(H/HH)、分(m/mm)、秒(s/ss)格式符
- 需求只在 pdf：SEQ段支持5种进制，字母也是流水号的一种进制形式，统一通过进制类型配置：o DECIMAL十进制：0-9（最常用，如0001、9999）o HEX十六进制：0-9A-F（如000A、00FF）o ALPHA_UPPER大写字母：默认A-Z全集26个字符；可选去除易混淆字符后为A-H、J-N、P-Y共23个字符o ALPHA_LOWER小写字母：默认a-z全集26个字符；可选去除易混淆字符后为a-h、j-n、p-y共23个字符o ALPHANUMERIC字母数字：默认0-9A-Z全集36个字符；可选去除易混淆字符后为0-9 + A-H + J-N + P-Y共33个字符（容量最大）
- 需求只在 pdf：去除易混淆字符（可选开关，仅字母进制生效）：SEQ段配置excludeAmbiguous（Y/N），开启后字母进制去除I、O、Z（及小写i、o、z），因与数字1、0、2相似易混淆；默认关闭（使用完整字符集）
- 需求只在 pdf：SEQ段支持补位（默认左补0）与溢出检测（超出长度范围时报错）
- 需求只在 pdf：SYS_VAR段支持租户ID、用户ID、用户名、部门编码、组织编码、套件编码、对象编码等变量
- 需求只在 pdf：数字流水号：FIXED("CG")+ SEQ(DECIMAL,4位)->CG0001、CG0002

### young-nights__ota-upgrade-of-qi-charger-based-on-can

段落标题不一致，需求条目 4 / 90 一致（pdf 拆出 97 条）

- 标题只在 Markdown：CAN-UDS OTA 功能需求文档
- 标题只在 Markdown：1. 概述
- 标题只在 Markdown：1.1 功能目标
- 标题只在 Markdown：1.2 系统架构
- 标题只在 Markdown：1.3 术语定义
- 标题只在 pdf：CAN-UDS OTA功能需求文档
- 标题只在 pdf：1.概述
- 标题只在 pdf：1.1功能目标
- 标题只在 pdf：1.2系统架构
- 标题只在 pdf：1.3术语定义
- 需求只在 Markdown：状态: 正式文档
- 需求只在 Markdown：适用范围: Qi 无线充电模块 CAN-UDS OTA / Qi IAP 升级与充电控制功能
- 需求只在 Markdown：代码基线: qi_wireless_code_app + qi_wireless_bootloader（对照源码逐项核对）
- 需求只在 Markdown：版本号只改固件编译常量 + 文档；XATO 头 version 区（0x4C）固定填 0x00，不携带版本
- 需求只在 Markdown：UDS 0xF195 直接取 SW_VERSION_STR，不读 OTA metadata / 镜像头
- 需求只在 Markdown：每次代码变更须在同一提交内递增 SW_VERSION_STR（默认 patch +1）
- 需求只在 Markdown：OTA 一律写入备份区（0x08010000）；BOOT 复位后校验并搬运至 App 区（0x08003000）
- 需求只在 Markdown：镜像须按 App 窗口链接（Reset Handler 落在 [0x08003100, 0x08010000)）
- 需求只在 Markdown：产线整片烧录用 merge_prod_bin.py 从 0x08000000 烧 Boot+App
- 需求只在 Markdown：签名格式: 64 字节 IEEE P1363（R‖S，各 32 字节）
- 需求只在 pdf：状态:正式文档
- 需求只在 pdf：适用范围: Qi无线充电模块CAN-UDS OTA / Qi IAP升级与充电控制功能
- 需求只在 pdf：代码基线:qi_wireless_code_app+qi_wireless_bootloader（对照源码逐项核对）
- 需求只在 pdf：CCU（主机）──CAN 250kbps──▶Qi充电模块（MCU1:AT32F426）
- 需求只在 pdf：版本号只改固件编译常量+文档；XATO头version区（0x4C）固定填0x00，不携带版本
- 需求只在 pdf：UDS 0xF195直接取SW_VERSION_STR，不读OTA metadata /镜像头
- 需求只在 pdf：每次代码变更须在同一提交内递增SW_VERSION_STR（默认patch+1）
- 需求只在 pdf：OTA一律写入备份区（0x08010000）；BOOT复位后校验并搬运至App区（0x08003000）
- 需求只在 pdf：镜像须按App窗口链接（Reset Handler落在[0x08003100,0x08010000)）
- 需求只在 pdf：产线整片烧录用merge_prod_bin.py从0x08000000烧Boot+App

### yuhui0531__md2ppt

段落标题不一致，需求条目 46 / 89 一致（pdf 拆出 87 条）

- 标题只在 Markdown：PRD: 导入已有提示词并进入工作台精调
- 标题只在 Markdown：1. 背景
- 标题只在 Markdown：2. 目标
- 标题只在 Markdown：3. 非目标
- 标题只在 Markdown：4. 目标用户
- 标题只在 pdf：PRD:导入已有提示词并进入工作台精调
- 标题只在 pdf：1.背景
- 标题只在 pdf：2.目标
- 标题只在 pdf：3.非目标
- 标题只在 pdf：4.目标用户
- 需求只在 Markdown：已经在外部工具中写好了逐页生图 prompt 的用户
- 需求只在 Markdown：从系统导出的 prompt ZIP 经过外部修改后，希望重新导入的用户
- 需求只在 Markdown：希望跳过"内容解析与 prompt 生成"阶段，只做精修和出图的用户
- 需求只在 Markdown：快速把一批 .md prompt 导入系统
- 需求只在 Markdown：在系统内继续人工修改 prompt
- 需求只在 Markdown：对整套 prompt 做统一风格检查
- 需求只在 Markdown：批量生图并导出 PPT
- 需求只在 Markdown：作为一个导入 prompt 的用户，我希望导入后仍然进入工作台，这样我可以逐页修改 prompt、新增页、删页，并继续做一致性修正。
- 需求只在 Markdown：作为一个导入 prompt 的用户，我希望后续批量生图和导出 PPT 的操作与原有流程一致，这样我不需要学习一套新的使用方式。
- 需求只在 Markdown：ZIP 与多个 .md 不能混传
- 需求只在 pdf：已经在外部工具中写好了逐页生图prompt的用户
- 需求只在 pdf：从系统导出的prompt ZIP经过外部修改后，希望重新导入的用户
- 需求只在 pdf：希望跳过"内容解析与prompt生成"阶段，只做精修和出图的用户
- 需求只在 pdf：快速把一批.md prompt导入系统
- 需求只在 pdf：在系统内继续人工修改prompt
- 需求只在 pdf：对整套prompt做统一风格检查
- 需求只在 pdf：批量生图并导出PPT
- 需求只在 pdf：作为一个导入prompt的用户，我希望导入后仍然进入工作台，这样我可以逐页修改prompt、新增页、删页，并继续做一致性修正。
- 需求只在 pdf：作为一个导入prompt的用户，我希望后续批量生图和导出PPT的操作与原有流程一致，这样我不需要学习一套新的使用方式。
- 需求只在 pdf：ZIP与多个.md不能混传

### yuqie6__WorkMirror

段落标题不一致，需求条目 23 / 132 一致（pdf 拆出 111 条）

- 标题只在 Markdown：复盘镜 WorkMirror PRD v0.2.0-alpha.2（产品化闭环版：Windows 托盘 Agent + 本地 Web UI；无 Wails/无 CLI）
- 标题只在 Markdown：0. 文档目的
- 标题只在 Markdown：0.1 文档关系与口径（UI）
- 标题只在 Markdown：0.2 现状对照（alpha.2）
- 标题只在 Markdown：1. 一句话定位（对外）
- 标题只在 pdf：复盘镜WorkMirror PRD v0.2.0-alpha.2（产品化闭环版：Windows托盘Agent +本地Web UI；无Wails/无CLI）
- 标题只在 pdf：0.文档目的
- 标题只在 pdf：0.1文档关系与口径（UI）
- 标题只在 pdf：0.2现状对照（alpha.2）
- 标题只在 pdf：1.一句话定位（对外）
- 需求只在 Markdown：PRD 负责"要做什么/验收口径/优先级"，不在这里堆砌全部 UI 细节。
- 需求只在 Markdown：Web UI 的交互与视觉规范以 docs/frontend.md 为准（工程师驾驶舱：Evidence First + No Silent Failures）。
- 需求只在 Markdown：若 PRD 与 docs/frontend.md 对 UI 细节冲突：以 PRD 的产品原则/验收为最终口径；实现细节以 docs/frontend.md 落地。
- 需求只在 Markdown：语义来源成为稳定契约：后端写入 semantic_source（ai/rule）与证据提示，前端不再用启发式猜测，离线/降级更可解释。
- 需求只在 Markdown：Local-first & Privacy by default：数据本地；敏感项默认最小化/可脱敏
- 需求只在 Markdown：Session 为权威路径：所有上层输出统一口径，避免多套"都能跑但不一致"
- 需求只在 Markdown：离线可用：无 AI Key 时仍能产出"规则回顾"，且 UI 明确标注能力差异
- 需求只在 Markdown：工程师驾驶舱：高信息密度、暗色优先（Tailwind zinc 体系）、语义色统一（Healthy/Warn/Error/AI）。
- 需求只在 Markdown：Evidence First：任何 summary/洞察/图表都必须在 1 次交互内 drill-down 到证据（Diff/Events/Browser）。
- 需求只在 Markdown：No Silent Failures：全局可见的系统健康（侧边栏常驻 + 状态页），离线/降级必须"一键可解释"（点击健康指示器直达诊断页，展示原因与影响范围）。
- 需求只在 pdf：PRD负责"要做什么/验收口径/优先级"，不在这里堆砌全部UI细节。
- 需求只在 pdf：Web UI的交互与视觉规范以docs/frontend.md为准（工程师驾驶舱：Evidence First + No Silent Failures）。
- 需求只在 pdf：若PRD与docs/frontend.md对UI细节冲突：以PRD的产品原则/验收为最终口径；实现细节以docs/frontend.md落地。
- 需求只在 pdf：语义来源成为稳定契约：后端写入semantic_source（ai/rule）与证据提示，前端不再用启发式猜测，离线/降级更可解释。下一版优先级将转向：更细粒度的证据覆盖率指标、可回放的语义升级策略与诊断闭环。
- 需求只在 pdf：Local-first&Privacy by default：数据本地；敏感项默认最小化/可脱敏
- 需求只在 pdf：Session为权威路径：所有上层输出统一口径，避免多套"都能跑但不一致"
- 需求只在 pdf：离线可用：无AI Key时仍能产出"规则回顾"，且UI明确标注能力差异
- 需求只在 pdf：工程师驾驶舱：高信息密度、暗色优先（Tailwind zinc体系）、语义色统一（Healthy/Warn/Error/AI）。
- 需求只在 pdf：Evidence First：任何summary/洞察/图表都必须在1次交互内drill-down到证据（Diff/Events/Browser）。
- 需求只在 pdf：No Silent Failures：全局可见的系统健康（侧边栏常驻+状态页），离线/降级必须"一键可解释"（点击健康指示器直达诊断页，展示原因与影响范围）。

### ywq2019__ai_test_agent

段落标题不一致，需求条目 91 / 111 一致（pdf 拆出 113 条）

- 标题只在 Markdown：一、项目概述
- 标题只在 Markdown：1.1 项目背景
- 标题只在 Markdown：1.2 技术架构选型
- 标题只在 Markdown：1.3 整体功能架构
- 标题只在 Markdown：二、通用基础规范
- 标题只在 pdf：1.1项目背景
- 标题只在 pdf：1.2技术架构选型
- 标题只在 pdf：1.3整体功能架构
- 标题只在 pdf：2.1权限规范
- 标题只在 pdf：2.2编码规范
- 需求只在 Markdown：基础开发框架：django vue3（前后端分离开源框架，支持列级别权限、多终端认证、插件化扩展）
- 需求只在 Markdown：平台整体分为基础系统模块、核心测试业务模块、AI智能扩展模块、自动化调度模块、报告统计模块五大板块，完全基于基础框架插件化开发，不改动底层原生架构，支持后续功能迭代扩展。
- 需求只在 Markdown：完全复用django-vue3-admin原生RBAC权限体系，支持菜单权限、按钮权限、接口权限、列级别数据权限，可针对不同角色配置各模块的新增、编辑、删除、查询、执行、导出等操作权限，支持数据范围权限管控。
- 需求只在 Markdown：系统所有唯一编码均为自动生成、全局不重复，支持数据库唯一索引约束；测试套件专属编码为10位字母组合（大小写混合），用于外部API调用、用例数据获取、自动化任务关联。
- 需求只在 Markdown：本模块为平台基础数据模块，用于统一管理所有需要进行UI自动化测试的业务项目，所有用例、测试套件、测试任务均关联对应项目，实现数据隔离。
- 需求只在 Markdown：项目名称：必填，唯一，业务项目全称
- 需求只在 Markdown：项目简称：必填，唯一，项目简短标识，用于数据展示简化
- 需求只在 Markdown：项目描述：选填，记录项目业务范围、测试场景说明
- 需求只在 Markdown：最新测试结果：系统自动同步，展示当前最新一次执行状态（PASS/FAIL/SKIP/ERROR）
- 需求只在 Markdown：执行统计：自动统计总执行次数、成功次数、失败次数、跳过次数、异常次数
- 需求只在 pdf：基础开发框架：django vue3（前后端分离开源框架，支持列级别权限、多终端认证、
- 需求只在 pdf：完全复用django-vue3-admin原生RBAC权限体系，支持菜单权限、按钮权限、接口权限、
- 需求只在 pdf：本模块为平台基础数据模块，用于统一管理所有需要进行UI自动化测试的业务项目，所
- 需求只在 pdf：2.1核心字段属性
- 需求只在 pdf：最新测试结果：系统自动同步，展示当前最新一次执行状态（PASS/FAIL/SKIP/ ERROR）
- 需求只在 pdf：3.1核心字段属性
- 需求只在 pdf：套件唯一编码：系统自动生成10位大小写字母组合，全局唯一，用于外部API调
- 需求只在 pdf：3.2核心功能需求
- 需求只在 pdf：用例关联能力：点击测试套件可选择对应项目下的测试用例，已添加的用例自动过
- 需求只在 pdf：4.1手动执行功能

### zhewu43__FocusFlight_wxminiprogram

段落标题不一致，需求条目 119 / 151 一致（pdf 拆出 153 条）

- 标题只在 Markdown：FocusFlight 产品需求文档 (PRD)
- 标题只在 Markdown：1. 产品概述
- 标题只在 Markdown：1.1 产品定位
- 标题只在 Markdown：1.2 目标用户
- 标题只在 Markdown：1.3 核心价值
- 标题只在 pdf：FocusFlight产品需求文档(PRD)
- 标题只在 pdf：1.产品概述
- 标题只在 pdf：1.1产品定位
- 标题只在 pdf：1.2目标用户
- 标题只在 pdf：1.3核心价值
- 需求只在 Markdown：未登录用户：自动分配临时飞行员ID（格式：FF123456）
- 需求只在 Markdown：已登录用户：升级为认证飞行员ID（格式：FL12345678）
- 需求只在 Markdown：显示"游客飞行员"或真实微信昵称
- 需求只在 Markdown：数据统计规则：只统计成功完成的航班（completed: true）
- 需求只在 Markdown：精确地理定位：排除虚拟城市，匹配真实地理位置
- 需求只在 Markdown：手动城市选择：支持真实城市和虚拟地点（家、公司）
- 需求只在 Markdown：热门航线：使用预设时间，确保显示与实际专注时间一致
- 需求只在 Markdown：手动选择：根据地理距离自动计算专注时长（5-180分钟）
- 需求只在 Markdown：💬 分享给好友（绿色主题）
- 需求只在 Markdown：🌟 分享朋友圈（黄色主题）
- 需求只在 pdf：飞行员ID系统：o未登录用户：自动分配临时飞行员ID（格式：FF123456）o已登录用户：升级为认证飞行员ID（格式：FL12345678）o显示"游客飞行员"或真实微信昵称
- 需求只在 pdf：数据统计规则：只统计成功完成的航班（completed:true）
- 需求只在 pdf：1.2航班选择系统
- 需求只在 pdf：智能定位系统：o精确地理定位：排除虚拟城市，匹配真实地理位置o手动城市选择：支持真实城市和虚拟地点（家、公司）
- 需求只在 pdf：智能时间计算：o热门航线：使用预设时间，确保显示与实际专注时间一致o手动选择：根据地理距离自动计算专注时长（5-180分钟）
- 需求只在 pdf：1.4社交分享系统
- 需求只在 pdf：双分享按钮设计：o💬分享给好友（绿色主题）o🌟分享朋友圈（黄色主题）
- 需求只在 pdf：1.5社交分享系统
- 需求只在 pdf：首页-航班选择界面
- 需求只在 pdf：专注页-计时器执行页面

### zxmqq1234__web3-pawID

段落标题不一致，需求条目 24 / 58 一致（pdf 拆出 55 条）

- 标题只在 Markdown：PawID Web3 项目 PRD：
- 标题只在 Markdown：1. 产品目标与边界：
- 标题只在 Markdown：2. 页面结构与层级：
- 标题只在 Markdown：3. 页面功能与交互规则：
- 标题只在 Markdown：3.1 创建身份：
- 标题只在 pdf：PawID Web3项目PRD：
- 标题只在 pdf：1.产品目标与边界：
- 标题只在 pdf：2.页面结构与层级：
- 标题只在 pdf：3.页面功能与交互规则：
- 标题只在 pdf：3.1创建身份：
- 需求只在 Markdown：步骤：① 上传照片；内容与输入：拖拽/选择 JPG、PNG、WebP；单张不超过 5MB；提供"使用示例猫咪/狗狗"；交互、校验与结果：选择后显示预览，允许替换；类型或大小不符时原位提示；未选择照片不可下一步
- 需求只在 Markdown：四项统计：家庭成员数、成长记录数、徽章数、PAWS 余额，均读取当前宠物的实际数据。
- 需求只在 Markdown："身份凭证"打开抽屉：身份编号、创建时间、所属网络 Monad 测试网、关联账户与存证交易标识；可复制并指向 Monad 测试网 Explorer；该链上信息在 Registry 合约部署并配置 VITE_MONAD_REGISTRY_ADDRESS 后生效，未部署期间如实标注待接入状态。
- 需求只在 Markdown："编辑资料"弹窗修改姓名、性别、生日、介绍；保存后身份卡、访客页及图谱名称同步更新，宠物 ID 不变。
- 需求只在 Markdown：点击"邀请家人" → 填写昵称（1–20 字） → 生成邀请链接及二维码 → 可复制链接或"以受邀者身份打开"。默认关系为共同监护，不推断情侣或婚姻关系。
- 需求只在 Markdown：受邀者确认页明确当前体验身份；接受后，家庭页增加一名共同监护人，记录加入时间，同时展示"共同守护者解锁 / 一起陪伴它成长"的双人宠物卡和彩带效果。
- 需求只在 Markdown：每只宠物首次新增共同监护人奖励 50 PAWS；重复点击、重复打开已接受邀请均不重复添加或发奖。拒绝后原邀请不可再接受，可由主监护人重新创建。
- 需求只在 Markdown：受邀者不能是主监护人或已有成员；邀请记录明确关联宠物 ID。
- 需求只在 Markdown：点击添加 → 按名称或 PawID 搜索内置示例宠物 → 选择对象 → 提交申请 → 显示待确认虚线 → 以对方身份处理接受/拒绝。
- 需求只在 Markdown：接受后连线变实线，标记"双向确认"，相关宠物视角同步更新；首次建立父母关系奖励 50 PAWS。
- 需求只在 pdf：四项统计：家庭成员数、成长记录数、徽章数、PAWS余额，均读取当前宠物的实际数据。
- 需求只在 pdf："身份凭证"打开抽屉：身份编号、创建时间、所属网络Monad测试网、关联账户与存证交易标识；可复制并指向Monad测试网Explorer；该链上信息在Registry合约部署并配置VITE_MONAD_REGISTRY_ADDRESS后生效，未部署期间如实标注待接入状态。
- 需求只在 pdf："编辑资料"弹窗修改姓名、性别、生日、介绍；保存后身份卡、访客页及图谱名称同步更新，宠物ID不变。
- 需求只在 pdf：点击"邀请家人"→填写昵称（1–20字）→生成邀请链接及二维码→可复制链接或"以受邀者身份打开"。默认关系为共同监护，不推断情侣或婚姻关系。
- 需求只在 pdf：受邀者确认页明确当前体验身份；接受后，家庭页增加一名共同监护人，记录加入时间，同时展示"共同守护者解锁/一起陪伴它成长"的双人宠物卡和彩带效果。
- 需求只在 pdf：每只宠物首次新增共同监护人奖励50 PAWS；重复点击、重复打开已接受邀请均不重复添加或发奖。拒绝后原邀请不可再接受，可由主监护人重新创建。
- 需求只在 pdf：受邀者不能是主监护人或已有成员；邀请记录明确关联宠物ID。
- 需求只在 pdf：点击添加→按名称或PawID搜索内置示例宠物→选择对象→提交申请→显示待确认虚线→以对方身份处理接受/拒绝。
- 需求只在 pdf：接受后连线变实线，标记"双向确认"，相关宠物视角同步更新；首次建立父母关系奖励50 PAWS。
- 需求只在 pdf："新增记录"弹窗字段：类型、标题（必填，1–30字）、日期（必填且不晚于今天）、描述（选填，最多500字）、照片（选填，同上传限制）、可见性（默认仅家庭）。

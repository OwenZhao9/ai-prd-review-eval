# v2 漏判与误判

## H009  标准：['R2']  预测：无问题
> FR-5.2: Executing a manual pump command MUST immediately run the specified pump for the given duration.
- 漏判：['R2']

## H011  标准：['R1']  预测：['R1', 'R2']
> Admin can choose allowed payment modes if supported
- 误判 R2：「if supported」「supported」没有给出可检查的判定标准，无法客观验证该需求是否满足。

## H015  标准：['R2', 'R3']  预测：['R2']
> Frontend should remain responsive and reliable under slow API calls.
- 漏判：['R3']

## H027  标准：无问题  预测：['R2']
> As a developer, I want to open a board in the browser that shows the current state without any build step, so I can see what's going on at a glance.
- 误判 R2：「at a glance」“at a glance”是无法测量的效果描述，同一句没有给出可测量的验收标准。

## H029  标准：['R2', 'R3']  预测：['R2']
> Configuration should be minimal and have sensible defaults
- 漏判：['R3']

## J005  标准：['R3']  预测：无问题
> The application must allow unauthenticated (guest) users to view room schedules, and guests must be rate-limited to 30 requests per minute.
- 漏判：['R3']

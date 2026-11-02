# v4 漏判与误判

## H009  标准：['R2']  预测：无问题
> FR-5.2: Executing a manual pump command MUST immediately run the specified pump for the given duration.
- 漏判：['R2']

## H015  标准：['R2', 'R3']  预测：['R2']
> Frontend should remain responsive and reliable under slow API calls.
- 漏判：['R3']

## H027  标准：无问题  预测：['R2']
> As a developer, I want to open a board in the browser that shows the current state without any build step, so I can see what's going on at a glance.
- 误判 R2：「at a glance」「一眼就能看到」是无法测量的效果描述，同一句没有给出可检查的标准。

## H029  标准：['R2', 'R3']  预测：['R2']
> Configuration should be minimal and have sensible defaults
- 漏判：['R3']

## J013  标准：['R6']  预测：无问题
> This must allow guest users to submit a booking request by providing an email address for confirmation.
- 漏判：['R6']

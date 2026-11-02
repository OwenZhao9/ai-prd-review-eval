# v3 漏判与误判

## H009  标准：['R2']  预测：无问题
> FR-5.2: Executing a manual pump command MUST immediately run the specified pump for the given duration.
- 漏判：['R2']

## H011  标准：['R1']  预测：['R1', 'R2']
> Admin can choose allowed payment modes if supported
- 误判 R2：「if supported」「supported」没有给出可检查的判定标准，无法验证该条件何时成立。

## H015  标准：['R2', 'R3']  预测：['R2']
> Frontend should remain responsive and reliable under slow API calls.
- 漏判：['R3']

## H018  标准：['R2']  预测：['R2', 'R3']
> User Story 5 (View Rooms): As any user (guest or authenticated), I want to see a clear, calendar-based view of all available rooms and their schedules so I can easily find an open slot.
- 误判 R3：「see a clear, calendar-based view of all available rooms and their schedules so I can easily find an open slot」该需求同时包含两个可独立验收的要求：展示所有房间及其日程的日历视图，以及让用户能轻松找到空闲时段。

## H027  标准：无问题  预测：['R2']
> As a developer, I want to open a board in the browser that shows the current state without any build step, so I can see what's going on at a glance.
- 误判 R2：「at a glance」「at a glance」是无法测量的效果描述，同一句没有给出可检查的标准。

## H029  标准：['R2', 'R3']  预测：['R2']
> Configuration should be minimal and have sensible defaults
- 漏判：['R3']

## H037  标准：['R3']  预测：['R2', 'R3']
> A human can start, stop, and gate agent work from a board without touching a terminal, and can leave the terminal running unattended within limits they set.
- 误判 R2：「within limits they set」「limits they set」没有给出可测量的具体限制值或可检查条件，无法客观验证。

## H038  标准：无问题  预测：['R1']
> Supports different log types: distraction, reflection, insight.
- 误判 R1：「different log types」「different」没有说明具体范围，读者无法确定是否只有这三种类型，还是这三种只是示例。

## J013  标准：['R6']  预测：无问题
> This must allow guest users to submit a booking request by providing an email address for confirmation.
- 漏判：['R6']

## J014  标准：['R6']  预测：['R1', 'R6']
> It supports these: distraction, reflection, insight.
- 误判 R1：「these: distraction, reflection, insight」these 指代不明，且列举未封闭，读者无法确定是否只有这三项。

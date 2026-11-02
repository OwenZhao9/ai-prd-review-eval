# v1 漏判与误判

## H004  标准：无问题  预测：['R6']
> Endpoint can be copy-pasted into CoinPay merchant dashboard
- 误判 R6：「Endpoint」关键对象 Endpoint 没有定义或指代不明，读者无法确定它指哪个接口或端点。

## H006  标准：无问题  预测：['R2']
> Plugin should avoid blocking admin pages with remote calls unless initiated by merchant
- 误判 R2：「avoid blocking」“avoid blocking”没有给出可测量的标准（如超时阈值或最大阻塞时长），无法客观验证是否满足。

## H009  标准：['R2']  预测：无问题
> FR-5.2: Executing a manual pump command MUST immediately run the specified pump for the given duration.
- 漏判：['R2']

## H011  标准：['R1']  预测：['R1', 'R6']
> Admin can choose allowed payment modes if supported
- 误判 R6：「supported」“supported”缺少明确主语，无法确定是系统支持还是支付方式本身受支持。

## H012  标准：['R1']  预测：['R1', 'R6']
> Merchant branding options can be passed if supported by CoinPay
- 误判 R6：「if supported by CoinPay（省略了主语）」条件从句缺少明确主语，无法确定是“branding options”还是“passing”受 CoinPay 支持。

## H014  标准：['R3']  预测：无问题
> NFR-3 (Performance): Web page load time should be under 3 seconds on the local network. Real-time status updates on the dashboard should have a latency of no more than 5 seconds from the actual event.
- 漏判：['R3']

## H015  标准：['R2', 'R3']  预测：['R2']
> Frontend should remain responsive and reliable under slow API calls.
- 漏判：['R3']

## H027  标准：无问题  预测：['R2']
> As a developer, I want to open a board in the browser that shows the current state without any build step, so I can see what's going on at a glance.
- 误判 R2：「at a glance」“at a glance”是无法测量的效果描述，同一句没有给出可测量的标准（如加载时间阈值或可见字段清单）。

## H029  标准：['R2', 'R3']  预测：['R2']
> Configuration should be minimal and have sensible defaults
- 漏判：['R3']

## H037  标准：['R3']  预测：['R2', 'R3', 'R6']
> A human can start, stop, and gate agent work from a board without touching a terminal, and can leave the terminal running unattended within limits they set.
- 误判 R2：「within limits they set」未给出可测量的限制标准或阈值，无法验证“在限制内”是否满足。
- 误判 R6：「they set」代词 they 在本需求内没有明确先行词，无法确定是谁设定的限制。

## J001  标准：['R1']  预测：['R1', 'R3']
> The application must allow unauthenticated (guest) users to view room schedules, and/or room details as appropriate.
- 误判 R3：「view room schedules, and/or room details」查看房间日程和查看房间详情是两个可独立验收的要求，删掉其中一个另一个仍然成立。

## J013  标准：['R6']  预测：无问题
> This must allow guest users to submit a booking request by providing an email address for confirmation.
- 漏判：['R6']

# v1 漏判与误判

## N005  标准：['R2', 'R3']  预测：['R2']
> Logs should be human-readable and processable by standard Unix utilities
- 漏判：['R3']

## N009  标准：['R2', 'R3']  预测：['R2']
> API errors should surface as useful notifications and retryable error states.
- 漏判：['R3']

## N010  标准：['R3']  预测：无问题
> User Story 6 (Submit Booking Request): As any user, I want to be able to select an available room and time slot to create a new booking. If I am a guest, I will be prompted for my email address.
- 漏判：['R3']

## N020  标准：无问题  预测：['R3']
> Plugin must send final payable amount including taxes, shipping, and discounts
- 误判 R3：「including taxes, shipping, and discounts」税费、运费和折扣是三个可独立验收的金额组成部分，删掉其中任一项需求仍然成立，属于一条需求包含多个独立要求。

## N034  标准：无问题  预测：['R1', 'R2']
> Forms should prevent invalid paths, status codes, and JSON before submission.
- 误判 R1：「invalid paths, status codes, and JSON」未定义什么算 invalid，不同读者对无效路径、状态码和 JSON 的判定标准会不一致。
- 误判 R2：「prevent invalid paths, status codes, and JSON」没有给出可测量的判定标准或阈值来界定何为 invalid，无法客观验证是否已阻止。

## N048  标准：['R2', 'R3']  预测：['R2']
> Security: All user data and authentication tokens must be handled securely. Communication with Firebase services must be over HTTPS.
- 漏判：['R3']

## N056  标准：['R3']  预测：['R6']
> An agent can learn the state of the project in under 500 tokens. gw brief output stays under 25 lines by design.
- 漏判：['R3']
- 误判 R6：「An agent can learn the state of the project」“the project”没有在本条需求内给出明确先行词，读者无法确定它指哪个项目。

## N078  标准：['R1', 'R2']  预测：['R1']
> The error UI should appear where the user is looking (near the button or content area), not as a modal dialog.
- 漏判：['R2']

## N088  标准：无问题  预测：['R2', 'R3']
> The fallback UI should display a friendly message ("Something went wrong — please reload the page") and a reload button.
- 误判 R3：「display a friendly message ... and a reload button」显示提示消息和提供重新加载按钮是两个可各自独立验收的要求，删掉其中一个另一个仍然成立。
- 误判 R2：「friendly」“friendly”是无法测量的形容词，同一句没有给出可检查的标准来判定消息是否友好。

## N094  标准：['R5']  预测：['R6']
> Tool Callback Return: Tool callbacks return Ok<CallToolResult>, and you must extract the .value property when returning from the request handler.
- 漏判：['R5']
- 误判 R6：「you must extract the .value property」需求中的关键对象用代词 it/this 指代，但在这条需求内找不到明确的先行词。

## N097  标准：['R5']  预测：无问题
> Error Handling: All errors should be caught within tool callbacks and returned as Ok results with isError: true, rather than throwing exceptions.
- 漏判：['R5']

## I001  标准：['R1']  预测：['R1', 'R3']
> The plugin must register as a WHMCS payment gateway module, and/or an addon module as appropriate.
- 误判 R3：「register as a WHMCS payment gateway module, and/or an addon module」注册为支付网关模块和注册为附加模块是两个可各自独立验收的要求，删掉其中一个另一个仍然成立。

## I006  标准：['R1']  预测：['R1', 'R2']
> Forms should prevent invalid paths, status codes, and JSON before submission if possible.
- 误判 R2：「prevent invalid paths, status codes, and JSON」未定义何为 invalid，也未给出可检查的判定标准或阈值，无法客观验证是否已阻止。

## I011  标准：['R2']  预测：['R2', 'R3']
> The fallback UI should display a friendly message and a reload button that is easy to find.
- 误判 R3：「display a friendly message and a reload button」显示提示消息与显示重载按钮是两个可各自独立验收的要求，用 and 连接，删掉其一另一个仍成立。

## I014  标准：['R3']  预测：['R3', 'R6']
> Plugin must send final payable amount including taxes, shipping, and discounts; it must also email the merchant a daily summary.
- 误判 R6：「it must also email」代词 it 在本条需求内没有明确先行词，无法确定是 Plugin 还是其他对象。

## I023  标准：['R4']  预测：['R3', 'R4']
> Forms should prevent invalid paths, status codes, and JSON before submission; max JSON size is TBR.
- 误判 R3：「prevent invalid paths, status codes, and JSON before submission」校验路径、状态码和 JSON 是三个可各自独立验收的要求，删掉任一其余仍成立。

## I029  标准：['R6']  预测：无问题
> It must register as a WHMCS payment gateway module.
- 漏判：['R6']

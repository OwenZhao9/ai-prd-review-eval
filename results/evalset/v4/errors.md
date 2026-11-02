# v4 漏判与误判

## N031  标准：['R2']  预测：无问题
> FR-5.3: The system MUST have a global Emergency Stop button that immediately halts all pump activity.
- 漏判：['R2']

## N040  标准：['R1', 'R5']  预测：['R1', 'R3', 'R5']
> Support for Pokémon Sets: Integrate with a database or a simple JSON store to allow users to use shorthand for common Smogon sets (e.g., "Lando-T-Scarf").
- 误判 R3：「Integrate with a database or a simple JSON store to allow users to use shorthand for common Smogon sets」同时提出两个可独立验收的要求：选择并集成存储方案，以及支持简写集合。

## N056  标准：['R3']  预测：无问题
> An agent can learn the state of the project in under 500 tokens. gw brief output stays under 25 lines by design.
- 漏判：['R3']

## N078  标准：['R1', 'R2']  预测：['R2']
> The error UI should appear where the user is looking (near the button or content area), not as a modal dialog.
- 漏判：['R1']

## I006  标准：['R1']  预测：['R1', 'R2']
> Forms should prevent invalid paths, status codes, and JSON before submission if possible.
- 误判 R2：「invalid paths, status codes, and JSON」没有定义什么算 invalid（路径格式、状态码范围、JSON 结构），无法客观验证。

## I011  标准：['R2']  预测：['R2', 'R3']
> The fallback UI should display a friendly message and a reload button that is easy to find.
- 误判 R3：「display a friendly message and a reload button」“显示消息”和“提供易于找到的重载按钮”是两个可以各自独立验收的要求，用 and 连接在一起。

## I031  标准：['R6']  预测：无问题
> This must send final payable amount including taxes, shipping, and discounts.
- 漏判：['R6']

## I034  标准：['R6']  预测：无问题
> This must not change any user-visible behavior.
- 漏判：['R6']

# v3 漏判与误判

## N033  标准：['R2']  预测：['R2', 'R3']
> Tenant routing should feel automatic after login/register.
- 误判 R3：「after login/register」登录和注册是两个可各自独立验收的场景，用斜杠并列写在同一需求里。

## N040  标准：['R1', 'R5']  预测：['R1', 'R3', 'R5']
> Support for Pokémon Sets: Integrate with a database or a simple JSON store to allow users to use shorthand for common Smogon sets (e.g., "Lando-T-Scarf").
- 误判 R3：「Integrate with a database or a simple JSON store to allow users to use shorthand for common Smogon sets」包含两个可独立验收的要求：选择并集成存储方式，以及支持用户使用简写。

## N056  标准：['R3']  预测：无问题
> An agent can learn the state of the project in under 500 tokens. gw brief output stays under 25 lines by design.
- 漏判：['R3']

## N078  标准：['R1', 'R2']  预测：['R1']
> The error UI should appear where the user is looking (near the button or content area), not as a modal dialog.
- 漏判：['R2']

## N079  标准：['R3']  预测：['R3', 'R6']
> The app can fetch public holidays based on country/state, but users can enable, disable, or edit them because college calendars differ.
- 误判 R6：「edit them」代词 them 指代不明：可能指 public holidays，也可能指 country/state，本条需求内没有明确先行词。

## I001  标准：['R1']  预测：['R1', 'R3']
> The plugin must register as a WHMCS payment gateway module, and/or an addon module as appropriate.
- 误判 R3：「register as a WHMCS payment gateway module, and/or an addon module」注册为支付网关模块与注册为附加模块是两个可各自独立验收的要求，被 and/or 串在同一条需求里。

## I006  标准：['R1']  预测：['R1', 'R3']
> Forms should prevent invalid paths, status codes, and JSON before submission if possible.
- 误判 R3：「prevent invalid paths, status codes, and JSON」路径、状态码和 JSON 三项校验可以各自独立验收，却串在同一条需求里。

## I011  标准：['R2']  预测：['R2', 'R3']
> The fallback UI should display a friendly message and a reload button that is easy to find.
- 误判 R3：「display a friendly message and a reload button」展示提示文案与展示重载按钮是两个可分别验收的要求，用 and 连接。

## I027  标准：['R5']  预测：['R3', 'R5']
> As an authenticated user, I want to view all my upcoming and past reservations, rendered with React Query infinite scroll.
- 误判 R3：「view all my upcoming and past reservations」查看即将到来的预订和查看历史预订是两个可以各自独立验收的要求，被 and 连接在同一条需求里。

## I031  标准：['R6']  预测：无问题
> This must send final payable amount including taxes, shipping, and discounts.
- 漏判：['R6']

## I034  标准：['R6']  预测：无问题
> This must not change any user-visible behavior.
- 漏判：['R6']

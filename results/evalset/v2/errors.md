# v2 漏判与误判

## N004  标准：['R2', 'R3']  预测：['R2']
> CoinPay needs first-party merchant plugins for WooCommerce and WHMCS so merchants can accept crypto and credit card payments through CoinPay with minimal setup, consistent branding, and a unified API experience.
- 漏判：['R3']

## N009  标准：['R2', 'R3']  预测：['R2']
> API errors should surface as useful notifications and retryable error states.
- 漏判：['R3']

## N052  标准：['R5']  预测：无问题
> User authentication must be handled by Firebase Authentication, supporting both email/password and Google Sign-In for users who choose to create an account.
- 漏判：['R5']

## N056  标准：['R3']  预测：无问题
> An agent can learn the state of the project in under 500 tokens. gw brief output stays under 25 lines by design.
- 漏判：['R3']

## N078  标准：['R1', 'R2']  预测：['R1']
> The error UI should appear where the user is looking (near the button or content area), not as a modal dialog.
- 漏判：['R2']

## I006  标准：['R1']  预测：['R1', 'R2']
> Forms should prevent invalid paths, status codes, and JSON before submission if possible.
- 误判 R2：「if possible」“if possible”使“阻止无效输入”这一效果无法被客观验证，没有给出可检查的条件或阈值。

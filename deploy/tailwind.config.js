// 构建时生成页面用到的 Tailwind 样式（public/app.css），浏览器里不再加载 Tailwind 运行时
module.exports = {
  content: ['./public/index.html'],
  theme: { extend: { colors: { slate: { 50: '#fafaf9', 100: '#f4f4f3', 200: '#e7e7e5', 300: '#d6d6d3', 400: '#a3a3a0', 500: '#737371', 600: '#525250', 700: '#3a3a38', 800: '#232322', 900: '#111111' } } } },
};

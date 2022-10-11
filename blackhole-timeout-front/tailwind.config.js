module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      minHeight: {
        "screen-75": "75vh",
      },
      screens: {
        '3xl': '1890px',
      },
    },
  },
  plugins: [],
}

import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue',
    './plugins/**/*.{js,ts}',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#8677A7",
        secondary: "#65558F",
        secondary2: "#420F75",
        background: "#b2aac7",
        cancel: "#800020",
        bordercancel: "#990033",
      }
    }
  },
  plugins: [],
}

export default config

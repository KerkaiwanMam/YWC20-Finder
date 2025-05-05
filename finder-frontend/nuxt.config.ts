import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui',
    '@nuxt/image',
    '@nuxt/icon',
    '@nuxt/fonts',
    '@nuxtjs/google-fonts',
  ],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  css: [
    '@/assets/css/main.css',
  ],
  googleFonts: {
    families: {
      'Noto Sans Thai': [100, 200, 300, 400, 500, 600, 700, 800, 900],
    },
    display: 'swap', // Optional, for performance
  },
  
})

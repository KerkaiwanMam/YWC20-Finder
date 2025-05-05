import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui', 
    '@nuxt/image', 
    '@nuxt/icon', 
    '@nuxt/fonts'
  ],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  css: [
    '@/assets/css/main.css',
  ],
  fonts: {
    google: {
      families: {
        'Noto+Sans+Thai': true,  // ฟอนต์ Noto Sans Thai
      },
    },
  },
})

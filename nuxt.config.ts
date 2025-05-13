export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: false,
  nitro: {
    preset: 'static'
  },
  modules: [
    '@nuxt/ui',
    '@nuxt/image',
    '@nuxt/icon',
    '@nuxtjs/google-fonts',
  ],
  css: [
    '@/assets/css/main.css',
    '@/assets/css/animations.css',
  ],
  ui: {
    theme: {
      colors: [
        'primary',
        'secondary',
        'secondary2',
        'background',
        'cancel',
        'bordercancel'
      ]
    }
  },
  googleFonts: {
    families: {
      'Noto Sans Thai': [100, 200, 300, 400, 500, 600, 700, 800, 900],
    },
    display: 'swap',
  },
  app: {
    baseURL: '/YWC20-Finder/', 
    head: {
      title: 'Finder',
      link: [
        {
          rel: 'icon',
          type: 'image/x-icon',
          href: '/YWC20-Finder/lovecat.png',
          sizes: '16x16'
        }
      ]
    }
  }
})

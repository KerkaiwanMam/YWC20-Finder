<template>
  <div class="min-h-screen bg-gradient-to-br from-black/20 via-primary to-secondary-2 text-white flex items-center justify-center">
        <RainCanvas />

    <div class="text-center px-6 py-8 max-w-1/2 bg-background2 rounded-lg shadow-lg p-8 backdrop-blur-sm animate-fade-in-up">
      <img src="/logo.svg" alt="Logo" class="w-max h-auto mx-auto mb-4 mt-8 animate-fade-in-up delay-100" />
      <div
        class="mb-4 inline-block px-3 py-1 rounded-full bg-background/30 text-white text-sm font-medium border border-secondary-2-500 animate-fade-in delay-100">
        🚀 Web Programming
      </div>

      <h1 class="text-2xl sm:text-4xl font-extrabold leading-tight mb-4 text-white/80 animate-fade-in-up delay-200 px-16">
        Young Webmaster Camp 20
      </h1>

      <p class="text-primary mb-6 text-lg animate-fade-in-up delay-300 px-16">
       ค้นหารายชื่อผู้ผ่านการคัดเลือก YWC 20!
      </p>

      <NuxtLink
        to="/Candidates"
        class="inline-block bg-primary hover:bg-background text-white font-semibold px-6 py-3 rounded-full shadow-lg transition duration-200 animate-fade-in-up delay-500">
        เริ่มค้นหา →
      </NuxtLink>

      <p class="mt-4 text-sm text-gray-400 animate-fade-in-up delay-700">
        90% of projects are free to do
      </p>

    </div>
  </div>
</template>

<script setup>
import RainCanvas from '@/components/Rain/RainCanvas.vue'


</script>
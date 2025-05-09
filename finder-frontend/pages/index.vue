<template>
  <div class="min-h-screen bg-gradient-to-br from-background via-primary to-secondary-2 text-white flex items-center justify-center">
    <div class="text-center px-6 py-8 max-w-1/2 bg-white/80 rounded-lg shadow-lg p-8 backdrop-blur-sm animate-fade-in-up">
      <NuxtImg :src="Images.logo" alt="Logo" class="w-24 h-24 mx-auto mb-4 animate-fade-in-up delay-100" />
      <div
        class="mb-4 inline-block px-3 py-1 rounded-full bg-background/30 text-secondary-2 text-sm font-medium border border-secondary-2-500 animate-fade-in delay-100">
        🚀 Web Programming
      </div>

      <h1 class="text-4xl sm:text-5xl font-extrabold leading-tight mb-4 text-secondary-2 animate-fade-in-up delay-200">
        Build real world projects<br />
        to learn and showcase
      </h1>

      <p class="text-primary mb-6 text-lg animate-fade-in-up delay-300 px-16">
        A platform to build high quality project challenges with beautiful & modular designs,
        guided by ex-FAANG senior engineers and an active community
      </p>

      <NuxtLink
        to="/Candidates"
        class="inline-block bg-green-500 hover:bg-green-600 text-white font-semibold px-6 py-3 rounded-full shadow-lg transition duration-200 animate-fade-in-up delay-500">
        Explore projects →
      </NuxtLink>

      <p class="mt-4 text-sm text-gray-400 animate-fade-in-up delay-700">
        90% of projects are free to do
      </p>

    </div>
  </div>
</template>

<script setup>
import { Images } from '@/assets/index'


</script>
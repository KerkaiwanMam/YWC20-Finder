<template>
  <div v-for="major in ['design', 'content', 'programming', 'marketing']" :key="major" class="mb-10">
    <h2 class="text-2xl font-bold text-gray-800 mb-4 border-b pb-2">
      {{ capitalize(major) }}
    </h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="c in candidates[major]"
        :key="c.interviewRefNo"
        class="bg-white rounded-2xl shadow-md p-6 hover:shadow-lg transition-shadow duration-300"
      >
        <div class="flex items-center justify-between mb-2">
          <span class="text-sm font-medium text-indigo-600 uppercase tracking-wide">
            {{ c.major }}
          </span>
          <span class="text-xs text-gray-400">Ref: {{ c.interviewRefNo }}</span>
        </div>
        <div class="text-lg font-semibold text-gray-900">
          {{ c.firstName }} {{ c.lastName }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    candidates: { type: Object, required: true },
  },
  methods: {
    capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
  },
};
</script>

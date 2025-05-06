<template>
  <div>
    <div
      v-for="major in ['design', 'content', 'programming', 'marketing']"
      :key="major"
      class="mb-8"
    >
      <h2 class="text-xl font-semibold text-gray-700 mb-2">
        {{ capitalize(major) }}
      </h2>
      <ul class="space-y-2">
        <li
          v-for="c in candidates[major]"
          :key="c.interviewRefNo"
          class="bg-white p-4 rounded shadow hover:bg-gray-50"
        >
          {{ c.major }} - {{ c.firstName }} {{ c.lastName }} ({{ c.interviewRefNo }})
        </li>
      </ul>
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

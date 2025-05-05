<template>
    <div>
      <div v-for="major in ['design', 'content', 'programming']" :key="major">
        <h2>{{ major }}</h2>
        <ul>
          <li v-for="c in candidates[major]" :key="c.interviewRefNo">
            {{ c.major }} - {{ c.firstName }} {{ c.lastName }} ({{ c.interviewRefNo }})
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      candidates: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
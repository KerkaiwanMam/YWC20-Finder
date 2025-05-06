<template>
    <div class="p-4">
      <input
        type="text"
        v-model="searchText"
        @input="onInput"  
        placeholder="ค้นหาด้วยชื่อ, สกุล หรือรหัสสัมภาษณ์"
        class="w-full p-2 border rounded-md"
      />
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchText: '',
        debounceTimer: null
      };
    },
    methods: {
      onInput() {
        clearTimeout(this.debounceTimer);
        this.debounceTimer = setTimeout(() => {
          this.$emit('search', this.searchText.trim());  
        }, 300); // หน่วง 300ms
      }
    },
    beforeDestroy() {
      clearTimeout(this.debounceTimer);
    }
  };
  </script>
  
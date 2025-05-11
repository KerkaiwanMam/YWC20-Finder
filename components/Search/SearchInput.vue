<template>
  <div class="p-4">
    <div class="flex gap-2">
      <input
        type="text"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        @keyup.enter="triggerSearch"
        placeholder="ค้นหาด้วยชื่อ, สกุล หรือรหัสสัมภาษณ์"
        class="w-full text-white/60 p-2 border rounded-md border-white bg-transparent outline-none"
      />
      <button @click="triggerSearch" class="bg-white text-black px-4 rounded-md hover:bg-gray-200 transition">
        ค้นหา
      </button>
      <!-- ปุ่มล้าง -->
      <button
        v-if="modelValue"
        @click="clearSearch"
        class="bg-cancel text-white px-4 rounded-md hover:bg-bordercancel transition"
      >
        ล้าง
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      default: ''
    }
  },
  methods: {
    triggerSearch() {
      this.$emit('search', this.modelValue.trim());
    },
    clearSearch() {
      this.$emit('update:modelValue', ''); // ลบข้อความในช่องค้นหา
      this.$emit('search', ''); // รีเซ็ตการค้นหา
    }
  }
};
</script>

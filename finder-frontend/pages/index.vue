<template>
    <div>
      <div class="bg-pink-500 text-white font-extrabold p-4">
        <h1>รายชื่อผู้สมัคร</h1>
      </div>

      <!-- ช่องค้นหา -->
      <SearchInput @search="handleSearch" />

      <!-- ข้อความผิดพลาด -->
      <div v-if="error" class="text-red-500 p-4">
        {{ error }}
      </div>

      <!-- กำลังโหลด -->
      <div v-else-if="loading" class="text-blue-500 p-4">
        กำลังโหลด...
      </div>

      <!-- แสดงรายชื่อผู้สมัคร -->
      <div v-else>
        <CandidatesList :candidates="filteredCandidates" />
      </div>
    </div>
</template>

<script>
import CandidatesList from '../components/CandidateList.vue';
import SearchInput from '../components/Search/SearchInput.vue';

export default {
  components: {
    CandidatesList,
    SearchInput
  },
  data() {
    return {
      candidates: null,
      error: null,
      searchQuery: '',
      filteredCandidates: [], // สำหรับเก็บผลลัพธ์ที่กรองแล้ว
      loading: false // ใช้สำหรับสถานะกำลังโหลด
    };
  },
  mounted() {
    this.fetchCandidates(); // ดึงข้อมูลทั้งหมดในตอนแรก
  },
  methods: {
    async fetchCandidates(query = '') {
      this.loading = true; // เริ่มต้นโหลดข้อมูล
      this.error = null;
      this.candidates = null;
      try {
        const url = query
          ? `http://localhost:5000/api/candidates?q=${encodeURIComponent(query)}`
          : `http://localhost:5000/api/candidates`;
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        const data = await res.json();
        if (data.error) {
          this.error = data.error;
        } else {
          this.candidates = data.content || data;
          this.filterCandidates(); // ฟิลเตอร์ข้อมูลเมื่อได้ผลลัพธ์
        }
      } catch (e) {
        this.error = 'ไม่สามารถโหลดข้อมูลได้: ' + e.message;
      } finally {
        this.loading = false; // สิ้นสุดการโหลด
      }
    },
    handleSearch(query) {
      this.searchQuery = query;
      this.filterCandidates(); // ฟิลเตอร์ข้อมูลใหม่เมื่อค้นหา
    },
    filterCandidates() {
      if (this.candidates) {
        if (this.searchQuery.trim() === '') {
          this.filteredCandidates = this.candidates; // แสดงข้อมูลทั้งหมดเมื่อไม่มีการค้นหา
        } else {
          // ฟิลเตอร์ข้อมูลให้แสดงเฉพาะที่ตรงกับคำค้นหาจากฟิลด์ต่างๆ
          this.filteredCandidates = this.candidates.filter(candidate =>
            candidate.firstName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            candidate.lastName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            candidate.interviewRefNo.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            candidate.major.toLowerCase().includes(this.searchQuery.toLowerCase())
          );
        }
      }
    }
  }
};
</script>

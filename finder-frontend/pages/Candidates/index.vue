<template>
  <div class="bg-white min-h-screen">
    <div class="bg-background2 text-white font-extrabold p-12 text-center">
      <img src="/logo.svg" alt="Logo" class="w-max h-auto mx-auto mb-4 mt-8 animate-fade-in-up delay-100" />
      <h1>รายชื่อผู้สมัคร</h1>
    </div>

    <div class="px-16 ">
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

  </div>
</template>

<script>
import CandidatesList from '../../components/CandidateList.vue';
import SearchInput from '../../components/Search/SearchInput.vue';

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
      this.loading = true;
      this.error = null;
      this.candidates = null;
      try {
        const url = query
          ? `http://localhost:8000/api/candidates?q=${encodeURIComponent(query)}`
          : `http://localhost:8000/api/candidates`;
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        const data = await res.json();
        console.log(data); // เพิ่มบรรทัดนี้เพื่อตรวจสอบข้อมูล
        if (data.error) {
          this.error = data.error;
        } else {
          // กำหนดค่าของ candidates โดยแยกข้อมูลตามหมวดหมู่
          this.candidates = {
            design: data.design || [],
            programming: data.programming || [],
            marketing: data.marketing || [],
            content: data.content || [],
          };
          this.filteredCandidates = this.candidates; // ✅ ใช้ค่าที่ได้จาก backend โดยตรง
        }
      } catch (e) {
        this.error = 'ไม่สามารถโหลดข้อมูลได้: ' + e.message;
      } finally {
        this.loading = false;
      }
    }, handleSearch(query) {
      console.log('Received search query:', query);  // เพิ่มบรรทัดนี้เพื่อตรวจสอบ
      this.searchQuery = query;
      this.fetchCandidates(query);  // ฟิลเตอร์ข้อมูลเมื่อค้นหา
    },

    // filterCandidates() {
    //   if (this.candidates) {
    //     const filtered = {
    //       design: [],
    //       programming: [],
    //       marketing: [],
    //       content: []
    //     };

    //     // กรองผู้สมัครจากทุกหมวดหมู่
    //     Object.keys(this.candidates).forEach((category) => {
    //       filtered[category] = this.candidates[category].filter(candidate =>
    //         candidate.firstName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
    //         candidate.lastName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
    //         candidate.interviewRefNo.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
    //         candidate.major.toLowerCase().includes(this.searchQuery.toLowerCase())
    //       );
    //     });

    //     // กรองหมวดหมู่ที่มีข้อมูลหลังจากกรอง
    //     this.filteredCandidates = filtered;
    //   }
    // }


  }

};
</script>
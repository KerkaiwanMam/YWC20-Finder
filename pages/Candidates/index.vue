<template>
  <div class="bg-background2 text-white flex items-center justify-center relative min-h-screen">

    <!-- Background RainCanvas -->
    <RainCanvas class="absolute top-0 left-0 w-full h-full z-0" />

    <!-- Main Content -->
    <div class="bg-background2 relative z-10 w-full max-w-4xl px-4  py-12">

      <!-- กำลังโหลด -->
      <div v-if="loading" class="text-center text-blue-500 text-xl py-20 animate-pulse">
        กำลังโหลดข้อมูลผู้สมัคร...
      </div>

      <!-- หลังโหลดเสร็จ -->
      <div v-else>
        <div class="text-white font-extrabold text-center mb-8">
          <img src="/logo.svg" alt="Logo" class="w-max h-auto mx-auto mb-4 mt-8 animate-fade-in-up delay-100" />
          <h1 class="text-3xl">รายชื่อผู้สมัคร</h1>
        </div>

        <!-- ช่องค้นหา -->
        <div class="mb-6">
          <SearchInput v-model="searchQuery" @search="handleSearch" />
        </div>

        <!-- ข้อความผิดพลาด -->
        <div v-if="error" class="text-red-500 text-center p-4">
          {{ error }}
        </div>

        <!-- รายชื่อ -->
        <div v-else>
          <CandidatesList :candidates="filteredCandidates" />
        </div>
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
          ? `https://ywc20-backend.onrender.com/api/candidates?q=${encodeURIComponent(query)}`
          : `http://127.0.0.1:8000/api/candidates` // ใช้ URL ของ backend ที่คุณต้องการ
          ;
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
        // ตรวจสอบว่ามีข้อผิดพลาดที่เกี่ยวข้องกับ status 500 หรือไม่
        if (e.message.includes('HTTP error! status: 500')) {
          this.error = 'ไม่พบรายชื่อที่คุณกำลังค้นหา กรุณากรอกรายละเอียดเพิ่มขึ้น';
        } else {
          this.error = 'ไม่สามารถโหลดข้อมูลได้: ' + e.message;
        }
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
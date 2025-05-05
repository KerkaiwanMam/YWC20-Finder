<template>
    <div>
        <div class="bg-pink-500 text-white font-extrabold p-4 ">
            <h1>รายชื่อผู้สมัคร</h1>
        </div>
        <!-- แสดงข้อความผิดพลาดเมื่อมีข้อผิดพลาด -->
        <div v-if="error" class="text-red-500 p-4">
            {{ error }}
        </div>
        <!-- แสดงข้อความ "กำลังโหลด..." เมื่อยังไม่โหลดข้อมูล -->
        <div v-else-if="candidates === null" class="text-blue-500 p-4">
            กำลังโหลด...
        </div>
        <!-- แสดงรายชื่อผู้สมัครเมื่อโหลดข้อมูลสำเร็จ -->
        <div v-else>
            <CandidatesList :candidates="candidates" />
        </div>
    </div>
</template>

<script>
import CandidatesList from '../components/CandidateList.vue';

export default {
    components: {
        CandidatesList
    },
    data() {
        return {
            candidates: null,
            error: null
        };
    },
    async mounted() {
        try {
            const res = await fetch('http://localhost:5000/api/candidates');
            if (!res.ok) {
                throw new Error(`HTTP error! status: ${res.status}`);
            }
            const data = await res.json();
            if (data.error) {
                this.error = data.error;
            } else {
                this.candidates = data;
            }
        } catch (e) {
            this.error = "ไม่สามารถโหลดข้อมูลได้: " + e.message;
        }
    }
};
</script>


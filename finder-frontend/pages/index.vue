<template>
    <div>
        <h1>รายชื่อผู้สมัคร</h1>
        <div v-if="error">{{ error }}</div>
        <div v-else-if="!candidates">กำลังโหลด...</div>
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
            const data = await res.json();
            if (data.error) {
                this.error = data.error;
            } else {
                this.candidates = data;
            }
        } catch (e) {
            this.error = "ไม่สามารถโหลดข้อมูลได้";
        }
    }
};
</script>
import requests
from config import CANDIDATES_API_URL, INTERVIEW_REF
from services.filter_service import filter_by_category, filter_by_query

def fetch_candidates(query: str = '', allowed_keys=None):
    if allowed_keys is None:
        allowed_keys = ['design', 'programming', 'marketing', 'content']
    
    try:
        # ทำการร้องขอข้อมูลจาก API
        response = requests.get(
            CANDIDATES_API_URL,
            headers={"x-reference-id": INTERVIEW_REF}
        )

        # ตรวจสอบสถานะของการร้องขอ (ตรวจสอบว่าไม่เกิดข้อผิดพลาดจาก API)
        response.raise_for_status()

        # ดึงข้อมูลจาก API
        all_data = response.json()

        # ตรวจสอบว่ามีข้อมูลใน API หรือไม่
        if not all_data:
            raise ValueError("ไม่พบข้อมูลจาก API")

        # กรองข้อมูลตามหมวดหมู่ที่เลือก
        categorized_data = filter_by_category(all_data, allowed_keys)

        # กรองข้อมูลตามคำค้นหาหากมีการระบุ query
        if query:
            categorized_data = filter_by_query(categorized_data, query)

        return categorized_data

    except requests.exceptions.RequestException as err:
        # จัดการข้อผิดพลาดที่เกิดจากการร้องขอ API
        raise ValueError(f"ข้อผิดพลาดในการร้องขอข้อมูลจาก API: {err}")
    
    except Exception as err:
        # จัดการข้อผิดพลาดทั่วไปในฟังก์ชัน
        raise ValueError(f"เกิดข้อผิดพลาดในการประมวลผลข้อมูล: {err}")

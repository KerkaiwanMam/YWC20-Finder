import requests

def fetch_candidates_by_major(interview_ref):
    url = "https://api.ywc20.ywc.in.th/homework/candidates"
    
    # ส่งคำขอไปยัง API โดยใช้ headers ที่ระบุ interviewRefNo
    headers = {
        "x-reference-id": interview_ref  # ใช้ interview_ref เป็นค่าใน header
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # ตรวจสอบข้อผิดพลาด HTTP
        data = response.json()

        # แสดงข้อมูลผู้สมัคร
        print(f"รายชื่อผู้สมัครสำหรับเลขประจำตัว {interview_ref}:")
        for candidate in data.get('design', []):  # ดึงข้อมูลจากหมวด design
            print(f"{candidate['major']} -- {candidate['firstName']} {candidate['lastName']} - เลขประจำตัว: {candidate['interviewRefNo']}")
        for candidate in data.get('content', []):  # ดึงข้อมูลจากหมวด content
            print(f"{candidate['major']} -- {candidate['firstName']} {candidate['lastName']} - เลขประจำตัว: {candidate['interviewRefNo']}")
        for candidate in data.get('programming', []):  # ดึงข้อมูลจากหมวด programming
            print(f"{candidate['major']} -- {candidate['firstName']} {candidate['lastName']} - เลขประจำตัว: {candidate['interviewRefNo']}")

    except requests.HTTPError as http_err:
        print(f"เกิดข้อผิดพลาด HTTP: {http_err}")
    except Exception as err:
        print(f"เกิดข้อผิดพลาด: {err}")

if __name__ == "__main__":
    interview_ref = "PG27"  # ค่าเลขประจำตัวที่ต้องการส่งใน header
    fetch_candidates_by_major(interview_ref)

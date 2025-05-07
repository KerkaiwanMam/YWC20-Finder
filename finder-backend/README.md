# YWC20 Candidates API Proxy (Flask)

แอป Flask นี้ทำหน้าที่เป็น Proxy API สำหรับเรียกข้อมูลผู้สมัครจากระบบ YWC Homework API พร้อมรองรับการเชื่อมต่อจาก Frontend เช่น Nuxt.js

## 🛠️ การติดตั้งและใช้งาน

### 1. Clone โปรเจกต์
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo


# 🐍 Flask App with Nodemon Auto-Reload

โปรเจกต์นี้เป็นตัวอย่างการใช้ `Flask` และสามารถรันด้วย `nodemon` เพื่อให้รีโหลดอัตโนมัติเมื่อไฟล์ `.py` ถูกเปลี่ยนแปลง

---

## ✅ Requirements

- Python 3.x
- pip
- Node.js & npm (สำหรับติดตั้ง nodemon)

---

## 🔧 Installation

### 1. ติดตั้ง Python dependencies

```bash
pip install -r requirements.txt

หรือถ้าไม่มีไฟล์ requirements.txt ให้ติดตั้ง Flask และ requests:
pip install flask requests flask-cors

2. ติดตั้ง nodemon (ผ่าน npm)
npm install -g nodemon

🚀 Run with Nodemon

nodemon --exec python app.py

uvicorn app:app --reload
uvicorn app:app --reload --port 5000

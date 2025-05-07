from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.candidates import router as candidates_router

app = FastAPI(
    title="YWC20 Finder API",
    version="1.0",
    description="เอกสาร API สำหรับค้นหาผู้สมัครที่ผ่านการคัดเลือก YWC20"
)

# ตั้งค่า CORS เพื่ออนุญาตการร้องขอจาก localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # หรือใช้ ["*"] ถ้าต้องการให้ทุกที่สามารถเชื่อมต่อได้
    allow_credentials=True,
    allow_methods=["*"],  # หรือระบุ HTTP methods ที่อนุญาต เช่น ["GET", "POST"]
    allow_headers=["*"],  # หรือระบุ headers ที่อนุญาต
)

# รวม router ที่ประกาศใน routes/candidates.py
app.include_router(candidates_router)

# เพิ่มการตั้งค่า port และ host ที่ต้องการ
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

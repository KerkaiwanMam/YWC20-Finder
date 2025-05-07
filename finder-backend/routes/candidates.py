from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List
from services.candidates_service import fetch_candidates

router = APIRouter()

# Pydantic model for candidate
class Candidate(BaseModel):
    firstName: str
    lastName: str
    interviewRefNo: str
    major: str

# Response model for grouped candidates
class CandidatesGroupedByCategory(BaseModel):
    design: List[Candidate]
    programming: List[Candidate]
    marketing: List[Candidate]
    content: List[Candidate]

@router.get("/api/candidates", response_model=CandidatesGroupedByCategory)
async def get_candidates(
    q: str = "", 
    category: List[str] = Query(default=["design", "programming", "marketing", "content"], description="ประเภทของผู้สมัคร (เลือกได้มากกว่า 1: design, programming, marketing, content)")
):
    """
    ค้นหาผู้สมัครที่ผ่านการคัดเลือกตามคำค้นหาและประเภท
    """
    try:
        data = fetch_candidates(query=q, allowed_keys=category)
        if not any(data.values()):
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลที่ตรงกับคำค้นหา")
        return data
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"เกิดข้อผิดพลาด: {err}")

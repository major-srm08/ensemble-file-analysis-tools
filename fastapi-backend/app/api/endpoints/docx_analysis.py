from fastapi import APIRouter
from app.services.docx_service import analyze_docx

router = APIRouter()

@router.get("/docx")
async def docx_analysis():
    result = analyze_docx()
    return {"status": "success", "data": result}


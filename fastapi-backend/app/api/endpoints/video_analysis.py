from fastapi import APIRouter
from app.services.video_service import analyze_video

router = APIRouter()

@router.get("/video")
async def video_analysis():
    result = analyze_video()
    return {"status": "success", "data": result}


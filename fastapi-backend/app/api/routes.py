from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from app.video_analysis.main import analyze_video
from app.docx_analysis.main import analyze_docx

router = APIRouter()

# Define a request model to accept a file path
class FilePathRequest(BaseModel):
    file_path: str

@router.post("/analyze/video")
async def analyze_video_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_video(file_path)
    return {
        "file_path": file_path,
        "analysis_result": analysis_result
    }

@router.post("/analyze/docx")
async def analyze_docx_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_docx(file_path)
    return {
        "file_path": file_path,
        "analysis_result": analysis_result
    }


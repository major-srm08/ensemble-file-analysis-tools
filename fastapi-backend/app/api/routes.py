from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from app.video_analysis.main import analyze_video
from app.docx_analysis.main import analyze_docx
from app.image_analysis.main import analyze_image
from app.xlsx_analysis.main import analyze_xlsx
from app.exe_analysis.main import analyze_exe

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
        "analysis_result": analysis_result
    }

@router.post("/analyze/image")
async def analyze_image_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_image(file_path)
    return {
        "analysis_result": analysis_result
    }
    
@router.post("/analyze/xlsx")
async def analyze_image_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_xlsx(file_path)
    return {
        "analysis_result": analysis_result
    }
    
@router.post("/analyze/exe")
async def analyze_exe_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_exe(file_path)
    return {
        "analysis_result": analysis_result
    }

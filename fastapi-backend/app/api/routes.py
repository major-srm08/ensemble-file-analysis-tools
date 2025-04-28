from fastapi import APIRouter, HTTPException, UploadFile, File
import shutil
from pydantic import BaseModel
import os
from app.video_analysis.main import analyze_video
from app.docx_analysis.main import analyze_docx
from app.image_analysis.main import analyze_image
from app.xlsx_analysis.main import analyze_xlsx
from app.exe_analysis.main import analyze_exe
from app.mp3_analysis.main import analyze_mp3

router = APIRouter()

UPLOAD_DIR = "/home/kali/Documents/GitHub/ensemble-file-analysis-tools/uploaded_files/"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure directory exists

SUPPORTED_FORMATS = {
    ".docx": analyze_docx,
    ".xlsx": analyze_xlsx,
    ".exe": analyze_exe,
    ".jpg": analyze_image,
    ".mp4": analyze_video,
    # ".pdf": analyze_pdf,  # To be implemented
    ".mp3": analyze_mp3, # To be implemented
}

# Define a request model to accept a file path
class FilePathRequest(BaseModel):
    file_path: str



@router.post("/upload/")
async def upload_and_analyze(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext not in SUPPORTED_FORMATS:
        raise HTTPException(status_code=400, detail="Unsupported file format.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)  # Full absolute path
    print(f"🔄 Saving file to: {file_path}")  # Debug output

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("✅ File saved successfully.")  # Debug output
        return {"filename": file.filename, "message": "File uploaded successfully", "path": file_path}

    except Exception as e:
        print(f"❌ Error saving file: {e}")  # Debug output
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")


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

@router.post("/analyze/mp3")
async def analyze_docx_file(request: FilePathRequest):
    file_path = request.file_path

    # Check if file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File not found!")

    # Perform analysis and return structured JSON response
    analysis_result = analyze_mp3(file_path)
    return {
        "analysis_result": analysis_result
    }
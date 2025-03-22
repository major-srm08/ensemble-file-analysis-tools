import logging
from app.video_analysis.analysis_plugins import (
    metadata_analysis,
    codec_inspection,
    frame_extraction,
    static_analysis,
    integrity_check,
    steganography_check,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze_video(file_path):
    logging.info(f"Analyzing video file: {file_path}")
    results = {}

    try:
        results["metadata_analysis"] = metadata_analysis.analyze(file_path)
        results["codec_inspection"] = codec_inspection.analyze(file_path)
        results["frame_extraction"] = frame_extraction.analyze(file_path)
        results["static_analysis"] = static_analysis.analyze(file_path)
        results["integrity_check"] = integrity_check.analyze(file_path)
        results["steganography_check"] = steganography_check.analyze(file_path)

        status = "suspicious" if any(tool.get("recommendation") for tool in results.values()) else "safe"

    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        results["error"] = {"status": "error", "details": str(e)}
        status = "error"

    return {"file_type": "mp4", "status": status, "tool_insights": results}


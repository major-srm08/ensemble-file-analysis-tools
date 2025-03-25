import logging
from app.image_analysis.analysis_plugins import (
    metadata_analysis,
    integrity_check,
    steganography_check,
    security_analysis,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze_image(file_path):
    logging.info(f"Analyzing file: {file_path}")
    results = {}

    try:
        results["metadata_analysis"] = metadata_analysis.extract_metadata(file_path)
        results["file_integrity_check"] = integrity_check.check_integrity(file_path)
        results["steganography_check"] = steganography_check.detect_steganography(file_path)
        results["security_analysis"] = security_analysis.security_scan(file_path)

        # status = "suspicious" if any(tool.get("recommendation") for tool in results.values()) else "safe"

    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        results["error"] = {"status": "error", "details": str(e)}
        status = "error"

    # return {"file_type": "docx", "status": status, "tool_insights": results}
    return results

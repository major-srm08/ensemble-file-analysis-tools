import logging
from app.docx_analysis.analysis_plugins import (
    metadata_analysis,
    ole_inspection,
    macro_analysis,
    static_content,
    integrity_check,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze_docx(file_path):
    logging.info(f"Analyzing file: {file_path}")
    results = {}

    try:
        results["metadata_analysis"] = metadata_analysis.analyze(file_path)
        results["ole_object_inspection"] = ole_inspection.analyze(file_path)
        results["macro_behavior_analysis"] = macro_analysis.analyze(file_path)
        results["static_content_analysis"] = static_content.analyze(file_path)
        results["file_integrity_check"] = integrity_check.analyze(file_path)

        status = "suspicious" if any(tool.get("recommendation") for tool in results.values()) else "safe"

    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        results["error"] = {"status": "error", "details": str(e)}
        status = "error"

    return {"file_type": "docx", "status": status, "tool_insights": results}


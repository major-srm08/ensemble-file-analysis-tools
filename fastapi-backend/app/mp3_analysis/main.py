import json
import logging
import os
import glob
from app.mp3_analysis.analysis_plugins import (
    metadata_analysis,
    codec_inspection,
    spectral_analysis,
    static_analysis,
    integrity_check,
    steganography_check,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze_mp3(file_path):
    logging.info(f"Analyzing file: {file_path}")
    results = {}

    try:
        # Run all analysis modules
        results["metadata_analysis"] = metadata_analysis.analyze(file_path)
        results["codec_inspection"] = codec_inspection.analyze(file_path)
        results["spectral_analysis"] = spectral_analysis.analyze(file_path)
        results["static_analysis"] = static_analysis.analyze(file_path)
        results["integrity_check"] = integrity_check.analyze(file_path)
        results["steganography_check"] = steganography_check.analyze(file_path)

        # Determine final status and collect recommendations if needed
        status = "safe"
        recommendations = []

        for tool, result in results.items():
            if result["status"] in ["suspicious", "error"]:
                status = "suspicious"
                if "recommendation" in result:
                    recommendations.append(result["recommendation"])

        final_result = {
            "file_type": "mp3",
            "status": status,
            "tool_insights": results
        }

        if recommendations:
            final_result["recommendations"] = recommendations

    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        final_result = {
            "file_type": "mp3",
            "status": "error",
            "error_details": str(e),
            "recommendation": "Check logs and verify the file manually."
        }

    logging.info(f"Analysis completed. Final Status: {final_result['status']}")
    return final_result


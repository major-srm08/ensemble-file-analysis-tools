from app.pdf_analysis.analysis_plugins.metadata_analysis import analyze_metadata
from app.pdf_analysis.analysis_plugins.pdfid_analysis import analyze_pdfid
from app.pdf_analysis.analysis_plugins.pdf_parser_analysis import analyze_pdf_parser
from app.pdf_analysis.analysis_plugins.peepdf_analysis import analyze_peepdf
from app.pdf_analysis.analysis_plugins.integrity_check import check_integrity

def analyze_pdf(pdf_path):
    result = {
        "file_type": "pdf",
        "status": "safe",
        "tool_insights": {}
    }

    tools = {
        "metadata_analysis": analyze_metadata,
        "pdfid_analysis": analyze_pdfid,
        "pdf_parser_analysis": analyze_pdf_parser,
        "peepdf_analysis": analyze_peepdf,
        "file_integrity_check": check_integrity
    }

    for tool_name, tool_func in tools.items():
        tool_result = tool_func(pdf_path)
        result["tool_insights"][tool_name] = tool_result

        if tool_result["status"] == "suspicious":
            result["status"] = "suspicious"
        elif tool_result["status"] == "error" and result["status"] != "suspicious":
            result["status"] = "error"

    return result

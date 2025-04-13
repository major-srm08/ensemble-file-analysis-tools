import json
import os

from analysis_plugins.metadata_analysis import analyze_metadata
from analysis_plugins.pdfid_analysis import analyze_pdfid
from analysis_plugins.pdf_parser_analysis import analyze_pdf_parser
from analysis_plugins.peepdf_analysis import analyze_peepdf
from analysis_plugins.integrity_check import check_integrity

def analyze_pdf(pdf_path):
    result = {
        "file_path": pdf_path,
        "analysis_result": {
            "file_type": "pdf",
            "status": "safe",
            "tool_insights": {}
        }
    }

    # Run all tools
    tools = {
        "metadata_analysis": analyze_metadata,
        "pdfid_analysis": analyze_pdfid,
        "pdf_parser_analysis": analyze_pdf_parser,
        "peepdf_analysis": analyze_peepdf,
        "file_integrity_check": check_integrity
    }

    # Execute tools and collect results
    for tool_name, tool_func in tools.items():
        tool_result = tool_func(pdf_path)
        result["analysis_result"]["tool_insights"][tool_name] = tool_result

        if tool_result["status"] == "suspicious":
            result["analysis_result"]["status"] = "suspicious"
        elif tool_result["status"] == "error" and result["analysis_result"]["status"] != "suspicious":
            result["analysis_result"]["status"] = "error"

    return result

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}.json")

            print(f"[+] Analyzing: {filename}")
            analysis_data = analyze_pdf(pdf_path)

            with open(output_path, "w") as f:
                json.dump(analysis_data, f, indent=4)

            print(f"[✓] Report saved: {output_path}")

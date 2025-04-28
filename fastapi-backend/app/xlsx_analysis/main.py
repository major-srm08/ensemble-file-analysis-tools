import os
import logging
import magic
import pandas as pd
import olefile
from oletools.olevba import VBA_Parser

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def analyze_xlsx(file_path):
    logging.info(f"Analyzing file: {file_path}")

    results = {}
    status = ""

    try:
        # Validate file type
        logging.info("Validating file type...")
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)

        if "excel" not in file_type and "spreadsheet" not in file_type:
            results["file_type_check"] = {
                "status": "suspicious",
                "details": f"Detected file type: {file_type}",
                "recommendation": "File type does not match .xlsx, investigate further."
            }
        else:
            results["file_type_check"] = {
                "status": "safe",
                "details": f"Detected file type: {file_type}"
            }

        # Check for macros and VBA code
        logging.info("Checking for macros and VBA code...")
        if olefile.isOleFile(file_path) or file_path.endswith(".xlsm"):
            vba_parser = VBA_Parser(file_path)
            if vba_parser.detect_vba_macros():
                macro_code = vba_parser.get_vba_code_all_modules()
                malicious_macros = any(keyword in macro_code for keyword in ["Shell", "Execute", "Run"])

                results["macro_analysis"] = {
                    "status": "suspicious" if malicious_macros else "safe",
                    "details": "File contains macros." if malicious_macros else "No malicious macros detected.",
                    "recommendation": "Review VBA code for potential threats." if malicious_macros else None
                }
            else:
                results["macro_analysis"] = {
                    "status": "safe",
                    "details": "No macros detected."
                }
        else:
            results["macro_analysis"] = {
                "status": "safe",
                "details": "File does not contain VBA macros."
            }

        # Analyze content obfuscation (Base64, Hex encoding)
        logging.info("Analyzing content obfuscation...")
        df = pd.read_excel(file_path, sheet_name=None)
        obfuscation_detected = False

        for sheet_name, sheet_data in df.items():
            for cell in sheet_data.stack():
                if isinstance(cell, str) and any(substr in cell for substr in ["=CHAR", "BASE64", "HEX", "ENCODE"]):
                    obfuscation_detected = True
                    break

        results["obfuscation_analysis"] = {
            "status": "suspicious" if obfuscation_detected else "safe",
            "details": "Potential obfuscated content found in cells." if obfuscation_detected else "No obfuscation detected.",
            "recommendation": "Review cell content for obfuscation techniques." if obfuscation_detected else None
        }

        # Check for hidden sheets
        logging.info("Checking for hidden content...")
        hidden_sheets = [sheet for sheet in df.keys() if sheet.startswith("_")]
        results["hidden_content_check"] = {
            "status": "suspicious" if hidden_sheets else "safe",
            "details": f"Hidden sheets detected: {hidden_sheets}" if hidden_sheets else "No hidden sheets found.",
            "recommendation": "Investigate hidden sheets for potential threats." if hidden_sheets else None
        }

        # Check for external links
        logging.info("Checking for external links...")
        external_links = []

        for sheet_name, sheet_data in df.items():
            for cell in sheet_data.stack():
                if isinstance(cell, str) and "http" in cell:
                    external_links.append(cell)

        results["external_links_check"] = {
            "status": "suspicious" if external_links else "safe",
            "details": f"External links found: {external_links}" if external_links else "No external links detected.",
            "recommendation": "Review external links to ensure they are not malicious." if external_links else None
        }

        # File size anomaly check
        logging.info("Checking for file size anomalies...")
        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:  # Larger than 10 MB
            results["file_size_check"] = {
                "status": "suspicious",
                "details": f"File size is {file_size / (1024 * 1024):.2f} MB",
                "recommendation": "Large file size may indicate embedded objects, review manually."
            }
        else:
            results["file_size_check"] = {
                "status": "safe",
                "details": f"File size is {file_size / (1024 * 1024):.2f} MB"
            }
        
        status = "suspicious" if any(tool.get("recommendation") for tool in results.values()) else "safe"

    except Exception as e:
        results["error"] = {
            "status": "error",
            "details": f"Error processing file: {str(e)}"
        }

    return {"file_type": "xlsx", "status": status, "tool_insights": results}


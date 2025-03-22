import os
import magic
import pandas as pd
import olefile
from oletools.olevba import VBA_Parser

def analyze_xlsx(file_path):
    result = {"type": "xlsx", "status": "safe", "recommendations": []}

    try:
        # Validate file type
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)
        if "excel" not in file_type and "spreadsheet" not in file_type:
            result["status"] = "suspicious"
            result["recommendations"].append("File type does not match .xlsx")
            return result

        # Check for macros and VBA code
        if olefile.isOleFile(file_path) or file_path.endswith(".xlsm"):
            vba_parser = VBA_Parser(file_path)
            if vba_parser.detect_vba_macros():
                result["status"] = "suspicious"
                result["recommendations"].append("File contains macros, review VBA code.")

                # Extract and analyze VBA code
                macro_code = vba_parser.get_vba_code_all_modules()
                if "Shell" in macro_code or "Execute" in macro_code or "Run" in macro_code:
                    result["recommendations"].append("Potentially malicious macro detected (Shell/Execute/Run commands).")

        # Analyze content obfuscation (strings like Base64 or Hex encoding)
        df = pd.read_excel(file_path, sheet_name=None)
        for sheet_name, sheet_data in df.items():
            for cell in sheet_data.stack():
                if isinstance(cell, str):
                    if any(substr in cell for substr in ["=CHAR", "BASE64", "HEX", "ENCODE"]):
                        result["status"] = "suspicious"
                        result["recommendations"].append(f"Potential obfuscated content detected in sheet '{sheet_name}'.")

        # Check for hidden content
        hidden_sheets = [sheet for sheet in df.keys() if sheet.startswith("_")]
        if hidden_sheets:
            result["status"] = "suspicious"
            result["recommendations"].append(f"Hidden sheets detected: {hidden_sheets}")

        # Check for external links
        external_links = []
        for sheet_name, sheet_data in df.items():
            for cell in sheet_data.stack():
                if isinstance(cell, str) and "http" in cell:
                    external_links.append(cell)
        if external_links:
            result["status"] = "suspicious"
            result["recommendations"].append(f"External links found: {external_links}")

        # File size anomaly check
        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:  # Larger than 10 MB
            result["recommendations"].append("File size is unusually large, investigate for embedded objects.")

    except Exception as e:
        result["status"] = "error"
        result["recommendations"].append(f"Error processing file: {str(e)}")

    return result


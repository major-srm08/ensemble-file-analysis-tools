import os
import fitz  # PyMuPDF

def check_integrity(pdf_path):
    """
    Performs a basic integrity check:
    - File exists
    - File is not empty
    - Can be opened by PyMuPDF (not corrupt)
    """

    if not os.path.exists(pdf_path):
        return {
            "tool": "integrity_check",
            "status": "error",
            "details": ["File does not exist."]
        }

    if os.path.getsize(pdf_path) == 0:
        return {
            "tool": "integrity_check",
            "status": "error",
            "details": ["File is empty."]
        }

    try:
        doc = fitz.open(pdf_path)
        num_pages = doc.page_count
        doc.close()

        return {
            "tool": "integrity_check",
            "status": "safe",
            "details": [f"PDF opened successfully with {num_pages} pages."]
        }

    except Exception as e:
        return {
            "tool": "integrity_check",
            "status": "error",
            "details": [f"Could not open PDF: {str(e)}"]
        }

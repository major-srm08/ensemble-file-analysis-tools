import fitz

def analyze_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    metadata = doc.metadata

    status = "safe"
    details = []

    if not metadata:
        details.append("No metadata found.")
    else:
        details.append(f"Metadata extracted: {metadata}")

    return {"status": status, "details": details}

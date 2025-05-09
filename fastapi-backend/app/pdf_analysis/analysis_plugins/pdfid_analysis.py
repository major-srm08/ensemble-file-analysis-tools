import subprocess

def analyze_pdfid(pdf_path):
    result = subprocess.run(["pdfid", pdf_path], capture_output=True, text=True)
    output = result.stdout

    status = "safe"
    details = []

    if "/JavaScript" in output or "/OpenAction" in output:
        status = "suspicious"
        details.append("Potential JavaScript found.")
    else:
        details.append("No suspicious elements detected.")

    return {"status": status, "details": details}

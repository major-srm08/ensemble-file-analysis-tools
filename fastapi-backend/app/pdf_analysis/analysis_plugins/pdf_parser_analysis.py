import subprocess

def analyze_pdf_parser(pdf_path):
    try:
        result = subprocess.run(["pdf-parser", pdf_path], capture_output=True, text=True)
        output = result.stdout

        status = "safe"
        details = []

        if "obj" in output and "stream" in output:
            details.append("PDF contains streams and objects.")
        else:
            details.append("No suspicious objects detected.")

    except Exception as e:
        status = "error"
        details.append(f"Error running pdf-parser: {str(e)}")

    return {"status": status, "details": details}

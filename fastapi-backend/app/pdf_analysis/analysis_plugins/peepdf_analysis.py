import subprocess
import os

def analyze_peepdf(pdf_path):
    # Path to local peepdf script
    peepdf_script = os.path.expanduser("~/peepdf/peepdf.py")

    if not os.path.exists(peepdf_script):
        return {
            "tool": "peepdf",
            "status": "error",
            "details": ["peepdf.py script not found at expected path."]
        }

    try:
        result = subprocess.run(
            ["python3", peepdf_script, "-i", pdf_path],
            capture_output=True,
            text=True,
            timeout=15
        )
        output = result.stdout.lower()

        if "javascript" in output or "openaction" in output:
            return {
                "tool": "peepdf",
                "status": "suspicious",
                "details": ["Potentially malicious features detected (e.g., JavaScript, OpenAction)."]
            }

        return {
            "tool": "peepdf",
            "status": "safe",
            "details": ["No suspicious elements found."]
        }

    except Exception as e:
        return {
            "tool": "peepdf",
            "status": "error",
            "details": [f"Error running peepdf: {str(e)}"]
        }

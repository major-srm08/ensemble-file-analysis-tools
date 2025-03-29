import subprocess
import json

def security_scan(image_path):
    """
    Scans the file for malware using ClamAV and returns structured results.
    """

    cmd = ["clamscan", "--no-summary", "--infected", image_path]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        # Check if the file is infected
        if "FOUND" in output:
            details = [line for line in output.split("\n") if "FOUND" in line]
            return {
                "status": "suspicious",
                "details": details,
                "recommendation": "Perform deeper analysis using yara rules or a sandbox."
            }
        else:
            return {
                "status": "safe",
                "details": ["No malware detected"]
            }

    except Exception as e:
        return {
            "status": "error",
            "details": [str(e)],
            "recommendation": "Ensure ClamAV is installed and updated."
        }

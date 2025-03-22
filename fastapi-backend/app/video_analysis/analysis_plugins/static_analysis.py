import re

# Only flag patterns that resemble real commands
KNOWN_MALICIOUS_PATTERNS = [
    r"rm -rf \S+",
    r"del /F /Q \S+",
    r"powershell -enc \S+"
]

def analyze(file_path):
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        suspicious_sequences = []
        for pattern in KNOWN_MALICIOUS_PATTERNS:
            if re.search(pattern.encode(), content):
                suspicious_sequences.append(pattern)

        status = "safe" if not suspicious_sequences else "suspicious"
        recommendation = "Inspect further if necessary." if suspicious_sequences else "No suspicious patterns found."

        return {
            "status": status,
            "details": suspicious_sequences,
            "recommendation": recommendation
        }

    except Exception as e:
        return {
            "status": "error",
            "details": [str(e)],
            "recommendation": "Ensure file is accessible."
        }


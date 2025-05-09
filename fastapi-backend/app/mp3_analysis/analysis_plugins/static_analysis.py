import re

def analyze(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        # Example: Look for suspicious byte sequences
        patterns = [b"malware", b"trojan", b"virus"]
        found_patterns = [p.decode() for p in patterns if p in data]

        if found_patterns:
            return {
                "status": "suspicious",
                "details": [f"Suspicious byte sequences found: {found_patterns}"],
                "recommendation": "Perform deeper static analysis using YARA rules."
            }

        return {
            "status": "safe",
            "details": ["No suspicious byte sequences found."]
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Check if the file is accessible and not encrypted."
        }

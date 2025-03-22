import re

def analyze(file_path):
    suspicious_patterns = [
        r'base64',  # Look for Base64 encoding
        r'obfuscate',  # Detect the word "obfuscate"
        r'0x[a-fA-F0-9]+',  # Detect hex values
        r'\bexec\b',  # Detect 'exec' keyword
    ]

    abnormalities = []
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        for pattern in suspicious_patterns:
            if re.search(pattern, content):
                abnormalities.append(f"Pattern '{pattern}' detected in file content.")
    if abnormalities:
        return {
            "status": "suspicious",
            "details": abnormalities,
            "recommendation": "Review content for obfuscated or malicious payloads."
        }
    else:
        return {
            "status": "safe",
            "deatils": ["No suspicious patterns detected."],
        }

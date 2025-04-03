import subprocess

def analyze_docx():
    process = subprocess.run(["python3", "app/docx_analysis/main.py"], capture_output=True, text=True)
    return process.stdout


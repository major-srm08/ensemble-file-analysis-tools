import subprocess

def analyze(file_path):
    try:
        command = f"strings {file_path} | grep -Ei 'cmd|powershell|base64|shellcode|exec'"
        output = subprocess.getoutput(command)

        if output:
            return {
                "status": "suspicious",
                "details": output.splitlines(),
                "recommendation": "Possible embedded commands detected. Inspect further."
            }
        else:
            return {
                "status": "safe",
                "details": ["No suspicious static content detected."]
            }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure 'strings' is available and the file is valid."
        }

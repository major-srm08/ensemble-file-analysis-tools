import subprocess

def analyze(file_path):
    try:
        command = f"olevba {file_path}"
        output = subprocess.check_output(command, shell=True, text=True)

        macros_detected = "Macros" in output
        details = output.splitlines()

        if macros_detected:
            return {
                "status": "suspicious",
                "details": details,
                "recommendation": "Analyze the VBA macro code for malicious content."
            }
        else:
            return {
                "status": "safe",
                "details": ["No macros detected."]
            }
    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure olevba is installed and the file is valid."
        }

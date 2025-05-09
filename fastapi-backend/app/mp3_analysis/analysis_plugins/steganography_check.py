import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze(file_path):
    """Check if MP3Stego signatures exist in the file."""
    result = {"status": "safe", "details": []}
    
    try:
        output = subprocess.run(["strings", file_path], capture_output=True, text=True)
        if "MP3Stego" in output.stdout:
            result["status"] = "suspicious"
            result["details"].append("Possible MP3Stego-embedded content detected.")
            result["recommendation"] = "Use forensic tools for deeper analysis."
    except Exception as e:
        logging.error(f"MP3Stego detection failed: {e}")
        result["status"] = "error"
        result["details"].append(str(e))

    return result

if __name__ == "__main__":
    test_file = "input/sample.mp3"
    print(analyze(test_file))

import subprocess
import json

def analyze(file_path):
    try:
        command = f'ffprobe -v quiet -print_format json -show_streams "{file_path}"'
        output = subprocess.check_output(command, shell=True, text=True)
        data = json.loads(output)

        codecs = []
        for stream in data.get("streams", []):
            if "codec_name" in stream:
                codecs.append(stream["codec_name"])

        suspicious_codecs = [c for c in codecs if c in ["vp6f", "flv", "xvid"]]

        if suspicious_codecs:
            return {
                "status": "suspicious",
                "details": [f"Unexpected codec detected: {', '.join(suspicious_codecs)}"],
                "recommendation": "Verify codec compatibility and safety."
            }
        else:
            return {
                "status": "safe",
                "details": ["No unusual codecs detected."]
            }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure FFmpeg is installed and the file is valid."
        }

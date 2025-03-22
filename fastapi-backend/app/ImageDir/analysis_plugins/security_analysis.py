import subprocess

def security_scan(image_path):
    """Scans the file for malware using ClamAV."""
    cmd = ["clamscan", "--no-summary", "--infected", image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)

    return result.stdout if result.stdout else f"{image_path} is clean."

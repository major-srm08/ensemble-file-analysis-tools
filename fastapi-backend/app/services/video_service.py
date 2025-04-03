import subprocess

def analyze_video():
    process = subprocess.run(["python3", "app/video_analysis/main.py"], capture_output=True, text=True)
    return process.stdout


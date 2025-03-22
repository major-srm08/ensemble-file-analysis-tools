import os
import json
import subprocess
from pathlib import Path

OUTPUT_DIR = "output/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_metadata(image_path):
    output_file = os.path.join(OUTPUT_DIR, f"{Path(image_path).stem}_metadata.json")
    cmd = ["exiftool", "-json", image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        metadata = json.loads(result.stdout)
        with open(output_file, "w") as f:
            json.dump(metadata, f, indent=4)
    return output_file


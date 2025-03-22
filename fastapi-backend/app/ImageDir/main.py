import os
from analysis_plugins.metadata_analysis import extract_metadata
from analysis_plugins.integrity_check import check_integrity
from analysis_plugins.steganography_check import detect_steganography
from analysis_plugins.security_analysis import security_scan

INPUT_DIR = "input/"
os.makedirs(INPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    for image_file in os.listdir(INPUT_DIR):
        image_path = os.path.join(INPUT_DIR, image_file)
        if image_file.lower().endswith(".jpg"):
            print(f"Processing {image_file}...")
            print(extract_metadata(image_path))
            print(check_integrity(image_path))
            print(detect_steganography(image_path))
            print(security_scan(image_path))

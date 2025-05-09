import hashlib
import json
import os
from PIL import Image

def calculate_hash(file_path, hash_algorithm="sha256"):
    """Calculates the hash of a file using the specified algorithm (default: SHA256)."""
    try:
        hash_func = getattr(hashlib, hash_algorithm)()  # Get the hash function

        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):  # Read in chunks
                hash_func.update(chunk)

        return hash_func.hexdigest()

    except FileNotFoundError:
        return None

def validate_jpg_structure(image_path):
    """Checks if the file is a valid and non-corrupt JPG image."""
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify the integrity of the image
        return True
    except (IOError, SyntaxError):
        return False

def check_integrity(image_path):
    """
    Performs integrity checks:
    1. Calculates SHA256 hash
    2. Validates JPEG structure
    """
    if not os.path.exists(image_path):
        return {
            "status": "error",
            "details": ["File not found"],
            "recommendation": "Ensure the file exists before performing integrity checks."
        }

    # Step 1: Calculate SHA256 Hash
    file_hash = calculate_hash(image_path)

    # Step 2: Validate JPEG Structure
    if not validate_jpg_structure(image_path):
        return {
            "status": "suspicious",
            "details": ["JPG file structure is invalid or corrupted"],
            "recommendation": "File might be damaged or intentionally modified."
        }

    return {
        "status": "safe",
        "details": [f"SHA256: {file_hash}", "File format is valid"],
    }

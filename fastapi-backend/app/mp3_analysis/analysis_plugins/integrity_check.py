import hashlib
import logging
import os
import re

# Common patterns of weak/vulnerable hashes (example: repeating characters, short hashes, etc.)
VULNERABLE_HASH_PATTERNS = [
    r"^0+$",  # All zeros (highly unusual)
    r"^f+$",  # All Fs (suspicious hash)
    r"^(.)\1+$",  # Repeated single character hash (e.g., "aaaaaaaa...")
    r"^1234.*$",  # Starts with 1234 (example of poor hashing)
]

def compute_hash(file_path):
    """Computes the SHA-256 hash of the given file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
    except Exception as e:
        logging.error(f"Error computing hash: {e}")
        return None
    return hash_sha256.hexdigest()

def is_vulnerable_hash(file_hash):
    """Checks if the computed hash matches a known weak/vulnerable pattern."""
    for pattern in VULNERABLE_HASH_PATTERNS:
        if re.match(pattern, file_hash):
            return True
    return False

def analyze(file_path):
    """Checks the integrity of the MP3 file using its hash."""
    if not os.path.exists(file_path):
        return {
            "status": "error",
            "details": "File not found.",
            "recommendation": "Ensure the file exists in the input directory."
        }

    computed_hash = compute_hash(file_path)

    if computed_hash is None:
        return {
            "status": "error",
            "details": "Failed to compute file hash.",
            "recommendation": "Ensure the file is not corrupted and check system file access permissions."
        }

    if is_vulnerable_hash(computed_hash):
        return {
            "status": "suspicious",
            "details": [f"File hash appears weak or vulnerable: {computed_hash}"],
            "recommendation": "Verify the file's origin and check against known malware databases."
        }

    return {
        "status": "safe",
        "details": [f"File hash is valid: {computed_hash}"]
    }

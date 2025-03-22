import hashlib

def check_integrity(image_path):
    """Checks the file integrity using SHA256 hash"""
    hash_sha256 = hashlib.sha256()
    
    with open(image_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):  # Read in chunks
            hash_sha256.update(chunk)

    return f"{image_path} is intact. SHA256: {hash_sha256.hexdigest()}"

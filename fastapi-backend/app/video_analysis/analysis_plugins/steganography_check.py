import cv2
import numpy as np
from scipy.stats import entropy

def analyze(file_path):
    try:
        video = cv2.VideoCapture(file_path)
        entropy_values = []

        # Read first 10 frames for entropy analysis
        for _ in range(10):
            ret, frame = video.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hist = np.histogram(gray_frame, bins=256, range=(0, 256))[0]
            ent = entropy(hist, base=2)
            entropy_values.append(ent)

        avg_entropy = np.mean(entropy_values) if entropy_values else 0
        threshold = 7.5  # Empirical threshold for detecting hidden data

        if avg_entropy > threshold:
            return {
                "status": "suspicious",
                "details": ["High entropy detected, possible steganographic content."],
                "recommendation": "Use specialized tools for deep steganalysis."
            }

        return {
            "status": "safe",
            "details": ["No significant steganographic content detected."]
        }

    except Exception as e:
        return {
            "status": "error",
            "details": [str(e)],
            "recommendation": "Ensure file is a valid video."
        }


import librosa
import numpy as np

def analyze(file_path):
    try:
        # Load MP3 file with librosa
        y, sr = librosa.load(file_path, sr=None)

        # Compute spectral centroid (analyzes frequency balance)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        mean_centroid = np.mean(spectral_centroid)

        # Example: Flagging high spectral centroid values as suspicious
        if mean_centroid > 5000:  # Arbitrary threshold for abnormality
            return {
                "status": "suspicious",
                "details": [f"High spectral centroid detected: {mean_centroid:.2f} Hz"],
                "recommendation": "Analyze the MP3 file further for potential manipulation."
            }

        return {
            "status": "safe",
            "details": ["Spectral analysis found no anomalies."]
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure the MP3 file is not corrupted and check `librosa` installation."
        }

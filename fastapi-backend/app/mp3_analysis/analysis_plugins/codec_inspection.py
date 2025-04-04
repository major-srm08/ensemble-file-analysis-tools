import logging
import mutagen

def analyze(file_path):
    """Analyzes the audio codec of the given MP3 file."""
    try:
        audio = mutagen.File(file_path, easy=True)
        
        if not audio:
            return {
                "status": "error",
                "details": "File format not recognized as a valid MP3.",
                "recommendation": "Ensure the file is a valid MP3 and not corrupted."
            }

        codec = audio.mime[0] if hasattr(audio, "mime") else "Unknown"
        allowed_codecs = ["audio/mpeg", "audio/mp3"]

        if codec.lower() in allowed_codecs:
            return {
                "status": "safe",
                "details": [f"Detected codec: {codec}"]
            }
        else:
            return {
                "status": "suspicious",
                "details": [f"Unexpected codec detected: {codec}"],
                "recommendation": "Check for possible file format tampering."
            }

    except Exception as e:
        logging.error(f"Codec Inspection Error: {e}")
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure the MP3 file is accessible and check the mutagen library."
        }

import os
import logging
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def analyze(file_path):
    try:
        if not os.path.exists(file_path):
            return {"status": "error", "details": "File not found."}

        audio = MP3(file_path)
        metadata = {
            "file_name": os.path.basename(file_path),
            "duration": f"{audio.info.length:.2f} seconds",
            "bitrate": f"{audio.info.bitrate} bps",
            "sample_rate": f"{audio.info.sample_rate} Hz",
            "channels": "Stereo" if audio.info.channels == 2 else "Mono"
        }

        if audio.tags:
            tags = ID3(file_path)
            metadata["title"] = tags.get(TIT2, "Unknown Title")
            metadata["artist"] = tags.get(TPE1, "Unknown Artist")
            metadata["album"] = tags.get(TALB, "Unknown Album")

        logging.info(f"Metadata analysis completed for {file_path}")

        return {"status": "safe", "details": metadata}

    except Exception as e:
        logging.error(f"Metadata analysis failed: {e}")
        return {"status": "error", "details": str(e)}

if __name__ == "__main__":
    file_path = "input/sample.mp3"  # Change this to your MP3 file path
    result = analyze(file_path)
    print(result)

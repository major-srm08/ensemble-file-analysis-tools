import pymediainfo

def analyze(file_path):
    try:
        metadata = pymediainfo.MediaInfo.parse(file_path)
        abnormalities = []
        recommendation = ""

        for track in metadata.tracks:
            if track.track_type == "General":
                encoded_date = track.encoded_date

                if encoded_date:
                    if "1970-01-01 00:00:00 UTC" in encoded_date:
                        abnormalities.append("Encoded Date is a common default value: 1970-01-01 00:00:00 UTC.")
                    else:
                        abnormalities.append(f"Unusual Encoded Date: {encoded_date}. Verify if legitimate.")

        status = "safe" if not abnormalities else "inconclusive"
        return {
            "status": status,
            "details": abnormalities,
            "recommendation": recommendation if abnormalities else "No action needed."
        }

    except Exception as e:
        return {
            "status": "error",
            "details": [str(e)],
            "recommendation": "Check if file is valid."
        }


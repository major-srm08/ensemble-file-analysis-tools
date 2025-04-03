import exiftool
from datetime import datetime
import pytz

def extract_metadata(image_path):
    try:
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(image_path)

        # Initialize variables
        abnormalities = []
        local_tz = pytz.timezone("Asia/Kolkata")
        now_local = datetime.now(local_tz)  # Current time in local timezone

        # List of timestamp fields to validate
        timestamp_keys = [
            "Create Date", "Modify Date", "Date/Time Original", "File Modification Date/Time"
        ]

        # Ensure metadata is a list
        if not isinstance(metadata, list):
            raise ValueError("Metadata is not in the expected list format.")

        # Process metadata
        for item in metadata:
            if not isinstance(item, dict):
                continue  # Skip if not a dictionary

            for key, value in item.items():
                # Validate timestamp fields
                if key in timestamp_keys:
                    try:
                        mod_date = datetime.strptime(value, "%Y:%m:%d %H:%M:%S%z")
                        if mod_date > now_local:
                            abnormalities.append(
                                f"{key} indicates a future date: {value} (interpreted as {mod_date}). "
                                f"Current local time: {now_local}."
                            )
                    except (ValueError, TypeError):
                        abnormalities.append(
                            f"{key} has an invalid format or type: {value}. Expected 'YYYY:MM:DD HH:MM:SS+TZ'."
                        )

                # Check for missing critical metadata fields
                elif key in ["Make", "Model"] and not value:
                    abnormalities.append(f"Missing camera information: {key} is empty or missing.")
                elif key == "GPS Latitude" and not value:
                    abnormalities.append("GPS location data is missing.")

        # Check if EXIF data is completely missing
        if not metadata or all(not item for item in metadata):
            abnormalities.append("No EXIF metadata found in the image.")

        # Return analysis results
        if abnormalities:
            return {
                "status": "suspicious",
                "details": abnormalities,
                "recommendation": "Verify suspicious metadata entries manually."
            }
        else:
            return {
                "status": "safe",
                "details": ["No abnormalities detected in metadata."]
            }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure the file is valid and ExifTool is installed."
        }


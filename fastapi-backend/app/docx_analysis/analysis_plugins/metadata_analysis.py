import exiftool
from datetime import datetime
import pytz

def analyze(file_path):
    try:
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(file_path)

        # Initialize variables
        abnormalities = []
        local_tz = pytz.timezone("Asia/Kolkata")
        now_local = datetime.now(local_tz)  # Get current time in local timezone

        # List of timestamp fields to validate
        timestamp_keys = [
            "Create Date",
            "Modify Date",
            "File Modification Date/Time",
            "File Access Date/Time",
            "File Inode Change Date/Time",
            "Zip Modify Date",
        ]

        # Ensure metadata is a list
        if not isinstance(metadata, list):
            raise ValueError("Metadata is not in the expected list format.")

        # Process metadata
        for item in metadata:
            if not isinstance(item, dict):
                continue  # Skip if the item is not a dictionary
            
            for key, value in item.items():
                # Validate only known timestamp fields
                if key in timestamp_keys:
                    try:
                        # Parse the timestamp
                        mod_date = datetime.strptime(value, "%Y:%m:%d %H:%M:%S%z")

                        # Check for future dates
                        if mod_date > now_local:
                            abnormalities.append(
                                f"{key} indicates a future date: {value} (interpreted as {mod_date}). "
                                f"Current local time: {now_local}."
                            )
                    except (ValueError, TypeError):
                        abnormalities.append(
                            f"{key} has an invalid format or type: {value}. Expected format: 'YYYY:MM:DD HH:MM:SS+TZ'."
                        )

                # Handle other fields like "Total Edit Time"
                elif key == "Total Edit Time":
                    if not isinstance(value, str) or not value.endswith("minute"):
                        abnormalities.append(
                            f"{key} has an invalid format or type: {value}. Expected format: 'X minute(s)'."
                        )

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

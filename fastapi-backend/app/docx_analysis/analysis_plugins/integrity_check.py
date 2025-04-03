import zipfile

def analyze(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as docx_zip:
            corrupt = docx_zip.testzip()

        if corrupt:
            return {
                "status": "suspicious",
                "details": [f"Corrupt file detected: {corrupt}"],
                "recommendation": "Revalidate the file for corruption."
            }
        else:
            return {
                "status": "safe",
                "details": ["File integrity check passed."]
            }
    except zipfile.BadZipFile:
        return {
            "status": "error",
            "details": "File is not a valid ZIP container.",
            "recommendation": "Ensure the file is a valid .docx file."
        }
    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Unexpected error occurred during integrity check."
        }

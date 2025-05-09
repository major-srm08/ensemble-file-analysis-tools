import oletools.oleid as oleid

def analyze(file_path):
    try:
        ole = oleid.OleID(file_path)
        indicators = ole.check()

        suspicious_indicators = []

        for indicator in indicators:
            name = indicator.name
            value = indicator.value
            risk = indicator.risk
            description = indicator.description

            # Logic for suspicious indicators
            if (
                (name == "File format" and "docx" not in str(value).lower()) or
                (name == "Container format" and value != "OpenXML") or
                (name == "Encrypted" and value) or
                (name == "VBA Macros" and value != "No") or
                (name == "XLM Macros" and value != "No") or
                (name == "External Relationships" and int(value) > 0) or
                (name == "ObjectPool" and value) or
                (name == "Flash objects" and int(value) > 0)
            ):
                suspicious_indicators.append(f"{name}: {description} (Value: {value}, Risk: {risk})")

        if suspicious_indicators:
            return {
                "status": "suspicious",
                "details": suspicious_indicators,
                "recommendation": "Inspect OLE indicators for potential threats."
            }
        else:
            return {
                "status": "safe",
                "details": ["No suspicious OLE indicators detected."]
            }
    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure the file is valid and oletools is installed."
        }

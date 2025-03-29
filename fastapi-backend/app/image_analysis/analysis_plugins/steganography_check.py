import pexpect
import os

def detect_steganography(image_path):
    """Detects hidden data in an image using Steghide and saves the result."""
    output_dir = "output/"
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    output_file = os.path.join(output_dir, f"{os.path.basename(image_path)}_steganalysis.txt")

    try:
        # Start steghide and handle interaction
        child = pexpect.spawn(f"steghide info {image_path}", timeout=10)
        child.expect(["Try to get information about embedded data.*\\(y/n\\)", pexpect.EOF, pexpect.TIMEOUT])

        # Automatically respond with 'y' and send an empty passphrase
        child.sendline("y")
        child.expect(pexpect.EOF)
        output = child.before.decode("utf-8").strip()

        # Check if hidden data exists
        if "embedding" in output.lower():
            output_text = {"status": "suspicious", "details": [f"Possible hidden data found in the image"], "recommendation": "Inspect the image for any traces of Steganography"}
        else:
            output_text = {"status": "safe", "details": [f"No hidden data found in the image"]}

        return output_text

    except Exception as e:
        return f"Error processing {image_path}: {str(e)}"


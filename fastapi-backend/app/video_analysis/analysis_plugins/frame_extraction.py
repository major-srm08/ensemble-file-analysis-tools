import cv2
import os

def analyze(file_path, output_dir="output/frames"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        cap = cv2.VideoCapture(file_path)
        frame_count = 0
        extracted_frames = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % 50 == 0:  # Extract every 50th frame
                frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)
                extracted_frames.append(frame_path)
            frame_count += 1

        cap.release()

        return {
            "status": "safe",
            "details": [f"{len(extracted_frames)} keyframes extracted."],
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e),
            "recommendation": "Ensure OpenCV is installed and the file is valid."
        }

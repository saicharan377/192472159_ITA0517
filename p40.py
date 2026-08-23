import cv2
import pytesseract

def extract_text_from_video():

    video_path = "input.mp4"

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Process every 30th frame
        if frame_count % 30 == 0:

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            # Threshold
            _, thresh = cv2.threshold(
                gray,
                150,
                255,
                cv2.THRESH_BINARY
            )

            text = pytesseract.image_to_string(
                thresh
            )

            if text.strip():

                print(
                    f"Frame {frame_count}:"
                )

                print(text)

    cap.release()

extract_text_from_video()
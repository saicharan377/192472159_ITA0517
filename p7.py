import cv2

# Function to play video
def play_video(delay, title):

    # Open video
    cap = cv2.VideoCapture("video.mp4")

    # Check whether video is opened
    if not cap.isOpened():
        print("Error: Video not found!")
        return

    while True:

        # Read frame
        ret, frame = cap.read()

        # Stop when video ends
        if not ret:
            break

        # Display frame
        cv2.imshow(title, frame)

        # Press q to stop
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    # Release video
    cap.release()
    cv2.destroyAllWindows()


# Normal speed
print("Playing Normal Video")
play_video(30, "Normal Video")


# Slow motion
print("Playing Slow Motion Video")
play_video(100, "Slow Motion")


# Fast motion
print("Playing Fast Motion Video")
play_video(5, "Fast Motion")
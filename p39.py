import cv2

def reverse_slow_motion():

    input_video = "input.mp4"
    output_video = "reverse_slow.mp4"

    cap = cv2.VideoCapture(input_video)

    frames = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("Video not found.")
        return

    width = frames[0].shape[1]
    height = frames[0].shape[0]

    original_fps = 30

    # Reduce FPS for slow motion
    slow_fps = original_fps / 2

    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )

    out = cv2.VideoWriter(
        output_video,
        fourcc,
        slow_fps,
        (width, height)
    )

    for frame in reversed(frames):
        out.write(frame)

    out.release()

    print("Reverse slow-motion video created.")

reverse_slow_motion()
import cv2

input_video = "input.mp4"
output_video = "reverse.mp4"

cap = cv2.VideoCapture(input_video)

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

width = int(frames[0].shape[1])
height = int(frames[0].shape[0])
fps = 30

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

for frame in reversed(frames):
    out.write(frame)

out.release()

print("Reverse video created successfully.")
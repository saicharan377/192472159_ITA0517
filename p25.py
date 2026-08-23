import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

img = cv2.imread("sample.jpg")

results = model(img)

for result in results:
    boxes = result.boxes

    for box in boxes:
        cls = int(box.cls[0])
        confidence = float(box.conf[0])
        name = model.names[cls]

        if name == "watch":
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.putText(
                img,
                f"{name} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

cv2.imshow("Watch Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
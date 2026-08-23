import cv2

def count_faces():

    img = cv2.imread("input.jpg")

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for x, y, w, h in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    count = len(faces)

    cv2.putText(
        img,
        f"Number of Faces: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    print("Number of faces:", count)

    cv2.imshow("Face Count", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

count_faces()
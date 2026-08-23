import cv2
import numpy as np

def create_rectangle():

    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    img = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    x1 = width // 4
    y1 = height // 4

    x2 = 3 * width // 4
    y2 = 3 * height // 4

    cv2.rectangle(
        img,
        (x1, y1),
        (x2, y2),
        (0, 0, 255),
        3
    )

    cv2.imshow("Rectangle", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_rectangle()
import cv2
import numpy as np

def create_image():

    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    box_w = width // 10
    box_h = height // 10

    # Top-left - Black
    img[0:box_h, 0:box_w] = (0, 0, 0)

    # Top-right - Blue
    img[0:box_h, width-box_w:width] = (255, 0, 0)

    # Bottom-left - Green
    img[height-box_h:height, 0:box_w] = (0, 255, 0)

    # Bottom-right - Red
    img[
        height-box_h:height,
        width-box_w:width
    ] = (0, 0, 255)

    cv2.imshow("Four Colored Boxes", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image()
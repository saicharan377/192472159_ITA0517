import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
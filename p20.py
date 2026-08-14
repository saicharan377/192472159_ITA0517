import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert image to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to binary image
    _, binary = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    # Create morphological kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilation = cv2.dilate(
        binary,
        kernel,
        iterations=1
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Dilation", dilation)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
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

    # Convert to float32
    gray = np.float32(gray)

    # Harris Corner Detection
    corners = cv2.cornerHarris(
        gray,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    # Dilate corners to make them visible
    corners = cv2.dilate(corners, None)

    # Copy original image
    output = img.copy()

    # Mark detected corners in red
    output[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Harris Corner Detection", output)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
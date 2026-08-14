import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    height, width = img.shape[:2]

    # Four points from original image
    src = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1],
        [width - 1, height - 1]
    ])

    # Four destination points
    dst = np.float32([
        [50, 50],
        [width - 50, 20],
        [20, height - 50],
        [width - 20, height - 20]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(src, dst)

    # Apply perspective transformation
    perspective = cv2.warpPerspective(
        img,
        matrix,
        (width, height)
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", perspective)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
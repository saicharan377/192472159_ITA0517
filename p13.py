import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Select three points from original image
    src = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1]
    ])

    # Destination points
    dst = np.float32([
        [50, 50],
        [cols - 100, 30],
        [30, rows - 50]
    ])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(src, dst)

    # Apply affine transformation
    affine = cv2.warpAffine(
        img,
        matrix,
        (cols, rows)
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformation", affine)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
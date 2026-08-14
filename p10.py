import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Rotate 90 degrees clockwise
    rotated = cv2.rotate(
        img,
        cv2.ROTATE_90_CLOCKWISE
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("90 Degree Clockwise Rotation", rotated)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
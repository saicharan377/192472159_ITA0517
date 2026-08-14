import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Rotate image by 180 degrees
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("180 Degree Rotation", rotated)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
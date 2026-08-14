import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(img, (15, 15), 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur", blurred)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
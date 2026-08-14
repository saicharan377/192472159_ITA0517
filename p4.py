import cv2

# Read image in gray-scale
img = cv2.imread("sample.jpg", 0)

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply histogram equalization
    equalized = cv2.equalizeHist(img)

    # Display original and equalized images
    cv2.imshow("Original Gray-scale Image", img)
    cv2.imshow("Histogram Equalized Image", equalized)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
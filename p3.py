import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert image to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
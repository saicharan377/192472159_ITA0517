import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Increase image size
    bigger = cv2.resize(
        img,
        None,
        fx=1.5,
        fy=1.5,
        interpolation=cv2.INTER_CUBIC
    )

    # Decrease image size
    smaller = cv2.resize(
        img,
        None,
        fx=0.5,
        fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
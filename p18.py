import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Select Region of Interest (ROI)
    roi = img[100:300, 100:300]

    # Copy the ROI
    copied = roi.copy()

    # Paste the copied region at another location
    img[150:350, 450:650] = copied

    # Display the cropped region
    cv2.imshow("Cropped ROI", roi)

    # Display final image
    cv2.imshow("Copy and Paste Result", img)

    # Save result
    cv2.imwrite("roi_result.jpg", img)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
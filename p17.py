import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Copy original image
    watermarked = img.copy()

    # Watermark text
    text = "WATERMARK"

    # Position of watermark
    position = (50, 450)

    # Font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Add watermark
    cv2.putText(
        watermarked,
        text,
        position,
        font,
        1.5,
        (255, 255, 255),
        3,
        cv2.LINE_AA
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    # Save watermarked image
    cv2.imwrite("watermarked.jpg", watermarked)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
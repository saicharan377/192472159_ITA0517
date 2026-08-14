import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):

    # Read the image
    img = cv2.imread(image_path)

    # Check whether image is loaded
    if img is None:
        print("Error: Image not found!")
        return

    # Color channels in OpenCV are BGR
    colors = ("b", "g", "r")

    # Calculate histogram for each channel
    for i, color in enumerate(colors):

        hist = cv2.calcHist(
            [img],
            [i],
            None,
            [256],
            [0, 256]
        )

        # Plot histogram
        plt.plot(hist, color=color)

    # Add graph details
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])

    # Display histogram
    plt.show()

    # Display input image
    cv2.imshow("Input Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
analyze_histogram("sample.jpg")
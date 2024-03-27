import cv2
import numpy as np

def high_boost_sharpening(image, A):
    # Define the high-boost mask
    mask1 = np.array([[0, -1, 0],
                      [-1, A + 4, -1],
                      [0, -1, 0]])
    mask2 = np.array([[-1, -1, -1],
                      [-1, A + 8, -1],
                      [-1, -1, -1]])

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian filter using filter2D
    filtered_image1 = cv2.filter2D(gray_image, -1, mask1)
    filtered_image2 = cv2.filter2D(gray_image, -1, mask2)

    # Combine the filtered images
    sharpened_image = cv2.addWeighted(filtered_image1, 0.5, filtered_image2, 0.5, 0)

    return sharpened_image

# Load the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Adjust the parameter A to control the strength of sharpening
A = 2

# Perform high-boost sharpening
sharpened_image = high_boost_sharpening(image, A)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

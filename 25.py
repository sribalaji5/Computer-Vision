import cv2
import numpy as np

def gradient_sharpening(image):
    # Define the gradient kernels
    kernel1 = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    
    kernel2 = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the convolution with both kernels
    gradient1 = cv2.filter2D(gray_image, -1, kernel1)
    gradient2 = cv2.filter2D(gray_image, -1, kernel2)

    # Combine the gradient images to obtain the sharpened image
    sharpened_image = cv2.addWeighted(gradient1, 0.5, gradient2, 0.5, 0)

    return sharpened_image

# Load the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Perform gradient sharpening
sharpened_image = gradient_sharpening(image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

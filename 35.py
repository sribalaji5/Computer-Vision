import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform the closing operation
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Calculate the black hat
black_hat = cv2.subtract(closing, image)

# Display the original image and the black hat result
cv2.imshow('Original Image', image)
cv2.imshow('Black Hat', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

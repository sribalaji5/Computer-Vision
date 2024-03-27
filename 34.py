import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform the opening operation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Calculate the top hat
top_hat = cv2.subtract(image, opening)

# Display the original image and the top hat result
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the binary image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform dilation and erosion
dilated_image = cv2.dilate(image, kernel, iterations=1)
eroded_image = cv2.erode(image, kernel, iterations=1)

# Calculate the morphological gradient
morphological_gradient = cv2.subtract(dilated_image, eroded_image)

# Display the original image and the morphological gradient
cv2.imshow('Original Image', image)
cv2.imshow('Morphological Gradient', morphological_gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

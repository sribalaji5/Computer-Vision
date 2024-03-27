import cv2
import numpy as np

# Load the binary image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for dilation
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the original and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the binary image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for erosion
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

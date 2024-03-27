import cv2
import numpy as np

# Load the binary image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) for opening
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size and shape of the kernel

# Perform opening
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

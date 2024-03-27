import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Calculate the unsharp mask
unsharp_mask = cv2.subtract(gray_image, blurred_image)

# Add the unsharp mask to the original image
sharpened_image = cv2.addWeighted(gray_image, 1.5, unsharp_mask, -0.5, 0)

# Convert the image back to BGR (if needed)
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the gradient magnitude
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert gradient magnitude to uint8 for visualization
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

# Display the boundary of the image
cv2.imshow('Boundary Image', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()

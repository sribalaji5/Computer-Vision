import cv2

# Read the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection along the X and Y axes
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradient along X-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradient along Y-axis

# Compute the gradient magnitude
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert the result to uint8 (absolute value) and scale it to 0-255
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

# Display the original and gradient magnitude images
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()

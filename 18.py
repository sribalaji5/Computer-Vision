import cv2

# Read the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection along the Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # ksize = size of the Sobel kernel, can be 1, 3, 5, or 7

# Convert the result to uint8 (absolute value) and scale it to 0-255
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display the original and Sobel Y-edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()

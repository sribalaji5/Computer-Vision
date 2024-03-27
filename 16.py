import cv2

# Read the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise (optional)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, threshold1=30, threshold2=100)  # Adjust thresholds as needed

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Read the background image and the image to be moved
background = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")
foreground = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", -1)  # Use -1 flag to load image with alpha channel

# Define the coordinates where you want to place the foreground image on the background
x_offset = 100
y_offset = 100

# Get the shape of the foreground image
rows, cols, channels = foreground.shape

# Create a region of interest (ROI) for the area where you want to place the foreground image
roi = background[y_offset:y_offset+rows, x_offset:x_offset+cols]

# Extract the alpha channel from the foreground image
alpha = foreground[:, :, 1] / 255.0  # Normalize alpha channel values to the range [0, 1]

# Perform alpha blending to merge the foreground and background images
for c in range(0, 3):
    background[y_offset:y_offset+rows, x_offset:x_offset+cols, c] = \
        alpha * foreground[:, :, c] + (1 - alpha) * roi[:, :, c]

# Display the result
cv2.imshow('Result', background)
cv2.waitKey(0)
cv2.destroyAllWindows()

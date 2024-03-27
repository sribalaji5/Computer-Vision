import numpy as np
import cv2

# Define the Laplacian kernel
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Load the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg", cv2.IMREAD_GRAYSCALE)

# Pad the image to handle border pixels
padded_image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_REPLICATE)

# Convolve the image with the Laplacian kernel
convolved_image = cv2.filter2D(padded_image, -1, laplacian_kernel)

# Remove the padding from the convolved image
convolved_image = convolved_image[1:-1, 1:-1]

# Add the convolved image to the original image
sharpened_image = cv2.add(image, convolved_image)

# Clip values to ensure they're in the valid range [0, 255]
sharpened_image = np.clip(sharpened_image, 0, 255)

# Convert back to uint8
sharpened_image = sharpened_image.astype(np.uint8)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

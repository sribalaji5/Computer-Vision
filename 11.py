import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Define the transformation matrix
# For example, let's perform a translation of 50 pixels in both x and y directions
# The transformation matrix for translation is:
# [[1, 0, tx],
#  [0, 1, ty]]
tx = 50  # translation in x direction
ty = 50  # translation in y direction
transformation_matrix = np.float32([[1, 0, tx],
                                    [0, 1, ty]])

# Apply the affine transformation using warpAffine function
height, width = image.shape[:2]
transformed_image = cv2.warpAffine(image, transformation_matrix, (width, height))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

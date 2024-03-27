import numpy as np
import cv2

# Read images
image1 = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")
image2 = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Define corresponding points in both images
pts_image1 = np.array([[50, 50], [200, 50], [200, 200], [50, 200]], dtype=np.float32)
pts_image2 = np.array([[0, 0], [300, 0], [300, 300], [0, 300]], dtype=np.float32)

# Compute homography matrix using DLT
homography_matrix, _ = cv2.findHomography(pts_image1, pts_image2, cv2.RANSAC)

# Apply perspective transformation
transformed_image = cv2.warpPerspective(image1, homography_matrix, (image2.shape[1], image2.shape[0]))

# Display the original and transformed images
cv2.imshow('Original Image', image1)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

original_points = np.float32([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])

shift_amount = 100
shifted_points = np.float32([[0, 0], [image.shape[1] + shift_amount, 0], [image.shape[1], image.shape[0]], [shift_amount, image.shape[0]]])

perspective_matrix = cv2.getPerspectiveTransform(original_points, shifted_points)

height, width = image.shape[:2]
transformed_image = cv2.warpPerspective(image, perspective_matrix, (width + shift_amount, height))

cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)


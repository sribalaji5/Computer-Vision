import cv2
import numpy as np

image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

height, width = image.shape[:2]

angle_clockwise = -30  
angle_counterclockwise = 30 

rotation_matrix_clockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_clockwise, 1)
rotation_matrix_counterclockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_counterclockwise, 1)

rotated_image_clockwise = cv2.warpAffine(image, rotation_matrix_clockwise, (width, height))
rotated_image_counterclockwise = cv2.warpAffine(image, rotation_matrix_counterclockwise, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Clockwise Rotated Image', rotated_image_clockwise)
cv2.imshow('Counterclockwise Rotated Image', rotated_image_counterclockwise)


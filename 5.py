import cv2
import numpy as np

image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")

kernel = np.ones((5,5), np.uint8)  

eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)


import cv2
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)


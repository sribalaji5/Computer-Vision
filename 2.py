import cv2
image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)


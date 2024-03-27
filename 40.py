import cv2

# Load the image
image = cv2.imread(r"C:\Users\sanja\OneDrive\Pictures\kakashi.jpg")  # Replace 'image.jpg' with the path to your image

# Define coordinates for the rectangular shape (x, y, width, height)
x, y, width, height = 100, 100, 200, 150

# Draw a rectangle around the object
cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Extract the object using slicing
extracted_object = image[y:y+height, x:x+width]

# Display the original image with the rectangle and the extracted object
cv2.imshow('Original Image with Rectangle', image)
cv2.imshow('Extracted Object', extracted_object)
cv2.waitKey(0)
cv2.destroyAllWindows()

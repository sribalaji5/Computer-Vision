import cv2

# Load the images
image1 = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")
image2 = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Define the coordinates of the region to be cropped from image1 (format: top-left (x1, y1), bottom-right (x2, y2))
x1, y1, x2, y2 = 100, 100, 300, 300

# Crop the region of interest (ROI) from image1
cropped_roi = image1[y1:y2, x1:x2]

# Get the dimensions of the cropped ROI
roi_height, roi_width, _ = cropped_roi.shape

# Define the coordinates where the cropped ROI will be pasted onto image2
paste_x, paste_y = 50, 50

# Ensure the paste area doesn't exceed the dimensions of image2
paste_area = image2[paste_y:paste_y + roi_height, paste_x:paste_x + roi_width]

# Perform copying and pasting
paste_area[:] = cropped_roi

# Display the result
cv2.imshow('Result', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the original image and the watermark image
original_image = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\anime.jpg")
watermark = cv2.imread(r"C:\Users\M.HARISH\Desktop\opencv\kakashi.jpg")

# Get the dimensions of the watermark image
watermark_height, watermark_width, _ = watermark.shape

# Define the position where you want to place the watermark (top-left corner)
position_x = 50
position_y = 50

# Overlay the watermark onto the original image
for y in range(watermark_height):
    for x in range(watermark_width):
        alpha = 0.5  # Adjust the opacity of the watermark
        original_image[position_y + y, position_x + x] = alpha * watermark[y, x] + (1 - alpha) * original_image[position_y + y, position_x + x]

# Display the watermarked image
cv2.imshow('Watermarked Image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

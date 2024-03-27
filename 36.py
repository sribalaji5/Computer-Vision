import cv2
import numpy as np

# Load the model
config_path = "coco.data"
model_path = "yolov3-spp.weights"
model = cv2.dnn.readNetFromDarknet(config_path, model_path)

# Load the class labels
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load the image
img = cv2.imread("watch.jpg")

# Get the height and width of the image
height, width, _ = img.shape

# Create a blob from the image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), (0, 0, 0), swapRB=True, crop=False)

# Set the blob as input to the model
model.setInput(blob)

# Get the output from the model
output = model.forward(model.getUnconnectedOutLayersNames())

# Initialize the list of detected watches
watches = []

# Loop over the results
for detection in output[0]:
    scores = detection[5:]
    class_id = np.argmax(scores)

    if classes[class_id] == "watch":
        confidence = scores[np.argmax(scores)]

        if confidence > 0.5:
            box = detection[:4] * [width, height, width, height]
            (centerX, centerY, width, height) = box.astype("int")

            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))

            watches.append((x, y, int(width * 1.25), int(height * 1.25)))

# Draw the bounding boxes around the detected watches
for watch in watches:
    (x, y, w, h) = watch
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Image", img)

# Wait for a key press
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()

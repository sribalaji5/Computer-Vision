import cv2
import numpy as np

# Read the input video
video_capture = cv2.VideoCapture(r"C:\Users\M.HARISH\Desktop\opencv\car_drift_racing (720p).mp4")

# Get the frame width and height
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the four corners of the original image
original_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

# Define the four corners of the desired perspective
# For demonstration, let's shift the top-right and bottom-right corners to the right
shift_amount = 100
shifted_points = np.float32([[0, 0], [width + shift_amount, 0], [width, height], [shift_amount, height]])

# Compute the perspective transformation matrix (homography matrix)
perspective_matrix = cv2.getPerspectiveTransform(original_points, shifted_points)

# Create VideoWriter object to write the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, 30, (width + shift_amount, height))

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Apply the perspective transformation
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (width + shift_amount, height))

    # Write the transformed frame to the output video
    output_video.write(transformed_frame)

    # Display the frame
    cv2.imshow('Transformed Frame', transformed_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
output_video.release()
cv2.destroyAllWindows()

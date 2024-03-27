import cv2

# Initialize the webcam
video_capture = cv2.VideoCapture(0)  # 0 for default webcam, change if you have multiple webcams

# Set the frame size (optional)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Get the frame rate of the video
fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object to write the output video for slow motion
output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_slow = cv2.VideoWriter('output_video_slow.mp4', fourcc, fps / 2, (output_width, output_height))  # Adjusted FPS for slow motion

# Create a VideoWriter object to write the output video for fast motion
output_video_fast = cv2.VideoWriter('output_video_fast.mp4', fourcc, fps * 2, (output_width, output_height))  # Adjusted FPS for fast motion

# Read and process each frame
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Apply slow motion
    output_video_slow.write(frame)
    output_video_slow.write(frame)

    # Apply fast motion
    output_video_fast.write(frame)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
output_video_slow.release()
output_video_fast.release()
cv2.destroyAllWindows()

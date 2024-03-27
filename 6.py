import cv2
video_capture = cv2.VideoCapture(r"C:\Users\M.HARISH\Desktop\opencv\car_drift_racing (720p).mp4")

fps = int(video_capture.get(cv2.CAP_PROP_FPS))

output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video_slow.mp4', fourcc, fps/2, (output_width, output_height)) # Adjusted FPS for slow motion
output_video = cv2.VideoWriter('output_video_fast.mp4', fourcc, fps*2, (output_width, output_height)) # Adjusted FPS for fast motion


# Read and process each frame
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Write the same frame twice for slow motion
    output_video.write(frame)
    output_video.write(frame)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
output_video.release()
cv2.destroyAllWindows()

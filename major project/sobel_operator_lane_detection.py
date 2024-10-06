import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture("test_video.mp4")

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        break  # If frame not captured, break the loop

    # Define region of interest (ROI) for the road
    roi_vertices = np.array([[(0, 720), (1280, 720), (800, 500), (500, 500)]], dtype=np.int32)
    mask = np.zeros_like(frame)
    cv2.fillPoly(mask, roi_vertices, (255, 255, 255))
    masked_frame = cv2.bitwise_and(frame, mask)

    # Preprocess the ROI frame to detect lanes using Sobel operator
    gray = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Sobel operator for gradient in x-direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Sobel operator for gradient in y-direction
    edges = np.sqrt(sobel_x**2 + sobel_y**2)  # Magnitude of gradients
    edges = np.uint8(edges)  # Convert to uint8
    edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)[1]  # Thresholding

    # Detect lines using Hough transform
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=50)

    # Draw detected lines on a blank image
    line_img = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1)
            if abs(slope) > 0.5:  # Accept only lines with a slope greater than 0.5
                cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 10)

    # Overlay detected lines on the original frame
    result = cv2.addWeighted(frame, 0.8, line_img, 1.0, 0.0)

    # Display the result
    cv2.imshow('Result', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('image.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(
    gray, 
    cv2.HOUGH_GRADIENT, dp=1, minDist=30,
    param1=50, param2=30, minRadius=10, maxRadius=100
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)

# Detect ellipses using contours
contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if len(contour) >= 5:  # Minimum points required to fit an ellipse
        ellipse = cv2.fitEllipse(contour)
        cv2.ellipse(image, ellipse, (0, 0, 255), 2)

# Display the result
cv2.imshow('Detected Circles and Ellipses', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

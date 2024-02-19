import cv2
import numpy as np
image1=cv2.imread("line2.jpg")

black_image=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

# cv2.imshow("black_image",black_image)

threshold = 120

# Creating  a binary mask with dark parts as white
mask = cv2.threshold(black_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Visualizing the mask
cv2.imwrite("Dark_Part_Mask.jpg", mask)

image = cv2.imread("Dark_Part_Mask.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying edge detection
edges = cv2.Canny(gray_image, 50, 150)

# Detect lines using Hough Transform
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100,
                         minLineLength=50, maxLineGap=10)

# Draw lines on the image (optional)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display or save the image (optional)
cv2.imshow("Image with Detected Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Morphological operations based on OpenCV using Dilation technique.
import cv2
import numpy as np
img = cv2.imread("1.jpg")
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)

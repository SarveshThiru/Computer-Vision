#Opening Operation
import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Input Image', img)
cv2.imshow('Opened Image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

#boundary of the image using Convolution kernel 
import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
mag = cv2.magnitude(dx, dy)
thresh = 50
mag[mag < thresh] = 0
mag[mag >= thresh] = 255
cv2.imwrite('boundary.jpg', mag)

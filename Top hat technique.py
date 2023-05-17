#Top Hat Technique
import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Output', top_hat)
cv2.waitKey(0)

#Morphological Gradient
import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Output', morph_gradient)
cv2.waitKey(0)

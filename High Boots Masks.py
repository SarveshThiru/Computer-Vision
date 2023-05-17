# Perform Sharpening of Image using High-Boost Masks
import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian_filter = cv2.Laplacian(gray, cv2.CV_64F)
laplacian_image = cv2.convertScaleAbs(laplacian_filter)
factor = 2.0
highboost_mask = gray.astype(float) * factor - laplacian_image
sharpened = cv2.convertScaleAbs(highboost_mask)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

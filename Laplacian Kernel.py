# Sharpening of Image using Laplacian mask with positive center coefficient
import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a = 1.5
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, a, -1],
    [0, -1, 0]
])
laplacian = cv2.filter2D(gray, -1, laplacian_kernel)
sharpened = cv2.add(gray, laplacian)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

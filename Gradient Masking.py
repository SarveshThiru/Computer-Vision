#Sharpening of Image using Gradient masking
import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
gradient_x = cv2.convertScaleAbs(sobel_x)
gradient_y = cv2.convertScaleAbs(sobel_y)
total_gradient = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)
inverted_gradient = cv2.bitwise_not(total_gradient)
sharpened = cv2.addWeighted(gray, 1, inverted_gradient, 1, 0)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Sharpening of Image using unsharp masking.
import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0, 0), 3)
highpass = cv2.subtract(gray, blur)
factor = 1.5
sharpened = cv2.addWeighted(gray, 1 + factor, highpass, -factor, 0)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

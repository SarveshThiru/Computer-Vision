#Morphological Erosion technique
import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = (5, 5)
kernel = np.ones(kernel_size, dtype=np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imwrite('eroded_image.jpg', eroded)

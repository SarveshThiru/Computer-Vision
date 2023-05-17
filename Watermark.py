#Insert water marking to the image
import cv2
import numpy as np

img = cv2.imread('1.jpg')
watermark = cv2.imread('watermark.png')
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))
watermarked = cv2.addWeighted(img, 1, watermark, 0.5, 0)
cv2.imwrite('watermarked_image.jpg', watermarked)

import cv2
import numpy as np

img = cv2.imread('LanPixelized.jpg')
cv2.imshow('img',img) #Showing original image
cv2.waitKey(0)

height, width = img.shape[:2]
res = cv2.resize(img,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('img',res) # Showing scaled image (3x times)
cv2.waitKey(0)

img = cv2.imread('LanPixelized.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst) # Showing displaced image
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst) # Showing rotated image
cv2.waitKey(0)

cv2.destroyAllWindows()
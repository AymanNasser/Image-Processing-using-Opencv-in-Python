import cv2 as cv
import numpy as np

# Thresholding ==> segmentation technique used to separate an object from
# cv.threshold(img, threshold value, max threshold value, threshold type),  returns ret & threshold value
# cv.THRESH_BINARY ==> any pixel value below threshold value is assigned to 0
# while any pixel above threshold value is assigned to 255 & cv.THRESH_BINARY_INV is the inverse of cv.THRESH_BINARY

# cv.THRESH_TRUNC ==> any pixel value below threshold will remain unchanged, but any value above the threshold
# will get the value of threshold value

# cv.THRESH_TOZERO ==>any pixel value below threshold will be zeroed, but any value above the threshold
# # will remain unchanged & cv.THRESH_TOZERO_INV is the inverse 

img = cv.imread('1.jpg', 1)
x, th1 = cv.threshold(img,50,255,cv.THRESH_BINARY)
x, th2 = cv.threshold(img,230,255,cv.THRESH_TOZERO)


cv.imshow('image',img)
cv.imshow('threshold',th1)
cv.imshow('threshold2',th2)

cv.waitKey(0)
cv.destroyAllWindows()
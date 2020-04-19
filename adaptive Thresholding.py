import cv2 as cv


import numpy as np


# Adaptive threshold ==> threshold is calculated for specific regions, not globally to all pixels
# cv.adaptiveThreshold(img, max value assigned to pixels which condition will be satisfied, adaptive method,
# threshold type, block size ==> size of neighbour hood area, C value (const value will be subtracted from
# adpative method)
# adaptive_method ==> 1- cv.ADAPTIVE_THRESH_MEAN_C, 2- cv.ADAPTIVE_THRESH_GAUSSIAN_C
img = cv.imread('1.jpg', 0)
x, th1 = cv.threshold(img,200,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('image',img)
cv.imshow('threshold3',th3)
cv.imshow('threshold2',th2)

cv.waitKey(0)
cv.destroyAllWindows()
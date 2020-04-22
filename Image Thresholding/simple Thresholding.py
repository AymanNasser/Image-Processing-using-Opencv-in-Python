import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Thresholding ==> segmentation technique used to separate an objects from images, we use one global value as a threshold
# If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value
# cv.threshold(img, threshold value, max threshold value, threshold type),  returns ret & threshold value
# Types of simple thresholding: cv.THRESH_BINARY, cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO, cv.THRESH_TOZERO_INV

# cv.THRESH_BINARY ==> any pixel value below threshold value is assigned to 0
# while any pixel above threshold value is assigned to 255 & cv.THRESH_BINARY_INV is the inverse of cv.THRESH_BINARY

# cv.THRESH_TRUNC ==> any pixel value below threshold will remain unchanged, but any value above the threshold
# will get the value of threshold value

# cv.THRESH_TOZERO ==>any pixel value below threshold will be zeroed, but any value above the threshold
# # will remain unchanged & cv.THRESH_TOZERO_INV is the inverse 

img = cv.imread('gradient.png', 1)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
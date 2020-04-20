import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Adaptive threshold ==> threshold is calculated for specific regions, not globally to all pixels, the algorithm determines the threshold for a pixel based on a small region around it.
# cv.adaptiveThreshold(img, max value assigned to pixels which condition will be satisfied, adaptive method,
# threshold type, block size ==> size of neighbour hood area, C value (const value will be subtracted from
# adpative method)

# adaptive_method ==> 1- cv.ADAPTIVE_THRESH_MEAN_C, 2- cv.ADAPTIVE_THRESH_GAUSSIAN_C
# cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

# Otsu's Binarization ==> Otsu's method avoids having to choose a value and determines it automatically.

# BlockSize: Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on
# The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.


img = cv.imread('sudoku 001.jpg', cv.IMREAD_GRAYSCALE)
ret1, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
ret2, th4 = cv.threshold(img,0,255,cv.THRESH_BINARY, cv.THRESH_OTSU)


titles = ['Original Image', 'Global Thresholding (v = 127)','Adaptive Mean Thresholding',
          'Adaptive Gaussian Thresholding', 'Otsus Bin']
images = [img, th1, th2, th3,th4]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

print(ret1,',' ,ret2)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
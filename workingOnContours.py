import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.
# The contours are a useful tool for shape analysis and object detection and recognition.

# In OpenCV, finding contours is like finding white object from black background. So , object to be found should be white and background should be black.
# cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs the contours and hierarchy.
# Retrieval mode ==> 1-RETR_EXTERNAL: retrieves only the extreme outer contours
#                    2-RETR_LIST: retrieves all of the contours without establishing any hierarchical relationships.
#                    3-RETR_CCOMP: retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components.
#                    At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
#                    4-RETR_TREE: retrieves all of the contours and reconstructs a full hierarchy of nested contours.

# Approximation method ==> 1-CHAIN_APPROX_NONE: stores absolutely all the contour points. That is, any 2 subsequent points (x1,y1) and (x2,y2)
#                          of the contour will be either horizontal, vertical or diagonal neighbors
#                          2-CHAIN_APPROX_SIMPLE: compresses horizontal, vertical, and diagonal segments and leaves only their end points.
#                          for example, an up-right rectangular contour is encoded with 4 points.
#                          3-CHAIN_APPROX_TC89_L1, 4-CHAIN_APPROX_TC89_KCOS

# cv.drawContours( Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours
# (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness)

img = cv.imread('data/opencv-logo.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Simple thresholding
ret,thresh = cv.threshold(imgGray,200,255,cv.THRESH_BINARY)

# Contours is a python list of all contours in the image, each contour is a numpy array of (x,y) coordinates of boundary points of the object
# Hierarchy is optional output vector containing information about the image topology. It has as many elements as the number of contours.

contours, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(img, contours, -1, (127,127,127), 3)
cv.imshow('image',img)

rows = 1
columns = 3


cv.waitKey(0)
cv.destroyAllWindows()



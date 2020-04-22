import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Contour Approximation ==> It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify.
#

img = cv.imread('data/shapes.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(imgGray,220,255, cv.THRESH_BINARY)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cont in contours:
    # cv.arcLength() calculates a contour perimeter or a curve length in pixels, The function computes a curve length or a closed contour perimeter.
    # closed: Flag indicating whether the curve is closed or not.

    # ** Don't know why we multiply by a very small value (0.01) **
    epsilon = 0.01*cv.arcLength(cont, True)

    # cv.approxPolyDP approximates a curve or a polygon with another curve/polygon with less vertices so that the distance between them is less or equal to the specified precision
    # epsilon: Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation
    # close: If true, the approximated curve is closed (its first and last vertices are connected). Otherwise, it is not closed.
    approx = cv.approxPolyDP(cont, epsilon, True)

    cv.drawContours(img, [approx], 0, (255,0,0), 3)
    # ravel ==> returns contiguous flattened array(1D array with all the input-array elements and with the same type as it)
    x = approx.ravel()[0]
    y = approx.ravel()[1] -5
    print(len(approx))
    if len(approx) == 3:
        cv.putText(img, "TRIANGLE", (x,y), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))
    elif len(approx) == 4:
        x1,y1,w,h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "SQUARE", (x, y), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
        else:
            cv.putText(img, "RECTANGLE", (x, y), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, "PENTAGON", (x, y), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
    else:
        cv.putText(img, "UNKNOWN", (x, y), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))


cv.imshow('IMAGE',img)

cv.waitKey(0)
cv.destroyAllWindows()



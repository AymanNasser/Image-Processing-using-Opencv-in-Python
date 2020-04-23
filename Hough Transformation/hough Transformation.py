import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Hough Transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form.
# It can detect the shape even if it is broken or distorted a little bit.
# Hough Transformation Algorithm ==> 1- Edge Detection (Canny, Thresholding, etc)
#                                    2- Mapping of edge points to the hough space & storage in an accumulator
#                                    3- Interpretation of the accumulator to yield lines of infinite length using thresholding
#                                    4- Conversion of infinite lines to finite ones

# cv.HoughLines(image, rho accuracy, theta accuracy, threshold, srn, stn, min_theta, max_theta) ==> Finds lines in a binary image using the standard Hough transform.
# cv.HoughLines simply returns an array of (rho, theta) values. ρ(rho) is measured in pixels and θ(theta) is measured in radians
# 1- Image: 8-bit, single-channel binary source image (edge detected result).
# 2- Rho: distance resolution of the accumulator in pixels.
# 3- Theta: angle resolution of the accumulator in radians.
# 4- Threshold: Accumulator threshold parameter. Only those lines are returned that get enough **votes** ( > threshold ).
#    number of votes depends upon the number of points on the line. So it represents the minimum length of line that should be detected.

# Standard Hough Line Transform Method
img = cv.imread('data/sudoku.png')
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(img, 50, 150, apertureSize=3)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)

# ρ = xCos(θ) + ySin(θ)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    # Origin or top-left corner
    x0 = a*rho
    y0 = b*rho
    # Standard formulas for achieving edge points
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv.imshow('Canny', edges)
cv.imshow('WINDOW', img)

cv.waitKey(0)
cv.destroyAllWindows()



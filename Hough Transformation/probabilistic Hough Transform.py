import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Probabilistic Hough Transform is an optimization of the stand Hough Transform, it doesn't take all the points into consideration.
# Instead, it takes only a random subset of points which is sufficient for line detection. We just have to decrease the threshold.

# minLineLength ==> Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap ==> Maximum allowed gap between line segments to treat them as a single line.

# Probabilistic Hough Line Transform Method
img = cv.imread('data/sudoku.png')
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(img, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# ρ = xCos(θ) + ySin(θ)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)


cv.imshow('Canny', edges)
cv.imshow('WINDOW', img)

cv.waitKey(0)
cv.destroyAllWindows()



import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# An image gradient (High-pass filters) is a directional change in the intensity or the color in an image
# 1-Sobel and Scharr Derivatives ==> is more resistant to noise. You can specify the direction of derivatives to be taken,
# vertical or horizontal (by the arguments, yorder and xorder respectively), If ksize = -1, a 3x3 Scharr filter

# 2-Laplacian Derivatives

img = cv.imread('sudoku 001.jpg', cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize= 3)
# We take the absolute of the resulted lap ==> when you convert data to np.uint8, all negative slopes are made zero. In simple words, you miss that edge.
lap = np.uint8(np.absolute(lap))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0 )
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1 )
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX,sobelY)

titles = ['Original', 'Laplacian', 'Sobel-X', 'Sobel-Y', 'Combined']
images = [img,lap,sobelX,sobelY,sobelCombined]

rows = 2
columns = 3
iterations = len(images)
for ite in range(iterations):
    plt.subplot(rows,columns, ite+1 ), plt.imshow(images[ite])
    plt.title(titles[ite])



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

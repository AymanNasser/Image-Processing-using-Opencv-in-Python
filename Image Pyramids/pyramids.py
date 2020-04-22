import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Set of images with different resolutions are called Image Pyramids (because when they are kept in a stack with
# the highest resolution image at the bottom and the lowest resolution image at top, it looks like a pyramid).
# There are two kinds of Image Pyramids. 1) Gaussian Pyramid, 2) Laplacian Pyramids

# 1-Gaussian Pyramid ==> Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns in Lower level (higher resolution) image.
# Then each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian weights. By doing so, a M×N image becomes M/2×N/2 image

# 2-Laplacian Pyramids are formed from the Gaussian Pyramids, # A level in Laplacian pyramid is formed by the difference
# between that level in gaussian pyramid & expanded version of its upper level in gaussian pyramid. Laplacian pyramid images are like edge images only.
# Most of its elements are zeros. They are used in image compression

# Once we decrease the resolution of an image using pyrdown ==> we lose information of this image


img = cv.imread('data/lena.jpg',1)
imgCopy = img.copy()

gausPyr = [imgCopy]
laplac = []
titles= []
images= []


for ite in range(5):
    imgCopy = cv.pyrDown(imgCopy)
    gausPyr.append(imgCopy)
    titles.append('Gaussian' + str(ite))
    images.append(gausPyr[ite])
    #print(ite)
laplac.append(gausPyr[5])

for itr in range(4,-1,-1):
    #print(itr)
    gausExten = cv.pyrUp(gausPyr[itr])
    # Not working
    temp = cv.subtract(gausPyr[itr-1], gausExten)

rows = 2
columns = 5
iterations = len(images)
for ite in range(iterations):
    plt.subplot(rows,columns, ite+1 ), plt.imshow(images[ite])
    plt.title(titles[ite])



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()



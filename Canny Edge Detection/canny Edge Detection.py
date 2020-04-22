import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Canny Edge Detection is a popular edge detection algorithm

# It is a multi-stage algorithm and we will go through each stages
# 1-Noise Reduction
# 2-Finding Intensity Gradient of the Image
# 3-Non-maximum Suppression
# 4-Hysteresis Thresholding
# 5-Edge Tracking by hystresis

# cv.Canny(src, first threshold for the hysteresis procedure, second threshold for the hysteresis procedure)

img = cv.imread('messi5.jpg',cv.IMREAD_GRAYSCALE)

edges = cv.Canny(img,100,200)

titles = ['Original', 'Canny']
images = [img,edges]

rows = 1
columns = 3
iterations = len(images)
for ite in range(iterations):
    plt.subplot(rows,columns, ite+1 ), plt.imshow(images[ite])
    plt.title(titles[ite])



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()



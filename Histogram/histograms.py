import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Histogram ==>  can be considered histogram as a graph or plot, which gives you an overall idea about the intensity distribution of an image.
# It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis.
# By looking at the histogram of an image, we get intuition about contrast, brightness, intensity distribution etc of that image

# BINS: histogram shows the number of pixels for every pixel value, ie from 0 to 255. ie you need 256 values to show the above histogram. But consider,
# what if you need not find the number of pixels for all pixel values separately, but number of pixels in a interval of pixel values? say for example, you need to find
# the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram.
# So what we do is simply split the whole histogram to 16 sub-parts and value of each sub-part is the sum of all pixel count in it. This each sub-part is called "BIN". In first case,
# number of bins were 256 (one for each pixel) while in second case, it is only 16. BINS is represented by the term histSize in OpenCV docs.

# DIMS : It is the number of parameters for which we collect the data. we regularly collect data regarding only one thing, intensity value. So here it is 1.
# RANGE : It is the range of intensity values we want to measure. Normally, it is [0,256], ie all intensity values.

# 1. Histogram Calculation in OpenCV ==> cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# 1.1 images: it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
# 1.2 channels: it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0].
# For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
# 1.3 mask: to find histogram of full image, it is given as "None". But if we want to find histogram of particular region of image,
# we have to create a mask image for that and give it as mask.
# 1.4 histSize: this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
# 1.5 ranges: this is our RANGE. Normally, it is [0,256].



#EX1:
#img = np.zeros((200,200), np.uint8)
#cv.rectangle(img, (0,100), (200,200), (255,255,255), -1)
#plt.hist(img.ravel(), 256 , [0,256])

#EX2:
#img = cv.imread('data/lena.jpg', 1)
#b, g ,r = cv.split(img)

#plt.hist(b.ravel(), 256, [0,256])
#plt.hist(g.ravel(), 256, [0,256])
#plt.hist(r.ravel(), 256, [0,256])

#EX3:
#img = cv.imread('data/lena.jpg', 0)
#histogram = cv.calcHist([img], [0], None, [256], [0,256] )
#plt.plot(histogram)

#EX4:
img = cv.imread('data/lena.jpg', cv.IMREAD_GRAYSCALE)
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
cv.imshow('WINDOWS', masked_img)
histogram = cv.calcHist([img], [0], masked_img, [16], [0,256])
plt.plot(histogram)


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()



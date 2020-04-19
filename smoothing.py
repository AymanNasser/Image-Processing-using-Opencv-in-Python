import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
# kernel, convolution matrix, or mask is a small matrix. It is used for blurring, sharpening,
# embossing, edge detection, and more. This is accomplished by doing a convolution between a kernel and an image.

# As in one-dimensional signals, images also can be filtered with various low-pass filters (LPF),
# high-pass filters (HPF), etc. LPF helps in removing noise, blurring images, etc. HPF filters help
# in finding edges in images.

# Homogeneous filters ==> each pixel is the mean of its kernel neighbours

# Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful
# for removing noise. It actually removes high frequency content (eg: noise, edges) from the image.
# So edges are blurred a little bit in this operation

# 1-Averaging ==> This is done by convolving an image with a normalized box filter.
# It simply takes the average of all the pixels under the kernel area and replaces the central element

# 2-Gaussian filter ==> using diff-weighted-pixels, for sides weights are low weighted while
# for center is high weighted

# 3-Median Blurring ==> median of all the pixels under the kernel area and the central element is
# replaced with this median value, This is highly effective against salt-and-pepper noise in an image.
# the central element is always replaced by some pixel value in the image. It reduces the noise effectively.
# Its kernel size should be a positive odd integer.

# 4-Bilateral Filtering ==> highly effective in noise removal while keeping edges sharp,
# But the operation is slower compared to other filters, Bilateral filtering also takes a Gaussian filter
# in space, but one more Gaussian filter which is a function of pixel difference.


img = cv.imread('opencv-logo.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25


dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img, (2,2))
gausBlur = cv.GaussianBlur(img, (5,5),0)
mediBlur = cv.medianBlur(img, 5)
bf = cv.bilateralFilter(img, 5, 75,75)

#blur = cv.boxFilter(img,2 ,(2,2))

titles = ['Original', '2D Convolution', 'Blur', 'GaussianBlur', 'MedianBlur', 'Bilateral']
images = [img,dst,blur,gausBlur,mediBlur, bf]

rows = 2
columns = 3
iterations = len(images)
for ite in range(iterations):
    plt.subplot(rows,columns, ite+1 ), plt.imshow(images[ite])
    plt.title(titles[ite])


plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
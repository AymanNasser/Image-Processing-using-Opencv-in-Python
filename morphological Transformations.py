import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Morphological transforamtions are performed on binary images,
# cv.dilate(img, kernel ==> defined shape,
# It needs two inputs, one is our original image, second one is called structuring element or kernel
# which decides the nature of operation.
# Two basic morphological operators are Erosion and Dilation.

# 1-Erosion ==> it erodes away the boundaries of foreground object, A pixel in the original image (either 1 or 0)
# will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# all the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size
# of the foreground object decreases or simply white region decreases in the image

# 2-Dilation ==> It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel
# is '1'. So it increases the white region in the image or size of foreground object increases.
# Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes
# white noises, but it also shrinks our object. So we dilate it

# 3-Opening ==> Opening is just another name of erosion followed by dilation. It is useful in removing noise
# 4-Closing ==> Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small
# holes inside the foreground objects, or small black points on the object.
# 5-Morphological Gradient, It is the difference between dilation and erosion of an image
# the result will look like the outline of the object.
# 6-Top Hat, 7-Open Hat

img = cv.imread('1.jpg', cv.IMREAD_GRAYSCALE)

_, th1 = cv.threshold(img,180,255,cv.THRESH_BINARY_INV)
# Generating a white rectangle of l=5, w=5 as a kernel
kernel = np.ones((2,2),np.uint8)

ero = cv.erode(th1, kernel, iterations=1)
dil = cv.dilate(th1, kernel, iterations=1)
ope = cv.morphologyEx(th1, cv.MORPH_OPEN, kernel)
clo = cv.morphologyEx(th1, cv.MORPH_CLOSE, kernel)

titles = ['images', 'mask', 'dilation', 'eroded', 'open', 'close']
images = [img, th1, dil, ero, ope, clo]
# range(no.) ==> no. represents number of iterations
for i in range(6):
    plt.subplot(3,2,i+1) , plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Image Blending
# 1-Load the two images
# 2-Find the Gaussian Pyramids for them (in this particular example, number of levels is 6)
# 3-From Gaussian Pyramids, find their Laplacian Pyramids
# 4-Now join the left half and right half in each levels of Laplacian Pyramids
# 5-Finally from this joint image pyramids, reconstruct the original image.

# 1-Loading images
apple = cv.imread('data/apple.jpg')
orange = cv.imread('data/orange.jpg')
# half stack methods cuts images and stack them together
# cutting left half of the apple and stacking it to the right half of the orange

#apple_orange = np.hstack((apple[: , :256], orange[:, 256:]))

# 2.1-Generating gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

apple_copy = gp_apple[5]
lapApple = [apple_copy]
# 3.1-Generating laplacian pyramid for apple
for i in range(5,0,-1):
    gausExtended = cv.pyrUp(gp_apple[i])
    laplaceTemp =  cv.subtract(gp_apple[i-1],gausExtended)
    lapApple.append(laplaceTemp)

# 2.2-Generating gaussian pyramid for orange
orange_copy = orange.copy()
gp_orage = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orage.append(orange_copy)

orange_copy = gp_orage[5]
lapOrange = [orange_copy]
# 3.2-Generating laplacian pyramid for orange

for i in range(5,0,-1):
    gausExtended = cv.pyrUp(gp_orage[i])
    laplaceTemp =  cv.subtract(gp_orage[i-1],gausExtended)
    lapOrange.append(laplaceTemp)


# 4-Add left and right halves of images in each level
appleOrangePyramid = []
n = 0

for appleCounter, orangeCounter in zip(lapApple, lapOrange):
    n += 1
    rows,cols,channels = appleCounter.shape
    laplaceTemp = np.hstack((appleCounter[:, 0:int(cols/2)], orangeCounter[:, int(cols/2):]))
    appleOrangePyramid.append(laplaceTemp)

# 5-Reconstructing
reconstruct = appleOrangePyramid[0]

for i in range(1,6):
    reconstruct = cv.pyrUp(reconstruct)
    reconstruct = cv.add(appleOrangePyramid[i],reconstruct)

cv.imshow('image', reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()



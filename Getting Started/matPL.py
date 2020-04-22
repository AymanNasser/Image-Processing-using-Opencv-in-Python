import cv2 as cv
from matplotlib import pyplot as plt

# Matplotlib reads the image in RBG format
# plt.subplot(rows, columns, index of image)
# plt.title ==> title of image


img = cv.imread('1.jpg', 1)
cv.imshow('image',img)

plt.imshow(img)
# removes x,y axis
plt.xticks([]),plt.yticks([])
plt.show()



cv.waitKey(0)
cv.destroyAllWindows()
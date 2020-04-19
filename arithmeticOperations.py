import cv2
import numpy as np



img = cv2.imread('../../FOEASU-Linux/opencv/samples/data/ela_modified.jpg', 1)


cv2.imshow('img0',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
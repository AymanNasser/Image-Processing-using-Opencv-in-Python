import cv2
import numpy as np

# cv2.bitwise_and/or/xor/not/etc(src1,src2) ==> logically perform as logic gates ==> useful for masking

img1 = np.zeros((250,250,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)


cv2.imshow('img',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
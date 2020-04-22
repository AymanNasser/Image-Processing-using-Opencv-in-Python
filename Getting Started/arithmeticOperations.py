import cv2
import numpy as np

# img.shape ==> returns a tuble of no. of [rows,columns,channels]
# img.size ==> returns total number of pixels
# img.dtype ==> returns image data type
# cv2.split(img) ==> returns b,g,r channels of img
# image = cv2.merge((b,g,r)) ==> merging (b,g,r) tubles into a new image
# ROI ==> region of interest in an image
# dest = cv.add(img1,img2) ==> adds 2 images of same size
# dest = cv2.resize(img, (rows,columns))
# dest = cv2.addwWeighted(src1, alpha, sr2, beta, gamma)
img = cv2.imread('../../FOEASU-Linux/opencv/samples/data/ela_modified.jpg', 1)
img2 = cv2.imread('../../FOEASU-Linux/opencv/samples/data/aero1.jpg', 1)
print(img.shape)
print(img.size)
# numpy indexing an image by passing the upper left hand side & bottom right hand side
ball = img[145:259, 351:557]

def mouse_is_clicked(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        string = str(x) +','+ str(y)
        cv2.putText(img, string, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,0), 2)
        cv2.imshow('img',img)

img = cv2.resize(img, (512,512))
img2 = cv2.resize(ball, (512,512))
# dest = cv2.add (img,img2)
dest = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('img',dest)
#cv2.setMouseCallback('img',mouse_is_clicked)





cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2 as cv
import numpy as np


# HSV (hue saturation value) ==> are alternative representations of the RGB color model

def changeColor(trackBarPos):
    pass

cap = cv.VideoCapture(0);

cv.namedWindow('image')
cv.namedWindow('res')
cv.namedWindow('mask')
cv.createTrackbar('LH', 'image', 0, 255,changeColor)
cv.createTrackbar('LS', 'image', 0, 255,changeColor)
cv.createTrackbar('LV', 'image', 0, 255,changeColor)

cv.createTrackbar('UH', 'image', 255, 255,changeColor)
cv.createTrackbar('US', 'image', 255, 255,changeColor)
cv.createTrackbar('UV', 'image', 255, 255,changeColor)


while True:
    #img = cv.imread('1.jpg')
    _ , img = cap.read()
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    lh = cv.getTrackbarPos('LH','image')
    ls = cv.getTrackbarPos('LS', 'image')
    lv = cv.getTrackbarPos('LV', 'image')

    uh = cv.getTrackbarPos('UH', 'image')
    us = cv.getTrackbarPos('US', 'image')
    uv = cv.getTrackbarPos('UV', 'image')

    l_b = np.array([lh,ls,lv])
    u_p = np.array([uh,us,uv])

    MASK = cv.inRange(hsv,l_b,u_p)

    result = cv.bitwise_and(img,img,mask=MASK)
    k = cv.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    cv.imshow('image', img)
    cv.imshow('res',result)
    cv.imshow('mask', MASK)

cap.read()
cv.destroyAllWindows()
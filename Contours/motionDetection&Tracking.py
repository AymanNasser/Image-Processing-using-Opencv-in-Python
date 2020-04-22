import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

cap = cv.VideoCapture('data/vtest.avi')

ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while cap.isOpened():
    # cv.absdiff() ==> returns the absolute difference

    if ret1 == True and ret2 == True:
        # By taking the difference between the two frames, all intensity for parts of the video where things don't move will be reduced to zero (since their values are the same in both frames).
        # The parts of the video where things DO move, however, will have different values in the two frames, and so the difference will result in a non-zero value
        diff = cv.absdiff(frame1,frame2)

        imgGray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(imgGray, (5,5), 0)
        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations=3)
        contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        # cv.boundingRect(array) ==> Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.
        # 1.a. Straight Bounding Rectangle ==> It is a straight rectangle, it doesn't consider the rotation of the object. So area of the bounding rectangle won't be minimum. It is found by the function
        # 1.b. Rotated Rectangle ==> bounding rectangle is drawn with minimum area, so it considers the rotation also
        (x,y,w,h) = cv.boundingRect(cont)
        if cv.contourArea(cont) < 1200:
            continue
        cv.rectangle(frame1, (x,y), (x+w,y+h),(255,0,0),5)


    #cv.drawContours(frame1, contours, -1, (0,0,255), 5)

    cv.imshow('image', frame1)
    frame1 = frame2
    ret2, frame2 = cap.read()

    if ret2 == False:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()



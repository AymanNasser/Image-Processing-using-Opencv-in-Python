import numpy as np
import cv2 as  cv

# Reading an image, writing a line, arrowLine on it
# cv.line(image variable, (x1,y1) , (x2,y2) , (BGR) color scheme, line thickness)
# cv.rectangle (imgage variable, top left vertix coordinate, bottom right vertix coordinate, (BGR), thickness)
# if -1 is specified for thickness of rectangle ==> fill
# cv.putText(image var, 'text to be specified', text coordinates, font type, font size, color, thickness, line type)

img = cv.imread('comp.png', 1)
# Generating image using numpy ==> np.zeros([image.height, image.width] , dataType)
img = np.zeros([512,512,3], np.uint8)

img = cv.line(img, (0,0) , (255,255), (40,50,255) , 5)
img = cv.rectangle(img, (0,0), (255,255), (50,222,255), 10)
img = cv.circle(img, (255,255), 50, (0,0,0), -1)
img = cv.putText(img, 'OPEN-CV', (370,280), cv.FONT_HERSHEY_PLAIN, 4, (0,0,255), 10, cv.LINE_AA)
cv.imshow('image', img)


cv.waitKey(0)
cv.destroyAllWindows()











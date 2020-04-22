import cv2
import numpy as np

# Printing specific members, classes that start with 'EVENT'
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

img = np.zeros((512,512,3), np.uint8)

# printing a text on a screen on (x,y) coordinates if mouse is right clicked
# or printing the BGR color spectrum on the x,y coordinates if mouse is left clicked
# using a call back function
def mouse_is_clicked(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        string = str(x) +','+ str(y)
        cv2.putText(img, string, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,0), 2)
        cv2.imshow('img0',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]

        BGRstr = str(r) + ',' + str(g) + ',' + str(b)
        cv2.putText(img, BGRstr, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,0), 2)
        cv2.imshow('img0',img)


cv2.imshow('img0',img)
cv2.setMouseCallback('img0',mouse_is_clicked)

cv2.waitKey(0)
cv2.destroyAllWindows()
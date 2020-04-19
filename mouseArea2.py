import cv2
import numpy as np


img = np.zeros((512,512,3), np.uint8)
points = []

# Generating shapes when mouse is clicked using array of points
# and connecting the last 2 element points[-1] & points[-2] together
# with a line
def mouse_is_clicked(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 2, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2], (255,255,0),)
        cv2.imshow('img0',img)

cv2.imshow('img0',img)
cv2.setMouseCallback('img0',mouse_is_clicked)

cv2.waitKey(0)
cv2.destroyAllWindows()
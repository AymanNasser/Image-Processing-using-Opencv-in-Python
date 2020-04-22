import cv2
import numpy as np

img = np.zeros((300,512,3),np.uint8)

# Create a window & name it
cv2.namedWindow('image')

def changeColor(trackBarPos):
    print(trackBarPos)


# cv2.createTrackBar(unique name, window name, initial value, final value, call_back function)
# cv2.getTrackBarPos(track_bar name, window name)
cv2.createTrackbar('BLUE', 'image', 0, 255,changeColor)
cv2.createTrackbar('GREEN', 'image', 0, 255,changeColor)
cv2.createTrackbar('RED', 'image', 0, 255,changeColor)
cv2.createTrackbar('0 : OFF\n 1: ON','image',0,1,changeColor)


while True:
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    B = cv2.getTrackbarPos('BLUE','image')
    G = cv2.getTrackbarPos('GREEN','image')
    R = cv2.getTrackbarPos('RED','image')
    S = cv2.getTrackbarPos('0 : OFF\n 1: ON','image')
    if S == 0:
        img[:] = 0
    else:
        img[:] = [B,G,R]

cv2.destroyAllWindows()
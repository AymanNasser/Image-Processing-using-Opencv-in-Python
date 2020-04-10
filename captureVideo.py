import cv2

# Capturing video frame using video capture from open-cv, returning the frame captured into a var
# called frame, then showing this frame var using imshow in an infinite loop, then releasing the resources
# when 'q' key is pressed

# Changing the color to any scale using cv2.cvtColor(source, code of color)
# cap = cv2.VideoCapture('friends.s04e01.720p.bluray.x264-sujaidr.mkv') == > processing on a video file
# var.isOpened() checks if the specified file is successfully opened or not
# var.get(properties)
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_BRIGHTNESS))

while(cap.isOpened()):

    ret, frame = cap.read()

    frame0 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

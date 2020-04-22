import cv2
import datetime

# Capturing video frame using video capture from open-cv, returning the frame captured into a var
# called frame, then showing this frame var using imshow in an infinite loop, then releasing the resources
# when 'q' key is pressed

# cap.read() returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
# Ret ==> will obtain return value from getting the camera frame, either true of false


# Changing the color to any scale using cv2.cvtColor(source, code of color)
# cap = cv2.VideoCapture('friends.s04e01.720p.bluray.x264-sujaidr.mkv') == > processing on a video file
# var.isOpened() checks if the specified file is successfully opened or not
# var.get(properties)
# for printing current date & time, import datetime, var = datetime.datetime.now()

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_BRIGHTNESS))
# Setting property using set operation

cap.set(3,1280)
cap.set(4,400)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_BRIGHTNESS))

while(cap.isOpened()):

    ret, frame0 = cap.read()

    frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2HLS)
    currDate = str (datetime.datetime.now())
    text = 'width = ' + str(cap.get(3)) + ' height = ' + str(cap.get(4)) 
    frame0 = cv2.putText(frame0, currDate, (10,50),cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255),5,cv2.LINE_AA)

    cv2.imshow('frame', frame0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

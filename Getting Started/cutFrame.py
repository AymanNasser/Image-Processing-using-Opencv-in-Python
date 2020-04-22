import cv2

# Processing on video file and specifying FOURCCs handle as XVID, * for writing the handle as a string
# using cv2.videoWriter(output file name, handle variable, fps, size of window)
# if ret(boolean) == true ==> checking if video to be captured is active or not
#  outFrame.write(source) ==> writing to the variable

cap = cv2.VideoCapture('friends.s04e01.720p.bluray.x264-sujaidr.mkv')

fourcc = cv2.VideoWriter_fourcc(*'XVID')

outFrame = cv2.VideoWriter('outputFrame.avi', fourcc, 20.0, (640,480))

while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s') :
            outFrame.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    else:
        break
cap.release()
outFrame.release()
cv2.destroyAllWindows()

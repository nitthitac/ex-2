import cv2
import time

cap = cv2.VideoCapture('D:/bookVideo/myVideo.mp4')
frame_rate = cap.get(cv2.CAP_PROP_FPS)
if cap.isOpened() == False:
    print('Error opening file')
else:
    while cap.isOpened():
        ret,frame = cap.read()
        if ret == True:
            time.sleep(1/frame_rate)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()
import cv2
import time

cap = cv2.VideoCapture(0)
print('Trying to connect to the camera...')
while not cap.isOpened():
    cap.open()
    time.sleep(1)
print('Camera connected')
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
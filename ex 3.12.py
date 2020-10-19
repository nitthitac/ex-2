import cv2
import time

cap = cv2.VideoCapture(0)
print('Trying to connect to the camera...')
while not cap.isOpened():
    cap.open()
    time.sleep(1)
print('Camera connected')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#create writer object to write video file
writer = cv2.VideoWriter('C:/bookVideo/myVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height)) #1
while True:
    ret,frame = cap.read()
    writer.write(frame) #2 write frame to destination
    gray = cv2. cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
writer.release() #3 release writer object
cv2.destroyAllWindows()
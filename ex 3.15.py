import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#top-left point of the rectangle
x = int(width/2)
y = int(height/2)
#width and height of the rectangle
w = 40
h = 50

while True:
    ret,frame = cap.read()
    cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
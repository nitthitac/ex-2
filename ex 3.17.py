import cv2
import numpy as np

def circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global total
        total = total+1
        cv2.circle (bg, (x,y), 50, (255,255,153), -1)
        cv2.putText(bg, param+str(total), (x-15,y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (150,150,150),2)

total = 0
text = '#'
bg = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('bg')
cv2.setMouseCallback('bg', circle, text)
while True:
    cv2.imshow('bg', bg)
    key = cv2.waitkey(1)
    if key == 27:
        break
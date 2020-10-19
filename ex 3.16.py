import cv2
import numpy as np

def circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(bg, (x,y), 50, (255,255,153), -1)

bg = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('bg')
cv2.setMouseCallback('bg', circle)
while True:
    cv2.imshow('bg', bg)
    key = cv2.waitkey(1)
    if key == 27:
        break

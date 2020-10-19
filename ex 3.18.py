import cv2
import numpy as np

def rectangle(event, x, y, flag, param):
    global drawing
    global x_tl, y_tl, x_br, y_br, new_bg, bg
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_tl, y_tl = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            x_br, y_br = x, y
            new_bg = bg.copy()
            cv2.rectangle(new_bg, (x_tl, y_tl), (x_br, y_br), (255, 255, 153), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing == True:
            drawing = False
            cv2.rectangle(new_bg, (x_tl, y_tl), (x_br, y_br), (255, 255, 153),2)
            bg = new_bg.copy()
drawing = False
bg = np.zeros((500,500,3), np.uint8)
new_bg = bg.copy()
cv2.namedWindow('new_bg')
cv2.setMouseCallback('new_bg', rectangle)
while True:
    cv2.imshow('new_bg', new_bg)
    key = cv2.waitKey(1)
    if key == 27:
        break


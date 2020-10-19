import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/User/Documents/bookPic/rada2.jpg')
cv2.namedWindow('rada2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('rada2', 300,500)
cv2.imshow('rada2', img)
cv2.waitKey(0) #wait until a key is pressed.
cv2.destroyAllWindows() #destroy all windows showing the images

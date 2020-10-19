import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rada1= cv2.imread('C:/Users/User/Documents/bookPic/rada1.png')
img_rada2 = cv2.imread('C:/Users/User/Documents/bookPic/rada2.jpg')

#create subplot (all concatenated images must have the same dimension)
img_size = tuple([175,300])
rs_rada1 = cv2.resize(img_rada1, img_size)
rs_rada2 = cv2.resize(img_rada2, img_size)
#concatanate image Horizontally
img_concate_Hori=np.concatenate((rs_rada1,rs_rada2), axis=1)
#concatanate image Vertically
img_concate_Verti=np. concatenate((rs_rada1,rs_rada2),axis=0)
cv2.namedWindow('Concatenated_Hori', cv2.WINDOW_NORMAL)
cv2.imshow('Concatenated_Hori',img_concate_Hori)
cv2.imshow ('Concatenated_Verti',img_concate_Verti)

cv2.waitKey(0) #wait until a key is pressed.
cv2.destroyAllWindows() #destroy all windows showing the images
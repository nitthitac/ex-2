import cv2
import matplotlib.pyplot as plt

PATH = 'D:/bookPic/'
filename = 'rada2.png'

#img = cv2.imread('wrongPath/rada2.png')
img = cv2.imread(PATH+filename)
print(type(img))
plt.imshow(img)
plt.show()
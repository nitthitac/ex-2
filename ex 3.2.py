import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'D:/bookPic/'
filename = 'rada2.jpg'

img = cv2.imread('wrongPath/rada2.jpg')
# img = cv2.imread(PATH+filename)
print(type(img))
if not isinstance(img, np.ndarray):
    print('Unsuccessfully load the image "{}"'.format(filename))
    exit()
plt.imshow(img)
plt.show()
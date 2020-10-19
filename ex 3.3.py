import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'D:/bookPic/'
filename = 'rada2.jpg'

#img = cv2.imread('wrongPath/rada2.jpg')
img = cv2.imread(PATH+filename)
print(type(img))
if not isinstance(img, np.ndarray):
    print('Unsuccessfully load the image "{}"'.format(filename))
    exit()
RGB_img = cv2.cvtColor(img, cv2.COLOR_B)
#downsize the image to half of the original
new_width, new_height = int(RGB_img.shape[1]/2), int(RGB_img.shape[0]/2)
RGB_resize = cv2.resize(RGB_img.copy(), (new_width, new_height))
#save the images
cv2.imwrite('C:/test/rada2_resize.jpg',RGB_resize)
cv2.imwrite('C:/test/rada2.jpg', img)

ax1 = plt.subplot(1, 3, 1)
plt.imshow(img)
ax1.set_title('img')
ax2 = plt.subplot(1, 3, 2, yticklabels = [])
plt.imshow(RGB_img)
ax2.set_title('RGB_img')
ax3 = plt.subplot(1, 3, 3, yticklabels = [])
plt.imshow(RGB_resize)
ax3.set_title('RGB_resize')
plt.show()
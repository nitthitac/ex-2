import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'C:/Users/User/Documents/bookPic/'
img = Image.open(PATH+'rada1.png')
arr_img = np.asarray(img)
gray_img = np.ndarray(arr_img.shape)
gray_img[:, :, 0] = arr_img[:, :, 0]/3 + arr_img[:, :, 1]/3 + arr_img[:, :, 2]/3
gray_img[:, :, 1] = arr_img[:, :, 0]/3 + arr_img[:, :, 1]/3 + arr_img[:, :, 2]/3
gray_img[:, :, 2] = arr_img[:, :, 0]/3 + arr_img[:, :, 1]/3 + arr_img[:, :, 2]/3
gray_img = gray_img.astype(int)
ax1 = plt.subplot(1, 2, 1)
ax1.set_title('Original')
plt.imshow(arr_img)
ax2 = plt.subplot(1, 2, 2, yticklabels = [])
ax2.set_title('Gray')
plt.imshow(gray_img)
plt.show()

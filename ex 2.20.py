import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'C:/Users/User/Documents/bookPic/'
img = Image.open(PATH+'rada1.png')
arr_img = np.asarray(img)

negative = 255-arr_img
ax1 = plt.subplot(1, 2, 1)
ax1.set_title('Original')
plt.imshow(arr_img)
ax2 = plt.subplot(1, 2, 2, yticklabels = [])
ax2.set_title('Negative')
plt.imshow(negative)
plt.show()
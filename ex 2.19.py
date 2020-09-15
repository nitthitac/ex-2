import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'C:/Users/User/Documents/bookPic/'
img = Image.open(PATH+'rada1.png')
arr_img = np.asarray(img)
factor = 0.7
new_img = arr_img.copy()
new_img = new_img*factor
new_img = new_img.astype(int)

ax1 = plt.subplot(1, 2, 1)
ax1.set_title('Original')
plt.imshow(arr_img)
ax2 = plt.subplot(1, 2, 2, yticklabels = [])
ax2.set_title('Dim 30%')
plt.imshow(new_img)
plt.show()
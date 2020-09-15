import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'C:/Users/User/Documents/bookPic/'
img = Image.open(PATH+'rada1.png')
print(type(img))
arr_img = np.asarray(img)
print(type(arr_img))
print(arr_img.shape)
print(arr_img.dtype)

#plotting subplots of the image in original and R-, G- and B- chanel
rows = 1
cols = 4
ax = [None]*4
channels = {0: 'R', 1: 'G', 2: 'B'}
ax[0] = plt.subplot(1, 4, 1)
plt.imshow(arr_img)
ax[0].set_title('Original')
for position, channel in zip(range(2, cols+1), channels):
    ax[position-1] = plt. subplot(rows, cols, position, yticklabels = [])

    #shows channel values (0-255) in grayscale
    plt.imshow(arr_img[:, :, channel], cmap = 'gray')
    ax[position-1].set_title(channels[channel])
plt.show()
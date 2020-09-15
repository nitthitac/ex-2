import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'C:/Users/User/Documents/bookPic/'
img = Image.open(PATH+'rada1.png')
arr_img = np.asarray(img)
zero_red = arr_img.copy()
zero_red[:, :, 0] = 0

#plotting subplots of the image in original and R-, G- and B- channel
rows = 1
cols = 2
fig = plt.figure()
fig.add_subplot(rows, cols, 1)
plt.imshow(arr_img)
fig.add_subplot(rows, cols, 2, yticklabels = [])
plt.imshow(zero_red)
plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros ((512, 512, 3), dtype=np.uint8)
cv2.line(img, pt1 = (0,0), pt2 = (100,100), color = (255,0,0), thickness = 10)
cv2.line(img, (200,200), (450,500), (0,255,0), 10)
plt.imshow(img)
plt.show()
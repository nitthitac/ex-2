import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.circle(img, center=(200,200), radius=50, color=(255,0,0), thickness=10)
cv2.circle(img, (400,400), 100, (0,255,0), -1)
plt.imshow(img)
plt.show()
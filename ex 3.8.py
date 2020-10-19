import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), dtype=np.uint8)
texts = 'Hello World'
cv2.putText(img, org=(0,500), text=texts, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255,255,255),
thickness=5)
#Text with green background
(width, height), _ = cv2.getTextSize(texts, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, thickness=5)
cv2.rectangle(img, (100,200), (100+width+10, 200+height+10), color=(0,255,0), thickness=-1)
cv2.putText(img, org=(105,200+height+5),text=texts, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
color=(255,255,255), thickness=5)
plt.imshow(img)
plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), dtype=np.uint8)
# Vertices
vertices_tri = np.array([[100,200], [200,200], [150,150]])
vertices_tri.reshape((-1,1,2))
vertices_arb = np.array([[200,300], [300,200], [200,400], [450,500]])
vertices_arb.reshape(-1,1,2)
vertices_tri2 = np.array([[400,300], [400,100], [480,300]])
# Connect the vertices
cv2.polylines(img, pts=[vertices_tri], isClosed=True, color=(255,0,0), thickness=5)
cv2.polylines(img, [vertices_arb], False, (0,255,0), 10)
# Ble triangle
cv2.fillPoly(img, pts=[vertices_tri2], color=(0,0,255))
plt.imshow(img)
plt.show()


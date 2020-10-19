import numpy as np
import cv2
import matplotlib.pyplot as plt

networkFile = 'googleNet/bvlc_googlenet.prototxt'
weightFile = 'googleNet/bvlc_googlenet.caffemodel'
imageFile = 'googleNet/twocups.jpg'
classFile = 'googleNet/classification_classes_ILSVRC2012.txt'

classes = None
with open(classFile, 'r') as f:
    classes = f.read().split('\n')

height = 224
width = 224
swap_rgb = False
mean = [104, 117, 123]
scale = 1.0
# Load weight and config file
net = cv2.dnn.readNetFromCaffe(networkFile, weightFile)
# Creating a blob
image = cv2.imread(imageFile)
blob = cv2.dnn.blobFromImage(image, scalefactor= scale, size=(width, height), mean= mean, swapRB = swap_rgb, crop=False)
net.setInput(blob)
# Feed forwarding blob into CNN
out = net.forward()
# Post processing
out = out.flatten()
classID = np.argmax(out)
className = classes[classID]
confindence = out[classID]
text = 'Class: {}-{:.2f}'.format(className, confindence)
print(text)
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.8
FONT_THICKNESS = 2
FONT_COLOR = (255,255,255)
text_width, text_height = cv2.getTextSize(text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
print(text_width,text_height)
cv2.rectangle(image, (5,5), (5+text_width+5, 25+text_height+5), (255,0,0), -1)
cv2.putText(image, text, (10,15+text_height), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)
plt.imshow(image)
plt.show()
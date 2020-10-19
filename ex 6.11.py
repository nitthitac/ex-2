import cv2
import numpy as np

networkFile = 'yolov3/yolov3.cfg'
weightFile = 'yolov3/yolov3.weights'
imageFile = 'images/twocups.jpg'
classFile = 'yolov3/coco.names'

# Yolo parameter
objectThreshold = 0.5
confThreshod = 0.5
nmsThreshold = 0.4

# Load weight and config file
net = cv2.dnn.readNetFromDarknet(networkFile, weightFile)
# Read classes
classes = None
with open("coco.names", "r") as f:
    classes = f.read().split('\n')
colors = np.random.uniform(50, 200, size=(len(classes), 3))

# Creating a blob
img = cv2.imread(imageFile)
height, width, channels = img.shape
blob = cv2.dnn.blobFromImage (img, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
# Feed forwarding blob into CNN
layer_names = net.getLayerName()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
outs = net.forward(output_layers)
# Postprocessing
classIDs = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > 0.5:
            # object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            classIDs.append(classID)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, confThreshod, nmsThreshold)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 0.75
fontthickness = 2
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h =boxes[i]
        label = str(classes[classIDs[i]])
        labelSize, baseLine = cv2.getTextSize(label, font, fontscale, fontthickness)
        y = max(y, labelSize[1])
        cv2.rectangle(img, (x, y - round(1.2 * labelSize[1])), (x + round(1.2 * labelSize[0]), y + baseLine),
                      (0, 0, 0), cv2.FILLED)
        color = colors[classIDs[i]]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y-3), font, fontscale, color, fontthickness)

        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
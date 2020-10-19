import numpy as np
from keras.datasets import cifar10
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from sklearn.metrics import confusion_matrix, classification_report

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print(x_train.shape, y_train.shape)
x_train = x_train/255.0
x_test = x_test/255.0
y_cat_train = to_categorical(y_train, 10)
y_cat_test = to_categorical(y_test, 10)

model = Sequential()
model.add(Conv2D(filters=64, kernel_size=(4,4), activation='relu', input_shape=x_train.shape[1:]))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters=128, kernel_size=(4,4), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
# model.add(conv2D(filters=256, kernel_size=(4,4), activation='relu'))
# model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))
print(model.summary())
model.compile(optimizer ='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_cat_train, eposhs=1)
model.save('D:/bookFiles/CNN_cifar10_D512_ep1.h5')
print(model.evaluate(x_test, y_cat_test))
predictions = model.predict_classes(x_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
import numpy as np
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, Maxpool2D
from sklearn.metrics import confusion_matrix, classification_report

# load data from keras
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape, x_train.max(), x_train.min())
# prepare data
y_test = to_categorical(y_test, 10)
y_train = to_categorical(y_train, 10)
x_train = x_train/255
x_test = x_test/255
x_train = x_train.reshape(x_train.shape+(1,))
x_test = x_test.reshape(x_test.shape+(1,))
print(x_train.shape)
# create a CNN model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(4,4), input_shape=x_train.shape[1:4], activation='relu'))
model.add(MaxPool2D(pool_size=(2,2), strides= 2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
print(model.summary())
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=2)
# evaluate model
print(model.metrics_names)
print(model.evaluate(x_test,y_test))
# another way to evaluate model
predictions = model.predict_classes(x_test)
y_test = np.argmax(y_test, axis=1)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
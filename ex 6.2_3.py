import numpy as np
np.random.seed(1337)
from numpy import genfromtxt
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from ann_visualizer.visualize import ann_viz
from sklearn.metrics import confusion_matrix, classification_report

data = genfromtxt('D:/bookFiles/iris.csv', delimiter=',', dtype=None, encoding=None)

# preparing data
x = np.stack((data['f0'], data['f1'], data['f2'], data['f3']), axis=1)
y = data['f4']
for i in data:
    if i[4] == 'Iris-setosa':
        i[4] = 0
    elif i[4] == 'Iris-versicolor':
        i[4] = 1
    else:
        i[4] = 2
y = np.uint8(y)
#  print(y[0::15])
y = to_categorical(y,3)
# print(y[0::5])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler_object = MinMaxScaler()
scaler_object.fit(x_train)
scaled_x_train = scaler_object.transform(x_train)
scaled_x_test = scaler_object.transform(x_test)
# build and train ANN
model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
ann_viz(model, title='IRIS ANN')
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(scaled_x_train, y_train, validation_data=(scaled_x_test, y_test), batch_size= 5, epochs=200, verbose=2)
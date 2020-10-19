from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.preprocessing.image import ImageDataGenerator
import sys

Kaggle_PATH = 'D:/bookFiles/Cat_Dog_Kaggle/train/'
dataset_PATH = 'D:/bookFiles/cats_vs_dogs/'

image_size = (200,200)
# build a CNN model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=image_size+(3,)))
model.add(MaxPooling2D((2,2)))
# model.add(Dropout(0.2))
model.add(Conv2D(filters=64, kelnel_size=(3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
# model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print (model.summary())

test_data_gen = ImageDataGenerator(rescale=1/255.0)
train_data_gen = ImageDataGenerator (rescale=1/255.0,
                                     rotation_range=20,
                                     width_shift_range=0.2,
                                     height_shift_range=0.2,
                                     horizontal_flip=True,
                                     shear_range = 0.2,
                                     zoom_range= 0.2,
                                     fill_mode='nearest')
train_data = train_data_gen.flow_from_directory(dataset_PATH+'train/', class_mode='binary',
                                                batch_size=64, target_size=(200,200))
test_data = test_data_gen.flow_from_directory(dataset_PATH+'test/', class_mode='binary',
                                              batch_size=64, target_size=(200,200))
results = model.fit_generator(train_data, steps_per_epoch=len(train_data), validation_data=test_data,
                              validation_steps=len(test_data), epochs=30)
_, acc = model.evaluate_generator(test_data, steps=len(test_data), verbose=0)
print('> %.3f' % (acc * 100.0))
model.save('D:/bookFiles/cats_vs_dogs/2Conv30EpDataaugmentation.h5')
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
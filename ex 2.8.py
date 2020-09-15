import numpy as np

arr1 = np.random.randint(100, size = (3,2))
print("arr1 = \n",arr1)
print("Max value = {} at {}".format(arr1.max(), arr1.argmax()))
print("Min value = {} at {}".format(arr1.min(), arr1.argmin()))
print("Mean value = ", arr1.mean())
import numpy as np

arr = np.random.randint(100, size = 10)
print("arr =", arr)
print("Max value = {} at {}".format(arr.max(), arr.argmax()))
print("Min value = {} at {}".format(arr.min(), arr.argmin()))
print("Mean value = ", arr.mean())
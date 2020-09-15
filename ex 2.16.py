import numpy as np

arr = np.arange(30).reshape((3, 10))
print("arr = ")
print(arr)
print()
copy_arr = arr.copy() [0:2, 0:5]
copy_arr[:, :] = 0
print(copy_arr)
print()
print("arr = ")
print(arr)
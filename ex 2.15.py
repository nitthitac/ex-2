import numpy as np

arr = np.arange(30).reshape((3, 10))
print("arr = ")
print(arr)
print()
new_arr = arr[0:2, 0:5]
print("new_arr =")
print(new_arr)
print()
new_arr[:,:] = 0
print("naw_arr = ")
print(new_arr)
print()
print("arr = ")
print(arr)
import numpy as np

arr = np.arange(30).reshape((3, 10))
print(arr)
print()
print(arr[1, :])
print()
print(arr[:, 6])
print()
print(arr[0:1, 0:3])
print()
print(arr[:1, :3])
print()
print(arr[:, 0:10:2])

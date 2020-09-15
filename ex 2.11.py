import numpy as np

arr1 = np.random.randint(10, size = 8)
print("arr1 = ", arr1)
arr2 = arr1.reshape((-1, 2))
print("arr1 = \n", arr2)
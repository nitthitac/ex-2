import numpy as np

arr1 = np.random.randint(10, size = 8)
arr2 = arr1.reshape((2, 4))
arr3 = arr1.reshape((2, 2, 2))
print("arr1 = ", arr1)
print("arr2 = \n", arr2)
print("arr3 = \n",  arr3)
import numpy as np

arr1 = np.random.randint(10, size = 10)
arr2 = np.random.randint(10, size = (3, 4))
arr3 = np.random.randint(10, size = (2, 2, 2))

print("arr1: ndim-{}, shape-{}, size-{}, dtype-{}".format(arr1.ndim, arr1.shape, arr1.size, arr1.dtype))
print(arr1)
print("arr2: ndim-{}, shape-{}, size-{}, dtype-{}".format(arr2.ndim, arr2.shape, arr2.size, arr2.dtype))
print(arr2)
print("arr3: ndim-{}, shape-{}, size-{}, dtype-{}".format(arr3.ndim, arr3.shape, arr3.size, arr3.dtype))
print(arr3)
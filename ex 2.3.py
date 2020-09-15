import numpy as np

arr_zero1 = np.zeros(5)
arr_zero2 = np.zeros((5,5))
arr_zero3 = np.zeros((5,5), dtype = np.int)

arr_one1 = np.ones(shape = 3)
arr_one2 = np.ones(shape = (3,2))

print("arr_zero1 = \n", arr_zero1)
print("arr_zero2 = \n", arr_zero2)
print("arr_zero3 = \n", arr_zero3)
print("arr_one1 = \n", arr_one1)
print("arr_one1 = \n", arr_one2)
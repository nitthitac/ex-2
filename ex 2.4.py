import numpy as np

np.random.seed(100)
arr_random1 = np.random.randint(10)
arr_random2 = np.random.randint(5, size = 10)
arr_random3 = np.random.randint(5, 30, 10)

print("arr_random1: ", type(arr_random1), "\n", arr_random1)
print("arr_random2: ", type(arr_random2), "\n", arr_random2)
print("arr_random3: ", type(arr_random3), "\n", arr_random3)

import numpy as np

array = np.random.randint(0, 100, size = 5)
max = array[0]
index = 0

print(array)

while index < len(array):
    if array[index] > max:
        max = array[index]
    index += 1

print(max)
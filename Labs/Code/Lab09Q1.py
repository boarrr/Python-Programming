import numpy as np
import math

arr = np.random.randint(0, 100, 10)
arrLen = len(arr)
i = 0

hist = np.zeros(10, dtype=int)

while i < arrLen:
  hist[math.floor(arr[i] // 10)] += 1
  i += 1

print(hist)
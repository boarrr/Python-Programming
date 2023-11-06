arr = [1,0,3,2,4,2,3,2,3,2,2]

arrLen = len(arr)
counts = [0] * (max(arr) + 1)
i = 0


while i < arrLen:
  counts[arr[i]] += 1
  i += 1

print(counts)
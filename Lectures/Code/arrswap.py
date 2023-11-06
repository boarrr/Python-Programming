arr = [2,6,8,5,2,9,7]

arrLen = len(arr)
i = 0
j = arrLen - 1
temp = 0

while i < arrLen / 2:
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  i += 1
  j -= 1

print(arr)
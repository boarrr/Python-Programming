
numArray = [1, 2, 3, 4, 5]

index = 0
total = 0
length = len(numArray)

while index < length:
  total = total + numArray[index]
  index = index + 1

print(total)
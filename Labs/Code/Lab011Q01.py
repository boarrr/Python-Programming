# A program that reads in a sorted array and finds the two integers closest in value

i = 0
arr = [1, 3, 4, 12, 15, 18]
n = len(arr)
min = arr[n - 1] - arr[0]

if n < 2:
  print("Invalid Input")
else:
  while i < n - 1:
    difference = arr[i + 1] - arr[i]

    if difference < min:
      min = difference
      closet = (arr[i], arr[i + 1])

    i += 1

print(closet)
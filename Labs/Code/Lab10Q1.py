# A program to find the local maximas within an array

arr = [3,2,4,1,3,7,5,6,4]
i = 1

while i < len(arr) - 1:
  if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
    print(f"Value {arr[i]} location {i}")

  i += 1

  
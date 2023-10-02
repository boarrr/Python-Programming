# A program to show the factorial of an inputted positive integer

num = int(input("Enter a number: "))
factorial = 1
i = 1

if (num != 0):
  while (i <= num):
    factorial = factorial * i
    i += 1

  print(f"The factorial of {num} is {factorial}")
else:
  print("The factorial of 0 is 0")
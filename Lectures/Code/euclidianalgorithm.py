# A program to demonstrate euclidian algorithm

userInput = input("Enter two numbers separated by a comma: ")

num1, num2 = userInput.split(",")
num1 = int(num1)
num2 = int(num2)

while num1 != num2:
  if num1 > num2:
    num1 -= num2
  else:
    num2 -= num1

print("The GCD is", num1)

# 15, 9
# 15, 6
# 9, 6
# 3, 6
# 3, 3
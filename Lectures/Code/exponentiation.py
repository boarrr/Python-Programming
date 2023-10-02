# A program demonstrating an exponentiation algorithm where a is to the power of b
# Example: a = 5, b = 3   = >   5 x 5 x 5 = 125

numA = int(input("Enter the first number: "))
numB = int(input("Enter the second number: "))
sum = 1

while (numB > 0):
  sum = sum * numA
  numB -= 1

print(sum)
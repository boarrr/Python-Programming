num = int(input("Enter a decimal number: "))

# Convert decimal to binary and print
while num > 0:
  print(num % 2, end="")
  num = num // 2
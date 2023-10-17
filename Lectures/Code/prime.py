import math

num = int(input("Enter a number: "))

isPrime = True

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        isPrime = False
        break

if isPrime == True:
    print("It is prime")
else:
    print("It isn't prime")
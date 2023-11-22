import math

factors = []
num = 8

for i in range(2, int(math.sqrt(num)) + 1):
  while num % i == 0:
    factors.append(i)
    num //= i

if num > 1:
  factors.append(num)

print(factors)
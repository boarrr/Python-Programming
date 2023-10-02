# Program to take user inputs to a predefined number and count the number of inputs over 50
# While saving elements in a list for later usage
# Author: Ryan Pitman
# Date: 02/10/2023

numInt = 10
over50 = []
count = 0

for i in range(0,numInt):
  userInput = int(input("Enter an integer: "))

  if userInput > 50:
    over50.append(userInput)

print("\nThe number of ints over 50 was:", len(over50))
print ("They were:")

for i in over50:
  print(i)

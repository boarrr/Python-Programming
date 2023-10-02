# A program to take user inputs to a predefined number and count the number of inputs over 50
# Author: Ryan Pitman
# Date: 02/10/2023

count = 0
numVals = 10

for i in range(0, numVals):
  userInput = int(input("Enter an integer: "))
  if (userInput > 50):
    count += 1

print("The number of elements over 50 is:", count)
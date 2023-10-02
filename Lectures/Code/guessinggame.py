# Author: Ryan Pitman
# Description: A simple number guessing game where the user has 3 attempts to guess a random number between 1 and 10
# 02/10/2023

import random

numGuesses = 3
randNum = random.randint(1, 10)
guessed = False

while (numGuesses != 0 and guessed == False):
  userInput = int(input("Enter a number: "))

  if (userInput == randNum):
    print("You got it right, the number was", randNum)
    guessed = True
  else:
    numGuesses -= 1

if (numGuesses == 0):
  print("You failed to guess the number correctly!")
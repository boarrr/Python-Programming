word = input('please enter a word: ')
userChar = input('please enter a character: ')

index = 0

count  = 0

length = len(word)

while index < length:
  if word[index] == userChar:
    count = count + 1
  
  index = index + 1


print(count)


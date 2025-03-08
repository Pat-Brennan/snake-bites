import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20 ...')

for guessTaken in range(1, 11):
  print('Take a guess')
  guess = int(input())

  if guess < secretNumber:
    print('a little higher ... ')
  elif guess > secretNumber:
    print('a little lower ...')
  else:
    break

if guess == secretNumber:
  print('You\'re the smartest person to ever live!')
else:
  print('* sigh *')

import random, sys

print('ROCK ... PAPER ... SCISSSORRRSSSS!!!')

#? Variables to keep track of the game
wins = 0
losses = 0
ties = 0

#? Initial loop
while True:
  print('%s wins, %s losses, %s ties' % (wins, losses, ties))
  while True:
    print('Make your move! (r)ock, (p)aper, (s)cissors')
    playerMove = input()
    if playerMove == 'q':
      sys.exit()
    if playerMove == 'r' or playerMove == 'p' or playerMove== 's':
      print('type r, p, s, or q')
      break

  if playerMove == 'r':
    print('Rock vs ...')
  elif playerMove == 'p':
    print('Paper vs ...')
  elif playerMove == 's':
    print('Scissors vs ...')
  
  randomNumber = random.randint(1, 3)
  if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
  elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
  elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')

  if playerMove == computerMove:
    #? Tie Condition
    ties = ties + 1
    print('TIE')
    #? Win Conditions
  elif playerMove == 'r'and computerMove == 's':
    wins = wins + 1
    print('You\'ve won!')
  elif playerMove == 'p'and computerMove == 'r':
    wins = wins + 1
    print('You\'ve won!')
  elif playerMove == 's'and computerMove == 'p':
    wins = wins + 1
    print('You\'ve won!')
    #? Lose Conditions
  elif playerMove == 'r' and computerMove == 'p':
    losses = losses + 1
    print('You\'ve been consumed by the darkness!')
  elif playerMove == 'p' and computerMove == 's':
    losses = losses + 1
    print('You\'ve been consumed by the darkness!')
  elif playerMove == 's' and computerMove == 'r':
    losses = losses + 1
    print('You\'ve been consumed by the darkness!')
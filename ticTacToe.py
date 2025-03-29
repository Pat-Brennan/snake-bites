theBoard = {
  'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
  'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-L'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-L'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-L'])

turn = 'X'
for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Move on Which Space?')
  move = input()
  theBoard[move] = turn
  if turn == 'X':
    turn = 'O'
  else:
    turn = 'X'
print(printBoard)

printBoard(theBoard)



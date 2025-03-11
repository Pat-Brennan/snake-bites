# Conways Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
  column = []
  for y in range(HEIGHT):
    if (x, y) in ((1,0), (2,1), (0,2), (1,2), (2,2)):
      column.append('#') # add a living cell
    else:
      column.append(' ') # add dead cell
    nextCells.append(column) # Next cels is a list of column lists

while True: # Main Program Loop
  print('\n\n\n\n\n') # separate each step with new lines
  currentCells = copy.deepcopy(nextCells)
  # Print current cells on screen
  for y in range(HEIGHT):
    for x in range(WIDTH):
      print(currentCells[x][y], end='') # Print the # or space
    print() # Print a new line at the end of each row

  # Calcualte the next step's cells based on current step's cells:
  for x in range(WIDTH):
    for y in range(HEIGHT):
      # Get Neighboring coordinates:
      # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
      leftCoord = (x - 1) % WIDTH
      rightCoord = (x + 1) % WIDTH
      aboveCoord = (y - 1) % HEIGHT
      belowCoord = (y + 1) % HEIGHT

      # Count the number of living neighbors:
      numNeighbors = 0
      if currentCells[leftCoord][aboveCoord] == '#':
        numNeighbors += 1 # Top-left neighbor is alive 
      if currentCells[x][aboveCoord] == 'x':
        numNeighbors += 1 # Top neighbor is alive
      if currentCells[rightCoord][aboveCoord] == '#':
        numNeighbors += 1 # Top-right neighbor is alive
      if currentCells[leftCoord][y] == '#':
        numNeighbors += 1 # left neighbor is alive
      if currentCells[rightCoord][y] == '#':
        numNeighbors += 1 # right neighbor is alive
      if currentCells[leftCoord][belowCoord] == '#':
        numNeighbors += 1 # below left neighbor is alive
      if currentCells[x][belowCoord] == '#':
        numNeighbors += 1 # beow neighbor is alive
      if currentCells[rightCoord][belowCoord] == '#':
        numNeighbors += 1 # bottom right neighbor is alive
      
      # Set Cell based on Conways game of life rules
      if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
        # Living cells with 2 or 3 neighbors stay alive 
        nextCells[x][y] = '#'
      elif currentCells[x][y] == ' ' and numNeighbors == 3:
        # Dead cells with 3 neighbors become alive
        nextCells[x][y] = '#'
      else:
        nextCells[x][y] = ' '
  time.sleep(0.60)


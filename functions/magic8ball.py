import random

def getAnswer(answerNumber):
  if answerNumber == 1:
    return 'It is certain'
  elif answerNumber == 2:
    return 'It is undecidely so.'
  elif answerNumber == 3:
    return 'Yes'
  elif answerNumber == 4:
    return 'Don\'t do it!'
  elif answerNumber == 5:
    return 'save yourself!'
  
r = random.randint(1, 5)
fortune = getAnswer(r)
print(fortune)
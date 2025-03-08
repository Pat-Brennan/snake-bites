def spam():
  eggs = 'spam local'
  print(eggs) #? Prints Spam Local

def bacon():
  eggs = 'bacon local'
  print(eggs)
  spam()
  print(eggs)

eggs = 'global'

bacon()
print(eggs) #? prints global


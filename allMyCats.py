# print('enter the name of Cat 1:')
# catName1 = input()
# print('enter the name of Cat 2:')
# catName2 = input()
# print('enter the name of Cat 3:')
# catName3 = input()
# print('enter the name of Cat 4:')
# catName4 = input()
# print('enter the name of Cat 5:')
# catName5 = input()

# print('The Cat names are ... ')
# print(catName1 + ', ' + catName2 + ', ' + catName3 + ', ' + catName4 + ', ' + catName5)


catNames = []
while True:
  print('Enter the name of cat ' + str(len(catNames) + 1) + '(or enter nothing to stop)')
  name = input()
  if name == '':
    break
  catNames = catNames + [name]
print('The cat names are ...')
for name in catNames:
  print( ' ' + name )
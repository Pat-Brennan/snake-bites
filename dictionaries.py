

myCat = {
  'Size': 'Chonker',
  'Color': 'Black',
  'Disposition': 'Desires Treats',
}

print(myCat['Size'])
print(myCat.keys())
print(list(myCat.keys()))

for k, v in myCat.items():
  print('Key: ' + k + 'Value: ' + v)


#? While the order of a dictionary may help determine if two lists are the same,
#? It is not the deciding factor

#? In otherwords, as long as a dictionary contains the same key:value pairs, they will evaluate to TRUE.

birthdays = {
  'Goku':'April 1st',
  'Vegeta': 'September 11th',
  'Krillin': 'April 20th'
}

while True:
  print('Enter a Name: (blank to quit)')
  name = input()
  if name == '':
    break

  if name in birthdays:
    print(birthdays[name] + 'is the birthday of ' + name)
  else:
    print('I do not have that birthday information for ' + name)
    print('What is their birthday?')
    bday= input()
    birthdays[name] = bday
    print('Birthday Database Updated')



while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':
    continue
  print('Heeey Joe! What\'s the password?')
  password = input()
  if password == 'swordfish':
    break
print('Access granted.')


users = ['Mary', 'Crash Bandicoot', 'Spyro', 'Jak', 'Admin']

if users:
  for user in users:
    if user == 'Admin':
      print('Hello Captain Admin. Would you like todays status report?')
    else:
      print(f'What up, {user}?!')


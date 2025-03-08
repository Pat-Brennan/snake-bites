
alien_colors = ['red', 'blue', 'green']

player_score = 0

alien = alien_colors[2]
while True:
  print('Look out! An Alien dude! What do you do? (shoot -or- run)')
  alien_state = input()

  if player_score == 20:
    print('Relax there killer I think you got them all SHEEEESH')
    break

  if alien_state == 'shoot':
    alien = alien_colors[0]
    print('Gnarly! You got them and there\'s Alien blood everywhere!')
    player_score += 5
    print(player_score)
  elif alien_state == 'run':
    print('You couldn\'t get away!')
    player_score -= 5
    print(player_score)

import random

messages = [
  'Is it here?',
  'Was it there?',
  'It must be?',
  'Otherwise who would!',
  'I don\'t think so.',
  'Hey that\'s my Purse!',
  'I don\'t know you!'
]

print(messages[random.randint(0, len(messages) - 1)])
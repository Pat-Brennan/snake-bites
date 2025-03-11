#! python 3
#bulletPointAdder.py - Adds bullet points to wikipedia articles

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars

#Separate lines and Add *s
lines = text.split('\n')
for i in range(len(lines)): #loop through all of the lines
  lines[i] = '* ' + lines[i] # add a star to each line
text = '\n'.join(lines)
pyperclip.copy(text)
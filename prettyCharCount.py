import pprint

message = "There we were, boats against the current, sailing into darkness."
count= {}

for char in message:
  count.setdefault(char, 0)
  count[char] = count[char] + 1

pprint.pprint(count)
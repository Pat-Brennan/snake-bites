def spam(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error! Invalid Argument')

print(spam(2))
print(spam(0))
print(spam(5))
print(spam(1))
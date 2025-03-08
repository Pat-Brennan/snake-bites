availableToppings = ['peppers', 'anchovies', 'pine apple', 'Broccoli', 'long hots', 'mozz sticks']

requestedToppings = ['french fries', 'onion rings', 'mozz sticks']

for requestedTopping in requestedToppings:
  if requestedTopping in availableToppings:
    print(f"Adding {requestedTopping}")
  else:
    print(f"sorry. we don't have {requestedTopping}. Now Scram!")

print("we've finished making your pizza!")

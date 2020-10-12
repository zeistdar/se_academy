# Bad(Not technically )
ls = []
for element in range(10):
  if not(element % 2):
    ls.append(element)

# We may also employ a lambda function
ls = list(filter(lambda element: not(element % 2), range(10)))

# Good
ls = [ls for ls in range(10) if not (ls % 2)]

# Write a list comprehension to get the multiples of 5 in ragne of 100
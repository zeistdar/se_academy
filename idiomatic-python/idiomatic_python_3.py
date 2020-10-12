cities = ['Nairobi', 'Kampala', 'Lagos']

# Bad
index = 0
while index < len(cities):
  print(cities[index])
  index += 1

# Good
for city in cities:
    print(city)

# Better if you want to get the index
for i, city in enumerate(cities):
    print(f'City: {city} at index: {i}')
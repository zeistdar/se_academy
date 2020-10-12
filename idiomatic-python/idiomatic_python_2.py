# Compare multiple integers
first_number = 3
second_number = 5
third_number = 9

# Bad
if first_number <= second_number and second_number <= third_number:
    print("This is a long statement")

# Good
if first_number <= second_number <= third_number:
    print("This looks kinda cool")


# Variable Swapping
a = 1
b = 2
print('Before swapping')
print(f'value a {a}')
print(f'value b {b}')
# Bad
c = a
a = b
b = c
print(f'value a {a}')
print(f'value b {b}')

# Good
a, b = b, a
print(f'value a {a}')
print(f'value b {b}')
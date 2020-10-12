# whenever you are not sure where the statement will fail or pass use
try:
    1 / 0
except ZeroDivisionError as e:
    print(str(e))
finally:
    # will always run
    print("You cannot divide by zero")

try:
    1 / 0
except ZeroDivisionError as e:
    print(str(e))
else:
    # will only run if try doesn't fail
    print("This will not run")
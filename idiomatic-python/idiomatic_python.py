# Bad
x = []
y = False
z = None

if len(x) == 0:
    print("Empty List: Bad way")
if y == False:
    print("False: Bad way")
if z == None:
    print("None: Bad Way")


# Good
if not x:
    print("Empty List: Pythonic Way")
if not y:
    print("False: Pythonic Way")
if not z:
    print("None: Pythonic Way")

# What if there was an element in a list what would be the pythonic way to write it?
list_of_names = ["Ethan", "Jeff"]
# If list is not empty print "I am on the right path"




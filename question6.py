""" 6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""

my_friends = ['achin', 'jean', 'marie', 'serilia', 'hanuman', 'john']

found = False
for friend in my_friends:
    if friend == 'john':
        found = True
        break

if found: 
    print("Found")
else:
    print("Not Found")
"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""


friends = list() 
print(id(friends))

friends.append('john')
print(id(friends))

friends.append("jean")
print(id(friends)) # id does'nt change of list

friends.sort() #sorting happens in alphabetical order
print(friends)

"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""


my_tuple = ('sachin', 'maharjan', '23')
people = list()

people.append(my_tuple)

people.append(('Kathy', 'Williams', '24'))
people.append(('Raman', 'Dangol', '22'))

print(people)

#sorts according to first member of tuple
people.sort()
print(people)

#sorts according to last name
people.sort(key = lambda people: people[1])
print(people)

#sorts according to age
people.sort(key = lambda people: people[2])
print(people)


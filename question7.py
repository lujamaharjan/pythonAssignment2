"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

myfriends = [
    ('kathy', 'whilliams', 24),
    ('Mohan', 'singh', None),
    ('preeti', 'dangol', None),
    ('Amina', 'shrestha', 30),
    ('Hari', 'dangol', 35),
    ('prinyanka', 'karki', 34)
]

total_age = 0
age_known = 0
for friend in myfriends:
    if friend[2] != None:
        total_age = total_age + friend[2]
        age_known += 1

average_age = total_age / age_known


for friend in myfriends:
    if friend[2] != None:
        if friend[2] < average_age:
            print(f'{friend[0]} is a younger')
        else:
            print(f'{friend[0]} is a older')
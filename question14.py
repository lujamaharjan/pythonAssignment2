"""
14. Write a function that reads a CSV file. It should return
a list of dictionaries, using the first row as key names, and
each subsequent row as values for those keys.

For the data in the previous example it would return:
[
    {'name': 'George', 'address':'4312 Abbey Road', 'age':22}, 
    {'name': 'john', 'address': '54 love Ave', 'age': 21}
]
"""
import csv 

def read_csv(filename):
    user_data = []
    with open(filename, mode='r') as reader:
        csv_reader = csv.DictReader(reader)
        for row in csv_reader:
            user_data.append(row)

    return user_data

print(read_csv('userdetail.csv'))


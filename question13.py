"""
Write a function to write a comma-separated value(CSV) file.
It should accept a filename and a list of tuple as 
parameters. The tuples should have a name, address, and age.
The file should create a header row followed by a row for
each tuple. If the following list of tuple was passed in:
[('George', '4321 Abbey Road', 22), ('John', '54 Love Ave', 21)]
It should write the following in the file:

name, address, age
George, 4321 Abbey Road, 22
John, 54 Love Ave, 21
"""
import csv

def csv_writer(data,filename='userdetail.csv'):
    with open(filename, mode="a") as user:
        user_writer = csv.writer(user, delimiter=",")
        if isinstance(data, list):
            for tup in data:
                user_writer.writerow(tup)
        else:
            user_writer.writerow(data)
        print('sucessfull!')

csv_writer([('John', 'ktm', 23), ('Serlia', 'london', 27)])




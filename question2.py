'''2. Write an if statement to determine whether a variable holding a year
is a leap year.'''

def take_year():
    """ take input from user, return integer year"""
    return int(input("Enter a year:: "))

try:
    year = take_year()

except ValueError:
    print("Input year in number")

if year % 4 == 0 and year % 100 == 0:
    print(f'{year} is  leap year')
else:
    print(f"{year} is not a leap year")
    
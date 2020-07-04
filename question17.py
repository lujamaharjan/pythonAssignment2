"""
Write a program that serves as a basic calculator.
It asks for two numbers, then it asks for an operator. 
Gracefully deal with input that doesn't cleanly convert
to numbers. Deal with division by zero errors.
"""

class Calculator():
    is_runing = True
    def __init__(self):
        self.first = 0
        self.second = 0

    def take_numbers(self):
        try:
            self.first = float(input("Enter first number: ")) 
            self.second = float(input("Enter second number: "))
        except ValueError:
            print(" please input the numbers only !")
            self.take_numbers()

    def take_operator(self):
        self.ops = input('Enter the operator ( + , - , *, /) ::')
        if self.ops not in ['+', '-', '*', '/', 'e']:
            self.take_operator()

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    def exit(self):
        Calculator.is_runing = False

    


cal = Calculator()

while(Calculator.is_runing):
    cal.take_numbers()
    print('+ :: addition')
    print('- :: subtract')
    print('* :: multiply')
    print('/ :: division')
    print('e :: exit')
    cal.take_operator()

    if cal.ops == '+':
        result = cal.add()
        print(result)

    elif cal.ops == '-':
        result = cal.sub()
        print(result)

    elif cal.ops == '*':
        result = cal.mul()
        print(result)

    elif cal.ops == '/':
        print(cal.div())

    elif cal.ops == 'e':
        break

    print("__________________")

    




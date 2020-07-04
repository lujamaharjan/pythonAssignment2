class Parenthesis:
    def __init__(self):
        self.open_list = ['[','{','(']
        self.close_list = [']', '}', ')']

    def is_valid(self, my_str):
        stack = []
        for i in my_str:
            if i in self.open_list:
                stack.append(i)
            elif i in self.close_list:
                pos = self.close_list.index(i)
                if((len(stack)> 0 ) and self.open_list[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return "Unbalanced"

        if len(stack) == 0:
            return "Balanced"
        else: 
            return "Unbalanced"


# driver code
check = Parenthesis()
print(check.is_valid("({})"))
print(check.is_valid('()[()]'))
print(check.is_valid("((("))
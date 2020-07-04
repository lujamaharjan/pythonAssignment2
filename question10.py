"""
Write a function that takes camel-cased strings
(i.e. ThisIsCamelCased), and convert tem to snake case
(i.e. this_is_camel_cased). Modify the function by adding
an argument, separator, so it will also convert
to the kebab case(i.e.this-is-camel-case) as well. 
"""


def convert(arg, filler="_"):
    my_string = [arg[0].lower()]
    for char in arg[1:]:
        if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            my_string.append(filler)
            my_string.append(char.lower())
        else:
            my_string.append(char)

    return ''.join(my_string)

test = "MyNameIsSachin"
print(convert(test, '-'))


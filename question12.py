"""
Create a function, is_palindrome, to
determine if a supplied word is the same
if the letters are reversed.
"""

def is_palindrome(word):
    '''word: str'''
    rev_word = (reversed(word))
    rev_word = ''.join(rev_word)
    if rev_word == word:
        return True
    return False

print(is_palindrome('1x1'))

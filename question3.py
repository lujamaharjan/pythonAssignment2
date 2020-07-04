""" Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text."""

import unittest

def is_anagram(first_word, second_word):

    if set(first_word) == set(second_word):
        print(f'{first_word} and {second_word} is anagram')
        return True

    else:
        print(f'{first_word} and {second_word} is not an anagram')
        return False

# driver code
first = input('Enter First string: ')
second = input("Enter second string: ")
is_anagram(first, second)

class TestStringMethods(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_anagram('listen', 'silent'), True)

    def test_negative(self):
        self.assertFalse(is_anagram('hello', 'world'), False)

if __name__ == '__main__':
    unittest.main()

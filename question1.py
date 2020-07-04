"""
1. Create a variable, paragraph, that has the following content:
"Python is a great language!", said Fred. "I don't ever remember
having this much fun before."
"""
import unittest

paragraph = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
print(paragraph)

class TestStringMethods(unittest.TestCase):
    def test_check(self):
        self.assertEqual(paragraph, '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

if __name__ == '__main__':
    unittest.main()
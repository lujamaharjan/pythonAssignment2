""" Write a fuction, is_prime, that
takes an integer and returns True if
the number is prime and False if the
number is not prime.
"""
import unittest

def is_prime(num):
    """ num: int """
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


class CheckPrime(unittest.TestCase):
    ''' Test cases '''
    def test_positive(self):
        """ ok if 29 is prime """
        self.assertEqual(is_prime(29), True)

    def test_negative(self):
        ''' ok if 8 is not prime '''
        self.assertEqual(is_prime(8), False)


if __name__ == '__main__':
    unittest.main()

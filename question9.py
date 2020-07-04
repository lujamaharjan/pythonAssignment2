""" Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found. """

import unittest

def binary_search(sorted_list, left, right, key):

    if  right >= left:
        mid =  left + (right - left) // 2
        if (sorted_list[mid] == key):
            return mid

        elif (sorted_list[mid] > key):
            return binary_search(sorted_list,left, mid -1, key)

        else:
            return binary_search(sorted_list, mid+1, right, key)

    else:
        return -1


class BinarySearch(unittest.TestCase):
    def setUp(self):
        self.x = [1,2,3,4,5,6,7,8,9]

    def test_positive(self):
        self.assertEqual(binary_search(self.x, 0, len(self.x)-1, 7), 6)

    def  test_negative(self):
        self.assertEqual(binary_search(self.x, 0, len(self.x)-1, 10), -1)

    def tearDown(self):
        del self.x

if __name__ == '__main__':
    unittest.main()
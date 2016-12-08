import unittest
from largest_loss import find_largest_loss
import sys

range = xrange if (sys.version_info.major == 2) else range

class TestLargestLoss(unittest.TestCase):

    def test_1(self):
        test_list = [5, 4, 3, 2, 1, 0]
        largest_loss = find_largest_loss(test_list)
        self.assertEqual(largest_loss, -5)

    def test_2(self):
        test_list = [0, 1, 2, 3, 4, 5]
        largest_loss = find_largest_loss(test_list)
        self.assertEqual(largest_loss, 1)

    def test_3(self):
        test_list = [0]
        largest_loss = find_largest_loss(test_list)
        self.assertEqual(largest_loss, 0)
        
    def test_4(self):
        test_list = [i for i in range(10000)]
        largest_loss = find_largest_loss(test_list)
        self.assertEqual(largest_loss, 1)


if __name__ == '__main__':
    unittest.main()
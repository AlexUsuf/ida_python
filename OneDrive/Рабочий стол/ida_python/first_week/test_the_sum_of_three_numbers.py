import unittest
from sum import the_sum_of_three_numbers

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1,1,1), 30)
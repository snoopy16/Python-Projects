# test_listsum.py
import unittest
from Recursion.listSum import list_sum

class TestListSum(unittest.TestCase):
    def test_empty_list(self):
        """Test Empty list"""
        self.assertEqual(list_sum([]), 0)

    def test_single_element(self):
        """Test Single element in a list"""
        self.assertEqual(list_sum([5]), 5)

    def test_multiple_elements(self):
        """Test multiple elements in the list - normal case"""
        self.assertEqual(list_sum([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        """Test negative numbers in the list"""
        self.assertEqual(list_sum([-1, -2, -3, -4]), -10)

    def test_mixed_numbers(self):
        """Test mixed numbers - positive and negtives"""
        self.assertEqual(list_sum([1, -2, 3, -4, 5]), 3)

if __name__ == "__main__":
    unittest.main()
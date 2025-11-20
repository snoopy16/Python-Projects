#test_twosum.py
import unittest
from Numbers.twosum import twoSum

class TestTwoSum(unittest.TestCase):
    def test_basic_example(self):
        """Provide a list of numbers and a target, return indices of numbers summing upto the target"""
        self.assertEqual(sorted(twoSum([2, 7, 11, 15], 9)), [0, 1])

    def test_multiple_solutions(self):
        """Test when multiple solutions are possible - first occurance of target sum is returned"""
        self.assertEqual(sorted(twoSum([1, 5, 0, 6], 6)), [0, 1])

    def test_duplicate_values(self):
        """Test duplicate values. Should raise ValueError"""
        with self.assertRaises(ValueError) as e:
            twoSum([3, 3, 5], 6)
            self.assertEqual(e, "Duplicate values found in input list")

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(sorted(twoSum([-1, 0, 1], 0)), [0, 2])

    def test_no_solution(self):
        """Test when there is no solution - Should return None"""
        self.assertIsNone(twoSum([1, 2, 3], 7))

    def test_large_numbers(self):
        """Test large numbers"""
        self.assertEqual(sorted(twoSum([1000, 2000, 3000], 5000)), [1, 2])

if __name__ == "__main__":
    unittest.main()

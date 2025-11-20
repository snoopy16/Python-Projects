# test_factorial
import unittest
from Recursion.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_basic(self):
        """Test basic functionality"""
        self.assertEqual(factorial(5), 120)

    def test_factorial_one(self):
        """Test Factorial for 1"""
        self.assertEqual(factorial(1), 1)

    def test_factorial_two(self):
        """Test Factorial for two"""
        self.assertEqual(factorial(2), 2)

    def test_factorial_large(self):
        """Test factorial for a large number"""
        self.assertEqual(factorial(6), 720)

    def test_factorial_negative(self):
        """Test if ValueError is  raised for negative input (no base case)"""
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_factorial_decimal(self):
        """Test Factorial for decimal number"""
        with self.assertRaises(ValueError):
            factorial(3.5)

    def test_factorial_zero(self):
         """Test that Factorial for 0 is 1"""
         self.assertEqual(factorial(0), 1)

if __name__ == "__main__":
    unittest.main()

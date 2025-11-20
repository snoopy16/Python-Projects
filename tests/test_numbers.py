# test_numbers.py
import unittest
from Numbers.palindrome import isPalindrome

class TestIsPalindrome(unittest.TestCase):

    def test_true_palindrome(self):
        """Test if the number is a true palindrome"""
        self.assertTrue(isPalindrome(121))

    def test_false_palindrome(self):
        """Test if the number is not a palindrome"""
        self.assertFalse(isPalindrome(120))
    
    def test_single_digit(self):
        self.assertTrue(isPalindrome(7))

    def test_negative_number(self):
        self.assertFalse(isPalindrome(-121)) 

    def test_string_input_true(self):
        """Test if the input is a string"""
        self.assertTrue(isPalindrome("mom"))
    
    def test_string_input_false(self):
        """Test if the input is a string"""
        self.assertFalse(isPalindrome("mommy"))

if __name__ == '__main__':
    unittest.main()
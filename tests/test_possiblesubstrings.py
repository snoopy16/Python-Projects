# test_possiblesubstrings.py
import unittest
from StringManupulation.PossibleSubstrings import printSubstrings

class TestPrintSubstrings(unittest.TestCase):
    def test_regular_string(self):
        """Test with regular string"""
        result = printSubstrings("abcd")
        expected = [
            'a', 'ab', 'abc', 'abcd',
            'b', 'bc', 'bcd',
            'c', 'cd',
            'd'
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_character(self):
        """Test with single character"""
        result = printSubstrings("x")
        expected = ['x']
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Test with empty strings"""
        result = printSubstrings("")
        expected = []
        self.assertEqual(result, expected)

    def test_repeating_characters(self):
        "Test with repeating Characters"
        result = printSubstrings("aa")
        expected = ['a', 'aa', 'a']
        self.assertEqual(sorted(result), sorted(expected))

    def test_spaces(self):
        """Test with spaces within the strings"""
        result = printSubstrings("ab c")
        expected = [
            'a', 'ab', 'ab ', 'ab c',
            'b', 'b ', 'b c',
            ' ', ' c',
            'c'
        ]
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == "__main__":
    unittest.main()

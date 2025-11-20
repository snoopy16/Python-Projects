# test_vowelsubstrings.py
import unittest
from StringManupulation.PossibleSubstrings import printSubstrings
from StringManupulation.VowelSubstrings import vowel_substrings
# Need to import this as vowel_substrings() uses printSubStrings() utility

class TestVowelSubstrings(unittest.TestCase):
    def test_banana(self):
        """Test with banana string"""
        result = vowel_substrings("banana")
        expected = ["a", "an", "ana", "anan", "anana",
                    "a", "an", "ana",
                    "a"]  # All substrings starting at vowel positions in "banana"
        self.assertEqual(result, expected)

    def test_all_vowels(self):
        """Test with string containing all vowels"""
        result = vowel_substrings("ae")
        expected = ["a", "ae", "e"]
        self.assertEqual(result, expected)

    def test_all_consonants(self):
        """Test with string containing all consonents"""
        result = vowel_substrings("bcdfg")
        expected = []
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Test with empty string"""
        result = vowel_substrings("")
        expected = []
        self.assertEqual(result, expected)

    def test_mixed_case(self):
        """Test with mixed case - Upper + Lower. Result will be all lower"""
        result = vowel_substrings("Apple".lower())
        expected = ["a", "ap", "app", "appl", "apple", "e"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
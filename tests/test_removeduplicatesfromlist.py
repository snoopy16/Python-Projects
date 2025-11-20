# test_removeduplicatesfromlist.py
import unittest
from Numbers.removeduplicatesfromlist import removeDuplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        """Test when duplicates exist in the list"""
        self.assertEqual(removeDuplicates([1,2,2,3,4,4,5]), [1,2,3,4,5])

    def test_all_unique(self):
        """Test when no duplicates exists in the list"""
        self.assertEqual(removeDuplicates([1,2,3,4,5]), [1,2,3,4,5])

    def test_all_duplicates(self):
        """Test when only one unique value remains"""
        self.assertEqual(removeDuplicates([1,1,1,1]), [1])  

    def test_empty_list(self):
        """Test when there are no elements"""
        self.assertEqual(removeDuplicates([]), [])

    def test_mixed_types(self):
        """Test with strings and numbers"""
        self.assertEqual(removeDuplicates([1,'1',1,'1']), [1,'1'])

    def test_bad_input(self):
        """Test when we pass single number or string instead of a list"""
        with self.assertRaises(AttributeError) as e:
            removeDuplicates(5)

if __name__ == '__main__':
    unittest.main()
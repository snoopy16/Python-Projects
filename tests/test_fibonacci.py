# test_fibonacci.py
import unittest
from Recursion.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_10(self):
        n_terms = 10
        series = [fibonacci(i) for i in range(n_terms)]
        self.assertEqual(series, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == "__main__":
    unittest.main()

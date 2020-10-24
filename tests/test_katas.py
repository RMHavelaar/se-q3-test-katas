__author__ = "Robert Havelaar"

import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        """Tests add function """
        self.assertEqual(katas.add(1, 1), 2)
        self.assertEqual(katas.add(0, 0), 0)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        """Tests multiply function """
        self.assertEqual(katas.multiply(1, 1), 1)
        self.assertEqual(katas.multiply(1, 0), 0)
        self.assertEqual(katas.multiply(-1, 0), 0)
        self.assertEqual(katas.multiply(-1, -1), 1)
        self.assertEqual(katas.multiply(2, -1), -2)

    def test_power(self):
        """Tests power function """
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(0, 2), 0)
        # self.assertEqual(katas.power(2, 0), 1)
        # self.assertEqual(katas.power(-2, 0), -1)
        self.assertEqual(katas.power(-2, 2), 4)
        # self.assertEqual(katas.power(-2, -2), -0.25)
        # self.assertEqual(katas.power(2, -2), -0.25)
        # self.assertEqual(katas.power(0, 0), 1)

    def test_factorial(self):
        """Tests factorial function """
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(10), 3628800)
        # self.assertEqual(katas.factorial(0), 1)
        # self.assertEqual(ValueError, katas.factorial, -1)

    def test_fibonacci(self):
        """Tests fibonacci function """
        self.assertEqual(katas.fibonacci(1), 0)
        self.assertEqual(katas.fibonacci(2), 1)
        self.assertEqual(katas.fibonacci(3), 1)
        self.assertEqual(katas.fibonacci(4), 2)
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(70), 117669030460994)


if __name__ == '__main__':
    unittest.main()
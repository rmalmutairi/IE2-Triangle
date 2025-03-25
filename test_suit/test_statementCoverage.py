import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):
    def test_negative_side(self):
        # Check an invalid side
        result = Triangle.classify(-1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_zero_side(self):
        # Another invalid side
        result = Triangle.classify(0, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_inequality_equal(self):
        # (a + b) == c => INVALID
        result = Triangle.classify(2, 3, 5)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_equilateral(self):
        result = Triangle.classify(5, 5, 5)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        result = Triangle.classify(2, 2, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_scalene(self):
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)

if __name__ == '__main__':
    unittest.main()
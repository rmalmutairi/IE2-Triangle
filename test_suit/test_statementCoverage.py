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
    def test_isosceles_ac_valid(self):
        """
        trian == 2 => a == c, sum > b => triggers line:
            elif trian == 2 and a + c > b:
        => ISOSCELES
        """
        result = Triangle.classify(4, 3, 4)  # a==c=4, sum=8 > b=3
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_isosceles_ac_invalid(self):
        """
        trian == 2 => a == c, but sum <= b => final return INVALID
        """
        result = Triangle.classify(4, 8, 4)  # a==c=4, sum=8 == b=8 => NOT strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_isosceles_bc_valid(self):
        """
        trian == 3 => b == c, sum > a => triggers line:
            elif trian == 3 and b + c > a:
        => ISOSCELES
        """
        result = Triangle.classify(5, 4, 4)  # b==c=4, sum=8 > a=5
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_isosceles_bc_invalid(self):
        """
        trian == 3 => b == c, but sum <= a => final return INVALID
        """
        result = Triangle.classify(9, 4, 4)  # b==c=4, sum=8 < a=9 => NOT strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
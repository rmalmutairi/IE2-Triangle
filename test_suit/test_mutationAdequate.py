import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):

    # Invalid side checks
    def test_side_negative(self):
        self.assertEqual(Triangle.classify(-1, 2, 3), Triangle.Type.INVALID)

    def test_side_zero(self):
        self.assertEqual(Triangle.classify(0, 3, 3), Triangle.Type.INVALID)

    # Triangle inequality edge: a+b == c => INVALID
    def test_inequality_equal(self):
        self.assertEqual(Triangle.classify(2, 3, 5), Triangle.Type.INVALID)

    # a+b < c => INVALID
    def test_inequality_less(self):
        self.assertEqual(Triangle.classify(2, 2, 5), Triangle.Type.INVALID)

    # SCALENE
    def test_scalene(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    # EQUILATERAL
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)

    # ISOSCELES edges
    def test_isosceles_ab_valid(self):
        # a == b
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)

    def test_isosceles_ab_invalid(self):
        # a == b but a+b == c => not strictly greater => INVALID
        self.assertEqual(Triangle.classify(2, 2, 4), Triangle.Type.INVALID)

    def test_isosceles_ac_valid(self):
        # a == c
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)

    def test_isosceles_ac_invalid(self):
        # a == c but a+c == b => invalid
        self.assertEqual(Triangle.classify(2, 4, 2), Triangle.Type.INVALID)

    def test_isosceles_bc_valid(self):
        # b == c
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)

    def test_isosceles_bc_invalid(self):
        # b == c but b+c == a => invalid
        self.assertEqual(Triangle.classify(4, 2, 2), Triangle.Type.INVALID)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()

import unittest
from isTriangle import Triangle

class TestDecisionCoverage(unittest.TestCase):

    # 1) a <= 0 or b <= 0 or c <= 0 => True
    def test_side_negative(self):
        result = Triangle.classify(-1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    # 2) a <= 0 or b <= 0 or c <= 0 => False
    def test_sides_positive(self):
        # Here we also might catch the next if for T or F...
        result = Triangle.classify(1, 2, 3)  
        # 1 + 2 == 3 => INVALID
        self.assertEqual(result, Triangle.Type.INVALID)

    # Test a condition where no sides are equal => trian == 0
    # "if trian == 0: if (a+b <= c or ...)"
    #  => True path => INVALID
    def test_trian_0_invalid(self):
        result = Triangle.classify(2, 2, 4)
        # 2 + 2 == 4 => INVALID
        self.assertEqual(result, Triangle.Type.INVALID)

    # Test the same "trian == 0" block => else => SCALENE
    def test_trian_0_scalene(self):
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)

    # Check trian > 3 => all sides equal => EQUILATERAL
    def test_trian_greater_than_3(self):
        result = Triangle.classify(5, 5, 5)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    # Check trian == 1 => a == b => ISOSCELES if sum > c
    def test_trian_eq_1_isosceles(self):
        result = Triangle.classify(2, 2, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    # Force the branch where trian == 1 but sum is NOT > c => INVALID
    def test_trian_eq_1_invalid(self):
        result = Triangle.classify(2, 2, 4)  # 2+2=4 => Not strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)

    # Similarly for trian == 2 => (a == c)
    def test_trian_eq_2_isosceles(self):
        result = Triangle.classify(2, 3, 2)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    # Sum not greater => INVALID
    def test_trian_eq_2_invalid(self):
        result = Triangle.classify(2, 4, 2)  # 2+2=4 => Not strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)

    # trian == 3 => (b == c)
    def test_trian_eq_3_isosceles(self):
        result = Triangle.classify(3, 2, 2)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    # trian == 3 => sum fail => INVALID
    def test_trian_eq_3_invalid(self):
        result = Triangle.classify(4, 2, 2)  # 2+2=4 => Not strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_isosceles_ac_valid(self):
        result = Triangle.classify(4, 5, 4)  # a=4, c=4, b=5 => 4+4=8 > 5
        self.assertEqual(result, Triangle.Type.ISOSCELES)
    
    def test_isosceles_ac_invalid(self):
        result = Triangle.classify(4, 8, 4)  # 4+4=8 => equals b, not strictly greater
        self.assertEqual(result, Triangle.Type.INVALID)
    
    def test_isosceles_bc_valid(self):
        result = Triangle.classify(5, 4, 4)  # b=4, c=4 => 4+4=8 > a=5
        self.assertEqual(result, Triangle.Type.ISOSCELES)
    
    def test_isosceles_bc_invalid(self):
        result = Triangle.classify(9, 4, 4)  # b=4, c=4 => 4+4=8 < a=9
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_isosceles_ac_true(self):
        # a == c, sum > b => ISOSCELES (trian == 2)
        self.assertEqual(Triangle.classify(5, 3, 5), Triangle.Type.ISOSCELES)

    def test_isosceles_ac_false(self):
        # a == c, but sum <= b => trian==2 but fails sum => INVALID
        self.assertEqual(Triangle.classify(4, 8, 4), Triangle.Type.INVALID)

    def test_isosceles_bc_true(self):
        # b == c, sum > a => ISOSCELES (trian == 3)
        self.assertEqual(Triangle.classify(3, 5, 5), Triangle.Type.ISOSCELES)

    def test_isosceles_bc_false(self):
        # b == c, but sum <= a => INVALID
        self.assertEqual(Triangle.classify(9, 4, 4), Triangle.Type.INVALID)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

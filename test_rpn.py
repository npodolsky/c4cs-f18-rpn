import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)

    def test_mul(self):
        result = rpn.calculate('2 3 *')
        self.assertEqual(6, result)

    def test_div(self):
        result = rpn.calculate('4 2 /')
        self.assertEqual(2, result)

    def test_exponentiation(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)

    def test_integerdiv(self):
        result = rpn.calculate('5 2 //')
        self.assertEqual(2, result)

    def test_percent(self):
        result = rpn.calculate('10 50 %')
        self.assertEqual(5, result)

    def test_div_by_0(self):
        result = rpn.calculate('4 3 - 0 /')
        self.assertEqual(1, result)

    def test_summation(self):
        result = rpn.calculate('2 3 4 5 s')
        self.assertEqual(14, result)

    def test_factorial(self):
        result = rpn.calculate ('2 2 + !')
        self.assertEqual(24, result)

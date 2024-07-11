import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(3, -5), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 5), -3)
        self.assertEqual(self.calc.subtract(3, -5), 8)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(3, -5), -15)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(5163521, 0), 0)
    def test_division(self):
        self.assertEqual(self.calc.multiply(3, 3), 1)
        self.assertEqual(self.calc.multiply(9, 3), 3)
        self.assertEqual(self.calc.multiply(3, -3), -1)
        self.assertEqual(self.calc.multiply(9, -3), -3)
        self.assertEqual(self.calc.multiply(3, -3), -1)
        self.assertEqual(self.calc.multiply(9, -3), -3)
        self.assertEqual(self.calc.multiply(4, 8), 0.5)
        self.assertEqual(self.calc.multiply(0, 0), None)
        self.assertEqual(self.calc.multiply(5163521, 0), None)

if __name__ == '__main__':
    unittest.main()
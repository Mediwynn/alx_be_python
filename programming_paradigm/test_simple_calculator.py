import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    
    def add(a, b):
        self.assertEqual(SimpleCalculator.add(3, 5), 8)
        self.assertEqual(SimpleCalculator.add(3, -5), -2)
        self.assertEqual(SimpleCalculator.add(0, 0), 0)

    def subtract(a, b):
        self.assertEqual(SimpleCalculator.subtract(3, 5), -3)
        self.assertEqual(SimpleCalculator.subtract(3, -5), 8)
        self.assertEqual(SimpleCalculator.subtract(0, 0), 0)

    def multiply(a, b):
        self.assertEqual(SimpleCalculator.multiply(3, 5), 15)
        self.assertEqual(SimpleCalculator.multiply(3, -5), -15)
        self.assertEqual(SimpleCalculator.multiply(0, 0), 0)
        self.assertEqual(SimpleCalculator.multiply(5163521, 0), 0)
    def divide(a, b):
        self.assertEqual(SimpleCalculator.multiply(3, 3), 1)
        self.assertEqual(SimpleCalculator.multiply(9, 3), 3)
        self.assertEqual(SimpleCalculator.multiply(3, -3), -1)
        self.assertEqual(SimpleCalculator.multiply(9, -3), -3)
        self.assertEqual(SimpleCalculator.multiply(3, -3), -1)
        self.assertEqual(SimpleCalculator.multiply(9, -3), -3)
        self.assertEqual(SimpleCalculator.multiply(4, 8), 0.5)
        self.assertEqual(SimpleCalculator.multiply(0, 0), None)
        self.assertEqual(SimpleCalculator.multiply(5163521, 0), None)

if __name__ == '__main__':
    unittest.main()
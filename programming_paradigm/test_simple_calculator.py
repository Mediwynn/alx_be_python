import unittest
from simple_calculator import SimpleCalculator

class test(unittest.TestCase):
    def add(a, b):
        result = a + b
        return result

    def subtract(a, b):
        result = a - b
        return result

    def multiply(a, b):
        result = a * b
        return result

    def divide(a, b):
        if b != 0:
            result = a / b
            return result
        else:
            return f"Error cannot divide by zero."
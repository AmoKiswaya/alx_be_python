import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(-1, 1), 0) 

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15) 

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)  
        self.assertEqual(self.calc.divide(-6, 3), -2)  
        self.assertIsNone(self.calc.divide(5, 0)) 

if __name__ == "__main__":
    unittest.main() 
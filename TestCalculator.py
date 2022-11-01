import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()

    def test_add(self):
        self.assertEqual(self.cal.add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(6, 2), 4)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(self.cal.divide(82, 16), 5.125)

    def test_step(self):
        self.assertEqual(self.cal.step(4, 2), 16)


if __name__ == '__main__':
    unittest.main()

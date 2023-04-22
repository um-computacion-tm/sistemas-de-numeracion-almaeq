from decim_a_todos import decim_to_bin, decim_to_octal, decim_to_hexa
from parameterized import parameterized, parameterized_class
import unittest

class TestDecimToBin(unittest.TestCase):
    @parameterized.expand([
        (97,"01100001"),
        (25,"00011001"),
        (567, "0000001000110111")
    ])
    def test(self, num, decimal):
        self.assertEqual(decim_to_bin(num),decimal)

class TestDecimToOctal(unittest.TestCase):
    @parameterized.expand([
        (49,"61"),
        (340, "524")
    ])
    def test(self, num, decimal):
        self.assertEqual(decim_to_octal(num),decimal)

class TestDecimToHexa(unittest.TestCase):
    @parameterized.expand([
        (128,"80"),
        (79,"4F"),
        (230,"E6")
    ])
    def test(self, num, decimal):
        self.assertEqual(decim_to_hexa(num),decimal)

if __name__ == '__main__':
    unittest.main()
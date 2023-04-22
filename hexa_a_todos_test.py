from hexa_a_todos import hexa_to_decim, hexa_to_bin, hexa_to_octal
from parameterized import parameterized, parameterized_class
import unittest

class TestHexaToDecim(unittest.TestCase):
    @parameterized.expand([
        ("C",12),
        ("E6",230),
        ("28",40)
    ])
    def test(self, num, hexa):
        self.assertEqual(hexa_to_decim(num),hexa)

class TestHexaToBin(unittest.TestCase):
    @parameterized.expand([
        ("D","1101"),
        ("F7","11110111"),
        ("101","000100000001")
    ])
    def test(self, num, hexa):
        self.assertEqual(hexa_to_bin(num),hexa)

class TestHexaToOctal(unittest.TestCase):
    @parameterized.expand([
        ("E","16"),
        ("D6CB","153313"),
        ("C9B4", "144664")
    ])
    def test(self, num, hexa):
        self.assertEqual(hexa_to_octal(num),hexa)

if __name__ == '__main__':
    unittest.main()
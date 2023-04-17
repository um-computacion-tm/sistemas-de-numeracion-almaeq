from bin_a_todos import bin_to_decim, bin_to_octal, bin_to_hexa
from parameterized import parameterized, parameterized_class
import unittest

class TestBinToDecim(unittest.TestCase):
    @parameterized.expand([
        ("01011100",92),
        ("10001001", 137)
    ])
    def test(self, num, binario):
        self.assertEqual(bin_to_decim(num),binario)

class TestBinToOctal(unittest.TestCase):
    @parameterized.expand([
        ("00111111","77"),
    ])
    def test(self, num, binario):
        self.assertEqual(bin_to_octal(num),binario)

class TestBinToHexa(unittest.TestCase):
    @parameterized.expand([
        ("001001010100","254"),
    ])
    def test(self, num, binario):
        self.assertEqual(bin_to_hexa(num),binario)


if __name__ == '__main__':
    unittest.main()
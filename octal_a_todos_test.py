from octal_a_todos import octal_to_decim, octal_to_bin, octal_to_hexa
from parameterized import parameterized, parameterized_class
import unittest

class TestOctalToDecim(unittest.TestCase):
    @parameterized.expand([
        ("67", 55 ),
        ("122", 82),
        ("375", 253)
    ])
    def test(self, num, octal):
        self.assertEqual(octal_to_decim(num),octal)

class TestOctalToBin(unittest.TestCase):
    @parameterized.expand([
        ("532", "101011010"),
        ("342", "011100010"),
        ("24", "010100")
    ])
    def test(self, num, octal):
        self.assertEqual(octal_to_bin(num),octal)

class TestOctalToHexa(unittest.TestCase):
    @parameterized.expand([
        ("24","14"),
        ("123","53")
        ])
    def test(self, num, octal):
        self.assertEqual(octal_to_hexa(num),octal)

if __name__ == '__main__':
    unittest.main()
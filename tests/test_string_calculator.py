import unittest
import sys
import os

# Add the parent directory (one level up) to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newline_as_delimiter(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3,-4")
        self.assertIn("Negatives not allowed", str(context.exception))

    def test_ignore_large_numbers(self):
        self.assertEqual(self.calc.add("2,1001,6"), 8)

    def test_delimiter_of_any_length(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_multi_char_delimiters(self):
        self.assertEqual(self.calc.add("//[***][#][%]\n1***2#3%4"), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)

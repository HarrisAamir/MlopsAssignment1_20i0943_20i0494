import unittest
from model import getLabel


class TestMyFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(getLabel("Credit card number is not valid"), "spam")
        self.assertEqual(getLabel("Amount credited with 1000$"), "spam")
        self.assertEqual(getLabel("New account created"), "ham")
        self.assertEqual(getLabel("your account was deactivated"), "spam")


if __name__ == '__main__':
    unittest.main()

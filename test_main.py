import unittest
from main import add_numbers

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(), 15)

if __name__ == "__main__":
    unittest.main()

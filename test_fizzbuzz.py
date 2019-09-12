import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

  def test_return_number_1(self):
        result = fizzbuzz.fizzbuzz(1)
        self.assertEqual(result,1)


if __name__ == '__name__':
    unittest.main()

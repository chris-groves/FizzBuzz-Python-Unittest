import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

  def test_return_number_1(self):
        result = fizzbuzz.fizzbuzz(1)
        self.assertEqual(result,1)

  def test_return_fizz_for_number_3(self):
        result = fizzbuzz.fizzbuzz(3)
        self.assertEqual(result,'Fizz')

  def test_return_fizz_for_multiple_of_3(self):
        result = fizzbuzz.fizzbuzz(9)
        self.assertEqual(result, 'Fizz')


if __name__ == '__name__':
    unittest.main()

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

  def test_return_buzz_for_number_5(self):
       result = fizzbuzz.fizzbuzz(5)
       self.assertEqual(result, 'Buzz')

  def test_return_buzz_for_multiple_of_5(self):
      result = fizzbuzz.fizzbuzz(10)
      self.assertEqual(result, 'Buzz')

  def test_return_fizzbuzz_for_15(self):
      result = fizzbuzz.fizzbuzz(15)
      self.assertEqual(result, 'Fizzbuzz')

  def test_return_fizzbuzz_for_30(self):
      result = fizzbuzz.fizzbuzz(30)
      self.assertEqual(result, 'Fizzbuzz')

  def test_return_number_for_7(self):
      result = fizzbuzz.fizzbuzz(7)
      self.assertEqual(result, 7)

if __name__ == '__name__':
    unittest.main()

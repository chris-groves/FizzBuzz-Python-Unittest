import unittest
from fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):

  def test_return_number_1(self):
        fizzbuzz = Fizzbuzz()
        result = fizzbuzz.fizzbuzz_number(1)
        self.assertEqual(result,1)

  def test_return_fizz_for_number_3(self):
        fizzbuzz = Fizzbuzz()
        result = fizzbuzz.fizzbuzz_number(3)
        self.assertEqual(result,'Fizz')

  def test_return_fizz_for_multiple_of_3(self):
        fizzbuzz = Fizzbuzz()
        result = fizzbuzz.fizzbuzz_number(9)
        self.assertEqual(result, 'Fizz')

  def test_return_buzz_for_number_5(self):
       fizzbuzz = Fizzbuzz()
       result = fizzbuzz.fizzbuzz_number(5)
       self.assertEqual(result, 'Buzz')

  def test_return_buzz_for_multiple_of_5(self):
      fizzbuzz = Fizzbuzz()
      result = fizzbuzz.fizzbuzz_number(10)
      self.assertEqual(result, 'Buzz')

  def test_return_fizzbuzz_for_15(self):
      fizzbuzz = Fizzbuzz()
      result = fizzbuzz.fizzbuzz_number(15)
      self.assertEqual(result, 'Fizzbuzz')

  def test_return_fizzbuzz_for_30(self):
      fizzbuzz = Fizzbuzz()
      result = fizzbuzz.fizzbuzz_number(30)
      self.assertEqual(result, 'Fizzbuzz')

  def test_return_number_for_7(self):
      fizzbuzz = Fizzbuzz()
      result = fizzbuzz.fizzbuzz_number(7)
      self.assertEqual(result, 7)

  def test_array_element_0_returns_1(self):
      fizzbuzz = Fizzbuzz()
      fizzbuzz.loop()
      result = fizzbuzz.array[0]
      self.assertEqual(result, 1)

  def test_array_element_99_returns_fizz(self):
      fizzbuzz = Fizzbuzz()
      fizzbuzz.loop()
      result = fizzbuzz.array[99]
      self.assertEqual(result, 'Buzz')

  def test_array_element_2_returns_fizz(self):
      fizzbuzz = Fizzbuzz()
      fizzbuzz.loop()
      result = fizzbuzz.array[2]
      self.assertEqual(result, 'Fizz')

  def test_array_element_46_returns_fizzbuzz(self):
     fizzbuzz = Fizzbuzz()
     fizzbuzz.loop()
     result = fizzbuzz.array[44]
     self.assertEqual(result, 'Fizzbuzz')

if __name__ == '__main__':
    unittest.main()

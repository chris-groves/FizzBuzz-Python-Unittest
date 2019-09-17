class Fizzbuzz:
    def __init__(self):
        self.array = []

    def fizzbuzz_number(self, number):
      if number % 3 == 0 and number % 5 == 0:
        return 'Fizzbuzz'
      elif number % 3 == 0:
        return 'Fizz'
      elif number % 5 == 0:
        return 'Buzz'
      else:
        return number

    def loop(self):
      x = 1
      while x < 101:
        self.array.append(x)
        x += 1

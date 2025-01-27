# Task1
# O(1)
digit = 2
digit_1 = 8


def minimum(number: int, number_1: int) -> int:
  """
  Returns the smaller of numbers.
  """
  if number < number_1:
    return number
  else:
    return number_1

result = minimum(number= digit, number_1= digit_1)
print(f"result: {result}")

# Task2
# O(1)
number = 4
number_1 = 10
number_2 = 7
number_3 = 18

min_1 = minimum(number, number_1)
min_2 = minimum(number_2, number_3)
result = minimum(min_1, min_2)

print(f"result: {result}")

# Task3
# O(1)
point = 3
point1 = 6
point2 = -5
point3 = -10


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
  """
  Calculates the distance between two points in a 2D plane.
  """
  dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
  return dist

dist = distance(x1 = point, y1 = point1, x2 = point2, y2 = point3)
print(f"distance: {dist}")

# Task4
# O(N)
def determine_prime_number(number: int) -> bool:
  """
  This function determines prime number.
  """
  counter = 0
  for el in range(1, number + 1):
    if number % el == 0:
        counter += 1
  if counter > 2:
      return "NO"
  return "YES"

number = int(input("number:"))
print(f"number {number}: {determine_prime_number(number=number)}")

# Task5
# O(N)
def fibonacci(n) -> int:
  """
  :param n: A non-negative integer.
  :return: The n-th fibonacci number.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
      num = 0
      num1 = 1
      for _ in range(2, n +1):
        num2 = num + num1
        num = num1
        num1 = num2
      return num1

n = int(input("n:"))
result = fibonacci(n)
print(f"fibonacci: {result}")

# Task6
# O(1)
def closest_mod_5(number: int) -> int:
  """
  :param number: An integer.
  :return: The smallest integer result that is greater or equal to number, and it is divisible by 5.
  """
  result = number % 5
  if result == 0:
    return number
  else:
    return number + (5 - result)

number = int(input("number:"))
result = closest_mod_5(number)
print(result)
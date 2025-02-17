# Task1
# O(1)
class RangeSquared:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        square = self.current ** 2
        self.current += 1
        return square

# Example
number = RangeSquared(3, 15)
for elem in number:
    print(elem)

# Task2
# O(N)
def factorial_gen(n:int | float):
    factorial = 1
    for elem in range(n + 1):
        yield factorial
        factorial *= (elem + 1)

# Example
for elem in factorial_gen(int(float(input()))):
    print(elem)

# Task3
# O(N)
def read_file_lines(filename:str):
    filename = "file.txt"
    encoding = "utf-8"
    mode = "r"

    try:
        with open(filename, mode=mode, encoding=encoding) as file:
            for line in file:
                yield line.rstrip()
    except FileNotFoundError:
        print(f"File {filename} is not found.")
    except Exception as e:
        print(f"Error: {e}.")

# Example
for line in read_file_lines("file.txt"):
    print(line)

# Task4
def calculate_complex_formula(a, b, c, d, e, f, g, h):
    result = 0

    result += calculate_term1(a, b, c, d, e)
    result += calculate_term2(f, g, h, d)

    return result

def calculate_term1(a, b, c, d, e):
    if a > 0:
        return b * c
    return -d / e

def calculate_term2(f, g, h, d):
     if g < h:
        return f * (g + h)
     return - (d - f) / g

# Task5
class User:
    adult_age = 18
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def greet(self):
        greeting = self._get_greeting()
        print(greeting)

    def _get_greeting(self) -> str:
        if self.age >= self.adult_age:
            print(f"Привет, {self.name}! Добро пожаловать на сайт для взрослых.")
        else:
            print(f"Привет, {self.name}! Добро пожаловать на детский сайт.")

user1 = User("Алекс", 25)
user1.greet()

user2 = User("Лиза", 12)
user2.greet()






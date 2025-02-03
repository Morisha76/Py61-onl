# Task1
# O(N)
print([number for number in range(10, 100) if number % 2 == 1])

# Task2
# O(N)
print([number**2 for number in range(1, 11)])

# Task3
# O(N)
print([number for number in range(100, 1000) if number % 5 == 0 and number % 3 == 0])

# Another_variant
print([number for number in range(100, 1000) if number % 15 == 0])

# The_third_variant
print([number for number in range(105, 1000, 15)])

# Task4
# O(N)
line = input()
numbers = line.split()
start = int(numbers[0])
end = int(numbers[1])
degree = int(numbers[2])

print([number ** degree for number in range(start, end + 1)])

# The_simple_variant
print([number ** 3 for number in range(5, 13)])

# Task5
# O(N)
line = input()
numbers = line.split()

print(list(filter(lambda number: '0' in number, numbers)))

# Task6
# O(N)
line = input()
words = line.split()

print(list(filter(lambda word: word.count('a') > 2, words)))

# Another_variant
words = input().split()

print([word for word in words if word.count('a') > 2])

# Task7
# O(N^2)
line = input()
words = line.split()

print(list(map(lambda word: word.upper(), words)))

# Task8
# O(N^2)
strings = input().split()

print(list(map(lambda string: ''.join(number for number in string if not number.isdigit()), strings)))

# Another_variant
strings = input().split()

def remove_digits(string):
    return ''.join(number for number in string if not number.isdigit())

print(list(map(remove_digits, strings)))

Additional_tasks
Task9
O(N)
numbers = input()
unique_numbers = list(map(int, numbers.split()))
seen = set()
duplicates = set()

for num in unique_numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)

# Task10
# O(N^2)
def prime_number(num: int) -> bool:
    if num < 1:
        return False
    for el in range(2, int(num**0.5) + 1):
        if num % el == 0:
            return False
    return True

def prime_generator(number: int):
    return filter(prime_number, range(2, number))

print(list(prime_generator(100)))

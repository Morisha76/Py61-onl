# Task1
# O(1) - ?
number = int(input("enter number:"))
elem = 1
while elem * elem < number:
    print(elem * elem, end=" ")
    elem += 1
print()

# Task2
# O(log n)
number = int(input("enter number:"))
while number >= 10:
    number //= 10
first_digit = number

print(first_digit)

# Task3
# O(log n)
number = int(input("enter number:"))
min_digit = 9
if number == 0:
    min_digit = 0
else:
    while number > 0:
        min_digit_1 = number % 10
        min_digit = min(min_digit, min_digit_1)
        number //= 10

print(min_digit)

# Task4
some_str = "My_program"  # O(1)
print(some_str[2])  # O(1)
print(some_str[-2])  # O(1)
print(some_str[0:5])  # O(1)
print(some_str[:-3])  # O(N)
print(some_str[::2])  # O(N)
print(some_str[1::2])  # O(N)
print(some_str[::-1])  # O(N)
print(some_str[::-2])  # O(N)
print(len(some_str))  # O(1)

# Task5
# O(N)
some_str = "My_program"
result = some_str.split("_")
reversed_result = result[::-1]
reversed_some_str = "_".join(reversed_result)
print(reversed_some_str)

# Task6
# O(N)
some_str = "deed"
reversed_some_str = some_str[::-1]
if some_str == reversed_some_str:
    print("True")
else:
    print("False")

# Another_variant
some_str = "world"
reversed_some_str = some_str[::-1]
if some_str == reversed_some_str:
    print("True")
else:
    print("False")

# Task7
# O(N)
some_str = "fluffy"
f_index = []
for el, letter in enumerate(some_str):
    if letter == "f":
        f_index.append(el)
if len(f_index) == 1:
    print(f_index[0])
elif len(f_index) > 1:
    print(f_index[0], len(f_index))

# Another_variant
some_str = "floor"
f_index = []
for el, letter in enumerate(some_str):
    if letter == "f":
        f_index.append(el)
if len(f_index) == 1:
    print(f_index[0])
elif len(f_index) > 1:
    print(f_index[0], len(f_index))

# The_third_variant
some_str = "pet"
f_index = []
for el, letter in enumerate(some_str):
    if letter == "f":
        f_index.append(el)
if len(f_index) == 1:
    print(f_index[0])
elif len(f_index) > 1:
    print(f_index[0], len(f_index))

# Task8
# O(N^2)
list_1 = [1, 6, 8, 25, 74, 29]
list_2 = [4, 7, 10, 56, 29, 8]
unique_digit = []
for el in list_1:
    if el not in list_2:
        unique_digit.append(el)
if not unique_digit:
    print("None")
else:
    unique_digit = min(unique_digit)
    print(unique_digit)

# Task9
# O(N)
numbers = [13, 43, 88, 97, 36]
count1 = 0
for el in numbers:
    tens = el // 10
    units = el % 10

    if tens > units:
        count1 += 1

print(count1)

# Task10
# O(N^2)
some_str = input("enter str:")
add_lst = []
result = []
for add in some_str:
    if add not in add_lst:
        add_lst.append(add)
        result.append(add)

print("".join(result))

# Tasks_with_if
# Task1
number = 243
number_str = str(number)
last_digit_str = number_str[2]
last_digit = int(last_digit_str)
if last_digit == 3:
    print("True")
else:
    print("False")

# If_the_criterion_does_not_work

number = 761
number_str = str(number)
last_digit_str = number_str[2]
last_digit = int(last_digit_str)
if last_digit == 3:
    print("True")
else:
    print("False")

# Task2
number_1, number_2, number_3 = 54, -35, 607
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print("True")
else:
    print("False")

# If_the_criterion_does_not_work
number_1, number_2, number_3 = 68, 3, 12
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print("True")
else:
    print("False")

# Task3
number_1, number_2 = 34, 88
if ((number_1 % 2 == 0 and number_2 % 2 == 0) or
        (number_1 % 2 != 0 and number_2 % 2 != 0)):
    print("True")
else:
    print("False")

# If_the_criterion_does_not_work
number_1, number_2 = 45, 92
if ((number_1 % 2 == 0 and number_2 % 2 == 0) or
        (number_1 % 2 != 0 and number_2 % 2 != 0)):
    print("True")
else:
    print("False")

# Task4
side_a, side_b, side_c = 15, 15, 25
if side_a == side_b == side_c:
    print("equilateral")
elif side_a == side_b or side_b == side_c or side_c == side_a:
    print("isosceles")
else:
    print("scalene")

# Task5
number_1 = 22
number_2 = 53
number_3 = 92
even_count = ((1 if number_1 % 2 == 0 else 0) +
              (1 if number_2 % 2 == 0 else 0) +
              (1 if number_3 % 2 == 0 else 0))
print(even_count)

# Task6
number = 87
if (8 + 7) > 10:
    print("two-digit")
else:
    print("one-digit")

# Another_number
number1 = 35
if (3 + 5) > 10:
    print("two-digit")
else:
    print("one-digit")

# Task7
number = "1007"
number_str = str(number)
digit_1 = number_str[0]
digit_2 = number_str[1]
digit_3 = number_str[2]
digit_4 = number_str[3]
if len(number) != 4:
    print("False")
elif digit_1 == digit_2 == digit_3 == digit_4:
    print("True")
else:
    print("False")

# Another_variant
number = "1111"
number_str = str(number)
digit_1 = number_str[0]
digit_2 = number_str[1]
digit_3 = number_str[2]
digit_4 = number_str[3]
if len(number) != 4:
    print("False")
elif digit_1 == digit_2 == digit_3 == digit_4:
    print("True")
else:
    print("False")

# Task8
year = 2004
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap_year")
else:
    print("Non_leap_year")

# Another_variant
year = 1997
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap_year")
else:
    print("Non_leap_year")

# Tasks_with_for
# Task9
for _ in range(20):
    print("10")

# Task10
for elem in range(20, 31):
    print(elem)

# Task11
for elem in range(100, -101, -1):
    print(elem, end=" ")

# Task12
summa = 0
for elem in range(100, 501):
    summa += elem
    print(f"summa = {summa}")

# Task13
a = 1
for elem in range(5, 21):
    a *= elem
print(f"a = {a}")

# Task14
n = 8
factorial = 1
for elem in range(1, n + 1):
    factorial *= elem
print(f"8! = {factorial}")

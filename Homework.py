# Task1
print (17/2*3+2)
print (2+17/2*3)
print (19%4+15/2*3)
print (15+6-10*4)
print (17/2%2*3**3)

# Task2
print (17/2*(3+2))
print ((2+17)/2*3)
print (19%(4+15)/(2*3))
print ((15+6-10)*4)
print ((17/2)%(2*3**3))

# Task3
total_amount_of_money = 11
bread_price = 1.50
loaf_of_bread = 3

spent_money = bread_price * loaf_of_bread
money_left = total_amount_of_money - spent_money

print (money_left)

# Task4
apples_1 = 2
apples_2 = 5

print(apples_1 , apples_2)

# Task5
days = 5
print(f"days = {days} = hours = {days * 24} = minutes = {days * 24 * 60} = seconds = {days * 24 * 60 * 60}")

# Task6
days = 182
print (f"weeks = {days / 7}")

# Additional_tasks
# Task7
side_1 = 150
side_2 = 65
square_side = 30

square_along_side_1 = side_1 // square_side
square_along_side_2 = side_2 // square_side
total_squares = square_along_side_1 * square_along_side_2

print(f"squares = {total_squares}")

# Task8
seconds_1 = 4000

hours = seconds_1 // 3600
seconds_2 = seconds_1 % 3600
minutes = seconds_2 // 60
seconds = seconds_2 % 60

print(f"hours = {hours}")
print(f"minutes = {minutes}")
print(f"seconds = {seconds}")

# Task9
cash = 361
a = 100
b = 50
c = 10
d = 1

count = cash // a
count_1 = (cash % a) // b
count_2 = ((cash % a) % b) // c
count_3 = (((cash % a) % b) % c) // d

print(f"100 - {count}")
print(f"50 - {count_1}")
print(f"10 - {count_2}")
print(f"1 - {count_3}")

# Task10
height = 6
up = 4
down = 2

climb_per_day = up - down
days_to_climb = (height - up + climb_per_day) // climb_per_day

print(f"days_to_climb = {days_to_climb}")

# Task11
road_length = 56
speed = 90
hours = 1
minutes = 5

total_minutes = (hours * 60) + 5
distance = (speed * total_minutes) // 60
final_position = distance % road_length

print(f"final_position = {final_position}")

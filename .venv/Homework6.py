# Task1
# O(N log N)
def sort_strings_by_length(string_list: list):
    return sorted(string_list, key=len, reverse=True)


strings = input().split()
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)

# Task2
# 0(N log N)
def sort_words_by_a_count(word_list: list):

    def count_a(word):
        return word.count('a')

    return sorted(word_list, key=count_a)


words = input().split()
sorted_words = sort_words_by_a_count(words)
print(sorted_words)

# Task3
# O(1)
school = {
    '9a': 20,
    '9b': 30,
    '9c': 18,
    '9d': 24,
    '9e': 21
}

# a) The_number_of_students_has_changed
school['9d'] = 25
print('The_number_of_students:', school)

# b) Added_new_class
school['9f'] = 15
print('New_class:', school)

# c) The_class_was_removed
del school['9c']
print('Removed_class:', school)

# d) Calculate_the_total_number_of_students
total_students = sum(school.values())
print('The_total_number:', total_students)

# Task4
# O(N)
phone_book = {}

while True:
    command = input().strip()
    if command == '.':
        break

    parts = command.split()
    if len(parts) == 2:
        name, number = parts
        phone_book[name] = number
    elif len(parts) == 1:
        name = parts[0]
        if name in phone_book:
            print(phone_book[name])
        else:
            print("Not found")
    else:
        print("Not found")

# Task5
# O(N)
def get_element(lst: list, index: int) -> str | int:

    try:
        return lst[index]
    except IndexError:
        return "Error: index is out of range"


my_list = list(input().split())
print(get_element(my_list, index=int(input())))

# Tasks_with_decorators
# Task6
import time

def retry_on_exeption(retries):
    def decorator_retry(func):
        def wrapper(*args, **kwargs):
            attemps = 0
            while attemps < retries:
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    attemps += 1
                    print(f"ValueError: {e}, retrying attempt {attemps}/{retries}")
                    time.sleep(2)

            print(f"Function failed after {retries} retries.")
        return wrapper
    return decorator_retry

# The_example_of_using_decotator
@retry_on_exeption(retries=3)
def some_func(number:int | float):
    if number < 1:
        raise ValueError("Error")
    else:
        return number + 1

result = some_func(0)
print(f"result: {result}")

# Another_variant_to_call_the_decorator
def some_func(number:int | float):
    if number < 1:
        raise ValueError("Error")
    else:
        return number + 1

decorated_func = retry_on_exeption(retries=3)(some_func)
result = decorated_func(5)
print(f"result: {result}")

# Task7
import time

def timeout(limit):
    def decorator_timeout(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()

            def check_time():
                average_time = time.time() - start_time
                if average_time > limit:
                    raise TimeoutError(f"Work time {average_time} seconds")

            def monitoring_func():
                check_time()
                result = func(*args, **kwargs)
                check_time()
                return result

            try:
                return monitoring_func()
            except Exception as e:
                raise
        return wrapper
    return decorator_timeout

# The_example_of_using_decotator
@timeout(limit=1)
def long_running_function(number:int):
    time.sleep(number)
    return number * 2

try:
    result = long_running_function(1)
    print(f"Результат: {result}")

    result = long_running_function(3)
    print(f"Результат: {result}")

except Exception as e:
    print(f"Ошибка: {e}")


# New_homework
# Task1
# O(1)
import os

dirname = "Work"
filename = "input.txt"
encoding = "utf-8"
mode = "w"
# os.mkdir(dirname)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open(file=f"{dirname}/{filename}",
            mode=mode,
            encoding=encoding
) as file:
    numbers_str = " ".join(map(str, numbers))
    file.write(numbers_str)

# Task2
# O(N)
import os

dirname = "Work"
filename = "input.txt"
encoding = "utf-8"
mode = "r"

# os.mkdir(dirname)
with open(file=f"{dirname}/{filename}",
            mode=mode,
            encoding=encoding
) as file:
    numbers_str = file.readline().strip()
    numbers = [int(num) for num in numbers_str.split()]

value = 1
for num in numbers:
    value *= num

dirname = "Work"
filename = "output.txt"
encoding = "utf-8"
mode = "w"

with open(file=f"{dirname}/{filename}",
            mode=mode,
            encoding=encoding
) as file:
    file.write(str(value))

# Task3
# O(N)
import os
import datetime

def datetime_date(date_str:str):
    return datetime.datetime.strptime(date_str, "%d.%m.%Y").date()

def older_than_month(arrival_data):
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=30)
    return arrival_data <= one_month_ago

def total_value(quantity:int, price:int | float) -> int | float:
    return quantity * price

dirname = "Work"
filename = "products.txt"
encoding = "utf-8"
mode = "r+"
products = []

with open(file=f"{dirname}/{filename}",
          mode=mode,
          encoding=encoding
) as file:
    for line in file:
        parts = line.strip().split()
        name, quantity, price, arrival_date_str = parts
        quantity = int(quantity)
        price = float(price)
        arrival_date = datetime_date(arrival_date_str)
        products.append((name, quantity, price, arrival_date))

print(f"Products held for more than one month and priced above 1000000:")
for name, quantity, price, arrival_date in products:
    if older_than_month(arrival_date) and total_value(quantity, price) > 1000000:
        print(f"{name}/{quantity}/{price}/{arrival_date}")

# Task4
# O(N)
import os
import random

correct_answers = 0

# os.mkdir("Quiz")
dirname = "Quiz"
filename = "question.txt"
encoding = "utf-8"
mode = "r+"

with open(file=f"{dirname}/{filename}",
          mode=mode,
          encoding=encoding
) as file:
    questions = file.readlines()

dirname = "Quiz"
filename = "answer.txt"
encoding = "utf-8"
mode = "r+"

with open(file=f"{dirname}/{filename}",
          mode=mode,
          encoding=encoding
) as file:
    answers = file.readlines()

question_indexes = list(range(len(questions)))
random.shuffle(question_indexes)

for el in question_indexes:
    question = questions[el].strip()
    correct_answer = answers[el].strip()

    print(f"{question}")
    user_answer = input("answer:").strip()

    if user_answer.lower() == correct_answer.lower():
        print("Right!")
        correct_answers += 1
    else:
        print(f"Wrong answer. Correct answer is {correct_answer}")

    print(f"Correct answers: {correct_answers}")

# Task5
# O(1)
import os
import json

# os.mkdir("JSON")
dirname = "JSON"
filename = "json.file"
encoding = "utf-8"
mode = "w"

dictionary = {
    "50255": {
        "Name": "Maks",
        "Age": "25"
    },
    "45672": {
        "Name": "Olga",
        "Age": "38"
    },
    "89346": {
        "Name": "Ben",
        "Age": "54"
    },
    "76352": {
        "Name": "Anna",
        "Age": "15"
    },
    "13245": {
        "Name": "Alex",
        "Age": "40"
    },
    "29487": {
        "Name": "Mila",
        "Age": "83"
    }
}
with open(file=f"{dirname}/{filename}",
          mode=mode,
          encoding=encoding
) as file:
    json.dump(dictionary, file, indent=4)

# Task6
# O(N^2)
import json
import csv
import os

dirname_json = "JSON"
filename_json = "file.json"
encoding = "utf-8"
mode_json = "r"
json_filepath = os.path.join(dirname_json, filename_json)

with open(json_filepath, mode_json, encoding=encoding) as json_file:
    data = json.load(json_file)

if data is not None:
    dirname_csv = "CSV"
    filename_csv = "file.csv"
    encoding = "utf-8"
    mode_csv = "w"
    csv_filepath = os.path.join(dirname_csv, filename_csv.replace(".csv", ".json"))

    with open(csv_filepath, mode_csv, newline='', encoding=encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')


        for person_id, person_data in data.items():
            data_list = ["person"]
            for value in person_data.values():
                data_list.append(value)
            csv_writer.writerow(data_list)
        else:
            print("json.file is empty.")

    print(f"From {json_filepath} to {csv_filepath}")
else:
    print("It is impossible to create CSV because JSON data could not be read.")

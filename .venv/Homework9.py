# Task1
# O(1)
class BankAccount:
    def __init__(self, balance:float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3

    def deposit(self, amount:float):
        if amount > 0:
            self.__balance += amount
            print(f"New balance: {amount}")
        else:
            print("No deposit possible.")

    def withdraw(self, amount:float):
        if amount <= 0:
            print("Unable to withdraw money.")
            return

        if amount > self.__balance:
            print("Insufficient funds.")
            return

        if amount > self.daily_limit:
            print(f"Daily limit exceed, max {self.daily_limit}.")
            return

        if self.withdrawals_today >= self.max_withdrawals:
            print(f"Withdrawals today exceed, max {self.max_withdrawals}.")
            return

        self.__balance -= amount
        self.withdrawals_today += 1
        print(f"Withdrawal {amount}. New balance: {self.__balance}.")

    def get_balance(self):
        return self.__balance

# Example
account = BankAccount(20000)
account.deposit(3000)
account.withdraw(25000)
account.withdraw(4000)
account.withdraw(1000)
print(account.get_balance())

# Task2
# O(1)
import time

class Animal:
    def __init__(self, name:str, age:int, hunger_rate: float = 0.1):
        self.name = name
        self.age = age
        self.hunger = 100
        self.last_fed_time = time.time()
        self.hunger_rate = hunger_rate

    def make_sound(self):
        raise NotImplementedError

    def eat(self):
        self.hunger = 100
        self.last_fed_time = time.time()
        print(f"{self.name} is not hungry.")

    def update_hunger(self):
        current_time = time.time()
        time_since_last_fed = current_time - self.last_fed_time
        hunger_decrease = time_since_last_fed * self.hunger_rate
        self.hunger = max(0, self.hunger - hunger_decrease)

    def is_hungry(self):
        self.update_hunger()
        return self.hunger < 20

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

    def hunt(self):
        self.update_hunger()
        print(f"{self.name} is hunting...")
        if self.is_hungry():
            print(f"{self.name} was successful in hunting!")
            self.eat()
        else:
            print(f"{self.name} is not hungry.")

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

    def trumpet(self):
        self.update_hunger()
        print("Elephant trumpet.")

class Penguin(Animal):
    def make_sound(self):
        return "Squawk!"

    def swim(self):
        self.update_hunger()
        print(f"{self.name} is swimming...")

# Example
animals = [
    Lion("Simba", 7, hunger_rate=10),
    Elephant("Tima", 15, hunger_rate=50),
    Penguin("Pin", 10, hunger_rate=99)
]

for animal in animals:
    print(f"{animal.name} say: {animal.make_sound()}")

Simba = animals[0]
Tima = animals[1]
Pin = animals[2]

Simba.hunt()
Tima.trumpet()
Pin.swim()

time.sleep(5)
Simba.hunt()
Tima.trumpet()
Pin.swim()

# Task3
# O(1)
class Temperature:
    def __init__(self, celsius:float = 0.0):
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value:float):
        if value < -273.15:
            raise ValueError
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

# Example
temp = Temperature(float(input()))
print(f"Celsius:{temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
print(f"Kelvin: {temp.kelvin}")



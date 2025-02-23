# Task8
# O(1)
class MyClass:
    def __init__(self, value1:int, value2:int):
        self.value1 = value1
        self.value2 = value2

    def printer(self):
        print(self.value1)
        print(self.value2)

    def change_values(self, new_value1:int, new_value2:int):
        self.value1 = new_value1
        self.value2 = new_value2
        print("Values were changed")

    def calculator_sum(self):
        value = self.value1 + self.value2
        print(value)

    def find_max(self):
        print(max(self.value1, self.value2))

# Example
object = MyClass(10, 5)
object.printer()
object.change_values(4,18)
object.calculator_sum()
object.find_max()

# Task2
# O(N)
class DecadeCounter:
    def __init__(self, min_value:int = 0, max_value:int = 100, initial_value:int = 0):
        self.min_value = min_value
        self.max_value = max_value
        self.initial_value = initial_value

    def increase(self):
        if self.initial_value < self.max_value:
            self.initial_value += 1
        else:
            print("Max_value reached")

    def decrease(self):
        if self.initial_value > self.min_value:
            self.initial_value -= 1
        else:
            print("Min_value reached")

    def get_value(self):
        return self.initial_value

if __name__ == "__main__":
    counter1 = DecadeCounter()
    print("default counter1:", counter1.get_value())

    counter2 = DecadeCounter(min_value=5, max_value=20, initial_value=10)
    print("counter2:", counter2.get_value())

    counter1.increase()
    print("counter1 after increase:", counter1.get_value())

    counter2.decrease()
    print("counter2 after decrease:", counter2.get_value())

    for _ in range(10):
        counter2.increase()
    print("counter2 after some increase:", counter2.get_value())
    counter2.increase()
    print("counter2 after trying to increase above max:", counter2.get_value())

    for _ in range(10):
        counter2.decrease()
    print("counter2 after some decrease:", counter2.get_value())
    counter2.decrease()
    print("counter2 after trying to increase above min:", counter2.get_value())

# Task3
# O(N)
class Store:
    def __init__(self, name:str):
        self.name = name
        self.products = {}

    def add_product(self, product_name:str, quantity:int):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
        print(f"Added {quantity} units of '{product_name}' to the store.")

    def remove_product(self, product_name:str, quantity:int):
        if product_name not in self.products:
            raise ValueError(f"The product '{product_name}' not found in the store.")

        if quantity > self.products[product_name]:
            raise ValueError(f"Insufficient product '{product_name}' for removal.")

        self.products[product_name] -= quantity
        if self.products[product_name] == 0:
            del self.products[product_name]
        print(f"Removed {quantity} units of '{product_name}' from the store.")

    def find_product(self, product_name:str):
        if product_name in self.products:
            return self.products[product_name]
        else:
            return None

    def display_products(self):
        if self.products:
            print(f"Products in store '{self.name}'.")
            for product, quantity in self.products.items():
                print(f"- {product}: {quantity}")
        else:
            print(f"The store '{self.name}' is empty.")

if __name__ == "__main__":
    my_store = Store("Fruitmarket")

    my_store.add_product("Apples", 100)
    my_store.add_product("Bananas", 80)
    my_store.add_product("Grapes", 200)
    my_store.add_product("Mangos", 30)

    my_store.display_products()

    quantity = my_store.find_product("Bananas")
    if quantity:
        print(f"There are {quantity} branches of bananas in the store.")
    else:
        print("Bananas not found in the store.")

    try:
        my_store.remove_product("Grapes", 100)
    except ValueError as e:
        print("Error when removing product:", e)

    my_store.display_products()

    try:
        my_store.remove_product("Oranges", 30)
    except ValueError as e:
        print("Error when removing product:", e)

    try:
        my_store.remove_product("Apples", 110)
    except ValueError as e:
        print("Error when removing product:", e)


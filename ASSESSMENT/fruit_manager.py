class FruitManager:
    def __init__(self):
        self.fruit_stock = {}

    def add_fruit(self, fruit_name, quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity

    def view_fruit_stock(self):
        print("Fruit Stock:")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity}")

    def update_fruit_stock(self, fruit_name, new_quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = new_quantity
        else:
            print("Fruit not found in stock.")

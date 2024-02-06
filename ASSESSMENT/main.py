from fruit_manager import FruitManager
from customer import Customer

def display_menu():
    print("\nMenu:")
    print("1. Add Fruit to Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")

def main():
    fruit_manager = FruitManager()
    customer = Customer()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            fruit_name = input("Enter fruit name: ")
            quantity = int(input("Enter quantity: "))
            fruit_manager.add_fruit(fruit_name, quantity)
            print("Fruit added to stock.")
            customer.log_transaction(f"Added {quantity} {fruit_name}(s) to stock.")
        elif choice == '2':
            fruit_manager.view_fruit_stock()
        elif choice == '3':
            fruit_name = input("Enter fruit name to update: ")
            if fruit_name in fruit_manager.fruit_stock:
                new_quantity = int(input("Enter new quantity: "))
                fruit_manager.update_fruit_stock(fruit_name, new_quantity)
                print("Fruit stock updated.")
                customer.log_transaction(f"Updated {fruit_name} stock to {new_quantity}.")
            else:
                print("Fruit not found in stock.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    # Writing transaction log to file
    with open("transaction_log.txt", "w") as f:
        for transaction in customer.transaction_log:
            f.write(transaction + "\n")

if __name__ == "__main__":
    main()
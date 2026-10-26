import json
import os

from product import Product # Get the Product class from product.py
from inventory import Inventory # Get the Inventory class from inventory.py

file_name = "inventory.json"
INVENTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


# ---------- File handling (functions, kept out of Product/Inventory per SRP) ----------

def load_inventory(filename=INVENTORY_FILE):
    """Load inventory.json and return an Inventory of Product objects."""
    inventory = Inventory()
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                products = json.load(file)
            for data in products:
                inventory.add_product(Product.from_dict(data))
            print(f"{file_name} found. Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error loading {filename}: {error}")
            print("Starting with an empty inventory.")
    else:
        print(f"{file_name} not found. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory, filename=INVENTORY_FILE):
    print("Saving inventory...")
    try:
        products = [product.to_dict() for product in inventory.get_products()]
        with open(filename, "w") as file:
            json.dump(products, file, indent=4)
        print(f"Inventory saved successfully to {filename}.")
    except OSError as error:
        print(f"Error saving inventory: {error}")


# ---------- Menu actions (user input lives here, not in the classes) ----------

def display_all(inventory):
    print("\nCurrent Inventory")
    inventory.display_all()


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity. Product not added.")
        return
    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    try:
        new_stock = int(input("\nNew Stock Quantity: "))
    except ValueError:
        print("Invalid stock quantity.")
        return
    if product.update_stock(new_stock):
        print("Stock updated successfully!")
    else:
        print("Invalid stock quantity.")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("\nProduct Found")
    print(f"ID: {product.get_id()}")
    print(f"Name: {product.get_name()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Stock: {product.get_stock()}")


def main():
    print("\n===================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===================================")

    inventory = load_inventory()

    while True:
        print("\n---------MENU---------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------")
        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System. Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
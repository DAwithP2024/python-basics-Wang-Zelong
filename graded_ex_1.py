import re
from io import StringIO

# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    else:
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    output = StringIO()
    total_cost = 0
    for product, price, quantity in cart:
        total_cost += price * quantity
        output.write(f"{product} - ${price} x {quantity} = ${price * quantity}\n")
    output.write(f"Total cost: ${total_cost}")
    return output.getvalue()

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    return bool(re.fullmatch(r'[A-Za-z]+\s[A-Za-z]+', name))

def validate_email(email):
    return "@" in email

# This function is not used in the tests, but it's part of the original code
def main():
    cart = []
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name with first and last name.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address containing '@'.")
        email = input("Please enter your email address: ")

    while True:
        display_categories()
        category_choice = input("Please select a category (number): ")
        if category_choice.isdigit() and int(category_choice) in range(1, len(products) + 1):
            category = list(products.keys())[int(category_choice) - 1]
            display_products(products[category])
            while True:
                print("\n1. Select a product to buy")
                print("2. Sort the products according to the price")
                print("3. Go back to the category selection")
                print("4. Finish shopping")
                choice = input("Choose an option: ")
                if choice == "1":
                    product_choice = input("Enter the product number: ")
                    quantity = input("Enter the quantity: ")
                    if product_choice.isdigit() and int(product_choice) in range(1, len(products[category]) + 1) and quantity.isdigit() and int(quantity) > 0:
                        add_to_cart(cart, products[category][int(product_choice) - 1], int(quantity))
                    else:
                        print("Invalid product or quantity, please try again.")
                elif choice == "2":
                    sort_order = input("Sort ascending (1) or descending (2): ").lower()
                    sorted_products = display_sorted_products(products[category], "asc" if sort_order == "1" else "desc")
                    display_products(sorted_products)
                elif choice == "3":
                    break
                elif choice == "4":
                    if cart:
                        total_cost = sum(price * quantity for product, price, quantity in cart)
                        address = input("Please enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    continue_shopping = input("Do you want to continue shopping? (1 for yes, 2 for no): ")
                    if continue_shopping == "2":
                        print("Thank you for shopping with us. Have a nice day!")
                        return  # Exit the program
                    elif continue_shopping == "1":
                        continue  # Continue the shopping loop
                    else:
                        print("Invalid option, please choose again.")
                else:
                    print("Invalid option, please choose again.")
        else:
            print("Invalid category selection, please try again.")

if __name__ == "__main__":
    main()

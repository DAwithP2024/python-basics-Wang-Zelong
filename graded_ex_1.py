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
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        for item in cart:
            print(f"{item[0]} - Quantity: {item[1]}")
        total_cost = sum(price * quantity for price, quantity in cart)
        print(f"Total cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name} <{email}>")
    print(f"Delivery address: {address}")
    for item in cart:
        print(f"{item[0]} - Quantity: {item[1]}")
    print(f"Total cost: ${total_cost:.2f}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    name = input("Please enter your name: ")
    while not validate_name(name):
        name = input("Invalid name. Please enter your name (First and Last): ")
    email = input("Please enter your email address: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter a valid email address: ")

    cart = []
    while True:
        display_categories()
        category_choice = input("Enter the category number you wish to explore: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
            category = list(products.keys())[int(category_choice) - 1]
            display_products(products[category])
            while True:
                product_choice = input("What would you like to do?\n1. Select a product to buy\n2. Sort the products by price\n3. Go back to the category selection\n4. Finish shopping\nYour choice: ")
                if product_choice == "1":
                    product_number = input("Enter the product number you wish to buy: ")
                    if product_number.isdigit() and 1 <= int(product_number) <= len(products[category]):
                        quantity = int(input(f"How many {products[category][int(product_number) - 1][0]} would you like to buy? "))
                        add_to_cart(cart, products[category][int(product_number) - 1][0], quantity)
                    else:
                        print("Invalid product number.")
                elif product_choice == "2":
                    sort_order = input("Sort by 1 for ascending or 2 for descending: ")
                    sorted_products = display_sorted_products(products[category], int(sort_order))
                    display_products(sorted_products)
                elif product_choice == "3":
                    break
                elif product_choice == "4":
                    if cart:
                        address = input("Please enter your delivery address: ")
                        total_cost = sum(price * quantity for price, quantity in cart)
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid category number. Please enter a correct number.")

if __name__ == "__main__":
    main()

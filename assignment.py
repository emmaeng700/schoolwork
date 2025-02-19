from tabulate import tabulate

# Categories of goods with available items
categories = {
    "Groceries": {"Milk": 3.50, "Bread": 2.00, "Eggs": 5.00},
    "Utensils": {"Spoon Set": 15.00, "Knife": 12.50, "Plate Set": 25.00},
    "Electronics": {"Headphones": 45.00, "USB Cable": 10.00, "Charger": 20.00}
}

# Initialize cart variables
cart = {category: [] for category in categories}
total_prices = []


# Function to create and display the receipt table
def create_table():
    if not any(cart.values()):
        print("No items purchased.")
        return

    table_data = []
    for category, items in cart.items():
        if items:
            table_data.append([f"--- {category} ---", ""])
            for item_name, item_price in items:
                table_data.append([item_name, f"${item_price:.2f}"])

    table_data.append(["Totals", ""])  # Empty row for spacing
    table_data.append(["TPBT", f"${sum(price for _, price in total_prices):.2f}"])  #
    table_data.append(["TPAT",
                       f"${sum(price + calculate_tax(price) for _, price in total_prices):.2f}"])

    print(tabulate(table_data, headers=["Item", "Price"], tablefmt="grid", stralign='center'))

    summary_table = [["Number of Items", sum(len(items) for items in cart.values())]]
    print(tabulate(summary_table, tablefmt="grid", stralign='center'))
    print("Thank you for shopping with us!")


# Function to calculate tax
def calculate_tax(price):
    tax_rate = 10.44 / 100
    return price * tax_rate


# Function to display available items by category
def show_available_items():
    print("\nAvailable Items:")
    for category, items in categories.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"- {item}: ${price:.2f}")
    print()
    print()

# Main function


def main():
    print("Welcome to Walmart Shopping Cart!")
    show_available_items()

    while True:
        command = input("""
Type 'exit' to checkout, 
'remove' to remove an item from the cart, 
or 'show' to see available items.
\nEnter the name of the item or command: """).strip().lower()

        if command == "exit":
            break

        elif command == "show":
            show_available_items()
            continue

        elif command == "remove":
            if not any(cart.values()):
                print("Your cart is empty. Nothing to remove.")
                continue

            remove = input("Enter the name of the item to be removed: ").strip().capitalize()

            found = False
            for category, items in cart.items():
                for i, (item_name, item_price) in enumerate(items):
                    if item_name == remove:
                        del cart[category][i]
                        total_prices.remove((item_name, item_price))
                        print(f"Removed '{remove}' from your cart.")
                        found = True
                        break
                if found:
                    break

            if not found:
                print(f"'{remove}' is not in your cart.")
            continue

        # Validate item selection
        selected_item = None
        # made a change: changed capitalize to title to resolve 'Spoon Set'
        for category, items in categories.items():
            if command.title() in items:
                selected_item = (command.title(), items[command.title()])  # second item in the tuple is its cost
                break

        if not selected_item:
            print("Item not available. Type 'show' to see available items.")
            continue

        # Add item to cart
        category = [cat for cat in categories if selected_item[0] in categories[cat]][0]
        cart[category].append(selected_item)
        total_prices.append(selected_item)

        print(f"'{selected_item[0]}' added to your cart.")
        print(f"Total: ${sum(price + calculate_tax(price) for _, price in total_prices):.2f}")  # total spent so far

    # Display receipt
    print("\n--- Receipt ---")
    create_table()


# Run the program
main()

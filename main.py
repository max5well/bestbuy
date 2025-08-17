from store import Store
from products import Product

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = Store(product_list)


def list_products(store):
    """List all active products."""
    for product in store.get_all_products():
        print(product)


def show_total(store):
    """Show total quantity of all products."""
    print(f"Total quantity: {store.get_total_quantity()}")


def make_order(store):
    """Interactive order process with error handling."""
    products = store.get_all_products()

    print("------")
    for i, p in enumerate(products, start=1):  # 1-based index
        print(f"{i}. {p}")
    print("------")

    shopping_list = []
    while True:
        choice = input("Which product # do you want? (Press Enter to finish) ")
        if choice.strip() == "":
            break
        try:
            index = int(choice) - 1
            product = products[index]
        except (ValueError, IndexError):
            print("Invalid product number. Try again.")
            continue

        try:
            amount = int(input("What amount do you want? "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue

        if amount > product.get_quantity():
            print("Not enough stock available!")
        else:
            shopping_list.append((product, amount))
            print("Product added to list!")

    if shopping_list:
        total = store.order(shopping_list)
        print(f"Total price: ${total}")
    else:
        print("No products ordered.")


def quit_app(_):
    """Exit the program."""
    print("Goodbye!")
    exit()


menu_selector = {
    1: ("List all products", list_products),
    2: ("Show total quantity", show_total),
    3: ("Make an order", make_order),
    4: ("Quit", quit_app)
}


def start(store):
    """Menu loop."""
    while True:
        print("\nMenu:")
        for key, func in menu_selector.items():
            print(f"{key}: {func[0]}")  # shows the label stored in the tuple

        try:
            choice = int(input("Choose an option: "))
            if choice in menu_selector:
                func = menu_selector[choice][1]  # get the actual function
                func(store)  # call it with store
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    start(best_buy)

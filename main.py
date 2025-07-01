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
    for product in store.get_all_products():
        print(product)

def show_total(store):
    print(f"Total quantity: {store.get_total_quantity()}")

def make_order(store):
    products = store.get_all_products()
    for i, p in enumerate(products):
        print(f"{i}: {p}")
    try:
        index, quantity = map(int, input("Enter index and quantity: ").split())
        total = store.order([(products[index], quantity)])
        print(f"Total price: ${total}")
    except Exception as e:
        print(f"Error: {e}")

def quit_app(_):
    print("Goodbye!")
    exit()


menu_selector = {
    1: ("List all products", list_products),
    2: ("Show total quantity", show_total),
    3: ("Make an order", make_order),
    4: ("Quit", quit_app)
}


def start(store):
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
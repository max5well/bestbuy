from products import Product

class Store:
    def __init__(self, products: list[Product]):
        self._products = products

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self._products:
            total_quantity += product._quantity
        return total_quantity

    def get_all_products(self) -> list[Product]:
        active_products = []
        for product in self._products:
            if product._active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Could not buy {product._name}: {e}")
        return total_price


#Best buy
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)

products = best_buy.get_all_products()
print(products)
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))




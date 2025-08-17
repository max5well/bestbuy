class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = quantity > 0

    def __str__(self):
        return f"{self._name}, Price: ${self._price}, Quantity: {self._quantity}"

    def get_name(self):
      return self._name

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self._quantity

    def set_quantity(self, quantity: int):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        self._quantity = quantity
        if self._quantity <= 0:
            self._active = False

    def is_active(self) -> bool:
        """
        Getter function for active status.
        Returns True if the product is active, otherwise False.
        """
        return self._active

    def activate(self) -> bool:
        """
        Setter function for activate status.
        """
        self._active = True

    def deactivate(self) -> bool:
        """
        Setter function to deactivate status.
        """
        self._active = False

    def show(self) -> str:
        """
        Show the product.
        """
        print(f"Product name: {self._name}, Price: {self._price} Quantity: {self._quantity}")

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float).
        Updates the quantity.
        Raises Exception if the product is inactive, the quantity is invalid,
        or there is not enough stock.
        """
        if not self._active:
            raise Exception("Product is not active.")

        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")

        if quantity > self._quantity:
            raise Exception("Not enough stock to complete the purchase.")

        total_price = quantity * self._price
        self._quantity -= quantity

        if self._quantity == 0:
            self._active = False

        return total_price



bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(20))
print(mac.buy(10))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
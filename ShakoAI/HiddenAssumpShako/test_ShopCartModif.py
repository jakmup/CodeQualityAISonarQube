class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def test_add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        self.items.append(item)

    def test_remove_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        self.items.remove(item)

    def test_calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Book(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.category = "Books"

class DVD(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.category = "DVDs"

class GroceryItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.category = "Grocery"

class ShoppingCartRepository:
    def __init__(self):
        self.shopping_carts = {}

    def test_get_shopping_cart(self, customer_id):
        if customer_id in self.shopping_carts:
            return self.shopping_carts[customer_id]
        else:
            return None

    def test_add_to_shopping_cart(self, customer_id, item):
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        if customer_id in self.shopping_carts:
            self.shopping_carts[customer_id].add_item(item)
        else:
            shopping_cart = ShoppingCart(customer_id=customer_id)
            shopping_cart.add_item(item)
            self.shopping_carts[customer_id] = shopping_cart
            return shopping_cart

    def test_remove_from_shopping_cart(self, customer_id, item):
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        if customer_id in self.shopping_carts:
            self.shopping_carts[customer_id].remove_item(item)
        else:
            raise ValueError("Shopping cart not found for customer_id {}".format(customer_id))

    def test_clear_all_shopping_carts(self):
        for customer_id, shopping_cart in self.shopping_carts.items():
            self.remove_from_shopping_cart(customer_id, shopping_cart)

shopping_cart = ShoppingCart()
book = Book("The Great Gatsby", 25.99)
dvd = DVD("The Matrix", 19.99)
grocery_item = GroceryItem("Eggs", 2.99)

shopping_cart.add_item(book)
shopping_cart.add_item(dvd)
shopping_cart.add_item(grocery_item)

shopping_cart_repository = ShoppingCartRepository()

print(shopping_cart.calculate_total())  # Output: 51.97

shopping_cart_repository.add_to_shopping_cart(123, book)
print(shopping_cart.calculate_total())  # Output: 51.97

shopping_cart_repository.add_to_shopping_cart(123, dvd)
print(shopping_cart.calculate_total())  # Output: 53.96

shopping_cart_repository.clear_all_shopping_carts()
print(shopping_cart.calculate_total())  # Output: 0.0
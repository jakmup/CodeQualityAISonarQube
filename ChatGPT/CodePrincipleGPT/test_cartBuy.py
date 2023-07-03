class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

class CartPrinter:
    def print_items(self, cart):
        print("Items in the cart:")
        for item in cart.items:
            print(item.name, "-", item.price)

class CartManager:
    def __init__(self, cart):
        self.cart = cart

    def add_item_to_cart(self, item):
        self.cart.add_item(item)

    def remove_item_from_cart(self, item):
        self.cart.remove_item(item)

    def calculate_total_price(self):
        return self.cart.calculate_total()

# Create some sample items
item1 = Item("Shirt", 25.99)
item2 = Item("Pants", 35.99)
item3 = Item("Shoes", 49.99)

# Create a shopping cart
cart = ShoppingCart()

# Create cart manager
cart_manager = CartManager(cart)

# Add items to the cart
cart_manager.add_item_to_cart(item1)
cart_manager.add_item_to_cart(item2)
cart_manager.add_item_to_cart(item3)

# Remove an item from the cart
cart_manager.remove_item_from_cart(item2)

# Create cart printer
cart_printer = CartPrinter()

# Print the items in the cart
cart_printer.print_items(cart)

# Calculate the total price
total_price = cart_manager.calculate_total_price()

# Print the total price
print("Total price:", total_price)

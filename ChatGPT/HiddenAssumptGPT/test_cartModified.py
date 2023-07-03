class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def print_items(self):
        print("Items in the cart:")
        for item in self.items:
            print(item.name, "-", item.price)

    def print_total_price(self):
        total_price = self.calculate_total()
        print("Total price:", total_price)

# Create some sample items
item1 = Item("Shirt", 25.99)
item2 = Item("Pants", 35.99)
item3 = Item("Shoes", 49.99)

# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

# Remove an item from the cart
cart.remove_item(item2)

# Print the items in the cart and the total price
cart.print_items()
cart.print_total_price()

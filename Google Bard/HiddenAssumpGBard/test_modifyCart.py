from typing import List

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)

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

# Calculate the total price
total_price = cart.calculate_total()

# Print the items in the cart and the total price
print("Items in the cart:")
for item in cart.items:
    print(item.name, "-", item.price)

print("Total price:", total_price)

class Cart:
    def __init__(self):
        self.items = []

    def test_add_item(self, item):
        self.items.append(item)

    def test_remove_item(self, item):
        self.items.remove(item)

    def test_get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def main():
    cart = Cart()
    cart.add_item(Item("Apple", 1.00))
    cart.add_item(Item("Orange", 0.50))
    print("Total price:", cart.get_total_price())

if __name__ == "__main__":
    main()

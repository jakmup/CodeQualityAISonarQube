class ShoppingCart:
    def __init__(self):
        self.items = []

    def test_add_item(self, item):
        if item.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        item_id = item.id
        if item_id in self.items:
            self.items[item_id].quantity += 1
        else:
            self.items.append({
                'id': item_id,
                'quantity': 1
            })

    def test_remove_item(self, item_id):
        item = self.get_item(item_id)
        if item is None:
            raise ValueError("Item not found in cart")

        if item.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        item.quantity -= 1

    def test_get_item(self, item_id):
        for item in self.items:
            if item['id'] == item_id:
                return item
        return None

    def test_get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item['quantity'] * item['price']
        return total_price

class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = 1

    def __str__(self):
        return f"{self.name} - {self.quantity} x {self.price}"

    def increase_quantity(self):
        self.quantity += 1

class ShoppingCartRepository:
    def __init__(self):
        self.cart = ShoppingCart()

    def test_add_item(self, item):
        self.cart.add_item(item)

    def test_remove_item(self, item_id):
        self.cart.remove_item(item_id)

    def test_get_cart(self):
        return self.cart
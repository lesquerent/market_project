class Order:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def insert_buy(self):
        pass

class Book:
    def __init__(self, quantity, price, buy=True):
        self.quantity = quantity
        self.price = price
        self.buy = buy
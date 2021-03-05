class Order:

    def __init__(self, quantity, price, _type):
        self.quantity = quantity
        self.price = price
        self.type = type

    def __str__(self):  # human-readable content
        return self._type + "%s @ %s" % (self.quantity, self.price)

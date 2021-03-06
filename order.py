import itertools

from functools import total_ordering


class Order:
    nb_of_id = itertools.count(1)  # Create a static element incremented at the creation of the class instance

    def __init__(self, quantity, price, type_of_order):
        self._quantity = quantity
        self._price = price
        self._type = type_of_order
        self._id = next(self.nb_of_id)  # Increment the static element corresponding to the id

    def __str__(self):  # human-readable content
        return self._type.upper() + " %s@%s id=%s" % (self._quantity, self._price, self._id)

    def __eq__(self, other):
        # noinspection PyProtectedMember
        return (self._quantity, self._price) == (other._quantity, other._price)

    def __lt__(self, other):
        # noinspection PyProtectedMember
        return self._price < other._price

    def get_id(self):
        return self._id

    def get_qty(self):
        return self._quantity

    def get_price(self):
        return self._price

    def set_qty(self, quantity):
        self._quantity = quantity


if __name__ == '__main__':
    order1 = Order(130, 13, 'sell')
    order2 = Order(120, 12, 'buy')

    print(order1.get_id())
    print(order2.get_id())
    print(order2 < order1)

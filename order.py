import itertools


class Order:
    nb_of_id = itertools.count(1)  # Create a static element incremented at the creation of the class instance

    def __init__(self, quantity, price, type_of_order):
        """
            Constructor off an order
        :param quantity: int
            The amount to sell
        :param price: double
            The unit price to sell
        :param type_of_order: ['sell', 'buy']
            The type of the order, sell or buy order
        """
        self._quantity = quantity
        self._price = price
        self._type = type_of_order.upper()
        self._id = next(self.nb_of_id)  # Increment the static element corresponding to the id

    def __str__(self):  # human-readable content
        return self._type.upper() + " %s@%s id=%s" % (self._quantity, self._price, self._id)

    def __eq__(self, other):
        # noinspection PyProtectedMember
        return (self._quantity, self._price) == (other._quantity, other._price)

    def __lt__(self, other):
        # noinspection PyProtectedMember
        return self._price <= other._price

    def get_id(self):
        return self._id

    def get_qty(self):
        return self._quantity

    def get_price(self):
        return self._price

    def set_qty(self, quantity):
        self._quantity = quantity

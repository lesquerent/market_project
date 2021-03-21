class Deal:
    def __init__(self, quantity, price, book_name):
        """
            Constructor off a deal
        :param quantity: int
            The amount of the deal
        :param price: double
            The unit price of the deal
        :param book_name : str
            The name of the book in which the deal was conclude
        """
        self._quantity = quantity
        self._price = price
        self._book_name = book_name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def get_book_name(self):
        return self._book_name

    def __str__(self):
        return 'Execute {quantity} at {price} on {book}'.format(quantity=self._quantity, price=self._price,
                                                                book=self._book_name)

from order import Order


class Book:
    def __init__(self, name='Default order book', buy_orders=[], sell_orders=[], execute_deals=[]):
        """
            Constructor off an order book
        :param name: str
            The name off the order book. Default : 'Default order book'.
        :param buy_orders: dict
            Dictionary containing all buy orders. Default : {}.
        :param sell_orders:  dict
            Dictionary containing all sell orders. Default : {}.
        """
        self._name = name
        self._buy_orders = buy_orders
        self._sell_orders = sell_orders
        self._execute_deals = execute_deals

    def insert_sell(self, quantity, price):
        sell_order = Order(quantity, price, type_of_order='sell')
        self._sell_orders.append(sell_order)
        self._sell_orders.sort()
        self._sell_orders.reverse()
        print('--- Insert {order} on {book}'.format(order=sell_order.__str__(), book=self._name))
        print(self.get_status())

    def insert_buy(self, quantity, price):
        buy_order = Order(quantity, price, type_of_order='buy')
        self._buy_orders.append(buy_order)
        self._buy_orders.sort()
        print('--- Insert {order} on {book}'.format(order=buy_order.__str__(), book=self._name))
        print(self.get_status())

    def insert_deals(self, deal):
        self._execute_deals.append(deal)

    def get_sell_order(self):
        return self._sell_orders

    def get_buy_orders(self):
        return self._buy_orders

    def get_status(self):
        status = ""
        if len(self._execute_deals) != 0:

            for deal in self._execute_deals:
                status += deal.__str__() + '\n'

        status += 'Book on {}\n'.format(self._name.upper())

        for sell_order in self._sell_orders:
            status += '        {order}\n'.format(order=sell_order.__str__())

        for buy_order in self._buy_orders:
            status += '        {order}\n'.format(order=buy_order.__str__())

        status += '------------------------'
        return status


if __name__ == '__main__':
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)

    # print(book.get_status())

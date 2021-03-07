from order import Order
from deal import Deal


class Book:
    def __init__(self, name='Default order book', buy_orders=[], sell_orders=[], execute_deals=[]):
        """
            Constructor off an order book
        :param name: str
            The name off the order book. Default : 'Default order book'.
        :param buy_orders: list
            List containing all buy orders. Default : [].
        :param sell_orders:  list
            List containing all sell orders. Default : [].
        :param execute_deals: list
            List containing all execute orders. Default : [].
        """
        self._name = name
        self._buy_orders = buy_orders
        self._sell_orders = sell_orders
        self._execute_deals = execute_deals

    def insert_sell(self, quantity, price):
        sell_order = Order(quantity, price, type_of_order='sell')

        if quantity != 0:
            self._sell_orders.append(sell_order)
            self._sell_orders.sort()
            # self._sell_orders.reverse()
            print('--- Insert {order} on {book}'.format(order=sell_order.__str__(), book=self._name))

        while len(self._buy_orders) != 0 and self._buy_orders[
            0].get_price() >= sell_order.get_price() and sell_order.get_qty() > 0:

            # Case quantity sell order > first buy order in our book
            if sell_order.get_qty() > self._buy_orders[0].get_qty():
                deal = Deal(self._buy_orders[0].get_qty(), self._buy_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

                new_qty = sell_order.get_qty() - self._buy_orders[0].get_qty()

                # Fill the first buy order
                self._buy_orders.remove(self._buy_orders[0])

                sell_order.set_qty(new_qty)
                print(deal.__str__())

            # Case quantity sell order < first buy order in our book
            else:
                deal = Deal(sell_order.get_qty(), self._buy_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

                # Update of the new quantity
                self._buy_orders[0].set_qty(self._buy_orders[0].get_qty() - sell_order.get_qty())

                sell_order.set_qty(0)

                if self._buy_orders[0].get_qty() == 0:
                    self._buy_orders.remove(self._buy_orders[0])

                self._sell_orders.remove(self._sell_orders[0])

                print(deal.__str__())

        print(self.get_status())

    def insert_buy(self, quantity, price):
        buy_order = Order(quantity, price, type_of_order='buy')

        if quantity != 0:
            self._buy_orders.append(buy_order)
            self._buy_orders.sort()
            self._buy_orders.reverse()
            print('--- Insert {order} on {book}'.format(order=buy_order.__str__(), book=self._name))

        while len(self._sell_orders) != 0 and self._sell_orders[
            0].get_price() <= buy_order.get_price() and buy_order.get_qty() > 0:

            # Case quantity sell order > first buy order in our book
            if buy_order.get_qty() > self._sell_orders[0].get_qty():
                deal = Deal(self._sell_orders[0].get_qty(), self._sell_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

                new_qty = buy_order.get_qty() - self._sell_orders[0].get_qty()

                # Fill the first buy order
                self._sell_orders.remove(self._sell_orders[0])

                buy_order.set_qty(new_qty)
                print(deal.__str__())

            # Case quantity sell order < first buy order in our book
            else:
                deal = Deal(buy_order.get_qty(), self._sell_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

                # Update of the new quantity
                self._sell_orders[0].set_qty(self._sell_orders[0].get_qty() - buy_order.get_qty())

                buy_order.set_qty(0)

                self._buy_orders.remove(self._buy_orders[0])

                if self._sell_orders[0].get_qty() == 0:
                    self._sell_orders.remove(self._sell_orders[0])

                print(deal.__str__())

        print(self.get_status())

    def insert_deals(self, deal):
        self._execute_deals.append(deal)

    def get_sell_order(self):
        return self._sell_orders

    def get_buy_orders(self):
        return self._buy_orders

    def get_status(self):
        status = ""
        """if len(self._execute_deals) != 0:

            for deal in self._execute_deals:
                status += deal.__str__() + '\n'"""

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

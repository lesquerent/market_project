from order import Order
from deal import Deal
import pandas as pd


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
        """
            Insert sell order in the order book and execute orders if it's possible.
        :param quantity: int
            The amount to sell
        :param price: double
            The unit price to sell
        :return: None
        """
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

        return None

    def insert_buy(self, quantity, price):
        """
            Insert buy order in the order book and execute orders if it's possible.
        :param quantity: int
            The amount to buy
        :param price: double
            The unit price to buy
        :return: None
        """

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

        return None

    def insert_deals(self, deal):
        """
            Insert a deal in the _execute_deals list containing all execute orders.
        :param deal: Deal
            The execute deal
        :return: None
        """
        self._execute_deals.append(deal)
        return None

    def get_sell_order(self):
        return self._sell_orders

    def get_buy_orders(self):
        return self._buy_orders

    def get_status(self):
        """
            Create a string with the status of the order book
        :return: string
            Status of the order book
        """
        status = ""

        status += 'Book on {}\n'.format(self._name.upper())
        order_book = self.create_df_order()
        status += order_book.to_string(index=False)
        # for sell_order in self._sell_orders:
        #     status += '        {order}\n'.format(order=sell_order.__str__())
        #
        # for buy_order in self._buy_orders:
        #     status += '        {order}\n'.format(order=buy_order.__str__())

        status += '\n------------------------'
        return status

    def create_df_order(self):
        """
            Create a pd.dataframe corresponding to the order book.
            Create the dataframe form _sell_orders and _buy_orders attributes to an unique dataframe.

        :return: pd.dataframe
            The pd.dataframe corresponding to the order book
        """
        df_sell_orders = pd.DataFrame([sell_order.__dict__ for sell_order in self._sell_orders])
        df_buy_orders = pd.DataFrame([buy_order.__dict__ for buy_order in self._buy_orders])
        df_all_orders = df_sell_orders.append(df_buy_orders)
        df_all_orders.columns = ['QTY', 'PRICE', 'TYPE', 'ID']
        return df_all_orders

"""
module models
"""
import datetime
class Orders:
    """class for orders"""
    orders = []
    def __init__(self, client, contact, order_item, price):
        """
        constructor method for class
        :param order_id:
        :param client:
        :param contact:
        :param order_item:
        :param price:
        """
        self.order_id = len(self.orders) + 1
        self.client = client
        self.contact = contact
        self.order_item = order_item
        self.price = price
        self.order_date = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p")
        self.order_status = 'submitted'

    def to_json(self):
        """
        method converts data to json format
        :return: json_data"""
        return self.__dict__
    @classmethod
    def add_order(cls, order):
        """
        class method adds a new order to the list of orders
        :param order:
        """
        cls.orders.append(order)
    @classmethod
    def get_all(cls):
        """
        class method gets all orders
        :return: cls.orders:
        """
        return cls.orders
    @classmethod
    def is_empty(cls):
        """
        class method for empty  orders list
        returns length of orders list equal to 0
        """
        return len(cls.orders) == 0
    @classmethod
    def get_by_id(cls, order_id):
        """
        class method gets specific order by id
        :param order_id
        :return: order
        """
        for order in cls.orders:
            if order['order_id'] == order_id:
                return order
        return None
    @classmethod
    def delete_order(cls, order_id):
        """
        class method deletes order
        :param order_id:
        """
        for order in cls.orders:
            if order['order_id'] == order_id:
                cls.orders.remove(order)
        return None
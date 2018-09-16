"""
module models
"""
class Orders:
    """class for orders"""
    def __init__(self, order_id, client, contact, order_item, price, order_status):
        """
        constructor method for class
        :param order_id:
        :param client:
        :param contact:
        :param order_item:
        :param price:
        """
        self.order_id = order_id
        self.client = client
        self.contact = contact
        self.order_item = order_item 
        self.price = price
        self.order_status = order_status

    def to_json(self):
        """
        method converts data to json format
        :return: json_data"""
        return self.__dict__
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
        json_data = {
            'order_id': self.order_id,
            'client': self.client,
            'contact': self.contact,
            'order_item': self.order_item,
            'price': self.price,
            'order_status': self.order_status
        }
        return json_data
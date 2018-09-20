"""
module views
"""
import re
import datetime
from flask import jsonify, Blueprint, make_response
from flask_restful import Api, Resource, reqparse
from .models import Orders

orders = []

orders_blue_print = Blueprint('ord_bp', __name__, url_prefix='/api/v1')
api = Api(orders_blue_print)

class OrdersHandler(Resource):
    """Class handles methods for all orders"""
    def __init__(self):
        """constructor method for the class"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('client', type=str, required=True,\
         help='please provide your name')
        self.reqparse.add_argument('contact', type=int, required=True,\
         help='please provide your contact(digits)')
        self.reqparse.add_argument('order_item', type=str, required=True,\
         help='please provide your order')
        self.reqparse.add_argument('price', type=int, required=True,\
         help='please enter the price')

    def get(self):
        """
        method to fetch all orders
        """
        response = jsonify({'orders': orders})
        if len(orders) == 0:
            return jsonify({'message': 'No orders have been placed yet'})
        return response
    
    def post(self):
        """
        method to post a question
        """
        order_id = len(orders) + 1
        order_date = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p")
        order_status = 'submitted'
        args = self.reqparse.parse_args()
        client_name = args['client']
        client_name = client_name.strip()
        response = Orders(order_id, client_name, args['contact'], args['order_item'],\
         args['price'], order_date, order_status)
        response = response.to_json()
        if response:
            if not re.match(r"^[a-zA-Z ]+$", client_name):
                return make_response(jsonify({'message': 'Username should only have letters'}), 400)
            if not re.match(r"^[0-9a-zA-Z ]+$", args['order_item']):
                return make_response(jsonify({'message': 'Contact can only be digits'}), 400)
            orders.append(response)
            return make_response(jsonify({'message': 'Order has been placed'}), 201)
        return make_response(jsonify({'message': 'Please enter a valid order'}), 400)

class SpecificOrder(Resource):
    """
    class handles methods for specific order
    """
    def __init__(self):
        """
        constructor method for the class
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('order_status', type=str, required=True,\
         help='please provide your name')

    def get(self, order_id):
        """
        method to get a specific question
        :param order_id:
        :return: order
        """
        for order in orders:
            if order['order_id'] == order_id:
                return order
        return make_response(jsonify({'message': 'Order not found'}), 404)
    
    def put(self, order_id):
        """
        method to update order-status
        :param order_id:
        """
        for order in orders:
            if order['order_id'] == order_id:
                args = self.reqparse.parse_args()
                response = args['order_status']
                if response:
                    if not re.match(r"^[a-zA-Z ]+$", response):
                        return make_response(jsonify({'message': 'Order status should only have letters'}), 400)
                    order['order_status'] = response
                    return make_response(jsonify({'message': 'order status updated'}), 201)
                return make_response(jsonify({'message': 'Please enter a valid order status'}), 400)
    
    def delete(self, order_id):
        """
        method deletes a specific order
        """
        for order in orders:
            if order['order_id'] == order_id:
                orders.remove(order)
                return jsonify({'message': 'Order deleted'})
        return make_response(jsonify({'message': 'Order not available'}), 404)

api.add_resource(OrdersHandler, '/orders')
api.add_resource(SpecificOrder, '/orders/<int:order_id>')
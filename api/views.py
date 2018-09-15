"""
module views
"""
import re
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
         help='please provide your contact')
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
        order_status = 'submitted'
        args = self.reqparse.parse_args()
        response = Orders(order_id, args['client'], args['contact'], args['order_item'],\
         args['price'], order_status)
        response = response.to_json()
        if response:
            client_name = args['client']
            client_name = client_name.strip()
            if not re.match(r"^[a-zA-Z]+$", client_name):
                return make_response(jsonify({'message': 'Username should only have letters'}), 400)
            orders.append(response)
            return make_response(jsonify({'message': 'Order has been placed'}), 201)
        return make_response(jsonify({'message': 'Order not placed'}), 400)

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
        return make_response(jsonify({'message': 'order not found'}), 404)

api.add_resource(OrdersHandler, '/orders')
api.add_resource(SpecificOrder, '/orders/<int:order_id>')
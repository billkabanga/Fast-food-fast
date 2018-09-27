"""
module views
"""
import re
from flask import jsonify, Blueprint, make_response
from flask_restful import Api, Resource, reqparse
from .models import Orders

orders_blue_print = Blueprint('ord_bp', __name__, url_prefix='/api/v1')
api = Api(orders_blue_print)

class OrdersHandler(Resource):
    """Class handles methods for all orders"""
    def __init__(self):
        """constructor method for the class"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('client', type=str, required=True,\
         help='please provide your name')
        self.reqparse.add_argument('contact', type=str, required=True,\
         help='please provide your contact(digits)')
        self.reqparse.add_argument('order_item', type=str, required=True,\
         help='please provide your order')
        self.reqparse.add_argument('price', type=int, required=True,\
         help='please enter the price')
    def get(self):
        """
        method to fetch all orders
        """
        response = jsonify({'orders': Orders.get_all()})
        if Orders.is_empty():
            return jsonify({'message': 'No orders have been placed yet'})
        return response
    def post(self):
        """
        method to post a question
        """
        args = self.reqparse.parse_args()
        if not re.match(r"^[a-zA-Z ]+$", args['client']):
            return make_response(jsonify({'message': 'Username should only have letters'}), 400)
        if not re.match(r"^[0-9a-zA-Z ]+$", args['order_item']):
            return make_response(
                jsonify({'message': 'order item can only have letters and digits'}), 400
                )
        if not re.match(r"^07[015789]\d{7}$", args['contact']):
            return make_response(jsonify({'message': 'Contact can only have 10 digits'}), 400)
        client_name = args['client']
        client_name = client_name.strip()
        response = Orders(client_name, args['contact'], args['order_item'],\
         args['price'])
        response = response.to_json()
        Orders.add_order(response)
        return make_response(jsonify({'message': 'Order has been placed'}), 201)

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
        order = Orders.get_by_id(order_id)
        if order:
            return jsonify({'order': order})
        return make_response(jsonify({'message': 'Order not found'}), 404)
    def put(self, order_id):
        """
        method to update order-status
        :param order_id:
        """
        args = self.reqparse.parse_args()
        response = args['order_status']
        if not re.match(r"^[a-zA-Z ]+$", response):
            return make_response(jsonify({'message': 'Order status should only have letters'}), 400)
        order = Orders.get_by_id(order_id)
        if order:
            order['order_status'] = response
            return make_response(jsonify({'message': 'order status updated'}), 201)
        return make_response(jsonify({'message': 'Order does not exist'}), 400)
    def delete(self, order_id):
        """
        method deletes a specific order
        """
        order = Orders.get_by_id(order_id)
        if order:
            Orders.delete_order(order_id)
            return jsonify({'message': 'Order deleted'})
        return make_response(jsonify({'message': 'Order not available'}), 404)
api.add_resource(OrdersHandler, '/orders')
api.add_resource(SpecificOrder, '/orders/<int:order_id>')

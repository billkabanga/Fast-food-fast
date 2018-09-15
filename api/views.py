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

api.add_resource(OrdersHandler, '/orders')
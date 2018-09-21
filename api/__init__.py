"""
module init
"""
from flask import Flask, jsonify, make_response
from config import DevelopmentConfig
from .views import orders_blue_print

def page_not_found(error):
    """
    function for custom error handling
    """
    return make_response(jsonify({'message':'Page not found'}), 404)

def create_app(DevelopmentConfig):
    """
    Function create_app:
    creates app and gives it the import name
    holds the configuration being used.
    registers the orders blueprint
    registers error handler for 404 URL error
    :return: app:
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(orders_blue_print)
    app.register_error_handler(404, page_not_found)

    return app
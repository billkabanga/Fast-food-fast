"""
module init
"""
from flask import Flask
from config import DevelopmentConfig
from .views import orders_blue_print


def create_app(DevelopmentConfig):
    """
    Function create_app:
    creates app and gives it the import name
    holds the configuration being used.
    registers the orders blueprint
    :return: app:
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(orders_blue_print)

    return app
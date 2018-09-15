"""
module tests
"""
import unittest
from api import create_app
from config import TestingConfig

BASE_URL = 'http://127.0.0.1:5000/api/v1/orders'

class OrdersTest(unittest.TestCase):
    """
    class for unittests for the apis
    """
    def setUp(self):
        """
        method sets up an instance of the app for the tests
        also creates a client to run the tests
        """
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
    def test_get_all_orders(self):
        """
        method tests if all orders are fetched
        asserts response code is 200
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            response = client.get(BASE_URL)
            self.assertEqual(response.status_code, 200)
    def test_post_order(self):
        """
        method tests if an order has been placed
        asserts that response code is 201
        """
        with self.client as client:
            response = client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            self.assertEqual(response.status_code, 201)
"""
module tests
"""
import unittest
import json
from api import create_app
from config import TestingConfig

BASE_URL = '/api/v1/orders'

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
    def test_empty_list(self):
        """
        method tests if all orders list is empty
        asserts response message is 'No orders have been placed yet'
        """
        with self.client as client:
            response = client.get(BASE_URL)
            response_data = json.loads(response.data.decode())
            self.assertIn('No orders have been placed yet', response_data['message'])
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
    def test_invalid_name_input(self):
        """
        method tests for invalid name input
        asserts that response code is 400
        """
        with self.client as client:
            response = client.post(BASE_URL, json=dict(client='Bill4568', contact='0784318356', \
            order_item="chips", price="2000"))
            self.assertEqual(response.status_code, 400)
    def test_invalid_contact_input(self):
        """
        method tests for invalid contact input
        asserts that response code is 400
        """
        with self.client as client:
            response = client.post(BASE_URL, json=dict(client='Bill', contact='078dchvsdgcs8', \
            order_item="chips", price="2000"))
            self.assertEqual(response.status_code, 400)
    def test_invalid_order_item(self):
        """
        method tests for invalid order item
        asserts that response code is 400
        """
        with self.client as client:
            response = client.post(BASE_URL, json=dict(client='James Angero',contact='0784318356', \
            order_item="****-*-*", price="2000"))
            self.assertEqual(response.status_code, 400)
    def test_get_specific_order(self):
        """
        method tests if specific order is fetched
        asserts status code is 200
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            response = client.get(BASE_URL+'/2')
            self.assertEqual(response.status_code, 200)
    def test_order_not_found(self):
        """
        method tests if specific order is fetched
        asserts status code is 404
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            response = client.get(BASE_URL+'/560')
            self.assertEqual(response.status_code, 404)
    def test_update_status(self):
        """
        method tests if order status is updated
        asserts status code is 201
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.get(BASE_URL+'/2')
            response = client.put(BASE_URL+'/2', json=dict(order_status='Accepted'))
            self.assertEqual(response.status_code, 201)
    def test_status_not_updated(self):
        """
        method tests if order status is not updated
        asserts status code is 400
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.get(BASE_URL+'/2')
            response = client.put(BASE_URL+'/2', json=dict())
            self.assertEqual(response.status_code, 400)
    def test_status_no_updated(self):
        """
        method tests if order status is not updated
        asserts status code is 400
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.get(BASE_URL+'/56')
            response = client.put(BASE_URL+'/56', json=dict(order_status='Accepted'))
            self.assertEqual(response.status_code, 400)
    def test_invalid_order_status(self):
        """
        method tests if order status is invalid
        asserts status code is 400
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.get(BASE_URL+'/2')
            response = client.put(BASE_URL+'/2', json=dict(order_status='***-/-*'))
            self.assertEqual(response.status_code, 400)
    def test_wrong_url(self):
        """
        method tests if a wrong URL is supplied
        asserts that response message is 'Wrong URL entry'
        """
        with self.client as client:
            response = client.post(BASE_URL+'/-*+*+', json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            response_data = json.loads(response.data.decode())
            self.assertIn('Wrong URL entry', response_data['message'])
    def test_order_deleted(self):
        """
        method tests if order is deleted
        asserts message 'order deleted'
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.post(BASE_URL, json=dict(client='Jude', contact='0784318356', \
            order_item="rice", price="2000"))
            response = client.delete(BASE_URL+'/3')
            response_data = json.loads(response.data.decode())
            self.assertIn('Order deleted', response_data['message'])
    def test_order_not_deleted(self):
        """
        method tests if order is not deleted
        asserts message 'order deleted'
        """
        with self.client as client:
            client.post(BASE_URL, json=dict(client='Bill', contact='0784318356', \
            order_item="chips", price="2000"))
            client.post(BASE_URL, json=dict(client='James', contact='0784318356', \
            order_item="rice", price="2000"))
            client.post(BASE_URL, json=dict(client='Jude', contact='0784318356', \
            order_item="rice", price="2000"))
            response = client.delete(BASE_URL+'/4586746')
            response_data = json.loads(response.data.decode())
            self.assertIn('Order not available', response_data['message'])

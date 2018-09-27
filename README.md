[![Build Status](https://travis-ci.org/billkabanga/Fast-food-fast.svg?branch=API-feature)](https://travis-ci.org/billkabanga/Fast-food-fast)
[![Coverage Status](https://coveralls.io/repos/github/billkabanga/Fast-food-fast/badge.svg?branch=API-feature)](https://coveralls.io/github/billkabanga/Fast-food-fast?branch=API-feature)
[![Maintainability](https://api.codeclimate.com/v1/badges/177b99474b3084f12799/maintainability)](https://codeclimate.com/github/billkabanga/Fast-food-fast/maintainability)

# Fast-food-fast
This is a food delivery service app for a restaurant. An app where customers can place orders for food and get served instantly.

## Getting started
This following information will help you setup and run the application on your local machine.

## Prerequisites
You will need the following:
* Internet
* HTML5
* GIT
* IDE
* Postman

## Project links:
**User Interface:** The user interface pages for this project are hosted on gh-pages on the url: (https://billkabanga.github.io/Fast-food-fast/UI/index.html)
The code for the UI templates can be accessed using the URL: (https://github.com/billkabanga/Fast-food-fast/tree/UI-feature)

**API endpoints:** The code for the endpoints can be found using the URL: (https://github.com/billkabanga/Fast-food-fast/tree/API-feature)

## Project functionality
**Interface**
* User(client/admin) can signup and login.
* Client can order for food.
* Admin can see a list of orders.
* Admin can accept and decline offers.
* Admin can mark orders as completed.
* Client can see a history of ordered food.

**API endpoints**
* Get a list of all orders.
* Fetch a specific order.
* Place a new order.
* Update the status of an order.

## Getting the application on the local machine.
Clone the remote repository to your local machine using the following command: `git clone https://github.com/billkabanga/Fast-food-fast.git`
You can now access the project on your local machine by pointing to the local repository using `cd` and `code .` if using Visual Studio code will open the code location.
Create a virtual environment in the local repository using the following code: `python -3 -m venv env`
Activate the virtual environment: `env/scripts/activate`

## Installing dependencies.
To install all the required extensions for project, use the following command: `pip install -r requirements.txt`

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

|     Endpoint                        | Verb          | Action                     |   Parameters     |
| ----------------------------------- |:-------------:|  ------------------------- | ----------------- |
| /api/v1/orders                      | GET           | Get all orders          | none   |
| /api/v1/orders/<int:orderId>        | GET           | Get a specific order          | order_id(URL)  |
| /api/v1/orders                   | POST          | Place a new order             | client,contact,order_item,price |
| /api/v1/orders/<int:orderId>| PUT          | Update status of an order | order_status,order_id(URL)  |
| /api/v1/orders/<int:orderId> | DELETE     | Delete a specific order | order_id(URL) |

**Running unittests for the API endpoints**
Use the `pytest tests --cov=api --cov-report term-missing` command to run the tests and get the coverage report.

## Deployment:
The app has been hosted on heroku, use the following link (https://bill-fast-food-fast.herokuapp.com/api/v1/orders)

## Built with:
**User Interface**
* HTML5
* CSS3

**API endpoints**
* Python 3
* Flask
* Flask-restful

## Author:
Author of this project-Twinomuhwezi Kabanga Bill, 
a young aspiring software developer utilising each day as one to learn and provide solutions to world problems.
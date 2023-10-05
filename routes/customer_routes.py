from flask import Blueprint
from controllers.customer_controllers import new, create_customer


customer_routes = Blueprint('customer_routes', __name__)

customer_routes.route('/customer/new')(new)
customer_routes.route('/customer/create',  methods=["POST"])(create_customer)
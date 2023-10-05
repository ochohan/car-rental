from flask import Blueprint

from controllers.car_controllers import index, search

car_routes = Blueprint('car_routes', __name__)


car_routes.route('/')(index)
car_routes.route('/search')(search)
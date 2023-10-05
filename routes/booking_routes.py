from flask import Blueprint
from controllers.booking_controllers import index, retrieve_booking, make_booking, confirm_booking

booking_routes = Blueprint('booking_routes', __name__)

booking_routes.route('/booking/makebooking')(index)
booking_routes.route('/booking/get', methods=["POST"])(retrieve_booking)

booking_routes.route('/booking')(index)

booking_routes.route("/make_booking", methods=["POST"])(make_booking)
booking_routes.route("/confirm_booking", methods=["POST"])(confirm_booking)

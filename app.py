from flask import Flask, request
import os
#Importing all the routes 
from routes.car_routes import car_routes
from routes.booking_routes import booking_routes
from routes.customer_routes import customer_routes
# from routes.users_routes import users_routes

app = Flask(__name__)
app.secret_key = os.urandom(24)


#Register all the routes in main app.py file
app.register_blueprint(car_routes)
app.register_blueprint(booking_routes)
app.register_blueprint(customer_routes)
# app.register_blueprint(users_routes)

from flask import render_template, request, redirect, make_response
from models.cars import all_cars, get_car


def index():
    
    return render_template('index.html')


def search():
    rental_start_date = request.args.get('pick-up-date')
    rental_end_date = request.args.get('drop-off-date')
    cars = all_cars(rental_start_date, rental_end_date)

    # Create a response object by rendering a template
    response = make_response(render_template('search.html', cars=cars))

    # Set cookies on the response
    response.set_cookie('rental_start_date', rental_start_date)
    response.set_cookie('rental_end_date', rental_end_date)

    return response

def find_car(car_id):
    car_details = get_car(car_id)
    return car_details
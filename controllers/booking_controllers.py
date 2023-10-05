from flask import render_template, request, redirect, make_response, request, url_for, flash
from models.booking import get_booking, create_booking
from models.customers import create_customers
from controllers.car_controllers import find_car
from helper.function import send_email, calculate_days_between






def index():
    return render_template('booking/manage.html')

def retrieve_booking():
    rental_id = request.form.get('booking_ref_number')
    last_name = request.form.get('last_name')
    response = get_booking(rental_id, last_name)
    if response:
        rental_info = response[0] 
        return render_template('booking/change_booking.html', rental_info=rental_info)
    else:
        return "Booking not found"  



def make_booking():
    car_id = request.form.get("car_id")
    
    rental_start_date = request.cookies.get("rental_start_date")
    rental_end_date = request.cookies.get("rental_end_date")

    if rental_start_date is None or rental_end_date is None:
        return redirect('/')

    booking_days = calculate_days_between(rental_start_date, rental_end_date)
    car = find_car(car_id)
    price_per_day = car['price_per_day']
    price_total = int(price_per_day) * int(booking_days)
    print(price_total, "The total is")

    return render_template("booking_details.html", price_total=price_total, booking_days=booking_days, car_id=car_id, rental_start_date=rental_start_date, rental_end_date=rental_end_date)


def customer(first_name, last_name, email, phone_number):
    customer_id = create_customers(first_name, last_name, email, phone_number)
    customer_id = customer_id
    return customer_id[0]['customer_id']
    



def confirm_booking():
    rental_start_date = request.cookies.get("rental_start_date")
    rental_end_date = request.cookies.get("rental_end_date")
    if rental_start_date is None or rental_end_date is None:
        return redirect('/')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    
    # Create a customer and get the customer_id
    customer_id = customer(first_name, last_name, email, phone_number)
    
    
    # # Get the car_id and rental dates from cookies
    car_id = request.form.get("car_id")
    rental_start_date = request.cookies.get("rental_start_date")
    rental_end_date = request.cookies.get("rental_end_date")
    print(rental_start_date)
    
    # Create a booking and get the rental_id
    rental = create_booking(customer_id, car_id, rental_start_date, rental_end_date)
    rental = rental[0]
    print(rental)

    car = find_car(car_id)


    #Sending a confirmation email
    subject = 'Booking Confirmation'
    html_content = render_template("booking_confirmation.html", car=car, rental = rental, first_name = first_name, last_name = last_name, email = email, phone_number = phone_number )
    
    if send_email(email, subject, html_content ):
        flash('Booking made and email sent!', 'success')
    else:
        flash('Error sending email', 'error')

    # Return the rental_id
    return render_template("booking_confirmation.html", car=car, rental = rental, first_name = first_name, last_name = last_name, email = email, phone_number = phone_number )


# def manage_booking():
#     # rental_id = 
#     # last_name =
#     get_booking(rental_id,last_name)

# // Calculate days
# 


# # Example usage
# start_date = "2023-06-23"
# end_date = "2023-06-30"

# days_between = calculate_days_between(start_date, end_date)
# print(f"Number of days between {start_date} and {end_date}: {days_between}")
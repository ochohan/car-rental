from flask import render_template, request, redirect, make_response
from models.customers import create_customers


def new():
    return render_template('customers/new.html')


def create_customer():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    customer_id = create_customers(first_name, last_name, email, phone_number)
    
    customer_id = str(customer_id[0]["customer_id"])
    response = make_response(f'{customer_id}')
    response.set_cookie('customer_id', customer_id)

    return response
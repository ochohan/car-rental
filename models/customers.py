from db.db import sql


def create_customers(first_name, last_name, email, phone_number):

  return sql( 'INSERT INTO customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s) RETURNING customer_id', [first_name, last_name, email, phone_number])
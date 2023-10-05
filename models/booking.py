from db.db import sql
def get_booking(rental_id,last_name):
    return sql("""
                    SELECT r.rental_id, r.rental_start_date, r.rental_end_date, r.rental_price
                    FROM rentals r
                    JOIN customers c ON r.customer_id = c.customer_id
                    WHERE r.rental_id = %s AND c.last_name = %s""",[rental_id,last_name])



# Function to create a new rental booking
def create_booking(customer_id, car_id, rental_start_date, rental_end_date):
    return sql('INSERT INTO rentals (customer_id, car_id, rental_start_date, rental_end_date) VALUES (%s, %s, %s, %s) RETURNING *', [customer_id, car_id, rental_start_date, rental_end_date])

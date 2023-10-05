from db.db import sql


def all_cars(pick_up, drop_off):
    return sql(
        """SELECT *
            FROM cars
            WHERE car_id NOT IN (
            SELECT car_id
            FROM rentals
            WHERE rental_start_date <= %s
              AND rental_end_date >= %s
            )""",
                [drop_off, pick_up],
            )


def get_car(car_id):
  car = sql("SELECT * FROM cars WHERE car_id = %s", [car_id])
  return car[0]

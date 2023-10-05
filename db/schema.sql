CREATE SEQUENCE customer_id_seq START 50000;

CREATE TABLE customers (
  customer_id VARCHAR(10) PRIMARY KEY DEFAULT ('C' || nextval('customer_id_seq')),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100),
  phone_number VARCHAR(20)
);
-- Cars table
CREATE TABLE cars (
  car_id SERIAL PRIMARY KEY,
  make VARCHAR(50),
  model VARCHAR(50),
  year INT,
  color VARCHAR(50),
  price_per_day DECIMAL(10, 2)
);

-- Rentals table
CREATE TABLE rentals (
  rental_id VARCHAR(20) PRIMARY KEY,
  customer_id VARCHAR(10),
  car_id INT,
  rental_start_date DATE,
  rental_end_date DATE,
  rental_price DECIMAL(10, 2),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (car_id) REFERENCES cars (car_id)
);



-- Function for rental_id generator
CREATE SEQUENCE rental_id_seq START 1;

-- Create a function to generate the rental ID
CREATE OR REPLACE FUNCTION generate_rental_id()
  RETURNS TRIGGER AS $$
  BEGIN
    NEW.rental_id := 'RN' || to_char(CURRENT_DATE, 'YYYYMMDD') || nextval('rental_id_seq');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;

-- Create a trigger to automatically generate the rental ID before inserting a new row
CREATE TRIGGER rental_id_trigger
  BEFORE INSERT ON rentals
  FOR EACH ROW
  EXECUTE FUNCTION generate_rental_id();


CREATE OR REPLACE FUNCTION public.calculate_rental_price()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
DECLARE
  v_price_per_day DECIMAL(10, 2);
  v_rental_days INT;
BEGIN
  -- Fetch the price_per_day for the rented car from the cars table
  SELECT price_per_day INTO v_price_per_day
  FROM cars
  WHERE car_id = NEW.car_id;

  -- Calculate the number of rental days
  v_rental_days := NEW.rental_end_date - NEW.rental_start_date;

  -- Calculate the rental price based on the v_price_per_day and v_rental_days
  NEW.rental_price := v_price_per_day * v_rental_days;

  RETURN NEW;
END;
$function$

/*
Used in the Python part of the session.
Sample full set of SQL for the person table.
This file can be run in an Adminer window vs MySQL.
The `my_db_app_solution.py` file assumes this is the SQL that has been run in Adminer.
...and that the `databases/handouts/docker-compose.yml` matches what is running in docker.
*/

DROP DATABASE IF EXISTS mini;

CREATE DATABASE mini;

-- Select test database in the DB dropdown

CREATE TABLE products (
  product_id INTEGER GENERATED ALWAYS AS IDENTITY,
  product_name VARCHAR(255) NOT NULL,
  product_price FLOAT NOT NULL,
  PRIMARY KEY(product_id)
);

CREATE TABLE couriers (
  courier_id INTEGER GENERATED ALWAYS AS IDENTITY,
  courier_name VARCHAR(255) NOT NULL,
  courier_number INTEGER NOT NULL,
  PRIMARY KEY(courier_id)
);

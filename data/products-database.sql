

DROP DATABASE IF EXISTS mini;

CREATE DATABASE mini;

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

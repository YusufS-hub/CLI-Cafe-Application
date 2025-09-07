import psycopg2 as psycopg
import os
from dotenv import load_dotenv
import csv


load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


path = '..\\data\\couriers.csv'
path1 = '..\\data\\products.csv'
path2 = '..\\data\\orders.csv'

def view_products():
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT product_id, product_name, product_price FROM products ORDER BY product_id ASC")
            products = cursor.fetchall()

            print("\n--- Products List ---")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: £{product[2]:.2f}")

            cursor.close()

    except Exception as e:
        print("Error retrieving products:", e)

def view_couriers():
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            cursor = connection.cursor()
           
            print('Selecting Records...')
            cursor.execute("SELECT courier_id, courier_name, courier_number FROM couriers ORDER BY courier_id ASC")
            couriers = cursor.fetchall()

            print("\n--- Couriers List ---")
            for courier in couriers:
                print(f"ID: {courier[0]}, Name: {courier[1]}, Phone Number: {courier[2]}")

            cursor.close()

    except Exception as e:
        print("Error retrieving couriers:", e) 


def view_orders():
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            cursor = connection.cursor()
           
            print('Selecting Records...')
            cursor.execute("SELECT order_id, customer_name, customer_address, customer_phone, status, items FROM orders ORDER BY order_id ASC")
            orders = cursor.fetchall()

            print("\n--- Orders List ---")
            for order in orders:
                print(f"ID: {order[0]}, Name: {order[1]}, Address: {order[2]}, Phone Number: {order[3]}, Status: {order[4]}, Items: {order[5]} ")

            cursor.close()

    except Exception as e:
        print("Error retrieving orders:", e)            

    
def insert_records_products():
    try:
        print('Opening connection...')
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:

            print('Opening cursor...')
            cursor = connection.cursor()

            print('Loading data from CSV...')
            with open(path1, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = [(row['product_name'], (row['product_price'])) for row in reader]

            print('Inserting records...')
            insert_sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
            cursor.executemany(insert_sql, rows)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted.")

            print('Selecting all records...')
            cursor.execute('SELECT product_name, product_price FROM products ORDER BY product_id ASC')
            row = cursor.fetchall()

            print('Displaying all records...')
            for row in row:
                print(f'Courier_Name: {row[0]}, Courier_Number: {row[1]}')

            cursor.close()
    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')

def insert_records_order():
    try:
        print('Opening connection...')
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:

            print('Opening cursor...')
            cursor = connection.cursor()

            print('Loading data from CSV...')
            with open(path2, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = [((
                    row['customer_name'],
                    row['customer_address'],
                    (row ['customer_phone']),
                    row['status'],
                     (row['items']),
                ))for row in reader]

            print('Inserting records...')
            insert_sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, status, items) VALUES (%s, %s,%s,%s,%s)"
            cursor.executemany(insert_sql, rows)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted.")

            print('Selecting all records...')
            cursor.execute('SELECT customer_name, customer_address, customer_phone, status, items FROM orders ORDER BY order_id ASC')
            row = cursor.fetchall()

            print('Displaying all records...')
            for row in row:
                print(f'Customer_Name: {row[0]}, Customer_Address: {row[1]}, Customer_Phone: {row[2]}, status {row[3]}, items {row[4]}' )

            cursor.close()
    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')
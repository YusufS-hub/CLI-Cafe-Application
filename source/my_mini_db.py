
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
        print("Error retrieving products:", e) 


            

    
def insert_records():
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
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = [(row['courier_name'], (row['courier_number'])) for row in reader]

            print('Inserting records...')
            insert_sql = "INSERT INTO couriers (courier_name, courier_number) VALUES (%s, %s)"
            cursor.executemany(insert_sql, rows)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted.")

            print('Selecting all records...')
            cursor.execute('SELECT courier_name, courier_number FROM couriers ORDER BY courier_id ASC')
            row = cursor.fetchall()

            print('Displaying all records...')
            for row in row:
                print(f'Courier_Name: {row[0]}, Courier_Number: {row[1]}')

            cursor.close()
    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')


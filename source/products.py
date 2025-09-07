import psycopg2 
import os
from dotenv import load_dotenv
import csv
import my_mini_db


# Main List of Products


Product_Path = '\\Users\\ysala\\OneDrive\\Documents\\DE-Gen\\yusuf-portfolio\\mini_project\\Week-5\\data\\products.csv'
products_list = []


def clear_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')


# Loading the product menu and getting users input in the product menu
def get_product_menu():
    print('''
╔═════════════════════════════════╗
║         Products Menu           ║
╠═════════════════════════════════╣
║  [0] Return to Main Menu        ║
║  [1] View Products              ║
║  [2] Add Product                ║
║  [3] Update Product             ║
║  [4] Delete Product             ║
╚═════════════════════════════════╝
          ''')
    try:
        return int(input("Enter your choice: "))
    except (ValueError,TypeError):
        print("Invalid Input Enter a Number")
        return



# Adding a append function
def create_product():
    name = input("Enter Name for the product: ")
    try:
        price = float(input("Enter a price for product: "))
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        return

    new_dict = {"name": name, "price": price}
    products_list.append(new_dict)


    try:
        conn = connect_db()
        cursor = conn.cursor()

        insert_sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
        cursor.execute(insert_sql, (name, price))

        conn.commit()
        cursor.close()
        conn.close()
        print("Product added to database successfully.")
    except Exception as e:
        print("Failed to insert product into database:", e)

# Update the db at a certain index 
def update_product():
    clear_menu()
    my_mini_db.view_products()
    
    try:
        user_index = int(input("Enter the ID of the product you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    new_prod_name = input("Enter new name for the product: ")
    try:
        new_prod_price = float(input("Enter new price for the product: "))
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        update_sql = """
            UPDATE products
            SET product_name = %s, product_price = %s
            WHERE product_id = %s
        """
        cursor.execute(update_sql, (new_prod_name, new_prod_price, user_index))

        conn.commit()
        cursor.close()
        conn.close()
        print("Product updated in the database successfully.")

    except Exception as e:
        print("Failed to update product in the database:", e)



# Delete the at a certain index
def delete_product():
    clear_menu()
    my_mini_db.view_products()
    try:
        user_index = input("Enter the ID value of the product you want to delete: ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    try:
        conn = connect_db()
        cursor = conn.cursor()

        confirm = input(f"Are you sure you want to delete product ID {user_index}? (y/n): ").lower()
        if confirm != 'y':
            print("Deletion cancelled.")
            return

        delete_sql = """
            DELETE FROM products
            WHERE product_id = %s
        """
        cursor.execute(delete_sql, (user_index,))

        conn.commit()
        cursor.close()
        conn.close()
        print("Product DELETED in the database successfully.")

    except Exception as e:
        print("Failed to Delete product in the database:", e)


# Saves File to the Data source and checks if products list is empty


load_dotenv()


def connect_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

def save_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Insert products into database
        insert_sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
        product_tuples = [(product['name'], product['price']) for product in products_list]
        cursor.executemany(insert_sql, product_tuples)

        conn.commit()
        print("Products were saved to the database successfully.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error saving products to the database:", e)

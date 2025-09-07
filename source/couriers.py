import psycopg2 
import os
from dotenv import load_dotenv
import my_mini_db


Couriers_Path = '\\Users\\ysala\\OneDrive\\Documents\\DE-Gen\\yusuf-portfolio\\mini_project\\Week-5\\data\\couriers.csv'
couriers = [] 


def clear_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def get_courier_menu():
    print('''
╔═════════════════════════════════╗
║         Couriers Menu           ║
╠═════════════════════════════════╣
║  [0] Return to Main Menu        ║
║  [1] View Couriers              ║
║  [2] Add Courier                ║
║  [3] Update Courier             ║
║  [4] Delete Courier             ║
╚═════════════════════════════════╝
          ''')
    try:
        return int(input("Enter your choice: "))
    except (ValueError,TypeError):
        print("Invalid Input Enter a Number")
        return

def connect_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


def create_courier():
    new_courier = input("Enter a new courier name you want to add: ")
    new_courier_phone = int(input("Enter a new courier phone number you want to add: "))
    new_dict = {
        "name": new_courier,
        "phone_number": new_courier_phone
    }
    couriers.append(new_dict)

    try:
        conn = connect_db()
        cursor = conn.cursor()

        insert_sql = "INSERT INTO couriers (courier_name, courier_number) VALUES (%s, %s)"
        cursor.execute(insert_sql, (new_courier, new_courier_phone))

        conn.commit()
        cursor.close()
        conn.close()
        print("Courier added to database successfully.")
    except Exception as e:
        print("Failed to insert Courier into database:", e)



def delete_courier():
    clear_menu()
    my_mini_db.view_couriers()
    try:
        user_index = int(input("Enter the ID value of the Courier you want to delete: "))
    except (IndexError,ValueError):
        print('Invalid Input!')
    try:
        conn = connect_db()
        cursor = conn.cursor()

        confirm = input(f"Are you sure you want to delete product ID {user_index}? (y/n): ").lower()
        if confirm != 'y':
            print("Deletion cancelled.")
            return

        delete_sql = """
            DELETE FROM couriers
            WHERE courier_id = %s
        """
        cursor.execute(delete_sql, (user_index,))

        conn.commit()
        cursor.close()
        conn.close()
        print("Courier DELETED from database successfully.")
    except Exception as e:
        print("Failed to Delete Courier from database:", e)


def update_courier():
    clear_menu()
    my_mini_db.view_couriers()
    try:
        user_index = int(input("Enter the ID value of the courier you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    new_courier_name = input("Enter new name for the courier: ")
    try:
        new_courier_number = int(input("Enter new phone_number for the courier: "))
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        return
    try:
        conn = connect_db()
        cursor = conn.cursor()

        update_sql = """
            UPDATE couriers
            SET courier_name = %s, courier_number = %s
            WHERE courier_id = %s
        """
        cursor.execute(update_sql, (new_courier_name, new_courier_number, user_index))

        conn.commit()
        cursor.close()
        conn.close()
        print("Courier Updated in the database successfully.")
    except Exception as e:
        print("Failed to Update Courier in the database:", e)



def save_couriers():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Insert couriers into database
        insert_sql = "INSERT INTO couriers (courier_name, courier_number) VALUES (%s, %s)"
        courier_tuples = [(courier['name'], courier['number']) for courier in couriers]
        cursor.executemany(insert_sql, courier_tuples)

        conn.commit()
        print("Couriers were saved to the database successfully.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error saving Couriers to the database:", e)
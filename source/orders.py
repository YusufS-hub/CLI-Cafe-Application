import psycopg2 
import os
from dotenv import load_dotenv
import my_mini_db

# Main Dictionary of Orders
Orders_Path = '\\Users\\YusufS(DE-X6-LM)\\Documents\\DE-Gen\\yusuf-portfolio\\mini_project\\Week-6\\data\\orders.csv'
orders_list = []

def clear_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


def get_order_menu():
    print('''
╔═════════════════════════════════╗
║         Couriers Menu           ║
╠═════════════════════════════════╣
║  [0] Return to Main Menu        ║
║  [1] View Orders                ║
║  [2] Add Order                  ║
║  [3] Update Order Status        ║
║  [4] Update Order               ║
║  [5] Delete Order               ║
╚═════════════════════════════════╝
          ''')
    return int(input("Enter your choice: "))


# def view_order():
#      with open(Orders_Path, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             print(row)
   
def create_order():
    name = input("Enter New Customer Name: ")
    address = input("Enter New Customer Address: ")
    phone = int(input("Enter New Phone Number: "))
    items = str(input('Enter the index of the items orders: '))

    new_dict = {
        'customer_name': name,
        'customer_address' : address,
        'customer_phone': phone,
        'status': 'Preparing',
        'items': items

    }

    try:
        conn = connect_db()
        cursor = conn.cursor()

        insert_sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, items) VALUES (%s, %s,%s,%s)"
        cursor.execute(insert_sql, (name, address, phone, items))

        conn.commit()
        cursor.close()
        conn.close()
        print("Order added to database successfully.")
    except Exception as e:
        print("Failed to insert Order into database:", e)

                    


def update_order():
    clear_menu()
    my_mini_db.view_orders()
    try:
        choice = int(input("Enter the ID of the order you want to update: "))
    except (ValueError, IndexError):
        print("Invalid order selection.")
        return

    print("Press Enter to leave a field unchanged.")

    try:
        new_customer_name = input("Enter New Customer Name: ")
        new_customer_address = input("Enter New Customer Address: ")
        new_customer_phone = input("Enter New Phone Number: ")
        new_items = str(input("Enter New items: "))
    except Exception:
        print('Invalid Input! Try Again')
        return


    try:
        conn = connect_db()
        cursor = conn.cursor()

        update_sql = """
            UPDATE orders
            SET customer_name = %s, customer_address = %s, customer_phone = %s, items = %s
            WHERE order_id = %s
        """
        cursor.execute(update_sql, (new_customer_name, new_customer_address, new_customer_phone, new_items , choice))

        conn.commit()
        cursor.close()
        conn.close()
        print("Order Updated in the database successfully.")
    except Exception as e:
        print("Failed to Update Order in the database:", e)

    



    
def update_order_status():
    for index, order in enumerate(orders_list):
        print(index, order['customer_name'], order['customer_address'],
              order['customer_phone'], order['courier'],
              order['status'], order['items'])
    try:
        user_idx = int(input("Enter the index value of the order you want to update: "))
        selected_order = orders_list[user_idx]
    except (ValueError, IndexError):
        print("Invalid order selection.")
        return

    print("+-------------------------+")
    print("| 0 - Cancel              |")
    print("| 1 - Preparing           |")
    print("| 2 - Out for Delivery    |")
    print("| 3 - Delivered           |") 
    print("+-------------------------+")

    try:
        while True:
            choice = int(input(f"Choose (0-3) For New status order (current: {selected_order['status']}): "))
            if choice == 0:
                return
            elif choice == 1:
                orders_list[user_idx]['status'] = 'Preparing'
                break
            elif choice == 2:
                orders_list[user_idx]['status'] = 'Out for Delivery'
                break
            elif choice == 3:
                orders_list[user_idx]['status'] = 'Delivered'
                break
            else:
                print('Invalid Input! Try Again')
    except Exception:
        print('Error Updating Status!')

    try:
        with open(Orders_Path, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
            for order in orders_list:
                csv_writer.writerow([
                    order['customer_name'],
                    order['customer_address'],
                    order['customer_phone'],
                    order['courier'],
                    order['status'],
                    order['items']
                ])
    except Exception as e:
        print('Error Updating Orders!', e)
        


def delete_order():
    for index, order in enumerate(orders_list):
        print(index, order['customer_name'], order['customer_address'],
              order['customer_phone'], order['courier'],
              order['status'], order['items'])
    try:
        customer_index = int(input("Enter the index value of the customer you want to delete: "))
        orders_list.pop(customer_index)
    except Exception:
        print('Error in Deleting Order! Try Again ')
        return
    try:
        with open(Orders_Path, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
            for order in orders_list:
                csv_writer.writerow([
                    order['customer_name'],
                    order['customer_address'],
                    order['customer_phone'],
                    order['courier'],
                    order['status'],
                    order['items']
                ])
    except Exception as e:
        print('Error Deleting Orders!', e)

def save_orders():
    try:
        with open(Orders_Path, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
            for order in orders_list:
                csv_writer.writerow([
                    order['customer_name'],
                    order['customer_address'],
                    order['customer_phone'],
                    order['courier'],
                    order['status'],
                    order['items']
                ])
    except Exception as e:
        print('Error Saving Orders!', e)
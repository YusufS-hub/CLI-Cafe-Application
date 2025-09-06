import csv

Orders_Path = '..\\data\\orders.csv'
orders_list = []


def load_orders(file=Orders_Path):
    try:
        with open(Orders_Path, 'r') as file:
            orders_data = csv.DictReader(file)
            for row in orders_data:
                orders_list.append(({
                    'customer_name': row['customer_name'],
                    'customer_address': row['customer_address'],
                    'customer_phone': int(row ['customer_phone']),
                    'courier': row['courier'],
                    'status': row['status'],
                    'items': (row['items']),
                }))
    except FileNotFoundError:
        print("Courier file not found. Starting with an empty courier list.")
    return orders_list



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


orders_list = load_orders(file=Orders_Path)


def view_order():
     with open(Orders_Path, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
   
def create_order():
    name = input("Enter New Customer Name: ")
    address = input("Enter New Customer Address: ")
    phone = int(input("Enter New Phone Number: "))
    courier = input('Enter the index of the courier delivering the order: ')
    items = str(input('Enter the index of the items orders: '))

    new_dict = {
        'customer_name': name,
        'customer_address' : address,
        'customer_phone': phone,
        'courier': courier,
        'status': 'Preparing',
        'items': items

    }
    orders_list.append(new_dict)
    with open(Orders_Path, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow([new_dict['customer_name'], new_dict["customer_address"], 
                             new_dict['customer_phone'], new_dict["courier"],
                             new_dict["status"],new_dict["items"]])


def update_order():
    for index, order in enumerate(orders_list):
        print(index, order['customer_name'], order['customer_address'],
              order['customer_phone'], order['courier'],
              order['status'], order['items'])
    try:
        choice = int(input("Enter the index of the order you want to update: "))
        selected_order = orders_list[choice]
    except (ValueError, IndexError):
        print("Invalid order selection.")
        return

    print("Press Enter to leave a field unchanged.")

    try:
        new_customer_name = input(f"New customer name (current: {selected_order['customer_name']}): ")
        new_customer_address = input(f"New address (current: {selected_order['customer_address']}): ")
        new_customer_phone = input(f"New phone number (current: {selected_order['customer_phone']}): ")
        new_courier = input(f"New courier number (current: {selected_order['courier']}): ")
        new_items = str(input(f"New items (current: {selected_order['items']}): "))
    except Exception:
        print('Invalid Input! Try Again')
        return

    if new_customer_name:
        orders_list[choice]['customer_name'] = new_customer_name
    if new_customer_address:
        orders_list[choice]['customer_address'] = new_customer_address
    if new_customer_phone:
        try:
            orders_list[choice]['customer_phone'] = int(new_customer_phone)
        except ValueError:
            print("Invalid phone number. Keeping previous value.")
    if new_courier:
        orders_list[choice]['courier'] = new_courier
    if new_items:
        orders_list[choice]['items'] = new_items
    

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
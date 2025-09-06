import csv
import psycopg2 as psycopg



Product_Path = '..\\data\\products.csv'
products_list = []


def get_product_menu():
    print('''
╔═════════════════════════════════╗
║         Couriers Menu           ║
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


def load_products(file = Product_Path):
    try:
        with open(Product_Path, 'r', newline='') as file:
            products_data = csv.DictReader(file)
            for row in products_data:
                products_list.append({
                    'name': row['product_name'],
                    'price': float(row['product_price'])
                })

    except FileNotFoundError:
        print("Product file not found. Starting with an empty product list.")
    return products_list


products_list = load_products(file=Product_Path)



def create_product():
    name = input("Enter Name for the product: ")
    try:
        price = float(input("Enter a price for product: "))
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        return
    new_dict = {
        "name": name,
        "price": price
    }
    
    products_list.append(new_dict) 

    with open(Product_Path, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_dict['name'], new_dict['price']])


def update_product():
    for x, product in enumerate(products_list):
        print(x, product['name'], product['price'])
    try:
        user_index = int(input("Enter the index value of the product you want to update: "))
        if user_index < 0 or user_index >= len(products_list):
            print("Invalid index.")
            return
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
        products_list[user_index]['name'] = new_prod_name
        products_list[user_index]['price'] = new_prod_price
    except Exception:
        print("An error occurred while updating the product.")
        return
    with open(Product_Path,'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['name', 'price'])
        for product in products_list:
            csv_writer.writerow([product['name'], product['price']])


def delete_product():
    for x,product in enumerate(products_list):
       print(x, product['name'], product['price'])
    try:
        user_index1 = int(input("Enter the index value of the product you want to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    products_list.pop(user_index1)
    with open(Product_Path,'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['name', 'price'])
        for product in products_list:
            csv_writer.writerow([product['name'], product['price']])


def save_products():
    with open(Product_Path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price'])
        for row in products_list:
            writer.writerow([row['name'], row['price']])
    if len(products_list) == 0:
        print("No products to save.")
        return
    print('Products were saved successfully')


import csv
Couriers_Path = '..\\data\\couriers.csv'
couriers = [] 



# Load couriers from the file
def load_couriers(file=Couriers_Path):
    try:
        with open(Couriers_Path, 'r') as file:
            couriers_data = csv.DictReader(file)
            for row in couriers_data:
                couriers.append(({
                    'name': row['courier_name'],
                    'phone_number': int(row['courier_number'])
                }))
    except FileNotFoundError:
        print("Courier file not found. Starting with an empty courier list.")
    return couriers

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



# Redefining couriers to load from the CSV file
couriers = load_couriers(file=Couriers_Path)

# Function to View Couries 
def view_courier():
     with open(Couriers_Path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)

#Creates new Couriers
def create_courier():
    new_courier = input("Enter a new courier name you want to add: ")
    new_courier_phone = int(input("Enter a new courier phone number you want to add: "))
    new_dict = {
        "name": new_courier,
        "phone_number": new_courier_phone
    }
    couriers.append(new_dict) 
    with open(Couriers_Path, 'a') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow([new_dict['name'], new_dict['phone_number']])

# Deletes selected courier by index
def delete_courier():
    for index, c in enumerate(couriers):
        print(index , c) 
    try:
        user_index = int(input("Enter the index value of the Courier you want to delete: "))
        couriers.pop(user_index)
    except (IndexError,ValueError):
        print('Invalid Input!')
    with open(Couriers_Path,'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(['name', 'phone_number'])
        for courier in couriers:
            csv_writer.writerow([courier['name'],courier['phone_number']])

# Updates Couriers Name by Index
def update_courier():
    for x, courier in enumerate(couriers):
        print(x, courier['name'], courier['phone_number'])
    try:
        user_index = int(input("Enter the index value of the courier you want to update: "))
        if user_index < 0 or user_index >= len(couriers):
            print("Invalid index.")
            return
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
        couriers[user_index]['name'] = new_courier_name
        couriers[user_index]['phone_number'] = new_courier_number
    except Exception:
        print("An error occurred while updating the product.")
        return
    with open(Couriers_Path,'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(['name', 'phone_number'])
        for courier in couriers:
            csv_writer.writerow([courier['name'], courier['phone_number']])


#Function To Save Couriers
def save_couriers():
    with open(Couriers_Path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'phone_number'])
        for row in couriers:
            writer.writerow([row['name'], row['phone_number']])
    if len(couriers) == 0:
        print("No products to save.")
        return
    print('Products were saved successfully')
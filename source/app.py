import os
import products
import orders
import couriers
import my_mini_db
import utilities
# Welcome user into application 
print("Welcome to the pop up coffee shop \n")

# Nice Ascii coffee mug
print("    (  )   (   )  )")
print("     ) (   )  (  (")
print("     ( )  (    ) )")
print("     _____________")
print("    <_____________> ___")
print("    |             |/ _ \\")
print("    |               | | |")
print("    |               |_| |")
print(" ___|             |\\___/")
print("/    \\___________/    \\")
print("\\_____________________/")


#os.system('cls' if os.name == 'nt' else 'clear')
def clear_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    utilities.loading_animation()
    while True:
        print("""
╔═════════════════════════════════╗
║            Main Menu            ║
╠═════════════════════════════════╣
║  [0] Exit Application           ║
║  [1] Enter Product Menu         ║
║  [2] Enter Orders Menu          ║
║  [3] Enter Couriers Menu        ║
╚═════════════════════════════════╝
        """)
        try:
            main_menu = int(input("Enter your choice: "))
        except:
            print("Invalid Input Enter a Number")
            continue
        if main_menu == 0:
            orders.save_orders()
            products.save_products()
            couriers.save_couriers()
            clear_menu()
            print("Exited Main Menu\nGoodbye!")
            quit()
        elif main_menu == 1:
           clear_menu()
           utilities.loading_animation()
           while True:
                user_choice = products.get_product_menu()
                if user_choice == 0:
                    clear_menu()
                    print("You have returned to the main menu")
                    break
                elif  user_choice == 1:
                    utilities.loading_animation()
                    my_mini_db.view_products()
                elif user_choice == 2:
                    products.create_product()
                    my_mini_db.view_products()
                elif user_choice == 3:
                    products.update_product()
                    my_mini_db.view_products()
                elif user_choice == 4:
                    products.delete_product()
                    my_mini_db.view_products()
        elif main_menu == 2:
            clear_menu()
            utilities.loading_animation()
            while True:
                users_order = orders.get_order_menu()
                if users_order == 0:
                    clear_menu()
                    print("You have returned to the main menu")
                    break
                elif users_order == 1:
                    utilities.loading_animation()
                    my_mini_db.view_orders()
                elif users_order == 2:
                     orders.create_order()
                     utilities.loading_animation()
                     my_mini_db.view_orders()
                elif users_order == 3:
                     orders.update_order_status()
                     my_mini_db.view_orders()
                     continue
                elif users_order == 4:
                    orders.update_order()
                    utilities.loading_animation()
                    my_mini_db.view_orders()
                elif users_order == 5:
                    orders.delete_order()
                    utilities.loading_animation()
                    my_mini_db.view_orders()
        elif main_menu == 3:
            clear_menu()
            utilities.loading_animation()
            while True:
                user_option = couriers.get_courier_menu()
                if user_option == 0:
                    clear_menu()
                    print("You have returned to the main menu")
                    break
                elif user_option == 1:
                    utilities.loading_animation()
                    my_mini_db.view_couriers()
                elif user_option == 2:
                    couriers.create_courier()
                    utilities.loading_animation()
                    my_mini_db.view_couriers()
                elif user_option == 3:
                    couriers.update_courier()
                    utilities.loading_animation()
                    my_mini_db.view_couriers()
                elif user_option == 4:
                    couriers.delete_courier()
                    utilities.loading_animation()
                    my_mini_db.view_couriers()
while True:
    try:
        main()
        break
    except ValueError as Whoops:
        print(f'{Whoops} type a integer! ')
    except TypeError as Whoa:
        print(f'{Whoa} type a integer! ')
    


main()
from Customer_Info import Customer
from pizza_info import Pizza
from pizza_order import Order
from FileController import FileController
from Payment import Payment
import json

if __name__ == "__main__":
    pay_obj = Payment()
    fc = FileController()
    print("\tWelcome to our Online Pizza Store!")
    while True:
        menu_list, all_orders = fc.read()
        message = input("Please select by entering the number: 1.Menu 2.Order 3.Exit ")
        try:
            if int(message) == 1:
                for pizza in menu_list:
                    print(pizza)

            elif int(message) == 2:
                order_id = 0
                customer_order = []
                if all_orders:
                    for order in all_orders:
                        order_id = max(order_id, order.get_id())
                    order_id += 1
                else:
                    order_id = 1
                while True:
                    id = "Please input the pizza id that you want to purchase: "
                    id += "(Enter q when finished) "
                    pizza_id = input(id)

                    if pizza_id == 'q':
                        final_order = Order(order_id, customer_order)
                        name = input("Please input your name: ")
                        address = input("Please input your delivery address: ")
                        tel = input("Please input your contact number: ")
                        customer_info = Customer(name=name, address=address, tel=tel)
                        fc.write(customer_info)
                        fc.write(final_order)
                        total_price = 0
                        for pizza in menu_list:
                            if str(pizza.id) in customer_order:
                                print(pizza)
                                total_price += pizza.price
                        print(f"Total HK${total_price}")
                        print(f"Your Pizza Order ID: NO.{order_id}")
                        pay_obj.get_card()
                        print(pay_obj)
                        print("\tThank you for using our service, your order will be done in 30 mins")
                        break
                    else:
                        customer_order.append(pizza_id)

            elif int(message) == 3:
                print("\tThank you for using our service!")
                break

        except ValueError:
            print("WARNING!!Please enter the number only")

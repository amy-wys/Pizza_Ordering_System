import os.path
from Customer_Info import Customer
from pizza_info import Pizza
from pizza_order import Order
import json

class FileController:
    customer_path = "customer_info.json"
    order_path = "orders.json"
    pizza_path = "pizzas.json"

    def __init__(self):
        self.pizza_list = []
        self.order_list = []
        self.customer_list= []

    def read(self):
        if os.path.exists(self.order_path):
            with open(self.order_path) as f:
                all_orders = json.load(f)
            self.order_list = [Order(**order) for order in all_orders]

        if os.path.exists(self.pizza_path):
            with open(self.pizza_path) as f:
                all_pizzas = json.load(f)
            self.pizza_list = [Pizza(**pizza) for pizza in all_pizzas]
        return self.pizza_list, self.order_list

    def write(self, obj):
        if isinstance(obj, Pizza):
            self.pizza_list.append(obj)
            plist = [p.__dict__ for p in self.pizza_list]
            with open(self.pizza_path, "w") as f:
                json.dump(plist, f)

        elif isinstance(obj, Customer):
            self.customer_list.append(obj.__dict__)
            with open(self.customer_path, "w") as f:
                json.dump(self.customer_list, f)

        else:
            self.order_list.append(obj)
            olist = [o.__dict__ for o in self.order_list]
            with open(self.order_path, "w") as f:
                json.dump(olist, f)

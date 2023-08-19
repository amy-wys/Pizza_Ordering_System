class Order:
    def __init__(self, order_id, pizza_id):
        self.order_id = order_id
        self.pizza_id = pizza_id

    def __str__(self):
        return f"{self.order_id} ordered {self.pizza_id}"

    def get_str(self):
        return f"{self.order_id} {self.pizza_id}"

    def get_id(self):
        return self.order_id



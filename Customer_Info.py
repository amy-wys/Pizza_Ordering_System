
class Customer:
    def __init__(self,name:str,address:str,tel:str):
        self.name=name
        self.address=address
        self.tel=tel

        def __str__(self):
            return f"{self.name} {self.address} / {self.tel} "

        def get_str(self):
            return f"{self.name} {self.address},{self.tel}"
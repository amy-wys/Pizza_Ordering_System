class Pizza:
    def __init__(self,id,size,flavour,price):
        self.size=size
        self.flavour=flavour
        self.price=price
        self.id=id

    def __str__(self):
        return f"({self.id}) {self.size} {self.flavour} - HK${self.price}"

    def get_str(self):
        return f"{self.id} {self.size}, {self.flavour}, {self.price}"


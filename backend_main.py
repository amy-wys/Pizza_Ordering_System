from pizza_info import Pizza
from FileController import FileController

if __name__ == '__main__':
    fc = FileController()
    _, _ = fc.read()
    while True:
        question = "Create new pizza recipes for the store?"
        question += "Enter y to continue, q to quit: "
        response = input(question)
        if response.lower() == 'q':
            break
        elif response.lower() == 'y':
            flavour = input("What flavour do you want to display? ")
            for size in ["S", "M", "L"]:
                while True:
                    try:
                        id = int(input(f"Input Pizza Id: "))
                        price = float(input(f"Price of {flavour} - {size}: "))
                        pizza = Pizza(id=id, flavour=flavour, size=size, price=price)
                        fc.write(pizza)
                        break
                    except Exception as e:
                        pass

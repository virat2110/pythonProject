class Product:
    def __init__(self, id, name, unit, price):
        self.id=id
        self.name=name
        self.unit=unit
        self.price=price

    def bill(self):
        return self.unit * self.price

    def display(self):
        print(f"product id:- {self.id} name of product:- {self.name} per unit price:- {self.price} quantitiy:- {self.unit}")
        print(f"total bill {p1.bill()}")

p1=Product(123, "book", 10, 1000)
p1.display()

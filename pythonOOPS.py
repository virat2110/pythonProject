class operations:
    x = int(input("enter value1 :"))
    y = int(input("enter value2 :"))
    def add(self):
        return self.x + operations.y    # can be accessed by both ways.
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
    def cube(self,z):
        return z ** 3



ob1 = operations()
z =  y = int(input("enter value3 :"))

print("addition is",ob1.add())
print("sub is",ob1.sub())
print("multiplication is",ob1.mul())
print("division is",ob1.div())

print("cube of z is: ",ob1.cube(z))

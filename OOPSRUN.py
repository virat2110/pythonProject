from OOPS import *

def main():
    c1 = Cube("white")
    c1.x = 10
    c1.y = 10
    c1.z = 10
    print("volume of first instance", c1.volume())
    c2 = Cube("red")  # another instance of class
    c2.x = 20
    c2.y = 30
    c2.z = 40
    print("volume of second instance", c2.volume())
    print(c1.x)
    c3 = Cube()  # i have not passed any argument so it will take default value see line 9 in OOPS

    print(c1.color)
    print(c2.color)
    print(c3.color)

main()

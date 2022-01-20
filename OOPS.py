class Cube:     # class CLASS_NAME:
    x=10
    y=20
    z=40
    color= ""      # intializing attribute

    def volume (self) :   # def NAME(self , <other parameter>)    self works as this
        return self.x*self.y*self.z
    def __init__(self, name="default"):            # it is a constructor in python so while creating instance we have to give parameters.
        self.color = name           # intializing attribute

print(Cube.y)

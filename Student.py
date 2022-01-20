class Student:
    clg = "KLCE"  # class attributes
    def __init__(self, id, name, course):    # it is instance attributes
        self.id = id                            # self is for current instance
        self.name = name
        self.course = course
    def display(self):    # Three types of methpod - instance method class-cls method static method
        print(f"This is {self.id} name {self.name} opted for course {self.course} studying in {s1.clg} ")

s1 = Student(2000030189," virat","PFSD")
s1.display()
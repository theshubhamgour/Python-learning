# Methods - Methods are functions that belong to objects.

class Student:
    college_name = "ABC College"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("Welcome Student",self.name)


s1 = Student("karan" , 98)
s1.welcome()


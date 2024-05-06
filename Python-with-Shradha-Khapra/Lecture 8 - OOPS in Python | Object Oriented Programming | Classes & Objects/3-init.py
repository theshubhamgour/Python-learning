# _ _init_ _ Function

# All classes have a function called __init__(), which is always executed when the object is being
# initiated.

class Student:
    name = "Barry"
    def __init__(self): #default parameter required
        print("Adding details in DB")

s1 = Student()
print(s1.name)


# *The self parameter is a reference to the current
# instance of the class, and is used to access variables
# that belongs to the class.

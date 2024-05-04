# Functions in Python - Block of statements that perform a specific task.

# def sum(a,b):
#     sum = a + b
#     print("The Sum is : ",sum)
#     return sum

# sum(5,6)

def print_hello():
    print("Hello")


output = print_hello()
print(output) # A function which do not return anything returns none


# Default Parameters - Assigning a default value to parameter, which is used when no argument is passed.
def muo(a=2,b=3):
    mul = a*b
    print(mul)
    return mul

muo(3) #here a will be passed as 3


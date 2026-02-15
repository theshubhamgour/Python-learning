# Function: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def hello():
    print("Hello, World!")

hello()  # Calling the function



def sum(a,b): # Parameters a and b are used to pass values to the function
    s = a + b
    return s

result = sum(5, 10)
print("The sum is:", result)
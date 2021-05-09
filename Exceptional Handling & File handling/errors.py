# Here we are going to see types of errors in python promgraming language
# First type of error is Syntax error

# Let us assume a small example where we want to add two numbers by apssing arguments
# here the program looks quite correct but it is missing : therefore on execution of the below programwe will see syntax error

# def function(a,b)
    # print(a+b)
# function(2, 3)

# The correct way to write this code is 
def function(a,b):
    print(a+b)
function(2, 3)


# Second type of error is Logical error_ which is quite difficult to figure out 
# because your complier doesnt throw any error here since it does'nt know what logic you are using in what way
# Let's see an example

# def function(a,b):
#     print(a*b)
# function(2, 2)

#in the above code when you will execute you will get a output but the problem is you wanred to add them and youre getting the value 
# of multiplication therefore whenever you try it for different value it will show output but it will not meet the user's expected output


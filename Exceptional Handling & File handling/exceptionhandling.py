# Now we are going to learn about exception
# in nutshell exception means something which will cause your program to terminate
#Let's see an example

# def function(a,b):
#     print(a/b)
# function(20, 0)
# print('hello')

# in the above example it will lead to terminatation why? because the Second value is being divided by 0, which mean it will 
# return infinity value in general.
# therefore it showed: ZeroDivisionError: division by zero
# therefore we will make use of exception which will not allow the program to execute further

# We will now make use of the three block

try:
    a=20
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
# So basically in the above code the try bock contains the main code and it is going to check if there is any exception which we have
# defined in the except block _ so if the exception occurs it will print the message written in the except block

# Now we will check the code for non zero value

# try:
#     a=20
#     b=10
#     print(a/b)
# except ZeroDivisionError:
#     print("There is a divide by zero error") 

# Thus this code worked for us properly and it didnt showed us the ZeroDivisionError
# So exception is only going to raise when we try to divide a number by zero

# try block contain the code which you might think it can be vulnerable exception is the block where the messege is being stored when
# exception occurs and finally is the block which will execute no matter what whether it has exception or not

# let us see an example

try:
    a=20
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
finally:
    print("Ths is going to be executed no matter what")



# try 
# |
# |
# |
# except
# |
# |
# |
# finally
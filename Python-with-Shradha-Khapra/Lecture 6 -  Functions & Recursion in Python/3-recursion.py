# Recursion - When a function calls itself repeatedly.
# # prints n to 1 backwards
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# Factorial

def fact(n):
    if (n ==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))
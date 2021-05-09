def add(a,b):
    return(a+b)
def square(c):
    return c*c

# now this will add 2 and 3 and then the result will be squared in the square argument
# 2+3=5 and 5*5=25 this should be the final output
result= square(add(2,3))
print(result)
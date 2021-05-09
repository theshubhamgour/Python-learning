'''
Author: Shubham Gour

'''

# Fifth function- Range function
# It specifies a particular Range- useful when you want to create a big list with less part of coding
numbers=list(range(10))
print(numbers)
# syntax- listname= list(range(last number))
# this will print numer from 0 t 9

# now you might be thinking what if i want to print a list from a specified point well you answer is given below
numbers2=list(range(2,16))
print(numbers2)
# here it will print number from 2 till 15 you just have too specify the start point and end point

# now if you want to print a list which have a difference of a interval say 3
interval=list(range(1,20,3))
print(interval)
# this will print [1, 4, 7, 10, 13, 16, 19] and you can clearly see that they have a interval of three in them

# Note: range functions are used in loops

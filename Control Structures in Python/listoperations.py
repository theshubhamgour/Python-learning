'''
Author: Shubham Gour

'''


numbers = [1,2,3,4]
# to insert a value in a list we use the below code
# here i want 2 to get replaced by 5 therefore i will write
numbers[2] = 5 
print(numbers)
# this is how you can enter a number in a particular loaction in list


# we will now create two new list
nano= [2,2,2,2]
newnano= [1,1,1,1]
# to add two list we write the below code
print(nano+newnano)

# To multiply a list with a number
print(nano*6)
# this will print the entire list 6 times in nutshell it willreplicate

# we will now create an new list
fruits= ["Apple", "Mango", "Orange", "Pineapple"]
# to check wheter a particular entry is present in a list or not we will follow the below code
print("Orange" in fruits) 
# this will show you true as an output
# now what if i search something which is not present in fruit list?? let's see
print("Banana" in fruits)
# Obviously it will give you output as false
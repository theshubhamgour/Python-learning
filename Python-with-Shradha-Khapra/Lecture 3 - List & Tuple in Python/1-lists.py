# List - A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)

marks = [12.5, 45.6, 345.6, 56.8, 47.99]
print(marks)
print(len(marks))
print(marks[0])


# ----------------------------------------------------------#
student = [ "Karan", 85, "Soham"]
print(student)
#TypeError: 'type' object does not support item assignment
# str[0] = "Maran"


# ----------------------------------------------------------#
# List Slicing - Similar to String Slicing
# list_name[ starting_idx : ending_idx ] #ending idx is not included

marks = [12.5, 45.6, 345.6, 56.8, 47.99]
print(marks[1:4])
print(marks[-3:-1])


# ----------------------------------------------------------#
# List Methods - Function for lists
list = [2,3,1]
list.append(4) #adds one element at the end
print(list)

list.sort( ) #sorts in ascending order
print(list)

list.sort( reverse=True ) #sorts in descending order
print(list)

list.reverse( ) #reverses list
print(list)

list.insert( 1, 5 ) #insert element at index
print(list)

list.remove(1) #removes first occurrence of element
print(list)

list.pop( 2 ) #removes element at idx
print(list)
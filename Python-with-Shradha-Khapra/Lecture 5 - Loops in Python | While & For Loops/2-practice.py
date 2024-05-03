# Print numbers from 1 to 100.
# number  = 1
# while number <=100:
#     print(number)
#     number+=1

# Print numbers from 100 to 1.
# numbers = 100
# while numbers >=1:
#     print(numbers)
#     numbers-=1

# Print the multiplication table of a number n.
# n = int(input("Enter a number : "))
# number = 1
# while number <=10:
#     print(n,"X",number,"=",number*n)
#     number+=1

# Print the elements of the following list using a loop:
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# index= 0
# while index < len(list):
#     print(list[index])
#     index+=1


tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter a number : "))
index = 0

while index < len(tup):
    if tup[index] == x:
        print("Found at index:", index)
        break  # Add break statement to exit loop once the number is found
    index += 1

# Print the elements of the following list using a loop:
# number = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for n in number:
#     print(n)

# Search for a number x in this tuple using loop:
number = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 9
index =0
for el in number:
    if (el == x ):
        print("n found: index = ",index)
    index +=1
print('End of loop')
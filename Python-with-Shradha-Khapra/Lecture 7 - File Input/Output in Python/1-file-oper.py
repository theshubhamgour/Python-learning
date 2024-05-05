# File I/O in Python
# Python can be used to perform operations on a file. (read & write data)

# Reading files
# f= open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0-demo.txt","r")
# data = f.read()
# print(data)


# Writing files
# f= open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0-demo.txt","a")
# f.write("\nAfter nodejs")
# f.close


# with function
# with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0-demo.txt","r") as f:
#     data = f.read()
#     print(data) 

# with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0-demo.txt","w") as f:
#     f.write("Hola") 


# File Deletion operation
# Module (like a code library) is a file written by another programmer that generally has
# a functions we can use.
import os
os.remove("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0.1-delete.txt")
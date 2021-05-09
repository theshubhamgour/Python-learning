# file handling is used to store data entered by the user
# this is usedfull where you are programming in relation to the databases as well as files 

# create a new file named: demo.txt
#  we are going to open, write read and change the data in the file and close the file

# to open a file
# --------("file name", write mode)
# file= open("demo.txt", 'w')
# #lets write something here
# file.close()
#note you have to close the file once opened

# Now we are going to write some data in the file
# first we will try to open in read mode and for this we will typr the below code
file = open("demo.txt", 'r')
content= file.read()
# it will read the data from read and store in content variable
print(content)
file.close()


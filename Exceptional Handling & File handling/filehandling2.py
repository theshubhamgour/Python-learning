
# here we will try to write data and read data using the power of python
# note the previous data will get deleted and to overcome that we will make use of append
# refer filehandling3.py file for append function

file= open("demo.txt", 'w')
file.write("This is a new text")
file.close()

file=open("demo.txt", 'r')
content= file.read()
print(content)


file=open("demo.txt",'w')
file.write("My name is name")
file.close()

file=open("demo.txt", 'r')
content2= file.read()
print(content2)
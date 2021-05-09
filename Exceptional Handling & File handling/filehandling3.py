# Here we will use append mode
# it will open the file and will not interfer with the previous data
# as expericend earlier the data was getting deleted so t prevent that we will make use of append
file=open("demo.txt",'a')
file.write("My name is append")
file.close()

#by using append our previous data will not get deleted
file= open("demo.txt",'r')
demo= file.read()
print(demo)
file.close()


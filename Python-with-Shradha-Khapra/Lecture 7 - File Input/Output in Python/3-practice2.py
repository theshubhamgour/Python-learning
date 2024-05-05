# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.
# def check_for_line():
#     word = "learning"
#     data = True
#     line_number = 1
#     with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/practice.txt","r") as f:
#      while data:
#         data  = f.readline()
#         if(word in data):
#            print(line_number)
#            return
#         line_number +=1
#     return - 1
# check_for_line()




# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/0.2-demofile.txt","r") as f:
    data = f.read()

    num  = data.split(",")
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)


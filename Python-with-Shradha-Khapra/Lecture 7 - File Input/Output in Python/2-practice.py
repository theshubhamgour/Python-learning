# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.")
#     f.write("I like programming in Java.")

# WAF that replace all occurrences of “java” with “python” in above file.
# with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/practice.txt","r") as f:
#     data  = f.read()
#     new_data =  data.replace("Java", "Python")
#     print(new_data)

# with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/practice.txt","w") as f:
#     f.write(new_data)


# Search if the word “learning” exists in the file or not.
with open("/Users/shubhamgour/Desktop/Python-learning/Python-with-Shradha-Khapra/Lecture 7 - File Input/Output in Python/practice.txt","r") as f:
    data  = f.read()
    word = "learning"
    if(data.find(word)!=1):
        print('Found')
    else:
        print("Not Found")


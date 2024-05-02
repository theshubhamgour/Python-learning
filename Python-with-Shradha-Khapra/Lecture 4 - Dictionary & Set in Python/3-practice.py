
'''
Store following word meanings in a python dictionary :
table : "a piece of furniture","list of facts & figures"
cat : "a small animal"
'''
dictonary = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(dictonary)


'''
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

"python","java","C++","python","javascript",
"java","python","java","C++","C"
'''

subject = {"python","java","C++","python","javascript", "java","python","java","C++","C"}
print(subject)

print("Total Classrooms required is: ",len(subject))




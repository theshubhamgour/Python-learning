# Conditional Statements
# if-elif-if (Syntax)

'''
if(condition):
 statement1
elif(condition):
 statement2
else:
statement3
'''

age = 17

if (age>=18):
    print("You are eligible")
elif(age<=18):
    print("Not eligible")
else:
    print("Out of Scope")



# ----------------------------------------------------------#
# Grade students based on marks
'''
marks >= 90, grade = “A”
90 > marks >= 80, grade =“B”
80 > marks >= 70, grade =“C”
70 > marks, grade = “D”
'''
marks = 90

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

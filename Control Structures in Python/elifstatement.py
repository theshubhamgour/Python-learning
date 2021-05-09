'''
Author: Shubham Gour

'''

# Design a grading system for students report card
marks= int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks<60:
    print("Grade D")
# Take note of elif it should not be unde if statement if done it will show error
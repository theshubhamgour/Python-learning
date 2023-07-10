student_marks= input("Enter the list of student_marks : ").split()
for n in range(0,len(student_marks)):
    student_marks[n]=int(student_marks[n])
print(student_marks)

# print(f"The maximum marks out of the list provided is : {max(student_marks)}")

highest = 0
for mark in student_marks:
    if mark > highest:
        highest = mark
print(f"The highest marks is: {highest}")

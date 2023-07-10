student_heights= input("Enter the list of student heights : ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
print(f"The total height of {len(student_heights)} student is {total_height}")

calculate_height = total_height / len(student_heights)
print(f"The calculated average height of {len(student_heights)} is {calculate_height}")

print(f"The calculated round average height of {len(student_heights)} is {round(calculate_height)}")


'''
Enter the list of student heights : 156 178 165 171 187
[156, 178, 165, 171, 187]
The total height of 5 student is 857
The calculated average height of 5 is 171.4
The calculated round average height of 5 is 171

'''
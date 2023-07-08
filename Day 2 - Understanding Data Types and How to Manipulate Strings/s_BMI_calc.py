# BMI Calculator Program
# Formula : BMI = weight / height*2

weigth = input("Enter your weight in KG : ")
height = input("Enter height : ")

BMI = int(weigth) / float(height)**2
BMI_INT = int(BMI)
print(BMI_INT)

# Enter your weight in KG : 64
# Enter height : 1.8
# 19
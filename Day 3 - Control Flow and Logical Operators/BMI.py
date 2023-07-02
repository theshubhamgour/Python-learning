#checking the BMI based on users weight and height

height =float(input("enter the height in meters(m) : "))
weight =float(input("enter the weight in kilograms(kg) : "))

#calculating the bmi
bmi = round(weight / height ** 2)   # **  Exponentiation Operator

# interpreting the value of the bmi according to bmi value
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese go to gym")
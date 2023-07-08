#rollercoaster example that uses nasted if else for the solution \

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("you can ride the rollercoster!")
    age = int(input("What is your age ? : "))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12")
else:
    print("Sorry,you have to grow taller before you can ride.")
height = int(input("Enter height in cm : "))
if height >= 120:
    print("Can Ride")
    age = int(input("Enter your age : "))
    if age <12:
        bill =5
        print("Child tickets are $5")
    elif age >=18:
        bill =7
        print("Youth tickets are $7")
    elif age >=45 and age<=55:
        print("Everything is going to be ok, this ride is on us")
    else:
        bill = 12
        print("The bill is $12")
else:
    print("Can't Ride")
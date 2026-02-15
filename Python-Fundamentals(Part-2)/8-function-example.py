
# def cal_avg ():
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     n3 = int(input("Enter third number: "))

#     average = (n1 + n2 + n3) / 3
#     print("Average of the three numbers is:", average)

# cal_avg()


def cal_avg_default_values (n1, n2=1, n3=1): # Default values for n2 and n3 are set to 1, so if they are not provided when calling the function, they will be used in the calculation.
    average = (n1 + n2 + n3) / 3
    print("Average of the three numbers is:", average)

cal_avg_default_values(2,5) # Here, n1 is provided as 2, n2 is provided as 5, and n3 will take the default value of 1. The average will be calculated as (2 + 5 + 1) / 3 = 8 / 3 = 2.67.
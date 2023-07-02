#write a program that adds the digits of two digit number eg: 35 -- 3+5 = 8
two_digit_number= input("enter a two digit number : ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)


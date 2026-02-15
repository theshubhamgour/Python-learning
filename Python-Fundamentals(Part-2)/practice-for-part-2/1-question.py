# Write a program that takes salary as input. Using conditional statements, 
# calculate the final tax rate based on these rules:
#  Q1 salary final tax rate
#  •If salary < 30,000 → 5% 
#  •If salary is 30,000–70,000 → 15% 
#  •If salary > 70,000 → 25%


salary = float(input("Enter your salary: "))

def final_tax_rate(salary):
    if salary < 30000:
        tax_rate = 0.05
    elif 30000 <= salary <= 70000:
        tax_rate = 0.15
    else:
        tax_rate = 0.25
    return tax_rate

tax_rate = final_tax_rate(salary)
print(f"The final tax rate for a salary of {salary} is: {tax_rate * 100}%")

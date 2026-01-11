# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
# compute simple interest:
# SI = (P ∗ R ∗ T)/100

principal_input = float(input("Enter the principal amount (P): "))
rate_input = float(input("Enter the rate of interest (R): "))
time_input = float(input("Enter the time in years (T): "))

simple_interest = (principal_input * rate_input * time_input) / 100
print("The simple interest is:", simple_interest)

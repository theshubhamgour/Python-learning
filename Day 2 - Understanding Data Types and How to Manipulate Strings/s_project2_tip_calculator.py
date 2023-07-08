# if the bill was $150.00 split between 5 people, with 12% tip
# Each person should pay (150.00/5)1.12 = 33.6
# Round the result to 2 digits decimal places = 33.60

print("")
print("-------------------Welcome to the tip Calculator-----------------------")
print("  _____ ___ ___    ___   _   _         _      _           ")
print(" |_   _|_ _| _ \  / __| /_\ | |__ _  _| |__ _| |_ ___ _ _ ")
print("   | |  | ||  _/ | (__ / _ \| / _| || | / _` |  _/ _ \ '_|")
print("   |_| |___|_|    \___/_/ \_\_\__|\_,_|_\__,_|\__\___/_|  ")
print("")

bill = float(input("what was the total bill ? : "))
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15? : "))
split = int(input("How many people to split the bill? : "))
tip_in_percent = tip /100
total_tip = bill * tip_in_percent
total_bill = bill + total_tip
bill_per_person = total_bill / split
final_amount = round(bill_per_person,2)
print(f"Each person to pay : ${final_amount}")
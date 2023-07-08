print("Welcome to python pizza delivery")

print(" ")
print("  ____  _              ")
print(" |  _ \\(_)__________ _ ")
print(" | |_) | |_  /_  / _` |")
print(" |  __/| |/ / / / (_| |")
print(" |_|   |_/___/___\__,_|")

print(" ")

size = input("What size of pizza do you want? : S , M or L ? : ")
add_peporoni = input("Do you want to add peporoni: Y or N ? :")
extra_cheeze = input("Do you want to add cheeze?: Y or N ? : ")

# Extra cheeze for any pizza +1
# Peporoni for small pizza +2
# Peporoni for medium and large pizza is +3

bill = 0
if size == 'S':
    bill+=15
if size == 'M':
    bill+=20
if size == 'L':
    bill+=25

if add_peporoni == 'Y':
    if size == 'S':
        bill+=2
    else:
        bill+=3

if extra_cheeze == 'Y':
    bill+=1

print(f"Your final bill is : ${bill}")
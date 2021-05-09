# In this program we will generate random values from 1 to 6 using python

# when we write a lengthy program each set is divided into modules and thus this is the case of modular programming where each module
# performs it's own work 
# we will use random module in python - so we will need to import module fro this we will write the below code


# in nutshell: - 
# 1st: import module
# 2nd: type module name give a dot operator and give the function name
import random
for x in range(5):
    result= random.randint(1, 6)
    print(result) 
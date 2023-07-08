print("")
print("   __                     ___    _     _ ")
print("  /__\\_   _____ _ __     /___\\__| | __| |")
print(" /_\\ \\ \\ / / _ \\ '_ \\   //  // _` |/ _` |")
print("//__  \\ V /  __/ | | | / \\_// (_| | (_| |")
print("\\__/   \\_/ \\___|_| |_| \\___/ \\__,_|\\__,_|")

print("")
user_inp  = int(input('Enter Height in cm : '))
user_age  = int(input('Enter a age : '))
if (user_inp > 120):
    print("Can Ride")
    if (user_age >18):
        print("Give $12")
    else: 
        print("Give $7")
else:
    print("Cannot Ride")
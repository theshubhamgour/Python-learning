import random
word_list = ["aardvark", "baboon", "camel"]
choose_word = random.choice(word_list)
guess = input("Enter a Superhero name : ").lower()
for letter in choose_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
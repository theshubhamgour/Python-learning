import random
word_list = ['Flash', 'Superman', 'IronMan']
choose_word = random.choice(word_list)
guess = input("Enter a Superhero name : ").lower()
for letter in choose_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
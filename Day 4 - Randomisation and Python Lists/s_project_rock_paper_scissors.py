import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(
    '''
█▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
█▀▄ █▄█ █▄▄ █░█   █▀▀ █▀█ █▀▀ ██▄ █▀▄   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
'''
)

game_images = [rock, paper, scissors]
print("Press 0 for Rock  1 for Paper and 2 for Scissors")
print("")

user_input = int(input("Enter your input : "))
print(game_images[user_input])


computer_choicce = random.randint(0, 2)
print("")
print(f"Computer Choice : ${computer_choicce}")
print(game_images[computer_choicce])

if user_input == 0 and computer_choicce == 2:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("You win")
    print("----------------------------------------------------")
elif computer_choicce == 0 and user_input == 2:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("You lose")
    print("----------------------------------------------------")
elif computer_choicce > user_input:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("You lose")
    print("----------------------------------------------------")
elif user_input > computer_choicce:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("You win")
    print("----------------------------------------------------")
elif computer_choicce == user_input:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("It is a Draw")
    print("----------------------------------------------------")
else:
    print('''
🆁 🅴 🆂 🆄 🅻 🆃
''')
    print("----------------------------------------------------")
    print("You typed and invalid number, You lose")
    print("----------------------------------------------------")

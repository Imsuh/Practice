import random

print("Rock Paper Scissor game:")

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissor \n"))

choice_list = [rock, paper, scissor]

if user_input < 0 or user_input >= 3:
    print("Invalid number entered, you lose!!")

else:
    print('You chose \n', choice_list[user_input])
    computer_input = random.randint(0, 2)
    print('Computer chose \n', choice_list[computer_input])

    if user_input == 0 and computer_input == 2:
        print("You win!")
    elif computer_input == 0 and computer_input == 2:
        print("You lose!!")
    elif computer_input > user_input:
        print("You lose!!")
    elif user_input > computer_input:
        print("You win!")
    else:
        print("Both chose same : DRAW !!")

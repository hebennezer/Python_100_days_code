# Game Rock, Paper and Scissors

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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Papar or 2 for Scissors\n>>>> "))
if my_choice >= 3 or my_choice < 0:
  print("You type an invalid number. you lose!")
else:
  print(f"You chose {game_images[my_choice]}")
  
  comp_choice = random.randint(0, 2)
  print(f"Computer chose {game_images[comp_choice]}")
  
  if my_choice == comp_choice:
    print("It's a draw!")
  elif my_choice == 0 and comp_choice == 2:
    print("You win!")
  elif my_choice == 2 and comp_choice == 1:
    print("You win!")
  elif my_choice == 1 and comp_choice == 0:
    print("You win!")
  else:
    print("You lose!")
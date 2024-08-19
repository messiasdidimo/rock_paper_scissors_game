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

print("What do you choose? Type 1 for rock, 2 for paper e 3 for scissors.")
player_choice = input()

print("You chose:")

if player_choice == "1":
  print(rock)
elif player_choice == "2":
  print(paper)
elif player_choice == "3":
  print(scissors)

print("Computer chose:")

computer_choice = str(random.randint(1, 3))

if computer_choice == "1":
  print(rock)
elif computer_choice == "2":
  print(paper)
elif computer_choice == "3":
  print(scissors)

if player_choice == computer_choice:
  print("It's a tie!")
elif player_choice == "1":
  if computer_choice == "2":
    print("Sorry, you lost!")
  else:
    print("Congrats, you won!")
elif player_choice == "2":
  if computer_choice == "3":
    print("Sorry, you lost!")
  else:
    print("Congrats, you won!")
elif player_choice == "3":
  if computer_choice == "1":
    print("Sorry, you lost!")
  else:
    print("Congrats, you won!")
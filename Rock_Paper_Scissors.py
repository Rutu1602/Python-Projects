# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

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

your_choice = input("What would you like to select? 0 for rock, 1 for paper, 2 for scissors\n")

if your_choice == '0':
    print("You choose rock\n" + rock)
elif your_choice == '1':
    print("You choose paper\n" + paper)
elif your_choice == '2':
    print("You choose scissors\n" + scissors)
else:
    print("Invalid choice")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer choose rock\n" + rock)
elif computer_choice == 1:
    print("Computer choose paper\n" +paper)
elif computer_choice == 2:
    print("Computer choose scissors\n" +scissors)
else:
    print("Invalid choice")

if your_choice == '0' and computer_choice == 0 or your_choice == '1' and computer_choice == 1 or your_choice == '2' and computer_choice == 2:
    print("It's a draw!")
elif your_choice == '0' and computer_choice == 2 or your_choice == '1' and computer_choice == 0 or your_choice == '2' and computer_choice == 1:
    print("You won!")
else:
    print("You loose!")



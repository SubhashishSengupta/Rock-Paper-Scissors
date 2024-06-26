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

# all_in_one = [rock, paper, scissors]

import random

computer = random.randint(0, 2)
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user = int(user)
if user == 0:
    print("You chose: \n" + rock + "\n")
    if computer == 0:
        print("Computer chose: \n" + rock  + "\n It's a Draw.")
    elif computer == 1:
        print("Computer chose: \n" + paper + "\n You Lose.")
    else:
        print("Computer chose: \n" + scissors + "\n You Win.")
elif user == 1:
    print("You chose: \n" + paper + "\n")
    if computer == 0:
        print("Computer chose: \n" + rock  + "\n You Win.")
    elif computer == 1:
        print("Computer chose: \n" + paper + "\n It's a Draw.")
    else:
        print("Computer chose: \n" + scissors + "\n You Lose.")
elif user == 2:
    print("You chose: \n" + scissors + "\n")
    if computer == 0:
        print("Computer chose: \n" + rock  + "\n You Lose.")
    elif computer == 1:
        print("Computer chose: \n" + paper + "\n You Win.")
    else:
        print("Computer chose: \n" + scissors + "\n It's a Draw.")
else:
    print("Invalid Request. Please try again.")
        
# print(all_in_one[computer])


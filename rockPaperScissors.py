import random
from enum import Enum

class RockPaperScissors(Enum):
    rock = 1
    paper = 2
    scissors = 3

print('Welcome to Rock, Paper, Scissors!')
choice = int(input("Enter 1 for Rock, \n2 for Paper or \n3 for scissors: \n"))

if choice < 1 or choice > 3:
    choice = int(input("You must choose 1, 2 or 3: \n"))

computer_choice = random.randint(1,3)

print("You chose " + str(RockPaperScissors(choice)).replace("RockPaperScissors.",""))
print("Computer chose " + str(RockPaperScissors(computer_choice)).replace("RockPaperScissors.",""))
print("")

if choice == 1 and computer_choice == 3:
    print("You win!")
elif choice == 2 and computer_choice == 1:
    print("You win!")
elif choice == 3 and computer_choice == 2:
    print("You win!")
elif choice == computer_choice:
    print("Tie!")
else:
    print("Computer wins!")
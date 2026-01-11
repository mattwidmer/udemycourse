#4 Rock Paper Scissors Using Lists

import random

choice = input("What do you choose? Rock, Paper, or Scissors? ")

computerchoice = random.randint(1,3)

if choice == "Rock":
    if computerchoice == 2:
        print("The computer played Paper! You lost.")
    elif computerchoice == 3:
        print("The computer played scissors! You won!")
    else:
        print("The computer played rock! You tied.")
elif choice == "Paper":
    if computerchoice == 2:
        print("The computer played Paper! You tied.")
    elif computerchoice == 3:
        print("The computer played scissors! You lost.")
    else:
        print("The computer played rock! You won!")
elif choice == "Scissors":
    if computerchoice == 2:
        print("The computer played Paper! You wont!")
    elif computerchoice == 3:
        print("The computer played scissors! You tied.")
    else:
        print("The computer played rock! You lost.")
else:
    print("Try typing Rock, Paper, or Scissors")
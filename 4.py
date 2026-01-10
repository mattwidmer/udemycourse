#choose your own adventure : 3 choices

wronganswer = "You must choose one of the given options. Try again."

print("You are the last surviving member of your team. There are two enemies remaining. On the left, the cash box has half the time left. On the right, you can rez one of your teammates.")
choice1 = input("Do you go left or right? ")
choice1 = choice1.lower()
if choice1 == "left":
    print("You go to the cash box and start stealing. You hear footsteps behind you.")
    choice2 = input("Do you stick it or take cover? ")
    choice2 = choice2.lower()
    if choice2 == "stick it":
        print("An M11 light came up behind you and sprayed you down. You have died.")
    elif choice2 == "take cover":
        print("You take cover in the corner of the room. The light sees you but can't spray you down")
        choice3 = input("Do you hide until you're fully healed or try to fight? (hide or fight) ")
        choice3 = choice3.lower()
        if choice3 == "Hide" or "hide":
            print("You hide in the corner until healed. The light holds a long angle on the cashout and you run out of time. Game over.")
        elif choice3 == "Fight" or "fight":
            print("You try to fight the light on low health and die. Game over.")
        else:
            print(wronganswer)
    else:
        print(wronganswer)
if choice1 == "right":
    print("You revive your teammate. It's now a 2v2 but your teammate is at half health.")
    choice2 = input("Do you take cover or steal? ")
    choice2 = choice2.lower()
    if choice2 == "take cover":
        print("You take cover and heal up with your teammate. It's a 2v2 and the enemies are nowhere to be seen.")
        choice3 = input("Do you steal the cashout or try to find the enemies? (Steal or Fight)")
        choice3 = choice3.lower()
        if choice3 == "steal":
            print("You and your teammate steal the cashout. The enemy comes at the last second but you successfully steal the cashout. Congratulations, you have won!")
        elif choice3 == "fight":
            print("You and your teammate chase down the enemies. You win the fight but lose the cashout. Game over.")
        else:
            print(wronganswer)
    elif choice2 == "steal":
        print("You and your lit teammate attempt to steal and die trying. Game over.")
        
else:
    "You must choose one or the other"
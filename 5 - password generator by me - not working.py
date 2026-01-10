#Password Generator
import random

#get inputs for how many of each they want
letterbudget = int(input("How Many Letters do You Want? 1, 2, 3, 4, 5 "))
numberbudget = int(input("How Many Numbers do You Want? 1, 2, 3, 4, 5 "))
characterbudget = int(input("How Many Special Characters do You Want? 1, 2, 3, 4, 5 "))

totalcharacters = letterbudget + numberbudget + characterbudget
#print(totalcharacters)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

password = []

#checking for which to use if the budget is used up
number_in_budget = (numberbudget > 0) and (numberbudget >= letterbudget) and (numberbudget >= characterbudget)
letter_in_budget = (letterbudget > 0) and (letterbudget >= numberbudget) and (letterbudget >= characterbudget)
character_in_budget = (characterbudget > 0) and (characterbudget >= letterbudget) and (characterbudget >= numberbudget)

#generate it letter by letter but with another for loop to 
#generate it letter by letter
for character in range(1,(totalcharacters + 1)):
    random_integer = random.randint(1,3)
    if (random_integer == 1) and (letter_in_budget == True):
        #set new random integer to pick a random letter
        random_integer = random.randint(0,25)
        #grab letter from list
        character = letters[random_integer]
        print("Picked: " + str(character))
        password.append(character)
        letterbudget -= 1
        letter_in_budget = (letterbudget > 0) and (letterbudget >= numberbudget) and (letterbudget >= characterbudget)
        print("Current letter budget: " + str(letterbudget))
    elif (random_integer == 2) and (number_in_budget == True):
        #set new random integer to pick a random number
        random_integer = random.randint(0,8)
        #grab number from list
        character = numbers[random_integer]
        print("Picked: " + str(character))
        password.append(character)
        numberbudget -= 1
        number_in_budget = (numberbudget > 0) and (numberbudget >= letterbudget) and (numberbudget >= characterbudget)
        print("Current number budget: " + str(numberbudget))
    elif (random_integer == 3) and (character_in_budget == True):
        #set new random integer to pick a random special character
        random_integer = random.randint(0,7)
        #grab special character from list
        character = special_characters[random_integer]
        print("Picked: " + str(character))
        password.append(character)
        characterbudget -= 1
        character_in_budget = (characterbudget > 0) and (characterbudget >= letterbudget) and (characterbudget >= numberbudget)
        print("Current character budget: " + str(characterbudget))
    else:
        print("Error randomly choosing between numbers, letters, and characters.")

#print using custom * operator to format it
print(*password, sep = '')
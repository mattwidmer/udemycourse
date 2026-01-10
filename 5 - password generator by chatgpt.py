#Humbled by chatgpt with the password generator. This is a learning experience
# Password Generator
import random

# get inputs
letterbudget = int(input("How Many Letters do You Want? 1, 2, 3, 4, 5: "))
numberbudget = int(input("How Many Numbers do You Want? 1, 2, 3, 4, 5: "))
characterbudget = int(input("How Many Special Characters do You Want? 1, 2, 3, 4, 5: "))

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers = ["1","2","3","4","5","6","7","8","9"]

special_characters = ["!","@","#","$","%","^","&","*"]

password = []

# add letters
for _ in range(letterbudget):
    password.append(random.choice(letters))

# add numbers
for _ in range(numberbudget):
    password.append(random.choice(numbers))

# add special characters
for _ in range(characterbudget):
    password.append(random.choice(special_characters))

# shuffle so order is random
random.shuffle(password)

# print password
print(*password, sep="")

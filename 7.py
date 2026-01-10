
#choosing random word
import random
word_list = ["Snake", "Lizard", "Salamander"]
#refreshing list of letters
def initialize_alphabet():
    global letters
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
initialize_alphabet()

#generate random word
def generate():
    global random_word
    random_word = str.lower(random.choice(word_list))
    print(random_word)
    global word_length
    word_length = len(random_word)
    print(word_length)
    print("The word is " + str(word_length) + " letters long.")

#tracking health
health = 6
def lower_health():
    global health
    health -= 1
    print("Your health is now " + str(health))

#make the word into list form
def listify(random_word):
    global random_word_list 
    random_word_list = []
    for x in random_word:
        random_word_list.append(x)
    print(random_word_list)
    #initialize the blank word in list form
    global running_word
    running_word = []
    for x in random_word:
        running_word.append("_")
    print(str(running_word))

#ask user to pick a letter
def ask_for_input():
    global chosen_letter
    chosen_letter = input("What letter will you choose? ").lower()
    print(chosen_letter)

#checking for matching letters and inserting them into the word
def check_for_match(chosen_letter, random_word_list):
    for index, letter in enumerate(random_word_list):
        if chosen_letter == letter:
            print("You got a match! The " + str(letter) +" was in place " + str(index + 1))
            global running_word
            running_word[index] = chosen_letter

#checking for non match and deducting a point if so
match = False
def check_for_no_match(chosen_letter, random_word_list):
    global match
    for index, letter in enumerate(random_word_list):
        if chosen_letter == letter:
            match = True
    if match == False:
        print("Sorry, no matches. You lose one life.")
        lower_health()
    elif match == True:
        match = False

#checks the for matches or no matches based on the guessed letter
def check_sequence(chosen_letter, random_word_list, running_word):
    check_for_match(chosen_letter, random_word_list)
    check_for_no_match(chosen_letter, random_word_list)
    print(running_word)

#Asks you if you want to try again and starts a new game if you say yes
def play_again():
    y_n = input("Play Again? Y/N: ").lower()
    if y_n == "y":
        new_game()

#Run
def new_game():
    global health
    health = 6
    generate()
    listify(random_word)
    while health > 0:
        #first check for win/loss
        for letter in running_word:
            if letter == "_":
                ask_for_input()
                check_sequence(chosen_letter, random_word_list, running_word)
                break
        else:
            print("You won! Congratulations. The word was " + str(running_word))
            play_again
            break

#running it the first time
new_game()

#Constantly checking for death
while health <= 0:
    print("You Lost! ")
    play_again()
    health = 6
import random

#capstone project - blackjack
#requirements - 

#dictionary that contain all cards - 1 is Ace, 11 is Jack, 12 is Queen, 13 is King
deck = ["dAce","d2","d3","d4","d5","d6","d7","d8","d9","d10","dJack","dQueen","dKing", 
        "cAce","c2","c3","c4","c5","c6","c7","c8","c9","c10","cJack","cQueen","cKing",
        "hAce","h2","h3","h4","h5","h6","h7","h8","h9","h10","hJack","hQueen","hKing",
        "sAce","s2","s3","s4","s5","s6","s7","s8","s9","s10","sJack","sQueen","sKing"
        ]

#function to convert a card ex. "d3" to "3 of Diamonds" 
def get_card_name(card:str) -> str:
    suit = ''
    value = card[1:]
    if card[0] == "d":
        suit = "Diamonds"
    elif card[0] == "c":
        suit = "Clubs"
    elif card[0] == "h":
        suit = "Hearts"
    elif card[0] == "s":
        suit = "Spades"
    return str(value) + " of " + suit

#function to get card value
def get_card_value(hand: list, card: str) -> int:
    card = card[1:]
    if card.isnumeric():
        result = card
    elif not card.isnumeric():
        #specifically for aces, if it were to add above 21, the ace value is 1
        if card == "Ace" and get_hand_value(hand) <= 10:
            result = 11
        elif card == "Ace" and get_hand_value(hand) <= 10:
            result = 1
        elif card == "Jack" or card == "Queen" or card == "King":
            result = 10
        else:
            print("Card Value Error")
    return result

#function to pick a random card from the deck and remove it from the deck_items list
def get_random_card(deck : list) -> str:
    chosen_card = random.choice(deck)
    deck = deck.remove(chosen_card)
    return chosen_card

#initializing empty lists that will contain whatever cards were picked
table_cards = []
dealer_cards = []
your_cards = []

#checking any player/dealer hand for a natural 21
def get_natural_21(hand_value:int, hand:list): 
    if hand_value == 21 and len(hand) == 2 :
        return True
    else:
        return False

#adding up values of all cards in a hand
def get_hand_value(hand:list) -> int:
    for card in hand:
        hand_value =+ get_card_value(hand, card)
    return hand_value


#order of operations for a blackjack game
# 1: Draw player's first card and reveal it
your_cards.append(get_random_card(deck))
print("You draw a " + get_card_name(your_cards[-1]))
# 2: Draw dealer's first card and reveal it
dealer_cards.append(get_random_card(deck))
print("The dealer draws a " + get_card_name(dealer_cards[-1]))
# 3: Draw player's second card and reveal it. check for natural 21
your_cards.append(get_random_card(deck))
print("You draw a " + get_card_name(your_cards[-1]))
if get_natural_21(get_hand_value(your_cards), your_cards) == True:
    print("Natural 21!")
    dealer_cards.append(get_random_card(deck))
    if get_hand_value(dealer_cards) == 21:
        print("The dealer drew a " + get_card_name(dealer_cards[-1])+ "for a total of 21! Tie game.")
        exit()
    elif get_hand_value(dealer_cards) < 21:
        print("The dealer drew a " + get_card_name(dealer_cards[-1])+ "for a total of " + str(get_hand_value(dealer_cards)) + ". You win!")
        exit()
    elif get_hand_value(dealer_cards) > 21:
        print("The dealer drew a " + get_card_name(dealer_cards[-1])+ "for a total of " + str(get_hand_value(dealer_cards)) + ". You win!")
        exit()
# 4: Draw dealer's second card and place it face down. If they get nat 21, end game and reveal the card.
dealer_cards.append(get_random_card(deck))
print("The dealer draws a card and places it face down")
if get_natural_21(get_hand_value(dealer_cards), dealer_cards) == True:
    print("The dealer drew a " + get_card_name(dealer_cards[-1]) + ". Natural 21! You lost.")
    exit()
# 5: Player's turn: ask the player to hit or stand. If they hit, draw a card into the player's hand and reveal it. Total the player's card values. Check if we bust. Print total hand value or bust.
if input("Your hand totals " + str(get_hand_value(your_cards)) + ". Hit or Stand?: ").lower()[0] == "s" :
    print("You stand at " + str(get_hand_value(your_cards)))
else:
    your_cards.append(get_random_card())
    print("You pulled a " + get_card_name(your_cards[-1]) + ". Your total is " + str(get_hand_value(your_cards)))
    if get_hand_value(your_cards) > 21: 
        print("Bust! You lose.")
        exit()
    elif get_hand_value(your_cards) == 21:
        print("21! Dealer's turn.")
    else:
        print("Your hand's value is now " + str(get_hand_value(your_cards)))
# 6: Dealer's turn: reveal dealer's second card. If dealer hand value >= 17 print 'dealer stands at (total)'. If dealer hand value < 17, draw a card for the dealer and add it to his hand. Reveal the third card.
print("The dealer reveals their second card. They had pulled a " + get_card_name(dealer_cards[-1]))
if get_hand_value(dealer_cards) < 17: 
    dealer_cards.append(get_random_card())
    print("Dealer pulled a " + get_card_name(dealer_cards[-1]))
    if get_hand_value(dealer_cards) == 21 and get_hand_value(your_cards) == 21:
        print("Tie! You both got 21.")
        exit()
    elif get_hand_value(dealer_cards) == 21:
        print("21! Dealer wins.")
        exit()
    elif get_hand_value(dealer_cards) < 21:
        print("Their total is now " + get_hand_value(dealer_cards))
else:
    print("The dealer's hand value is " + str(get_hand_value(dealer_cards)) + ". They stand.")
# 7: Player's turn again. Print total or bust. If bust, end game and print 'dealer wins'
if get_hand_value(your_cards) < 21:
    if 
    your_cards.append(get_random_card())
    print()
# 8: Dealer's turn again. Print total or bust. If bust, end game and print 'you win'

#Things we need to check every turn: if either party goes over 21, check if the last card is an ace. If it is, take away 11 and add 1 to their total hand value
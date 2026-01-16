#Blackjack
import random

#initializing lists
deck = ["d1","d2","d3","d4","d5","d6","d7","d8","d9","d10","d11","d12","d13", 
        "c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13",
        "h1","h2","h3","h4","h5","h6","h7","h8","h9","h10","h11","h12","h13",
        "s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13"
        ]
player_hand = []
dealer_hand = []

#
#read only functions
#
#takes one card and returns the name
def get_card_name(card:str) -> str:
    suit = ''
    if card[0] == "d":
        suit = "Diamonds"
    elif card[0] == "c":
        suit = "Clubs"
    elif card[0] == "h":
        suit = "Hearts"
    elif card[0] == "s":
        suit = "Spades"
    if card[1:] == "1":
        value = "Ace"
    elif card[1:] == "11":
        value = "Jack"
    elif card[1:] == "12":
        value = "Queen"
    elif card[1:] == "13":
        value = "King"
    else:
        value = card[1:]
    return str(value) + " of " + suit

def get_card_value(card:str) -> int:
    card_value = 0
    if card[1:] == "1":
        card_value = 11
    elif card[1:] == "11":
        card_value = 10
    elif card[1:] == "12":
        card_value = 10
    elif card[1:] == "13":
        card_value = 10
    else:
        card_value = int(card[1:])
    return card_value

#takes a hand and adds up values - clause for Ace included
def get_hand_value(hand:list)-> int:
    hand_value = 0 
    for card in hand:
        hand_value += get_card_value(card)
    #check if there's an ace and if hand value is over 21. If true, subtract 10 from hand value
    ace_in_hand = False
    for card in hand:
        if card[1:] == "1":
            ace_in_hand = True
    if ace_in_hand == True and hand_value > 21:
        hand_value -= 10
    return hand_value

#checks the current hand value and returns true if over 21
def check_for_bust(hand:list) -> bool:
    hand_value = get_hand_value(hand)
    if hand_value > 21:
        return True
    else:
        return False

#
#manipulation functions
#
#draw a card into passed hand and remove it from the deck
def draw_card(deck:list, hand:list):
    drawn_card = random.choice(deck) 
    deck = deck.remove(drawn_card)
    hand = hand.append(drawn_card)

def deal_cards(deck:list, dealer_hand:list, player_hand:list):
    #first round
    draw_card(deck, player_hand)
    print("You are dealt your first card. It is the " +  get_card_name(player_hand[0]))
    draw_card(deck, dealer_hand)
    print("The dealer draws their first card. It is the " + get_card_name(dealer_hand[0]))
    #second round
    draw_card(deck, player_hand)
    print("You are dealt your second card. It is the " +  get_card_name(player_hand[1]))
    if get_hand_value(player_hand) == 21:
        print("Natural 21!")
    draw_card(deck, dealer_hand)
    print("The dealer draws their second card and places it face down.")
    if get_hand_value(dealer_hand) == 21:
        print("The dealer drew a Natural 21 with the " + get_card_name(dealer_hand[-1]))
        if get_hand_value(player_hand) == 21 and get_hand_value(dealer_hand) == 21:
            print(" You both got a natural 21! Tie.")
            exit()
        else:
            print("The dealer wins with a Natural 21.")
            exit()
    
#player alway goes before dealer. We only need to check for bust after a card is drawn
def player_turn(player_hand:list):
    print("Your starting hand is the " + get_card_name(player_hand[0]) + " and the " + get_card_name(player_hand[1]))
    print("The total value of your hand is " + str(get_hand_value(player_hand)))
    
    while check_for_bust(player_hand) == False:
        player_choice = input("Do you hit or stand? ")
        player_choice = player_choice.strip().lower()[0]
        if player_choice == "h":
            draw_card(deck, player_hand)
            print("You drew the " + get_card_name(player_hand[-1]))
            print("The total value of your hand is " + str(get_hand_value(player_hand)))
            if check_for_bust(player_hand) == True:
                print("Bust! You lose.")
                exit()
        elif player_choice == "s" :
            print("You stand. Your final hand value is " + str(get_hand_value(player_hand)) + ". Dealer's turn.")
            return
#dealer's turn (final turn)
def dealer_turn(dealer_hand:list):
    #keep drawing cards face up until the total is 17 or over
    while len(dealer_hand) >= 2 and get_hand_value(dealer_hand) < 17:
        draw_card(deck, dealer_hand)
        print("The dealer draws a card and places it face up. The card is the " + get_card_name(dealer_hand[-1]) + ". Their hand value is now " + str(get_hand_value(dealer_hand)))
        if check_for_bust(dealer_hand) == True:
            print("Dealer bust! You win.")
            exit()
    else:
        print("The dealer stands with a final hand value of " + str(get_hand_value(dealer_hand)))
        print("The dealer ends with " + str(get_hand_value(dealer_hand)) + ". You end with " + str(get_hand_value(player_hand)))
        if get_hand_value(dealer_hand) > get_hand_value(player_hand):
            print("The dealer wins.")
            exit()
        elif get_hand_value(dealer_hand) < get_hand_value(player_hand):
            print("You win!")
            exit()
    
#running everything
deal_cards(deck,dealer_hand,player_hand)
player_turn(player_hand)
dealer_turn(dealer_hand)

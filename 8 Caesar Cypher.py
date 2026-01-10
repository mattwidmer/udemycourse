#Day 8 Caesar Cypher - assisted by chatgpt to find out about string import but written by me
import string

#initialization
text = "The quick brown fox jumped over the lazy dog."
shift_amount = 0

#ask user for shift amount
def ask_for_shift_amount():
    global shift_amount
    shift_amount = int(input("How much to shift each letter by? "))

#shift the alphabet by the set amount using string import and str. function. I learned about import string here
def encode_text(shift_amount):
    global encoded_alphabet
    encoded_alphabet = string.ascii_lowercase[shift_amount:] + string.ascii_lowercase[:shift_amount]
    print(encoded_alphabet)

#creating translation table and translating the original text - can be condensed into one line. I learned about translation tables here
def create_translation_table(encoded_alphabet, text):
    global translation_table
    translation_table = str.maketrans(encoded_alphabet, string.ascii_lowercase)

#encoding text
def encode_text(text):
    text = text.translate(translation_table)
    print(text)

#decoding text
#use translation table backwards on the already encoded string - must be used with encoded string
def decode_text(text):
    text = text.translate(translation_table)
    print(text)
    
#running
ask_for_shift_amount()
encode_text(shift_amount)
create_translation_table(encoded_alphabet, text)
encode_text(text)
decode_text(text)
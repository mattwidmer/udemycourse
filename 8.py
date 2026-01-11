#Day 8 Caesar Cypher - assisted by chatgpt to find out about string import but written by me
import string

#initialization
text = "The quick brown fox jumped over the lazy dog."

#ask user for shift amount
def ask_for_shift_amount():
    return int(input("How much to shift each letter by? "))

#shift the alphabet by the set amount using string import and str. function. I learned about import string here
def shift_alphabet(shift_amount):
    return string.ascii_lowercase[shift_amount:] + string.ascii_lowercase[:shift_amount]

#creating translation table and translating the original text - can be condensed into one line. I learned about translation tables here
def create_translation_tables(encoded_alphabet):
    return str.maketrans(encoded_alphabet, string.ascii_lowercase), str.maketrans(string.ascii_lowercase, encoded_alphabet)

#encoding text
def encode_text(text, translation_table):
    text = text.translate(translation_table)
    print(text)

#decoding text
#use translation table backwards on the already encoded string - must be used with encoded string
def decode_text(text, translation_table):
    text = text.translate(translation_table)
    print(text)

#running
shift_amount = ask_for_shift_amount()
shifted_alphabet = shift_alphabet(shift_amount)
translation_table, reverse_translation_table = create_translation_tables(shifted_alphabet)
print(translation_table, reverse_translation_table)
encode_text(text, translation_table)
decode_text(text, reverse_translation_table)
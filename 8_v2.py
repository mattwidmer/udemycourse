import string

#initialization
text = "The quick brown fox jumped over the lazy dog."

#ask user for shift amount
def ask_for_shift_amount():
    return int(input("How much to shift each letter by? "))

#shift the alphabet by the set amount using string import and str. function. I learned about import string here
def shift_alphabet(alphabet_str, shift_amount):
    return alphabet_str[shift_amount:] + alphabet_str[:shift_amount]


shift_amount = ask_for_shift_amount()
alphabet_lc = string.ascii_lowercase
alphabet_uc = string.ascii_uppercase
offset_alphabet_lc = shift_alphabet(string.ascii_lowercase, shift_amount)
offset_alphabet_uc = shift_alphabet(string.ascii_uppercase, shift_amount)

def get_shifted_char(char):
    if char in alphabet_lc:
        return offset_alphabet_lc[alphabet_lc.index(char)]
    if char in alphabet_uc:
        return offset_alphabet_uc[alphabet_uc.index(char)]
    return char

def get_unshifted_char(char):
    if char in alphabet_lc:
        return alphabet_lc[offset_alphabet_lc.index(char)]
    if char in alphabet_uc:
        return alphabet_uc[offset_alphabet_uc.index(char)]
    return char

encoded_string = ""
for c in text:
    encoded_string += get_shifted_char(c)
decoded_string = ""
for c in encoded_string:
    decoded_string += get_unshifted_char(c)

print(text)
print(encoded_string)
print(decoded_string)
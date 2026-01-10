#check if number is odd or even using modulo

number = int(input("Choose an Integer. "))
remainder = int(number % 2)
if remainder == 0:
    state = "Even"
else:
    state = "Odd"

print("Your number is " + state)

#nested if statements
age = int(input("How old are you? "))
height = int(input("How tall are you in inches? "))
if height > 50:
    if age < 12:
        price = 5
    elif 12 >= age < 18:
        price = 10
    elif age >= 18:
        price = 15
else:
    price = "You are too short to ride this ride."

photos = input("Do you want photos? Yes or No: ")
if photos == "Yes":
    price += 3

print(f"Your total price is ${price}")
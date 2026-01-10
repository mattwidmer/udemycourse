#Tip Calculator
print("Welcome to the Tip Calculator!")
total = input("What was the total bill? $")
tip_percentage = input("How much would you like to tip? 10, 12, or 15? ")
n_guests = input("How many people will be splitting the bill? ")
tip_amount = float(total) * (float(tip_percentage) / 100.0) / float(n_guests)
tip_amount_rounded = round(tip_amount, 2)
print(f"Each person should pay ${tip_amount_rounded}.")
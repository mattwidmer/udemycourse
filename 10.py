#Calculator
calculation = 0.0
operation = ''
first_number = 0.0
second_number = 0.0

#ask user to continue
another_calculation = True
def get_another_calculation():
    user_response = input("Do another calculation? Y/N: ")
    if user_response.strip().lower()[0] == "n":
        return False
    else:
        return True

#get operation from user
def get_operation():
    user_response = input("What operation would you like? Addition, Subtraction, Multiplication, Division: ")
    user_response = user_response.strip().lower()[0] 
    if user_response == "a":
        operation = "a"
    elif user_response == "s":
        operation = "s"
    elif user_response == "m":
        operation = "m"
    elif user_response == "d":
        operation = "s"
    return operation

#get a number from the user
def get_number()-> float:
    chosen_number = input("What number? ").strip()
    chosen_number = float(chosen_number)
    return chosen_number

#runs a calculation with two numbers based on input operation
def calculate(n1:float,n2:float, operation:str) -> float:
    if operation == "a":
        return n1 + n2
    elif operation == "s":
        return n2 - n2 
    elif operation == "m":
        return n1 * n2
    elif operation == "d":
        return n1 / n2

#running
while another_calculation == True:
    first_number = get_number()
    operation = get_operation()
    second_number = get_number()
    calculation = calculate(first_number,second_number,operation)
    print("The answer is " + str(calculation))
    another_calculation = get_another_calculation()
else:
    print("Finished Calculation. The final result was " + str(calculation))
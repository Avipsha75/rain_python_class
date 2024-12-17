#Game Simple Number
for i in range (1, 10):
    first_number = int(input("Enter your first number: ")) # User input number in integer

    double_number = first_number * 2 # double
    print(f"Your double number is {double_number}") #print result

    addition_number = double_number + 10 # add 10 or we can also write double_bumber += 10 which means double_number = double_number + 10
    print(F"Add 10 = {addition_number}")

    half_number = addition_number / 2 #divide 2
    print(f"Half number = {half_number}") #print result

    subtraction_number = half_number - first_number
    print(f"Subtraction number = {subtraction_number}") #print result

    user_choice = input("""
    Do you want to continue? Yes or No
    """)
    if user_choice.lower() == "no":
        break
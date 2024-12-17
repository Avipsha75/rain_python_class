first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: ")) # We can do this way as well

#first_number = int(first_number): We can do this way as well
user_choice = input("""
                    Please choose your option
                    + for Addition
                    - for Subtraction
                    * for Multiplication
                    / for Division
                    % for Modulus
                    ** for Exponent
                    """)
if user_choice == "+":
    print(" Addition =", first_number + second_number)
elif user_choice == "-":
    print(" Subtraction =", first_number - second_number)
elif user_choice == "*":
    print(" Multiplication =", first_number * second_number)
elif user_choice == "/":
    print("Division =", first_number / second_number)
elif user_choice == "%":
    print("Modulus =", first_number % second_number)
elif user_choice == "**":
    print("Exponent =", first_number ** second_number)
else:
    print("Invalid input")


while True:
    # To find LCM of two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    max_num = max(num1, num2)

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            print(f"The LCM of {num1} and {num2} is {max_num}")
            break  # Exit the inner loop when LCM is found
        max_num += 1  # Increment the max number until we find the LCM
    
    # Ask user if they want to continue
    user_choice = input("""
    Do you want to continue? Yes or No
    """)
    if user_choice.lower() == "no":
        break  # Exit the outer loop if user says "no"
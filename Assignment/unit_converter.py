while True:
    user_choice = input("""
        Please choose your option
        1. KM to Miles
        2. Miles to KM
        3. Centimeter to Inches
        4. Inches to Centimeter
        """)
    if user_choice == "1":
        user_input = float(input("Enter KM: "))
        result = user_input * 0.621371
        print(f"{user_input} KM is equal to {result} Miles")

    elif user_choice == "2":
        user_input = float(input("Enter Miles: "))
        result = user_input * 1.60934
        print(f"{user_input} Miles is equal to {result} KM")

    elif user_choice == "3":
        user_input = float(input("Enter Centimeter: "))
        result = user_input * 0.393701
        print(f"{user_input} Centimeter is equal to {result} Inches")

    elif user_choice == "4":
        user_input = float(input("Enter Inches: "))
        result = user_input * 2.54
        print(f"{user_input} Inches is equal to {result} Centimeter")
    else:
        print("Invalid input")

    user_choice = input("""
        Do you want to continue? Yes or No
        """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the converter. Goodbye!")
        break
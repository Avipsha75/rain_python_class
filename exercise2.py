while True:
    user_choice = input("""
        Please choose your option
        1. Simple Interest
        2. Compound Interest
        """)
    if user_choice == "1":
        p = float(input("Enter principal amount: "))
        t = float(input("Enter time period: "))
        r = float(input("Enter rate of interest: "))
        si = (p * t * r)/100
        print("Simple Interest =", si)
    elif user_choice == "2":
        p = float(input("Enter principal amount: "))    
        r = float(input("Enter rate of interest: "))
        t = float(input("Enter time period: "))
        ci = p * (1 + r / 100) ** t-p
        print("Compound Interest =", ci)
    else:
        print("Invalid input")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
while True:
    #Multiplication Table
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
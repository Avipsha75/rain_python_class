while True:
    # Check leap year
    year = int(input("Enter a year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
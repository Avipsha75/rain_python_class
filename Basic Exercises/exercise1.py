while True:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    meter = float(input("Enter length in meter: "))
    kilometer = meter / 1000
    print(f"{meter} meters is equal to {kilometer} kilometers.")    

    feet = float(input("Enter length in feet: "))
    inches = feet * 12
    print(f"{feet} feet is equal to {inches} inches.")

    dollar = float(input("Enter the currency in dollars: "))
    Nepali_rupees = dollar * 133
    print(f"{dollar} $ is equal to Rs {Nepali_rupees}.")
    user_choice = input("""
        Do you want to continue? Yes or No
        """)
    if user_choice.lower().strip() == "no": # .lower() is used to convert the string into lowercase and .strip() is used to remove the extra spaces.
        print("Thank you for using the converter. Goodbye!")
        break
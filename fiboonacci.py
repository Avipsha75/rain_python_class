while True:
    # Fibonacci Sequence
    n = int(input("Enter a number: "))
    a, b = 0, 1
    while a < n:
        print(a, end=" ")  # This will print the Fibonacci sequence on the same line
        a, b = b, a + b

    # Ask the user if they want to continue
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
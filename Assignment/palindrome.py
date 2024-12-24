while True:
    # Check for palindrome
    user_input = input("Enter a word: ")
    if user_input == user_input[::-1]:
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
    
    

    
    
    
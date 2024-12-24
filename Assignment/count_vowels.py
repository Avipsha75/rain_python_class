while True:
    # Count Vowels
    user_input = input("Enter a word: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1

    # These should be inside the loop
    print(f"Number of vowels in the string: {count}")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break 
    
    



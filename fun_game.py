def setup_mission():
    print("Setting up mission.......")
    available_food = [
        "apple",
        "banana",
        "orange",
        "mango",
        "grapes",
        "watermelon",
        "pineapple",
        "strawberry",
        "blueberry",
        "kiwi",
        "cherry",
        "pear",
        "pizza",
        "burger",
        "pasta",
        "sushi",
        "ramen",
    ]
    available_crews = int(input("Enter available crews:"))
    print("Setup Completed......")

    return available_crews, available_food

def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")

    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!")

    print("Your battery is dead please change the battery")

    print("Mission completed")

alien_attack_game()

    






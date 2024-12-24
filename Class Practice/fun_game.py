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

# check batteries over hundred
def get_charged_batteries():
    batteries = [50, 30 ,4, 45, 12, 18, 30] ## battery basket
    minimum_battery_power = 20 ## battery use minimum 20% charge
    usuable_battery_power = 0
    usuable_battery_count = 0
    for battery in batteries: ## check every battery
        if battery > minimum_battery_power: #check if battery is over charge 20% to use
            usuable_battery_power += battery # if yes use power added
            usuable_battery_count += 1 # if yes use battery count added
            if usuable_battery_power >= 100: # if power is over 100
                return usuable_battery_power, usuable_battery_count

def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1] ##reverse string
    return human_message

def food_divide_equally(foods, crews_member):
    equally_foods = len(foods) // crews_member
    remaining_foods = len(foods) % crews_member
    return equally_foods, remaining_foods

def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")

    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!")

    print("Your battery is dead please change the battery")
    battery_power, battery_count = get_charged_batteries()

    print("Hurray!!! Your battery is charged.")

    print("Oops... Alien has arrived saying:")
    print("rednerrus")

    decrypted_text = decrypt_alien_message("rednerrus")

    print(f"Alien is saying: {decrypted_text}")
    print("Alien has captured all astronauts")

    print("if astronaut wants to escape they have divide each food and give remaining foods")

    equally_divided, remaining_food = food_divide_equally(foods, crews_number)

    print(f"You have {equally_divided} foods divided equally and remaining = {remaining_food}")

    print("Okay... Now you can go to Earth")

    print("Mission completed")

alien_attack_game()

    






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

available_crews = 3

each_crew_food = len(available_food) // available_crews

remaining_food_count = len(available_food) % available_crews

print(f"Each crew get {each_crew_food} food and Remaining food count = {remaining_food_count}")

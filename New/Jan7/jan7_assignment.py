from collections import OrderedDict

grocery_list = OrderedDict()

def add_item(item, quantity):
    if item in grocery_list:
        grocery_list[item] += quantity  
    else:
        grocery_list[item] = quantity  

def remove_item(item):
    if item in grocery_list:
        del grocery_list[item]
        print(f"Removed {item} from the list.")
    else:
        print(f"{item} not found in the list.")

def display_list():
    print("\nGrocery List:")
    for item, quantity in grocery_list.items():
        print(f"- {item}: {quantity}")
    print("\nTotal Items:", len(grocery_list))

def clear_list():
    grocery_list.clear()
    print("The grocery list has been cleared.")

def grocery_list_menu():
    while True:
        print("\n--- Grocery List Organizer ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display List")
        print("4. Clear List")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            item = input("Enter the item name: ").strip()
            try:
                quantity = int(input("Enter the quantity: "))
                add_item(item, quantity)
                print(f"Added {quantity} of {item}.")
            except ValueError:
                print("Please enter a valid quantity.")
        elif choice == '2':
            item = input("Enter the item name to remove: ").strip()
            remove_item(item)
        elif choice == '3':
            display_list()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("Exiting Grocery List Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    grocery_list_menu()

def display(menu_card):
    print("Menu Card:")
    for starter_key, starter_value in menu_card.items():
        print(f"{starter_key}: {starter_value}")

def add(menu_card):
    key = input("Enter the starter key to be added: ")
    value = input("Enter the starter name to be added: ")
    menu_card[key] = value
    print("Item added successfully.")
    return menu_card

def update(menu_card):
    starter_key = input("Enter the starter key to be updated: ")
    if starter_key in menu_card:
        updated_value = input("Enter the new starter name to be updated: ")
        menu_card[starter_key] = updated_value
        print("Item updated successfully.")
    else:
        print("Entered key is not in the menu.")
    return menu_card

def remove(menu_card):
    starter_key = input("Enter the starter key to be removed: ")
    if starter_key in menu_card:
        removed_item = menu_card.pop(starter_key)
        print(f"Item '{removed_item}' removed successfully.")
    else:
        print("Entered key is not in the menu.")
    return menu_card

def main():
    menu_card = {
        '1': 'paneer 65', 
        '2': 'chilly paneer', 
        '3': 'veg crispy',
        '4': 'Corn kabab',
        '5': 'veg spring roll',
        '6': 'stuffed mushrooms',
        '7': 'baby corn fry',
        '8': 'cheese balls',
        '9': 'paneer tikka',
        '10': 'veg kebab'
    }
    
    actions = {
        1: ('Display Menu Card', display),
        2: ('Add Starter', add),
        3: ('Update Starter', update),
        4: ('Remove Starter', remove),
        5: ('Exit', None)
    }

    while True:
        print("\nMenu Management")
        for key, (description, _) in actions.items():
            print(f"{key}. {description}")
        choice = int(input("Enter your choice: "))
        
        if choice in actions:
            if choice == 5:
                break
            else:
                menu_card = actions[choice][1](menu_card)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

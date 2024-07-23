
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
    menu_card = {'1': 'paneer 65', '2': 'chilly paneer', '3': 'veg crispy'}
    while True:
        print("\nMenu Management")
        print("1. Display Menu Card")
        print("2. Add Starter")
        print("3. Update Starter")
        print("4. Remove Starter")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display(menu_card)
        elif choice == 2:
            menu_card = add(menu_card)
        elif choice == 3:
            menu_card = update(menu_card)
        elif choice == 4:
            menu_card = remove(menu_card)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

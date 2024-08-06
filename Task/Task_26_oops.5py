class MenuCard:
    def __init__(self):
        self.menu_card = {'1': 'paneer 65', '2': 'chilly paneer', '3': 'veg crispy'}

    def display(self):
        print("Menu Card:")
        for key, value in self.menu_card.items():
            print(f"{key}: {value}")

    def add(self):
        key = input("Enter the starter key to be added: ")
        value = input("Enter the starter name to be added: ")
        self.menu_card[key] = value
        print("Item added successfully.")

    def update(self):
        starter_key = input("Enter the starter key to be updated: ")
        if starter_key in self.menu_card:
            updated_value = input("Enter the new starter name to be updated: ")
            self.menu_card[starter_key] = updated_value
            print("Item updated successfully.")
        else:
            print("Entered key is not in the menu.")

    def remove(self):
        starter_key = input("Enter the starter key to be removed: ")
        if starter_key in self.menu_card:
            removed_item = self.menu_card.pop(starter_key)
            print(f"Item '{removed_item}' removed successfully.")
        else:
            print("Entered key is not in the menu.")

def main():
    menu = MenuCard()
    while True:
        print("\nMenu Management")
        print("1. Display Menu Card")
        print("2. Add Starter")
        print("3. Update Starter")
        print("4. Remove Starter")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            menu.display()
        elif choice == 2:
            menu.add()
        elif choice == 3:
            menu.update()
        elif choice == 4:
            menu.remove()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def create_burger(*foods):
    if not foods:
        print("No foods added to your burger.")
        return foods

    print("Burger Order:")
    for food in foods:
        print(f"{food}")
    print("Your burger has been ordered with the above foods.")

def main():
    items_input = input("Enter the items for your burger, separated by commas: ").split(',')
    order_items = []
    for item in items_input:
        order_items.append(item.strip())
    create_burger(*order_items)

if __name__ == "__main__":
    main()

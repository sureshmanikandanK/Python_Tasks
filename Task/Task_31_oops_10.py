class ShoppingCart:
    def __init__(self):
        self.items = {
            "bread": 200,
            "milk": 150,
            "cheese": 500,
            "butter": 250,
            "coffee": 300,
            "tea": 180,
            "juice": 400,
        }
        self.user_items = {}

    def adding_items(self, item,price):
        self.user_items[item] = price
        print(f"Added {item} to cart.")

    def remove_items(self, item):
        self.user_items.pop(item)
        print(f"Removed {item} from cart.")

    def total_items(self):
        print(f"Total Items: {len(self.items)}")

    def total_price(self):
        total_price = sum(self.items.values())
        print(f"Total price: {total_price}")
    def Display(self):
        print(f'The Products are {self.user_items}')


Items = ShoppingCart()
Items.adding_items("Parota",'400')
Items.total_price()
# Items.remove_items("Parota")
Items.total_items()
Items.Display()


class Bookstore:
    No_of_Books = 0

    def __init__(self):
        self.Name = ""
        self.Author = ""
        Bookstore.No_of_Books += 1

    def Create(self):
        self.Name = input('Enter Book name: ')
        self.Author = input('Enter Author name: ')

    def Display(self):
        print(f'{self.Name} {self.Author} {Bookstore.No_of_Books}')
Obj1 = Bookstore()
Obj1.Create()
Obj1.Display()

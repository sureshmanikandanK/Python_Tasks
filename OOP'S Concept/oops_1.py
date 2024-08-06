#create a class and Object

class Student:
    def __init__(self,firstname,lastname):
        self.firstname = firstname #instance variable
        self.lastname = lastname
    def Display(self):
        print(f'{self.firstname} {self.lastname}')
    

Obj1=Student('Suresh','Manikandan')
# print(Obj1.firstname)
Obj1.Display()
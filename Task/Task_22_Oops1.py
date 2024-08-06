
class Demo:
    def __init__(self,first,last):
        self.first = first 
        self.last = last
    def Fun(self):
        print(f'{self.first} {self.last}')
    def Gun(self):
        print(f'{self.first} {self.last}')
    

Obj1=Demo(11,21)
Obj2=Demo(51,101)
Obj1.Fun()
Obj1.Gun()
Obj2.Fun()
Obj2.Gun()





class Person:
    def __init__(self,id,name):
        self.id=id
        self._name=name

    def Displayinfo(self):
        print(f'Name : {self._name} Id: {self.id}')

class employee(Person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    
    
# Emp=Person('Suresh','4455')
# Emp.Displayinfo()

Emp=employee('4455','Suresh','20000')
Emp.Displayinfo()
print(Emp.salary)
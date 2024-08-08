# Public : These are accesible from the outside
# Protected : _single underscore within the class and its subclass
class Employee:
    def __init__(self,name,salary):
        self.name=name#public
        self._salary=salary#protected instaance attribute
    def Displaysalary(self):
        print(f'{self.name} and salary is {self._salary}')
        

e1=Employee('suresh','52200')
print(e1._salary)
e1._salary='40000'
print(e1.name)
e1.Displaysalary()

# Private: __double underscore
class Employee:
    def __init__(self,name,salary):
        self.name=name#public
        self.__salary=salary#Private instaance attribute
        # self.__Displaysalary()
    def Displaysalary(self,salary):
        self.__salary = salary

        print(f'{self.name} and salary is {self.__salary}')
        

e1=Employee('suresh','52200')
# print(e1.__salary)
print(e1.name)
e1.name='Ajith'
e1.__salary='54444'
e1.Displaysalary(50000)

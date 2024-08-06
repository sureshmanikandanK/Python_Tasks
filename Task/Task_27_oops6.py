class Arithmetic:
    def __init__(self) -> None:
        value1=0
        value2=0
    def Accept(self):
        self.value1=int(input("Enter value 1"))
        self.value2=int(input("Enter value 2"))
    def Addition(self):
        print(f"{self.value1} + {self.value2 } ={self.value1+self.value2}")
    def Subraction(self):
        print(f"{self.value1} - {self.value2 } ={self.value1-self.value2}")
    def Multiplication(self):
        print(f"{self.value1} * {self.value2 } ={self.value1*self.value2}")
    def Division(self):
        print(f"{self.value1} / {self.value2 } ={self.value1/self.value2}")
Operations=Arithmetic()
Operations.Accept()
Operations.Addition()
Operations.Subraction()
Operations.Multiplication()
Operations.Division

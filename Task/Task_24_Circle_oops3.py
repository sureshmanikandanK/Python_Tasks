class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0
        self.Area=0
        self.circumference=0
    def Accept(self):
        self.Radius=int(input('Enter the Radius: '))
    def CalculateArea(self):
        self.Area = Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.circumference=2*Circle.PI*self.Radius

    def Display(self):
        print(f' Area of Circle : {self.Area}')
        print(f'Circumfernce of the circle : {self.circumference}')

Answer=Circle()
Answer.Accept()
Answer.CalculateArea()
Answer.CalculateCircumference()
Answer.Display()
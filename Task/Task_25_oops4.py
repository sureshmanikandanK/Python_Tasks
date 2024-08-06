class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.Name=""
        self.Amount=0

    def create(self):
        self.Name=input('Enter your Name ')
    
    def Deposit (self):
       self.Amount=int(input('Enter Amount '))

    def Withdraw(self,afterWidthdraw):
        self.Amount1=int(input('Enter the amount to widthdraw '))
        afterWidthdraw=self.Amount-self.Amount1
        print(f'{afterWidthdraw}')

    def CalculateInterest(self):
        print(self.Amount*BankAccount.ROI/100)

    def Display(self):
        print(f'{self.Name} {self.Amount}')

user=BankAccount()
user.create()
user.Deposit()
user.Withdraw()
user.CalculateInterest()
user.Display()
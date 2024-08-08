class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 1000

    def create(self):
        self.Name = input('Enter your Name: ')
    
    def Deposit(self):
        deposit_amount = int(input('Enter Amount to Deposit: '))
        self.Amount += deposit_amount

    def Withdraw(self):
        withdraw_amount = int(input('Enter the amount to Withdraw: '))
        self.Amount -= withdraw_amount
        self.Amount = max(self.Amount, 0)
        print(f'Remaining balance: {self.Amount}')

    def CalculateInterest(self):
        interest = self.Amount * BankAccount.ROI / 100
        print(f'Interest amount: {interest}')

    def Display(self):
        print(f'Account Holder: {self.Name}, Balance: {self.Amount}')

user = BankAccount()
user.create()
user.Deposit()
user.Withdraw()
user.CalculateInterest()
user.Display() 


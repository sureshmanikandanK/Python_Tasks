#Instance Variable : Name,Amount,Address,Account No
#Instance Method: CreateAccount(),DisplayAccountInfo()

class Bank_Account:
    Bank_name = 'Indian'
    ROI_On_FD = '12%'
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.Account_No = 0
    def CreateAccount(self):
        self.Name = input("Please provide your Name: ")
        self.Amount = input("Please provide the Amount: ")
        self.Address = input("Please provide your Address: ")
        self.Account_No = int(input("Please provide your Account Number: "))
    def DisplayAccountInfo(self):
        print(f'Your Account details : \n{self.Name}\n {self.Amount}\n {self.Address}\n {self.Account_No}')
    @classmethod
    def DisplayBankInfo(cls):
        print(f'Bank Name : {cls.Bank_name} and you have ROI of :{cls.ROI_On_FD}')
    @staticmethod
    def DisplayKYCInfo(customer_name, customer_photo, address):
        print(f"Customer AAdhar: {customer_name}")
        print(f"Customer Photo: {customer_photo}")
        print(f"Address: {address}")
    
        
Bank_Account.DisplayKYCInfo('102211202121', 'Photo', 'Chennai')
def main():
    Account=Bank_Account()
    Account.CreateAccount()
    Account.DisplayAccountInfo()
    print(Account.Bank_name)
    print(Account.ROI_On_FD)
    Account.DisplayBankInfo()

if __name__ == '__main__':
    main()
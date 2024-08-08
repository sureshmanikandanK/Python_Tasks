class Bank:
    @staticmethod
    def DisplayKYCInfo(customer_name, customer_id, address):
        print(f"Customer Name: {customer_name}")
        print(f"Customer ID: {customer_id}")
        print(f"Address: {address}")
        
Bank.DisplayKYCInfo('Suresh', '101', 'Chennai')

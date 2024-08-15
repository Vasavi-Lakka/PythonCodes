


































'''class Bank:
    bank_name='SBI'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'Name of the Customer {self.name}')
        print(f'acount of the Customer {self.account}')
        print(f'balance of the Customer {self.balance}')
        print(f'address of the Customer {self.address}')
    def withdraw(self):
        amount=int(input('enter amount:'))
        if self.balance>=amount:
            self.balance-=amount
            print('withdrawal is successful')
            print(f'balance is {self.balance}')
        else:
            print("InSufficient Balance")
            print(f'balance is {self.balance}')
    def deposit(self):
        amount=int(input('enter amount:'))
        if amount>0:
            self.balance+=amount
            print('Deposit done')
            print(f'Total balance {self.balance}')

        
jaya=Bank('Jayasree',98765,10000,'delhi')
sushma=Bank('sushmitha',87654,20000,'chennai')
jaya.customer_details()
#jaya.withdraw()
jaya.deposit()

print(jaya.name)
print(sushma.name)

print(jaya.bank_name)
print(sushma.bank_name)

'''

class Bank:
    bank_name='SBI'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    @classmethod
    def bank_details(cls):
        print(cls.bank_name)
        print(cls.bank_ifsc)
        print(cls.bank_roi)
        print(cls.bank_address)
    @staticmethod
    



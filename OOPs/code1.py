class Bank:
    bank_Name='SBI'
    bank_address='kizikisthan'
    bank_roi=6
    bank_ifsc=1245
jaya=Bank()
vasu=Bank()
print(Bank.bank_Name)
print(jaya.bank_Name)
print(vasu.bank_Name)
Bank.bank_roi=5
print(Bank.bank_roi)
print(jaya.bank_roi)
print(vasu.bank_roi)
Bank.bank_num=683475561581
print(Bank.bank_num)
print(vasu.bank_num)
print(jaya.bank_num)
jaya.bank_email='vasu@12'
print(jaya.bank_email)
print(Bank.bank_email)

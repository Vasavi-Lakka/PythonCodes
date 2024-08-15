'''a=input()
b=int(input())
c=input()
print(a[:b]+c+a[b+1:])'''

'''
s=str(input())
n=int(input())
s1=str(input())
S=s.replace(s[n],s1)
print(S)'''


s=input()
r=int(input())
n=s[-1:-4:-1]
print(n[::-1]*r)

































'''class Bank:
    bank_name='SBI'
    bank_ifsc=12456
    bank_address='kizikisthan'
    bank_roi=6

Gwen=Bank()
stacy=Bank()
#Accesing the generic properties by class and object
#clas:- className.classVariablename
#object:-objectname.classVariableName
print("Accesing the generic properties by class")

print(Bank.bank_name)
print(Bank.bank_roi)
print(Bank.bank_address)

print("Accesing the generic properties by object")

print(Gwen.bank_name)
print(stacy.bank_name)
print(Gwen.bank_roi)
print(stacy.bank_roi)

print(stacy.bank_address)
print(Gwen.bank_address)

#Modificationo of  the generic properties by class
#className.ClassVariableName=NewValue

print("modifying the class variable with new Value")

Bank.bank_roi=5

print(Bank.bank_roi)
print(Gwen.bank_roi)
print(stacy.bank_roi)
print(Bank.bank_mobile)



#Creating new generic property by class
#className.NewClsvariableName=value
Bank.bank_mobile=9878765869


print(Bank.bank_mobile)

'''
























class School:
    school_name='St Arnolds high school'
    school_Address='Medarametla'
    school_Number=987654321
    school_Principal='Antony'
    def __init__(self, n,rolnum, cls, sec, fee):
        self.StudentName=n
        self.StudentRolNum=rolnum
        self.StudentClass=cls
        self.StudentSection=sec
        self.Studentfee=fee
    def studentDetails(self):
        print(f'student Name:{self.StudentName}')
        print(f'student Roll Number:{self.StudentRolNum}')
        print(f'student Class:{self.StudentClass}')
        print(f'student Section:{self.StudentSection}')
        print(f'student Fee:{self.Studentfee}')
    def Student_fee(self):
        amount=int(input('Enter the amount:'))
        if amount>=self.Studentfee:
            self.Studentfee-=amount
            print('Amount Paid')
            print(f'Remaing money need to return: {self.Studentfee}')
        elif self.Studentfee>=amount:
            self.Studentfee-=amount
            print('payment Successfull')
            print(f'Need to pay remaining fee Balance: {self.Studentfee}')
        elif self.Studentfee==amount:
            print('Total Amount Paid')
            print('Payment Successfull')
vasavi=School('Vasavi Lakka', 215, '10th', "A",59100)

vasavi.studentDetails()

vasavi.Student_fee()























'''
vasavi=School('Vasavi Lakka', 66735726819, '10th', "A")
Sudha=School('Vasudha', 72412897561, '9th','B')

print('school:',vasavi.school_name)
print("Name:",vasavi.StudentName)
print("Class:",vasavi.StudentClass)
print("section:",vasavi.Section)


print('school:',Sudha.school_name)
print("Name:",Sudha.StudentName)
print("Class:",Sudha.StudentClass)

print("section:",Sudha.Section)
'''




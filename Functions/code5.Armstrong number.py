#WIthoutFunction
'''
n=int(input())
summ=0
fs=0
dummy=n
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    fs+=rem**l
if fs==n:
    print(n,'is armstrong')
else:
    print(n,'is not Armstromg')
'''


#With function without range
'''
def isArmstrong(n):
    fs=0
    dummy=n
    L=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fs+=rem**L
    if fs==n:
        print(n,'Armstrong')
    else:
        print(n,'not')
n=int(input())
isArmstrong(n)
'''

#function with range
def isArmstrong(n):
    fs=0
    L=len(str(n))
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fs+=rem**L
    if fs==n:
        return True
    else:
        return False
def printArm(LL,UL):
    for n in range(LL,UL+1):
        if isArmstrong(n):
            print(n,'is Armstrong')
LL=int(input())
UL=int(input())
printArm(LL,UL)
     























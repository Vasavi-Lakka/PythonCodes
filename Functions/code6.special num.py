#special number (factorial sum of individual digits equals to itself)
'''
n=int(input())
fs=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    fs+=fact
if fs==n:
    print(n,"is Special num")
else:
    print('not')
'''
#With function
'''
def isSpecial(n):
    fs=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        fs+=fact
    if fs==n:
        print(n,'is special')
    else:
        print(n, 'is Not Special')
n=int(input())
isSpecial(n)
'''
#function with range
def isSpecial(n):
    fs=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        fs+=fact
    if fs==n:
        return True
    else:
        return False
def printSpecialNum(LL,UL):
    for i in range(LL,UL+1):
        if isSpecial(i):
            print(i,'is Special')
LL=int(input())
UL=int(input())
printSpecialNum(LL,UL)
































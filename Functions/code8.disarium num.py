#Disarium num
'''
n=int(input())
summ=0
L=len(str(n))
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**L
    L-=1
if summ==n:
    print(n,'is Disarium')
else:
    print(n,'not')
'''
#by usingfunction

def isDisarium(n):
    summ=0
    dummy=n
    L=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**L
        L-=1
    if summ==n:
        #print(n,'is disarium')
        return True
    else:
        #print(n,'is Not')
        return False
    
#n=int(input())
#isDisarium(n)
def printDisariumNums(LL,UL):
    for n in range(LL,UL+1):
        if isDisarium(n):
            print(n,'is Disarium')
LL=int(input())
UL=int(input())
printDisariumNums(LL,UL)















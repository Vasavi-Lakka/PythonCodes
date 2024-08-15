#perfect num
'''
n=int(input())
ds=0

for i in range(1,n//2+1):
    if n%i==0:
        ds+=i
if ds==n:
    print(n,'is perfect')
else:
    print(n,'not perfect')
'''
#using function with range and without range

def isPerfect(n):
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if ds==n:
        return True
        #print(n, 'is perfect')
    else:
        return False
        #print(n,'is not perefct')
#n=int(input())
#isPerfect(n)
def printPerfectNums(LL,UL):
    for i in range(LL,UL+1):
        if isPerfect(i):
            print(i,'is perfect')
LL=int(input())
UL=int(input())
printPerfectNums(LL,UL)
    

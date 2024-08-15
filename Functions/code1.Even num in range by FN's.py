 









#print even numbers in a given range
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
def evenNum(LL,UL):
    for n in range(LL,UL+1):
        if isEven(n):
            print(n)
LL=int(input())
UL=int(input())
evenNum(LL,UL)

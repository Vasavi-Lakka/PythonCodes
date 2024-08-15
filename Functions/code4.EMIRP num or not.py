def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def reverse(n):
    rev=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        rev=rev*10+rem
    return rev
def isEMIRP(n):
    rev=reverse(n)
    if n!=rev and isPrime(n) and isPrime(rev):
        return True
    else:
        return False
def emirpNum(LL,UL):
    for n in range(LL,UL+1):
        if isEMIRP(n):
            print(n,'is EMIRP num')
LL=int(input())
UL=int(input())
emirpNum(LL,UL)

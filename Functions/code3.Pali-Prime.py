#Print Pali-prime in given range
'''
def pali(n):
    s=str(n)
    if s[::-1]==s:
        return True
    else:
        return False
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def pali_prime(LL,UL):
    for n in range(LL,UL+1):
        if pali(n):
            if prime(n):
                print(n,"is pali-prime")
        
LL=int(input())
UL=int(input())
pali_prime(LL,UL)

'''
#Check given num is pali-prime or not
'''
def pali(n):
    s=str(n)
    if s[::-1]==s:
        return True
    else:
        return False
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def pali_prime(n):
    if pali(n):
        if prime(n):
            print(n,"is pali-prime")
        
n=int(input())
pali_prime(n)
'''
#nother approach

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
def isPaliPrime(n):
    rev=reverse(n)
    if n==rev and isPrime(n):
        return True
    else:
        return False
def primepali(LL,UL):
    for n in range(LL,UL+1):
        if isPaliPrime(n):
            print(n,'is paliprime')
LL=int(input())
UL=int(input())
primepali(LL,UL)



















    





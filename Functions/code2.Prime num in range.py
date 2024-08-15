#To check given num is prime or not
'''
def primeOrNot():
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                print(n,"is not prime")
        else:
            print(n,"is prime")
    else:
        print(n,"is not prime")
n=int(input())

primeOrNot()
'''

#WAp to print prime num in givenn range
def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def prime(LL,UL):
    for n in range(LL,UL+1):
        if isPrime(n):
            print(n)
LL=int(input())
UL=int(input())
prime(LL,UL)

def printPrime(LL,UL):
    for n in range(LL,UL+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    return False
            else:
                return True
        print(printPrime(val1,val2))

def primeNo(ll,ul):
    for n in range(ll,ul+1):
        if printPrime(n):
            print(n)
    primeNo(10,15)

#Perfect NUmber
'''
n=int(input())
ds=0
i=1
while i<=n//2:
    if n%i==0:
        ds+=i
    i+=1
if ds==n:
    print(n, "is Perfect num")
else:
    print("NOT")
'''
#Print n perfect numbers
'''
c=int(input())
ds=0
n=1
while True:
    if n>0:
        summ=0
        i=1
        while i<=n//2:
            if n%i==0:
                summ+=i
            i+=1
        if summ==n:
            print(n)
            ds+=1
    if ds==c:
        break
    n+=1
             
'''
#WAP to print nth perfect number
'''
c=int(input())
DS=0
n=1
while True:
    if n>0:
        summ=0
        i=1
        while i<=n//2:
            if n%i==0:
                summ+=i
            i+=1
        if summ==n:
            DS+=1
    if DS==c:
        print(n)
        break
    n+=1
'''
#WAP to print 2 to 4 perfect numbers

n=1
DS=0
while True:
    if n>0:
        summ=0
        i=1
        while i<=n//2:
            if n%i==0:
                summ+=i
            i+=1
        if summ==n:
            DS+=1
            if DS>=2 and DS<=4:
                    print(n)
    if DS==4:
        break
    n+=1




















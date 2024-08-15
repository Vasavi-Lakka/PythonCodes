#Special Number
'''
n=int(input())
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    summ+=fact

if summ==n:
    print("Special")
else:
    print("Not")
'''
#Print 1st n numbers of special numbers
'''
c=int(input())
fs=0
n=1
while True:
    if n>0:
        fact=1
        summ=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            for i in range(1,rem+1):
                fact*=i
            summ+=fact
        if summ==n:
            print(n)
            fs+=1

    if fs==c:
        break
    n+=1
'''
#Print nth special number

c=int(input())
n=1
fs=0
while True:
    if n>0:
        summ=0
        fact=1
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            for i in range(1,rem+1):
                fact*=i
            summ+=fact
        if summ==n:
            fs+=1
    if fs==c:
        print(n)
        break
    n+=1


#Print 1 to 3 specail numbers
'''    
n=1
fs=0
while True:
    if n>0:
        summ=0
        fact=1
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            for i in range(1,rem+1):
                fact*=i
            summ+=fact
        if summ==n:
            fs+=1
            if fs>=1 and fs<=3:
                print(n)
    if fs==3:

        break
    n+=1

'''

















    

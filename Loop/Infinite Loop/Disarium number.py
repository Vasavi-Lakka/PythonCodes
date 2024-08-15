#Disarium number
'''
n=int(input())
summ=0
dummy=n
L=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**L
    L-=1
if summ==n:
    print(n,"is disarium num")
else:
    print("Not")
'''
#Print n disarium numbers
'''
c=int(input())
DS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**L
            L-=1
        if summ==n:
            print(n)
            DS+=1
    if DS==c:
        break
    n+=1
'''
#Print nth disarium number
'''
c=int(input())
DS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**L
            L-=1
        if summ==n:
        
            DS+=1
    if DS==c:
        print(n)
        break
    n+=1

'''
#Print 10 to 13 disarium numbers

DS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**L
            L-=1
        if summ==n:
            
            DS+=1
            if DS>=10 and DS<=13:
                print(n)
    if DS==13:
        break
    n+=1






















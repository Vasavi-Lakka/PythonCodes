#Harshad number
'''
n=int(input())
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem
if n%summ==0:
    print(n, 'is harshad numer')
else:
    print('Not')
'''

#print of n harshad numbers
'''
c=int(input())
HS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem
        if n%summ==0:
            print(n)
            HS+=1
    if HS==c:
        break
    n+=1
'''   
#print of nth harshad numbers
'''
c=int(input())
HS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem
        if n%summ==0:
            
            HS+=1
    if HS==c:
        print(n)
        break
    n+=1
'''
#print of nth harshad numbers

HS=0
n=1
while True:
    if n>0:
        summ=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem
        if n%summ==0:
            
            HS+=1
            if HS>=10 and HS<=20:
                print(n)
    if HS==30:
       
        break
    n+=1











 

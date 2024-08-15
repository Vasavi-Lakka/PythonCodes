#Armstrong number
'''
n=int(input())
summ=0

    
dummy=n
        
L=len(str(dummy))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**L
if summ==n:
    print(n ,'is Armstrong')
else:
    print("NOT")
    '''
            
#print n armstrong n umbers
'''
c=int(input())
AC=0
n=1
while True:
    if n>0:
        dummy=n
        summ=0
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy=dummy//10
            summ+=rem**L
        if summ==n:
            print(n)
            AC+=1
    if AC==c:
        break
    n+=1
    '''

#nth Armstrong number
'''c=int(input())
AC=0
n=1
while True:
    if n>0:
        dummy=n
        summ=0
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy=dummy//10
            summ+=rem**L
        if summ==n:
            
            AC+=1
    if AC==c:
        print(n)
        break
    n+=1
'''

#WAP to print 5 to 10 Armstrong number


AC=0
n=1
while True:
    if n>0:
        dummy=n
        summ=0
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy=dummy//10
            summ+=rem**L
        if summ==n:
            
            AC+=1
            if AC>=5 and AC<=10:
                print(n)
    if AC==12:
     
        break
    n+=1
















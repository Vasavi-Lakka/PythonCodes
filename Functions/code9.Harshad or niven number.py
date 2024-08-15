#Harshad Number
'''
n=int(input())
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem
if n%summ==0:
    print(n,'is Harshad number')
else:
    print(n,'is not niven number')
'''

#by using function
def isHarshad(n):
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem
    if n%summ==0:
        #print(n,'is Harshad num')
        return True
    else:
        #print(n,'is not harshad')
        return False
    
#n=int(input())
#isHarshad(n)
def printHarshadNums(LL,UL):
    for n in range(LL,UL+1):
        if isHarshad(n):
            print(n,'is Harshad')
LL=int(input())
UL=int(input())

printHarshadNums(LL,UL)

















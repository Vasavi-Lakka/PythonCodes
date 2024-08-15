#Palindrome number
'''
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    rev=rev*10+rem
if n==rev:
    print(n,'is palindrome')
else:
    print('Not')
'''

#print n palindrome numbers
'''
c=int(input())
ps=0
n=1
while True:
    if n>0:
        rev=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            rev=rev*10+rem
        if n==rev:
            print(n)
            ps+=1
    if ps==c:
        break
    n+=1
'''
#Print nth palindrome number
'''
c=int(input())
ps=0
n=1
while True:
    if n>0:
        rev=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            rev=rev*10+rem
        if n==rev:
            ps+=1
    if ps==c:
        print(n)
        break
    n+=1
'''
#Print 20 to 30 palindrome number

ps=0
n=1
while True:
    if n>0:
        rev=0
        dummy=n
        while dummy>0:
            rem=dummy%10
            dummy//=10
            rev=rev*10+rem
        if n==rev:
            ps+=1
            if ps>=20 and ps<=30:
                print(n)
    if ps==30:
        
        break
    n+=1













